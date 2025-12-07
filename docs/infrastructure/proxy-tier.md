---
id: proxy-tier
title: Proxy Tier Lab
sidebar_position: 2
tier_level: 1
budget_range:
  min: 10000
  max: 20000
  currency: USD
student_capacity: 15
last_updated: 2025-12-07
---

# Proxy Tier Lab ($10-20K)

The **Proxy Tier** enables Physical AI education through simulation-only infrastructure, eliminating the cost and complexity of physical humanoid robots while preserving all learning objectives through Gazebo, Unity, and NVIDIA Isaac Sim virtual environments.

## Budget Breakdown

### Hardware Components

| Component                          | Quantity | Unit Cost (USD) | Total Cost (USD) | Description                                    |
|------------------------------------|:--------:|----------------:|-----------------:|------------------------------------------------|
| GPU Workstation (NVIDIA RTX 4060)  | 3        | $2,200          | $6,600           | Isaac Sim and VLA training (mid-range)         |
| Workstation (CPU-only)             | 2        | $1,000          | $2,000           | ROS 2 development and Gazebo (no GPU needed)   |
| Network Switch (1 GbE, 24-port)    | 1        | $300            | $300             | Lab network connectivity                       |
| Monitors (27" 1440p)               | 5        | $250            | $1,250           | Dual monitors per workstation (10 total)       |
| Peripherals (keyboard, mouse)      | 5        | $60             | $300             | Per workstation                                |
| **Total Hardware**                 |          |                 | **$10,450**      |                                                |

### Software Requirements

| Software                           | License Type   | Annual Cost (USD) | Description                                    |
|------------------------------------|----------------|------------------:|------------------------------------------------|
| ROS 2 Humble                       | Open Source    | $0                | Robot middleware (Apache 2.0 license)          |
| Gazebo Fortress                    | Open Source    | $0                | Physics simulation (Apache 2.0 license)        |
| NVIDIA Isaac Sim                   | Free           | $0                | Synthetic data generation (free tier)          |
| Unity Pro (Educational)            | Educational    | $0                | High-fidelity visualization (edu license)      |
| GitHub Team (10 users)             | Commercial     | $400              | Version control and CI/CD                      |
| **Total Annual Software Cost**     |                | **$400**          |                                                |

### Total Budget Range

**Minimum Configuration** (3 GPU + 2 CPU workstations): **$10,450**
**Expanded Configuration** (5 GPU workstations for 15 students): **$18,000**

---

## Hardware Specifications

### GPU Workstation (RTX 4060)

**Purpose**: Isaac Sim rendering, VLA model inference, synthetic data generation

**Specs**:
- CPU: Intel i7-13700 (16 cores) or AMD Ryzen 7 7700X
- RAM: 32 GB DDR5
- GPU: NVIDIA RTX 4060 (8 GB VRAM)
- Storage: 1 TB NVMe SSD
- OS: Ubuntu 22.04 LTS

**Performance**:
- Isaac Sim: 1.5-2.0× real-time factor (single humanoid)
- VLA Inference: 10-15 Hz (OpenVLA-7B with FP16)
- Gazebo: 30-60 FPS with complex scenes

**Limitations**: 8 GB VRAM limits VLA model size (7B max, cannot run 13B+ models). For larger models, upgrade to RTX 4070 (12 GB) at +$600/unit.

### CPU-Only Workstation

**Purpose**: ROS 2 node development, Gazebo (simple scenes), documentation

**Specs**:
- CPU: Intel i5-13400 (10 cores)
- RAM: 16 GB DDR4
- Storage: 512 GB SSD
- OS: Ubuntu 22.04 LTS

**Use Case**: Students writing ROS 2 code, running lightweight simulations, preparing reports.

---

## Space and Facilities

### Required Area

**150-250 sq ft** (e.g., 12×15 ft classroom or 15×17 ft lab)

### Layout

```
┌─────────────────────────────────────┐
│  GPU WS1   GPU WS2   GPU WS3        │
│  [====]    [====]    [====]         │
│                                      │
│  CPU WS4   CPU WS5                  │
│  [====]    [====]                   │
│                                      │
│  Network Switch                     │
│  Instructor Desk                    │
└─────────────────────────────────────┘
```

### Power and Cooling

- **Power**: 2-3 kW total (5 workstations × 400-600W each)
- **Electrical**: Standard 120V outlets (2-3 circuits)
- **Cooling**: Standard HVAC sufficient (no specialized cooling needed)

---

## Strengths and Limitations

### Advantages

✅ **Lowest Cost**: $10-20K vs. $50K+ for physical robots
✅ **Zero Safety Risk**: No physical robot hazards, no liability insurance needed
✅ **Rapid Iteration**: Students test algorithms instantly (no hardware setup time)
✅ **Scalable**: Supports 15+ students with time-shared workstations
✅ **Maintenance-Free**: No robot repairs, battery replacements, or calibration
✅ **Curriculum Validation**: Test course content before hardware investment

### Limitations

❌ **No Physical Robot Experience**: Students miss hands-on manipulation/navigation
❌ **Sim-to-Real Gap**: Theoretical only—cannot validate transfer to real hardware
❌ **Perception Limitations**: Simulated sensors lack real-world noise/artifacts
❌ **Reduced Industry Appeal**: Employers value physical robot project experience
❌ **Capstone Constraints**: Projects limited to simulation demonstrations

---

## Recommended Use Cases

### Ideal For

1. **Community Colleges**: Budget-constrained programs introducing Physical AI
2. **Online Programs**: Remote students cannot access physical labs
3. **Curriculum Pilots**: New programs testing interest before hardware investment
4. **Undergraduate Introductory Courses**: Focus on concepts over hands-on skills
5. **Supplementary Labs**: Complement existing wheeled robot labs with humanoid simulation

### Not Ideal For

- Graduate research programs requiring real-world validation
- Industry-sponsored programs with employer expectations for physical robots
- Institutions with existing robotics labs and available budgets ($40K+)

---

## Student Learning Experience

### Week 1-12: Full Simulation Curriculum

Students complete all modules (ROS 2, Gazebo/Unity, Isaac Sim, VLA) using simulated Unitree H1 or custom humanoid models. Learning objectives achieved through:

- **Module 1**: Multi-robot ROS 2 coordination in Gazebo (5 virtual robots)
- **Module 2**: Gazebo physics tuning, Unity photorealistic rendering
- **Module 3**: Isaac Sim synthetic data generation (10K-image datasets)
- **Module 4**: VLA training on synthetic data, testing in simulation

### Week 13-16: Simulation-Based Capstone

**Example Project**: "VLA-Driven Humanoid Warehouse Restocking"

1. **Simulation Environment**: Isaac Sim warehouse with shelves, objects, 2 humanoid robots
2. **VLA Task**: "Pick blue box from conveyor, place on shelf B3"
3. **Evaluation**: 50 trials with randomized object poses, lighting, clutter
4. **Deliverable**: Technical report analyzing success rate (target: 85%+), failure modes, sim-to-real gap (theoretical discussion)

### Optional: Partner Institution Visits

Coordinate with nearby universities or industry labs for **1-2 day field trips** where students observe/teleoperate physical humanoid robots. Provides hands-on exposure without capital investment.

---

## Setup Timeline

| Phase                    | Duration      | Description                          |
|--------------------------|---------------|--------------------------------------|
| **Procurement**          | 4-6 weeks     | Order workstations, network gear     |
| **Installation**         | 1 week        | Assemble workstations, network setup |
| **Software Setup**       | 1 week        | Install Ubuntu, ROS 2, Isaac Sim     |
| **Testing**              | 1 week        | Validate all software, example code  |
| **Faculty Training**     | 1 week        | Instructor familiarization          |
| **Total Setup Time**     | **8-10 weeks**|                                      |

**Recommendation**: Start setup 2-3 months before semester begins.

---

## Maintenance and TCO

### Annual Recurring Costs

| Cost Category              | Year 1    | Year 2    | Year 3    | 5-Year Total |
|----------------------------|----------:|----------:|----------:|-------------:|
| Initial Hardware           | $10,450   | $0        | $0        | $10,450      |
| Software Licenses          | $400      | $400      | $400      | $2,000       |
| Hardware Upgrades          | $0        | $0        | $2,000    | $2,000       |
| Consumables (misc)         | $200      | $200      | $200      | $1,000       |
| Facility Costs (power)     | $300      | $300      | $300      | $1,500       |
| **Total Annual Cost**      | **$11,350** | **$900** | **$2,900** | **$16,950**  |

**5-Year TCO**: ~$17K (extremely low compared to $50-180K physical robot tiers)

### Upgrade Path

After 2-3 years, if enrollment grows and funding increases:

1. **Add GPU Capacity**: +2 RTX 4070 workstations ($4,400) for 20-student capacity
2. **Transition to Miniature Tier**: Purchase 1 Unitree H1 ($90K) + safety gear ($5K) = $95K incremental

---

## Success Metrics

### Course Objectives Achieved

✅ **100% of learning objectives** met through simulation
✅ **Students can**:
- Design ROS 2 multi-robot systems
- Implement Nav2 navigation in Gazebo
- Generate synthetic datasets in Isaac Sim
- Train and deploy VLA models in simulation

### Limitations Acknowledged

⚠️ **Sim-to-Real Transfer**: Taught conceptually but not validated experimentally
⚠️ **Hardware Debugging**: Students miss experience troubleshooting sensor noise, motor failures
⚠️ **Safety Protocols**: Theoretical understanding only (no e-stop drills, collision recovery)

---

## Comparison: Proxy vs. Miniature Tier

| Feature                  | Proxy Tier         | Miniature Tier      |
|--------------------------|-------------------:|--------------------:|
| **Budget**               | $10-20K            | $50-70K             |
| **Physical Robots**      | 0                  | 1-2                 |
| **Student Capacity**     | 15                 | 10-12               |
| **Sim-to-Real**          | Theoretical        | Experimental        |
| **Industry Appeal**      | Moderate           | High                |
| **Maintenance Burden**   | Minimal            | Moderate            |

**Decision Point**: If budget allows $50K+, Miniature Tier provides significantly better student outcomes through hands-on physical robot experience.

---

## Next Steps

1. **Budget Approval**: Present this specification to department/administration
2. **Vendor Quotes**: Contact Dell, HP, or custom PC builders for workstation quotes
3. **Space Allocation**: Secure 150-250 sq ft classroom or lab space
4. **Software Licensing**: Register for Unity Educational license (requires .edu email)
5. **Timeline Planning**: Allow 8-10 weeks setup time before semester start

**Need Help?** Consult the [Deployment Options](/infrastructure/deployment-options) guide for vendor contacts and setup checklists.

---

## References

- [Lab Tiers Overview](/infrastructure/lab-tiers-overview)
- [Miniature Tier Comparison](/infrastructure/miniature-tier)
- [ROI Analysis](/appendices/roi-analysis)
