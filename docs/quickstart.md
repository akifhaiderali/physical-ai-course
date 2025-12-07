---
id: quickstart
title: Quickstart Guide
sidebar_position: 2
last_updated: 2025-12-07
---

# Quickstart Guide

Welcome to the Physical AI & Humanoid Robotics Course! This guide helps you get started whether you're an **educator delivering the course**, a **contributor developing content**, or a **student learning independently**.

---

## For Educators (Course Delivery)

### Getting Started

This course is designed for delivery in a **12-16 week semester** with hands-on lab components. You can adopt the full 4-module curriculum or select individual modules based on your program needs.

### Course Structure Overview

- **Module 1: ROS 2 Fundamentals** (Weeks 1-4) - Robot middleware, navigation, multi-robot systems
- **Module 2: Simulation Environments** (Weeks 5-7) - Gazebo and Unity for robotics simulation
- **Module 3: NVIDIA Isaac Sim** (Weeks 8-9) - Synthetic data generation, sim-to-real transfer
- **Module 4: Vision-Language-Action (VLA)** (Weeks 10-12) - Multimodal AI for robotic manipulation
- **Capstone Project** (Weeks 13-16) - Integrative project demonstrating all modules

### Setting Up Your Course

#### 1. Choose Your Lab Infrastructure Tier

Review the [Lab Infrastructure](/category/lab-infrastructure) section to select the tier that fits your budget and student capacity:

- **Proxy Tier ($10-20K)**: Simulation-only, GPU workstations, no physical robots
- **Miniature Tier ($50-70K)**: Compact humanoid robots (Unitree H1), GPU workstations
- **Premium Tier ($120-180K)**: Full-scale humanoid robots, research-grade infrastructure

**Recommendation**: Start with Proxy Tier for curriculum validation, then upgrade to Miniature/Premium as enrollment grows.

#### 2. Review the Week-by-Week Schedule

The [Week-by-Week Schedule](/appendices/week-by-week) provides a detailed mapping of:
- Weekly topics and learning objectives
- Assigned exercises and assessments
- Module transitions and capstone milestones

**Adaptation**: You can compress the schedule to 12 weeks by reducing capstone time or extend to 16 weeks for deeper exploration.

#### 3. Prepare Exercises

Each module includes hands-on exercises with:
- **Setup requirements** (hardware, software, prerequisites)
- **Step-by-step procedures** with expected outputs
- **Assessment criteria** with grading rubrics

**Preparation checklist**:
- [ ] Install required software (ROS 2 Humble, Gazebo, Isaac Sim, Unity)
- [ ] Test all code examples in Docker environments (see [Docker Testing](/tests/DOCKER_TESTING.md))
- [ ] Calibrate physical robots (if using Miniature/Premium tier)
- [ ] Setup GitHub Classroom for student code submissions

#### 4. Customize for Your Institution

**ABET Accreditation**: Review [Learning Outcomes](/intro#learning-outcomes) to map to your program outcomes.

**Licensing**: Ensure compliance with software licenses (Unity Pro Educational, NVIDIA Isaac Sim free tier).

**Assessment Methods**: Adapt the [Capstone Project rubric](/capstone/capstone-project) to align with your grading policies.

### Teaching Resources

- **Lecture Slides**: Available in the [course repository](https://github.com/your-organization/physical-ai-course) (to be published)
- **Code Examples**: See `static/code-examples/` directory with tested, documented code
- **References**: 50-100 peer-reviewed sources (2015-2025) in APA format (see [References](/appendices/references))

### Support and Community

- **Office Hours**: Recommended 2 hours/week for lab troubleshooting
- **Discussion Forum**: Setup a Slack/Discord for student collaboration
- **Issues**: Report technical issues at [GitHub Issues](https://github.com/your-organization/physical-ai-course/issues)

---

## For Contributors (Content Development)

### Contributing to the Course

This course is built with **Docusaurus 3.x** and follows **Spec-Driven Development** principles. All content adheres to the [Constitution](.specify/memory/constitution.md) for quality and consistency.

### Prerequisites

**Required Knowledge**:
- Markdown and MDX syntax
- Git and GitHub workflows
- Docusaurus basics (helpful but not required)

**Required Tools**:
- **Node.js 18+** and npm
- **Git** for version control
- **Code editor** (VS Code recommended with MDX extension)
- **Docker** for testing code examples (optional but recommended)

### Local Development Setup

#### 1. Clone the Repository

```bash
git clone https://github.com/your-organization/physical-ai-course.git
cd physical-ai-course
```

#### 2. Install Dependencies

```bash
npm install
```

This installs Docusaurus and all required plugins (~1276 packages).

#### 3. Start the Development Server

```bash
npm start
```

This launches a local development server at `http://localhost:3000` with hot-reloading for instant preview of changes.

#### 4. Build for Production

```bash
npm run build
```

This generates a static site in the `build/` directory. The build will **fail** if:
- Broken links are detected
- Invalid frontmatter is found
- Citations are missing from `static/references.bib`

### Project Structure

```
physical-ai-course/
├── docs/                          # All course content (Markdown/MDX)
│   ├── modules/                   # 10 module chapters (4 modules, ~2.5 chapters each)
│   ├── exercises/                 # 4 hands-on exercises (1 per module)
│   ├── capstone/                  # Capstone project specification
│   ├── infrastructure/            # Lab tier specifications (5 chapters)
│   └── appendices/                # Glossary, references, week-by-week
├── static/                        # Static assets
│   ├── code-examples/             # Executable code for exercises
│   ├── img/                       # Diagrams, robot photos, lab layouts
│   └── references.bib             # BibTeX bibliography (APA 7th edition)
├── src/                           # React components and styling
│   └── css/custom.css             # Academic styling overrides
├── specs/001-physical-ai-course/  # Specification artifacts
│   ├── spec.md                    # Feature specification
│   ├── plan.md                    # Implementation plan
│   ├── tasks.md                   # Task breakdown
│   ├── data-model.md              # Content entity definitions
│   └── contracts/                 # YAML schemas for validation
├── tests/                         # Testing infrastructure
│   └── code-examples/             # Docker tests for code snippets
├── .github/workflows/             # CI/CD automation
│   ├── deploy.yml                 # GitHub Pages deployment
│   └── test-code-examples.yml     # Code validation workflow
├── docker-compose.yml             # Docker test environments
├── docusaurus.config.js           # Site configuration
├── sidebars.js                    # Navigation structure
└── package.json                   # Node.js dependencies
```

### Content Development Workflow

#### Adding a New Module Chapter

1. **Create the file**: `docs/modules/<module-id>/<chapter-id>.md`
2. **Add frontmatter** (validate against `specs/001-physical-ai-course/contracts/chapter-schema.yaml`):

```yaml
---
id: my-new-chapter
title: My New Chapter
sidebar_position: 5
module: 2
learning_objectives:
  - "Design [specific skill]"
  - "Implement [specific skill]"
  - "Explain [specific concept]"
related_exercises:
  - my-related-exercise
related_references:
  - SomeAuthor2023
word_count: 1200
last_updated: 2025-12-07
---
```

3. **Write the content** (800-1500 words):
   - Introduction (context and relevance)
   - Learning objectives (measurable outcomes)
   - Topic sections with code examples
   - Summary (recap and next steps)
   - References (APA 7th edition)

4. **Update sidebar**: Add to `sidebars.js` under appropriate module category

5. **Add citations**: Ensure all cited sources exist in `static/references.bib`

6. **Test locally**: Run `npm start` and verify content renders correctly

#### Adding a New Exercise

1. **Create the file**: `docs/exercises/<exercise-id>.md`
2. **Add frontmatter** (validate against `specs/001-physical-ai-course/contracts/exercise-schema.yaml`):

```yaml
---
id: my-new-exercise
title: "Exercise 2.3: My Hands-On Exercise"
sidebar_position: 3
module: 2
duration: 90
difficulty: intermediate
prerequisites:
  - prerequisite-exercise-id
learning_outcomes:
  - "Create [specific artifact]"
  - "Validate [specific result]"
equipment_required:
  hardware:
    - "Ubuntu 22.04 workstation"
  software:
    - "ROS 2 Humble"
    - "Gazebo Fortress"
code_examples:
  - path: "static/code-examples/module2-simulation/my_example.py"
    description: "Example script description"
assessment_criteria:
  - criterion: "Functional correctness"
    weight: 40
    description: "Code executes without errors"
  - criterion: "Code quality"
    weight: 30
    description: "Follows style guide and includes documentation"
  - criterion: "Analysis and reporting"
    weight: 30
    description: "Results documented with visualizations"
last_updated: 2025-12-07
---
```

3. **Write the exercise**:
   - Overview and prerequisites
   - Setup instructions (hardware and software)
   - Step-by-step procedure with expected outputs
   - Troubleshooting common errors
   - Assessment criteria and rubric

4. **Add code examples**: Place in `static/code-examples/<module-id>/`

5. **Create Docker test**: Add test script in `tests/code-examples/`

6. **Validate**: Ensure assessment criteria weights sum to 100%

#### Adding Code Examples

1. **Create the code file**: `static/code-examples/<module-id>/<example-name>.<ext>`

2. **Add header comment**:

```python
#!/usr/bin/env python3
"""
Example Title

Module: 2
Exercise: my-new-exercise
Author: Physical AI Course Contributors
License: Apache 2.0
Last Updated: 2025-12-07

Description:
This script demonstrates [specific concept].

Prerequisites:
- ROS 2 Humble
- Python 3.10+

Usage:
    python3 my_example.py [args]
"""
```

3. **Write the code** (follow PEP 8 for Python, Google Style for C++)

4. **Add tests**: Create `tests/code-examples/test_<example-name>.py`

5. **Test in Docker**:

```bash
docker-compose run <container-name> pytest tests/test_<example-name>.py
```

6. **Verify CI passes**: Push to a branch and check GitHub Actions

### Quality Gates

Before submitting a pull request, ensure:

- [ ] **Build passes**: `npm run build` completes without errors
- [ ] **Links valid**: No broken links to internal pages or external sources
- [ ] **Citations valid**: All BibTeX keys referenced in markdown exist in `references.bib`
- [ ] **Word count**: Module chapters are 800-1500 words
- [ ] **Code tested**: All code examples pass Docker tests
- [ ] **Frontmatter valid**: YAML validates against schemas in `contracts/`
- [ ] **Style consistent**: Academic tone, no hallucinations, APA citations

### Contributing Guidelines

1. **Fork the repository** on GitHub
2. **Create a feature branch**: `git checkout -b feature/my-contribution`
3. **Make your changes** following the workflows above
4. **Test locally**: `npm run build && npm run validate:citations && npm run validate:links`
5. **Commit with descriptive messages**: `git commit -m "Add chapter on Isaac Sim domain randomization"`
6. **Push to your fork**: `git push origin feature/my-contribution`
7. **Open a pull request** with a clear description of changes

**Code Review**: All PRs require review by course maintainers. Expect feedback on:
- Technical accuracy (backed by peer-reviewed sources)
- Pedagogical soundness (clear learning objectives)
- Consistency with existing content

### References

- [Docusaurus Documentation](https://docusaurus.io/docs)
- [Markdown Guide](https://www.markdownguide.org/)
- [APA 7th Edition Style](https://apastyle.apa.org/)

---

## For Students (Self-Study)

### Learning Independently

This course is designed for university instruction but can be completed independently with the right prerequisites and equipment.

### Prerequisites

**Knowledge Requirements**:
- **Programming**: Python and C++ at intermediate level
- **Robotics Fundamentals**: Kinematics, sensors, actuators (undergraduate robotics course)
- **Linux**: Comfortable with terminal commands and package management
- **Machine Learning**: Basic neural networks and computer vision concepts

**Equipment Requirements**:

**Minimum (Simulation-Only)**:
- Ubuntu 22.04 Desktop (native or VM)
- 16GB RAM, 4-core CPU
- 50GB free disk space
- (Optional) NVIDIA GPU for Isaac Sim and VLA modules

**Recommended (Hands-On)**:
- Ubuntu 22.04 workstation with NVIDIA RTX 3060+ GPU
- Compact humanoid robot (Unitree H1 or similar, ~$90K)
- Safety barriers and workspace (10x10 ft minimum)

### Self-Study Path

#### Module 1: ROS 2 Fundamentals (4 weeks)

**Topics**:
- ROS 2 architecture and nodes
- Publishers, subscribers, services, actions
- Navigation with Nav2
- Multi-robot coordination

**Exercises**:
- [Exercise 1.1: Talker-Listener System](/exercises/ros2-talker-listener)
- [Exercise 1.2: Custom Service](/exercises/ros2-custom-service)

**Resources**:
- [ROS 2 Documentation](https://docs.ros.org/en/humble/)
- [Nav2 Tutorials](https://navigation.ros.org/)

#### Module 2: Simulation Environments (3 weeks)

**Topics**:
- Gazebo physics simulation
- URDF/SDF robot modeling
- Unity for high-fidelity visualization

**Exercises**:
- [Exercise 2.1: Gazebo World Design](/exercises/gazebo-world-design)
- [Exercise 2.2: URDF Robot Modeling](/exercises/gazebo-urdf-modeling)

**Resources**:
- [Gazebo Tutorials](https://gazebosim.org/docs)
- [Unity Robotics Hub](https://github.com/Unity-Technologies/Unity-Robotics-Hub)

#### Module 3: NVIDIA Isaac Sim (2 weeks)

**Topics**:
- Isaac Sim setup and Omniverse
- Synthetic data generation
- Domain randomization for sim-to-real transfer

**Exercises**:
- [Exercise 3.1: Synthetic Data Generation](/exercises/isaac-synthetic-data)

**Resources**:
- [Isaac Sim Documentation](https://docs.omniverse.nvidia.com/isaacsim/latest/)
- [NVIDIA Omniverse](https://www.nvidia.com/en-us/omniverse/)

**Note**: Requires NVIDIA GPU and free Omniverse account

#### Module 4: Vision-Language-Action (VLA) (3 weeks)

**Topics**:
- Multimodal AI for robotics
- OpenVLA, RT-1, RT-2 models
- VLA-driven manipulation

**Exercises**:
- [Exercise 4.1: VLA Inference](/exercises/vla-inference)
- [Exercise 4.2: VLA Manipulation](/exercises/vla-manipulation)

**Resources**:
- [OpenVLA GitHub](https://github.com/openvla/openvla)
- [RT-2 Paper (Brohan et al., 2023)](https://arxiv.org/abs/2307.15818)

#### Capstone Project (4 weeks)

**Goal**: Integrate all modules to demonstrate autonomous task execution on a humanoid robot using VLA-based control.

**Deliverables**:
1. Project proposal (Week 13)
2. Simulation demo in Isaac Sim (Week 14)
3. (Optional) Physical robot demo (Week 15)
4. Final presentation and report (Week 16)

**See**: [Capstone Project Specification](/capstone/capstone-project)

### Setting Up Your Environment

#### Install ROS 2 Humble

```bash
# Ubuntu 22.04
sudo apt update && sudo apt install -y curl gnupg lsb-release
sudo curl -sSL https://raw.githubusercontent.com/ros/rosdistro/master/ros.key -o /usr/share/keyrings/ros-archive-keyring.gpg
echo "deb [signed-by=/usr/share/keyrings/ros-archive-keyring.gpg] http://packages.ros.org/ros2/ubuntu $(lsb_release -cs) main" | sudo tee /etc/apt/sources.list.d/ros2.list > /dev/null
sudo apt update && sudo apt install -y ros-humble-desktop
source /opt/ros/humble/setup.bash
echo "source /opt/ros/humble/setup.bash" >> ~/.bashrc
```

#### Install Gazebo Fortress

```bash
sudo apt install -y ros-humble-gazebo-ros-pkgs
```

#### Install NVIDIA Isaac Sim (GPU required)

1. Create NVIDIA account at [nvidia.com](https://www.nvidia.com)
2. Download Omniverse Launcher
3. Install Isaac Sim 2023.1.1 from Omniverse Launcher
4. Follow [Isaac Sim Quickstart](https://docs.omniverse.nvidia.com/isaacsim/latest/installation/install_workstation.html)

#### Install Unity (Optional)

1. Download Unity Hub from [unity.com](https://unity.com)
2. Install Unity Editor 2022.3 LTS
3. Install Robotics package from Package Manager

### Getting Help

- **Documentation**: Start with this site's [Introduction](/intro) and [Glossary](/appendices/glossary)
- **Community**: Join the [ROS Discourse](https://discourse.ros.org/) and [NVIDIA Isaac Sim Forums](https://forums.developer.nvidia.com/c/omniverse/simulation/69)
- **Issues**: Report technical problems at [GitHub Issues](https://github.com/your-organization/physical-ai-course/issues)
- **Office Hours** (if enrolled): Check with your instructor for virtual office hours

### Assessment

**Self-Assessment**:
- Complete all exercises and check against assessment criteria
- Run Docker tests for code examples: `docker-compose run <container> pytest`
- Compare your capstone project against the [rubric](/capstone/capstone-project#assessment-rubric)

**Seeking Feedback**:
- Share your work on ROS Discourse or robotics forums
- Contribute improvements to this course via GitHub PRs

---

## Next Steps

- **Educators**: Review the [Week-by-Week Schedule](/appendices/week-by-week) and [Lab Infrastructure](/category/lab-infrastructure)
- **Contributors**: Read the [Constitution](.specify/memory/constitution.md) and [Data Model](specs/001-physical-ai-course/data-model.md)
- **Students**: Start with [Module 1: ROS 2 Fundamentals](/modules/ros2-fundamentals) and [Exercise 1.1](/exercises/ros2-talker-listener)

---

**Need help?** Consult the [Glossary](/appendices/glossary) for technical terms or open an [issue](https://github.com/your-organization/physical-ai-course/issues) for support.
