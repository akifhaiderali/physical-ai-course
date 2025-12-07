---
id: week-by-week
title: Week-by-Week Schedule
sidebar_position: 2
semester_length: 16
last_updated: 2025-12-07
---

# Week-by-Week Schedule

This schedule maps the 4-module Physical AI & Humanoid Robotics Course to a **16-week semester**. Adapt this timeline to 12-14 week terms by reducing capstone duration or condensing simulation modules.

---

## Semester Overview

| Weeks    | Module                        | Focus                                        |
|----------|-------------------------------|----------------------------------------------|
| 1-4      | Module 1: ROS 2 Fundamentals  | Robot middleware, navigation, multi-robot    |
| 5-7      | Module 2: Simulation          | Gazebo physics, Unity visualization          |
| 8-9      | Module 3: NVIDIA Isaac Sim    | Synthetic data, domain randomization         |
| 10-12    | Module 4: VLA Models          | Vision-language-action, multimodal AI        |
| 13-16    | Capstone Project              | Integrative humanoid robot project           |

---

## Week 1: Introduction to ROS 2

**Module**: 1 - ROS 2 Fundamentals

**Topics**:
- Course overview and Physical AI landscape
- ROS 2 architecture and DDS middleware
- Nodes, topics, publishers, and subscribers
- Setting up ROS 2 Humble development environment

**Exercises**:
- [Exercise 1.1: Building a ROS 2 Talker-Listener System](/exercises/ros2-talker-listener)

**Readings**:
- [Chapter 1: ROS 2 Fundamentals](/modules/module1-ros2/ros2-fundamentals)

**Assessments**:
- Lab Report 1: Talker-Listener implementation and analysis (due Week 2)

---

## Week 2: ROS 2 Services, Actions, and Parameters

**Module**: 1 - ROS 2 Fundamentals

**Topics**:
- Services for synchronous request-response
- Actions for long-running tasks with feedback
- Parameters and dynamic reconfiguration
- Launch files for multi-node orchestration

**Exercises**:
- [Exercise 1.2: Custom ROS 2 Service Implementation](/exercises/ros2-custom-service)

**Readings**:
- [Chapter 1: ROS 2 Fundamentals](/modules/module1-ros2/ros2-fundamentals) (continued)

**Assessments**:
- Quiz 1: ROS 2 communication patterns (10 pts)

---

## Week 3: Autonomous Navigation with Nav2

**Module**: 1 - ROS 2 Fundamentals

**Topics**:
- Nav2 stack architecture (planner, controller, recoveries)
- Behavior trees for navigation control
- Costmaps: static, obstacle, inflation layers
- Path planning algorithms (NavFn, Smac)

**Exercises**:
- [Exercise 1.3: Nav2 Configuration and Tuning](/exercises/ros2-navigation)

**Readings**:
- [Chapter 2: ROS 2 Navigation with Nav2](/modules/module1-ros2/ros2-navigation)

**Assessments**:
- None (focus on complex exercise)

---

## Week 4: Multi-Robot Coordination

**Module**: 1 - ROS 2 Fundamentals

**Topics**:
- Namespace isolation and topic remapping
- DDS domain IDs and discovery mechanisms
- Task allocation (centralized vs. distributed)
- Multi-robot collision avoidance

**Exercises**:
- [Exercise 1.4: Multi-Robot Task Coordination](/exercises/multi-robot-coordination)

**Readings**:
- [Chapter 3: Multi-Robot Coordination](/modules/module1-ros2/multi-robot-systems)

**Assessments**:
- Module 1 Exam: ROS 2 fundamentals, navigation, multi-robot (20 pts, Week 5)

---

## Week 5: Gazebo Simulation - Robot Modeling

**Module**: 2 - Simulation Environments

**Topics**:
- Gazebo architecture (Classic vs. Fortress)
- URDF and SDF robot description formats
- Physics engine configuration (ODE, Bullet, DART)
- Inertial properties and contact dynamics

**Exercises**:
- [Exercise 2.1: Creating Robot Models in Gazebo](/exercises/gazebo-urdf-modeling)

**Readings**:
- [Chapter 4: Robot Simulation with Gazebo](/modules/module2-simulation/gazebo-simulation)

**Assessments**:
- Lab Report 2: URDF humanoid model design (due Week 6)

---

## Week 6: Gazebo Simulation - Sensors and ROS 2 Integration

**Module**: 2 - Simulation Environments

**Topics**:
- Camera, depth, and lidar sensor simulation
- Sensor noise models for realism
- Gazebo-ROS 2 bridge (ros_gz)
- Hardware-in-the-loop testing workflow

**Exercises**:
- [Exercise 2.2: World Design and Sensor Integration](/exercises/gazebo-world-design)

**Readings**:
- [Chapter 4: Robot Simulation with Gazebo](/modules/module2-simulation/gazebo-simulation) (continued)

**Assessments**:
- Quiz 2: Gazebo sensors and physics (10 pts)

---

## Week 7: Unity for High-Fidelity Visualization

**Module**: 2 - Simulation Environments

**Topics**:
- Unity Robotics Hub architecture
- URDF importer and ROS-TCP-Connector
- Photorealistic rendering (URP/HDRP)
- VR/AR teleoperation interfaces

**Exercises**:
- [Exercise 2.3: Unity-ROS 2 Visualization](/exercises/unity-ros2-integration)

**Readings**:
- [Chapter 5: High-Fidelity Visualization with Unity](/modules/module2-simulation/unity-visualization)

**Assessments**:
- Module 2 Project: Multi-robot Gazebo simulation with Unity visualization (30 pts, due Week 8)

---

## Week 8: NVIDIA Isaac Sim Fundamentals

**Module**: 3 - NVIDIA Isaac Sim

**Topics**:
- Omniverse platform and Nucleus database
- USD (Universal Scene Description) format
- GPU-accelerated physics with PhysX 5
- Isaac ROS Bridge for sensor data streaming

**Exercises**:
- [Exercise 3.1: Isaac Sim Setup and Scene Design](/exercises/isaac-sim-setup)

**Readings**:
- [Chapter 6: NVIDIA Isaac Sim Fundamentals](/modules/module3-isaac/isaac-sim-basics)

**Assessments**:
- Lab Report 3: Isaac Sim performance comparison vs. Gazebo (due Week 9)

---

## Week 9: Synthetic Data Generation and Domain Randomization

**Module**: 3 - NVIDIA Isaac Sim

**Topics**:
- Domain randomization theory (addressing reality gap)
- Texture, lighting, and object pose randomization
- Synthetic data annotation (bounding boxes, segmentation)
- Sim-to-real validation protocols

**Exercises**:
- [Exercise 3.2: Synthetic Data Generation Pipeline](/exercises/isaac-synthetic-data)

**Readings**:
- [Chapter 7: Synthetic Data Generation and Domain Randomization](/modules/module3-isaac/synthetic-data-generation)

**Assessments**:
- Module 3 Assignment: Generate 10K-image synthetic dataset with validation report (25 pts, due Week 10)

---

## Week 10: Vision-Language-Action (VLA) Introduction

**Module**: 4 - Vision-Language-Action Models

**Topics**:
- VLA problem formulation (multimodal transformers)
- Evolution: RT-1, RT-2, OpenVLA
- Task specification with natural language
- Model architecture (vision encoder, language encoder, action decoder)

**Exercises**:
- [Exercise 4.1: VLA Inference with OpenVLA](/exercises/vla-inference)

**Readings**:
- [Chapter 8: Vision-Language-Action Models - Introduction](/modules/module4-vla/vla-introduction)

**Assessments**:
- Quiz 3: VLA architectures and multimodal learning (10 pts)

---

## Week 11: VLA Training and Fine-Tuning

**Module**: 4 - Vision-Language-Action Models

**Topics**:
- Training pipelines (Open-X Embodiment dataset)
- Fine-tuning pretrained VLA for humanoid platforms
- Data augmentation for sim-to-real transfer
- Inference optimization (quantization, batching)

**Exercises**:
- [Exercise 4.2: VLA Model Fine-Tuning](/exercises/vla-fine-tuning)

**Readings**:
- [Chapter 9: VLA Implementation and Training](/modules/module4-vla/vla-implementation)

**Assessments**:
- Lab Report 4: VLA fine-tuning results and performance analysis (due Week 12)

---

## Week 12: VLA Deployment on Humanoid Robots

**Module**: 4 - Vision-Language-Action Models

**Topics**:
- VLA-ROS 2 integration architecture
- Safety mechanisms (joint limits, collision checking, e-stop)
- Performance evaluation (task success rate, execution time)
- Human-in-the-loop task specification and monitoring

**Exercises**:
- [Exercise 4.3: VLA Deployment on Physical Humanoid](/exercises/vla-deployment)

**Readings**:
- [Chapter 10: VLA Deployment on Humanoid Robots](/modules/module4-vla/vla-deployment)

**Assessments**:
- Module 4 Exam: VLA models, training, deployment (20 pts, Week 13)

---

## Week 13: Capstone Project - Proposal and Planning

**Module**: Capstone Project

**Topics**:
- Capstone project requirements and rubric review
- Team formation (3 students per team)
- Task selection and scope definition
- System architecture design (ROS 2 + Isaac Sim + VLA)

**Deliverables**:
- **Capstone Proposal** (due end of Week 13):
  - Task specification (natural language command)
  - System architecture diagram
  - Timeline with milestones
  - Risk analysis and mitigation strategies

**Readings**:
- [Capstone Project Specification](/capstone/capstone-project)

**Assessments**:
- Capstone Proposal: 10% of capstone grade

---

## Week 14: Capstone Project - Simulation Demonstration

**Module**: Capstone Project

**Milestones**:
- Complete Isaac Sim simulation environment
- Integrate VLA model with ROS 2 navigation/manipulation stacks
- Generate synthetic training data (if training custom VLA)
- Demonstrate task execution in simulation (90%+ success rate)

**Deliverables**:
- **Simulation Demo Video** (5 minutes, due end of Week 14):
  - Narrated walkthrough of system components
  - 10 successful task executions in varied scenarios
  - Analysis of failure modes and proposed fixes

**Support**:
- Instructor office hours: 4 hours/week for debugging assistance
- Lab access: 24/7 for simulation work

**Assessments**:
- Simulation Demo: 25% of capstone grade

---

## Week 15: Capstone Project - Physical Robot Deployment (Optional)

**Module**: Capstone Project

**Milestones** (for Miniature/Premium lab tiers only):
- Deploy VLA model to physical humanoid robot
- Conduct 20 real-world task trials
- Measure task success rate, safety violations, execution time
- Compare sim-to-real performance gap

**Deliverables**:
- **Physical Demo Video** (3 minutes, optional):
  - 5 successful real-world task executions
  - Comparison table: simulation vs. reality metrics

**Note**: Proxy tier students complete extended simulation scenarios (multi-robot, long-horizon tasks) instead of physical deployment.

**Assessments**:
- Physical Demo (if applicable): 15% of capstone grade (bonus for Proxy tier)

---

## Week 16: Capstone Project - Final Presentation

**Module**: Capstone Project

**Deliverables**:
- **Final Presentation** (15 minutes + 5 min Q&A, during Week 16 finals period):
  - Problem statement and motivation
  - System architecture and design decisions
  - Simulation results (quantitative metrics)
  - Physical deployment results (if applicable)
  - Lessons learned and future work

- **Technical Report** (10-15 pages, due end of Week 16):
  - Introduction and related work
  - Methods (ROS 2 setup, VLA training, simulation config)
  - Results (tables, graphs, statistical analysis)
  - Discussion (sim-to-real gap, failure analysis)
  - Conclusion and recommendations
  - References (APA format, minimum 15 sources)

**Assessments**:
- Final Presentation: 30% of capstone grade
- Technical Report: 20% of capstone grade

**Total Capstone Grade Breakdown**:
- Proposal: 10%
- Simulation Demo: 25%
- Physical Demo: 15% (or extended simulation for Proxy tier)
- Final Presentation: 30%
- Technical Report: 20%
- **Total**: 100 points (25% of overall course grade)

---

## Grading Summary (Entire Course)

| Component            | Weight | Details                                      |
|----------------------|--------|----------------------------------------------|
| **Lab Reports**      | 20%    | 4 reports × 5% each (Weeks 1, 5, 8, 11)     |
| **Quizzes**          | 15%    | 3 quizzes × 5% each (Weeks 2, 6, 10)        |
| **Module Exams**     | 20%    | 2 exams × 10% each (Weeks 5, 12)            |
| **Module Projects**  | 20%    | Module 2 (15%) + Module 3 (5%) + Module 4 (0%) |
| **Capstone Project** | 25%    | See Week 16 breakdown above                  |
| **Total**            | 100%   |                                              |

---

## Adaptation Guidelines

### For 12-Week Semesters

**Compressed Schedule**:
- **Weeks 1-3**: Module 1 (combine navigation + multi-robot into Week 3)
- **Weeks 4-5**: Module 2 (Gazebo + Unity combined)
- **Weeks 6-7**: Module 3 (Isaac Sim + synthetic data)
- **Weeks 8-9**: Module 4 (VLA intro + implementation, skip deployment chapter)
- **Weeks 10-12**: Capstone (proposal + simulation only, skip physical deployment)

**Trade-off**: Less depth in each module, no physical robot testing.

### For 14-Week Semesters

**Moderate Compression**:
- **Weeks 1-4**: Module 1 (unchanged)
- **Weeks 5-6**: Module 2 (Gazebo + Unity in 2 weeks)
- **Weeks 7-8**: Module 3 (Isaac Sim + synthetic data)
- **Weeks 9-11**: Module 4 (VLA intro + implementation + deployment)
- **Weeks 12-14**: Capstone (proposal + simulation + final presentation, optional physical demo)

**Trade-off**: Reduced capstone time, physical deployment only for advanced teams.

### For Advanced Tracks (Graduate Level)

**Extended Topics** (16+ weeks):
- **Week 17**: Advanced VLA topics (hierarchical planning, multi-task learning)
- **Week 18**: Fleet-scale deployment (10+ humanoid coordination)
- **Weeks 19-20**: Research paper writing and conference-style presentations

---

## Prerequisites Checklist

Before Week 1, students should have:

- [ ] **Programming**: Python (intermediate) and C++ (basic)
- [ ] **Robotics**: Completed undergraduate robotics course (kinematics, sensors, actuators)
- [ ] **Linux**: Comfortable with terminal, package managers (apt), basic bash scripting
- [ ] **Machine Learning**: Familiarity with neural networks, computer vision concepts
- [ ] **Math**: Linear algebra (transformations, matrices), probability (Gaussian distributions)

**Recommended Pre-Course Resources**:
- ROS 2 Humble tutorials: https://docs.ros.org/en/humble/Tutorials.html
- Python refresher: Real Python (https://realpython.com/)
- Linear algebra review: MIT OCW 18.06

---

## Lab Infrastructure Requirements by Week

| Week     | Required Infrastructure                                    |
|----------|-----------------------------------------------------------|
| 1-4      | ROS 2 Humble workstations (Proxy tier sufficient)        |
| 5-7      | Gazebo + Unity workstations (GPU recommended)            |
| 8-9      | NVIDIA Isaac Sim workstations (RTX 2060+ required)       |
| 10-12    | GPU workstations for VLA inference (RTX 3060+ recommended)|
| 13-16    | Physical humanoid robots (Miniature/Premium tier) or extended simulation (Proxy tier) |

---

## Additional Resources

- **Office Hours**: Instructor 2 hrs/week, TA 4 hrs/week
- **Discussion Forum**: Slack/Discord for peer collaboration
- **Code Repository**: GitHub Classroom for assignment submissions
- **Lab Safety Training**: Required before Week 15 physical robot access

---

## References

- [Course Introduction](/intro)
- [Lab Infrastructure Options](/category/lab-infrastructure)
- [Capstone Project Details](/capstone/capstone-project)
- [Glossary of Terms](/appendices/glossary)
