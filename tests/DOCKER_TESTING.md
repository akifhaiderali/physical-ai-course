# Docker Testing Infrastructure

This document describes the Docker-based testing infrastructure for code examples in the Physical AI & Humanoid Robotics Course.

## Overview

Each module has a dedicated Docker container for isolated, reproducible testing of code examples. This ensures:

- **Reproducibility**: Consistent environment across development and CI/CD
- **Isolation**: No conflicts between module dependencies (ROS 2 vs VLA libraries)
- **Accessibility**: Students/educators can test examples without full hardware setup
- **CI Integration**: Automated validation on every code change

## Prerequisites

### General Requirements
- **Docker**: Version 20.10 or later
- **Docker Compose**: Version 2.0 or later
- **Disk Space**: ~30GB for all container images

### GPU-Dependent Containers (Isaac Sim, VLA, Capstone)
- **NVIDIA GPU**: CUDA-compatible (GTX 1060 or better)
- **NVIDIA Container Toolkit**: For GPU passthrough to containers
- **NVIDIA Driver**: Version 525.60.11 or later

### Installation

**Install Docker (Ubuntu/Debian):**
```bash
sudo apt-get update
sudo apt-get install docker.io docker-compose-v2
sudo usermod -aG docker $USER
```

**Install NVIDIA Container Toolkit (for GPU containers):**
```bash
distribution=$(. /etc/os-release;echo $ID$VERSION_ID)
curl -s -L https://nvidia.github.io/nvidia-docker/gpgkey | sudo apt-key add -
curl -s -L https://nvidia.github.io/nvidia-docker/$distribution/nvidia-docker.list | sudo tee /etc/apt/sources.list.d/nvidia-docker.list
sudo apt-get update && sudo apt-get install -y nvidia-container-toolkit
sudo systemctl restart docker
```

**Verify GPU Access:**
```bash
docker run --rm --runtime=nvidia nvidia/cuda:12.1.0-base-ubuntu22.04 nvidia-smi
```

## Container Reference

### 1. ROS 2 Test Environment (`ros2-test`)

**Purpose**: Test ROS 2 nodes, topics, services, Nav2 navigation examples

**Image**: `osrf/ros:humble-desktop-full` (Ubuntu 22.04, ROS 2 Humble)

**Usage**:
```bash
# Interactive shell
docker-compose run ros2-test

# Run specific example
docker-compose run ros2-test bash -c "source /opt/ros/humble/setup.bash && python3 talker.py"

# Test navigation example
docker-compose run ros2-test bash -c "source /opt/ros/humble/setup.bash && ros2 launch nav2_bringup tb3_simulation_launch.py"
```

**Code Location**: `static/code-examples/module1-ros2/`

**Environment Variables**:
- `ROS_DOMAIN_ID=42` - Isolated ROS 2 network
- `DISPLAY` - X11 forwarding for rviz visualization

---

### 2. Gazebo Test Environment (`gazebo-test`)

**Purpose**: Test Gazebo world files, robot models (URDF/SDF), physics simulation

**Image**: `osrf/ros:humble-desktop-full` (includes Gazebo Fortress)

**Usage**:
```bash
# Interactive shell
docker-compose run gazebo-test

# Launch Gazebo world
docker-compose run gazebo-test bash -c "source /opt/ros/humble/setup.bash && gazebo worlds/humanoid_lab.world"

# Validate URDF model
docker-compose run gazebo-test bash -c "source /opt/ros/humble/setup.bash && check_urdf models/unitree_h1.urdf"
```

**Code Location**: `static/code-examples/module2-simulation/`

**Model Path**: `static/code-examples/module2-simulation/models/`

---

### 3. Unity Test Environment (`unity-test`)

**Purpose**: Test Unity C# scripts, robot controller validation

**Image**: `gableroux/unity3d:2022.3.10f1-ubuntu`

**Usage**:
```bash
# Limited headless testing
docker-compose run unity-test

# Note: Full Unity testing requires manual Unity Editor validation
# This container validates script compilation only
```

**Code Location**: `static/code-examples/module2-simulation/unity/`

**Limitations**:
- Unity requires graphical interface for full testing
- Container validates script syntax and compilation only
- Full scene testing requires manual Unity Editor run

---

### 4. Isaac Sim Test Environment (`isaac-sim-test`)

**Purpose**: Test Isaac Sim scripts, synthetic data generation, domain randomization

**Image**: `nvcr.io/nvidia/isaac-sim:2023.1.1`

**Requirements**: NVIDIA GPU, Omniverse Nucleus connection

**Usage**:
```bash
# Interactive shell
docker-compose run isaac-sim-test

# Run synthetic data generation script
docker-compose run isaac-sim-test python3 generate_synthetic_data.py

# Test domain randomization
docker-compose run isaac-sim-test python3 domain_randomization_example.py
```

**Code Location**: `static/code-examples/module3-isaac/`

**Environment Variables**:
- `NVIDIA_VISIBLE_DEVICES=all` - GPU passthrough
- Omniverse cache: `~/.nvidia-omniverse`

**Limitations**:
- Requires Omniverse Nucleus setup (cloud or local)
- GPU-only (no CPU fallback)

---

### 5. VLA Test Environment (`vla-test`)

**Purpose**: Test Vision-Language-Action models (OpenVLA, RT-1, RT-2)

**Image**: `pytorch/pytorch:2.1.0-cuda12.1-cudnn8-runtime`

**Requirements**: NVIDIA GPU (recommended), or CPU (slow inference)

**Usage**:
```bash
# Interactive shell
docker-compose run vla-test

# Test OpenVLA inference
docker-compose run vla-test python3 openvla_inference.py

# Test RT-2 model
docker-compose run vla-test python3 rt2_manipulation.py
```

**Code Location**: `static/code-examples/module4-vla/`

**Model Cache**: `~/.cache/huggingface` (HuggingFace models)

**Dependencies** (auto-installed):
- `transformers` - HuggingFace library
- `openvla-lib` - OpenVLA framework

---

### 6. Capstone Integration Test (`capstone-test`)

**Purpose**: Full-stack integration testing (ROS 2 + VLA + Isaac Sim)

**Image**: `nvcr.io/nvidia/isaac-sim:2023.1.1` (with ROS 2 bridge)

**Requirements**: NVIDIA GPU, Omniverse Nucleus

**Usage**:
```bash
# Run full capstone integration test
docker-compose run capstone-test bash -c "source /opt/ros/humble/setup.bash && python3 vla_humanoid_task.py"
```

**Code Location**: `static/code-examples/capstone/`

---

## CI/CD Integration

### GitHub Actions Workflow

The `.github/workflows/test-code-examples.yml` workflow runs Docker tests on every PR:

```yaml
name: Test Code Examples

on:
  pull_request:
    paths:
      - 'static/code-examples/**'

jobs:
  test-ros2:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Run ROS 2 tests
        run: docker-compose run ros2-test bash -c "source /opt/ros/humble/setup.bash && python3 -m pytest tests/"

  test-gazebo:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Validate Gazebo models
        run: docker-compose run gazebo-test bash -c "source /opt/ros/humble/setup.bash && check_urdf models/*.urdf"

  test-vla:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Run VLA inference tests (CPU mode)
        run: docker-compose run vla-test python3 -m pytest tests/ --device=cpu
```

**Limitations in CI**:
- Isaac Sim tests skipped (requires GPU + Omniverse license)
- Unity tests skipped (requires graphical interface)
- VLA tests run in CPU mode (slow but functional)

---

## Testing Guidelines

### Adding New Code Examples

1. **Place code in module directory**:
   - Module 1: `static/code-examples/module1-ros2/`
   - Module 2: `static/code-examples/module2-simulation/`
   - Module 3: `static/code-examples/module3-isaac/`
   - Module 4: `static/code-examples/module4-vla/`

2. **Add test script**: Create `tests/test_<example_name>.py` with assertions

3. **Document dependencies**: Add requirements to `requirements.txt` in module directory

4. **Run local test**:
   ```bash
   docker-compose run <container-name> pytest tests/test_<example_name>.py
   ```

5. **Verify CI passes**: Push to PR and check GitHub Actions

### Mocking Hardware APIs

For examples requiring physical hardware (Jetson Orin, Unitree H1):

- **Mock robot APIs** with reasonable defaults
- **Example**: Mock Unitree SDK with simulated joint states
  ```python
  class MockUnitreeH1:
      def get_joint_states(self):
          return [0.0] * 19  # 19-DOF humanoid
  ```

- **Document mocking** in code comments
- **Test against real hardware** manually before production

---

## Troubleshooting

### X11 Display Errors (Gazebo/rviz)

**Error**: `cannot open display: :0`

**Fix**:
```bash
xhost +local:docker
export DISPLAY=:0
docker-compose run gazebo-test
```

### NVIDIA GPU Not Detected

**Error**: `nvidia-smi: command not found`

**Fix**:
1. Verify NVIDIA drivers: `nvidia-smi` on host
2. Install NVIDIA Container Toolkit (see Prerequisites)
3. Restart Docker: `sudo systemctl restart docker`

### Isaac Sim Nucleus Connection Failed

**Error**: `Failed to connect to Nucleus server`

**Fix**:
1. Install Omniverse Launcher on host
2. Start Nucleus Local Service
3. Mount Omniverse cache: `~/.nvidia-omniverse:/root/.nvidia-omniverse`

### Slow VLA Inference in CI

**Issue**: VLA tests timeout in GitHub Actions (CPU-only)

**Fix**:
- Use smaller test models (e.g., RT-1-X 1B instead of 7B)
- Mock VLA inference with pre-computed outputs
- Tag GPU-required tests: `@pytest.mark.gpu`

---

## Contact

For Docker infrastructure issues, contact the course maintainers or open an issue at:
https://github.com/your-organization/physical-ai-course/issues
