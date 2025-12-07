---
id: capstone-project
title: Capstone Project - VLA-Driven Humanoid Task Execution
sidebar_position: 1
duration: 4
team_size: 3
modules_integrated: "1, 2, 3, 4"
last_updated: 2025-12-07
---

# Capstone Project: VLA-Driven Humanoid Task Execution

## Project Overview

The capstone project integrates all four course modules to demonstrate autonomous task execution on humanoid robots using vision-language-action (VLA) models. Teams of 3 students design, implement, and evaluate a complete Physical AI system executing natural language commands.

**Example Tasks**:
- "Pick up the red mug and place it on the shelf"
- "Navigate to the kitchen and open the drawer"
- "Rearrange objects on the table by color"

## Learning Objectives

Upon completion, students will be able to:

1. **Integrate** ROS 2 navigation (Module 1) with VLA-based task planning (Module 4)
2. **Generate** synthetic training data using Isaac Sim domain randomization (Module 3)
3. **Deploy and evaluate** sim-to-real transfer on physical humanoid robots
4. **Design** safety mechanisms and failure recovery for VLA control systems
5. **Analyze** performance metrics including task success rate, execution time, and reality gap

## Project Requirements

### Functional Requirements

1. **Natural Language Interface**: Accept task commands via text or speech
2. **Perception**: Process RGB-D camera input to detect objects and obstacles
3. **Planning**: Use VLA model to generate manipulation actions
4. **Navigation**: Integrate Nav2 for mobile base control (if applicable)
5. **Safety**: Implement joint limit checking, collision avoidance, e-stop handling

### Technical Requirements

- **ROS 2 Humble**: All components communicate via ROS 2
- **Simulation**: Test in Isaac Sim or Gazebo before physical deployment
- **VLA Model**: Use OpenVLA or fine-tuned RT-2 variant
- **Hardware**: Deploy to Unitree H1 (Miniature tier) or simulation (Proxy tier)

## Deliverables

| Deliverable            | Due Week | Format                     | Weight |
|------------------------|----------|----------------------------|--------|
| **Project Proposal**   | Week 13  | 2-page PDF                 | 10%    |
| **Simulation Demo**    | Week 14  | 5-min video + code repo    | 25%    |
| **Physical Demo**      | Week 15  | 3-min video (if applicable)| 15%    |
| **Final Presentation** | Week 16  | 15-min slides + Q&A        | 30%    |
| **Technical Report**   | Week 16  | 10-15 page report          | 20%    |

## Assessment Rubric

### Technical Implementation (40%)

| Criterion                          | Excellent (9-10)              | Good (7-8)                   | Needs Work (5-6)             |
|------------------------------------|-------------------------------|------------------------------|------------------------------|
| **ROS 2 Integration**              | All modules communicate correctly | Minor topic/service issues   | Frequent communication failures |
| **VLA Model Performance**          | 85%+ task success in sim      | 70-84% success               | &lt;70% success                 |
| **Sim-to-Real Transfer**           | &lt;15% performance gap          | 15-30% gap                   | >30% gap                     |
| **Safety Implementation**          | Comprehensive checks, e-stop  | Basic joint limits only      | No safety mechanisms         |

### Sim-to-Real Performance (30%)

**Metric**: Task success rate on physical robot (or extended simulation for Proxy tier)

- **90-100% of sim performance**: 27-30 pts
- **80-89% of sim performance**: 24-26 pts
- **70-79% of sim performance**: 21-23 pts
- **Below 70% of sim performance**: 0-20 pts

### Documentation and Presentation (30%)

| Component                | Weight | Criteria                                  |
|--------------------------|--------|-------------------------------------------|
| **Proposal**             | 10%    | Clear task definition, realistic timeline |
| **Simulation Demo**      | 25%    | 10 successful trials, failure analysis    |
| **Final Presentation**   | 30%    | Technical depth, clear visuals, Q&A       |
| **Technical Report**     | 20%    | Methods, results, discussion, references  |
| **Code Quality**         | 15%    | Documentation, testing, version control   |

## Timeline

### Week 13: Proposal Phase

**Activities**:
- Form teams of 3 students
- Select task from provided list or propose custom task
- Design system architecture (ROS 2 nodes, data flow)
- Identify risks and mitigation strategies

**Proposal Contents**:
1. Task specification (natural language command)
2. System architecture diagram
3. Module integration plan (ROS 2, Isaac Sim, VLA)
4. Timeline with milestones
5. Team responsibilities

**Approval**: Instructor reviews proposals and provides feedback by end of Week 13

### Week 14: Simulation Demonstration

**Milestones**:
- Complete Isaac Sim environment setup
- Integrate VLA model with ROS 2 navigation
- Generate synthetic training data (if training custom model)
- Achieve 90%+ task success in simulation

**Submission**: 5-minute video demonstrating:
- System overview (30 sec)
- 10 successful task executions with randomized scenes (3 min)
- Failure mode analysis (90 sec)
- Code repository link (GitHub)

### Week 15: Physical Deployment (Optional)

**For Miniature/Premium Tiers**:
- Deploy to Unitree H1 or other humanoid
- Run 20 real-world trials
- Measure success rate, execution time, safety incidents

**For Proxy Tier**:
- Extended simulation scenarios (multi-robot, long-horizon tasks)
- Theoretical analysis of sim-to-real gap

### Week 16: Final Presentation and Report

**Presentation Format** (15 min + 5 min Q&A):
1. Introduction and motivation (2 min)
2. System architecture (3 min)
3. Simulation results with metrics (4 min)
4. Physical deployment results (3 min)
5. Lessons learned and future work (3 min)

**Technical Report Structure**:
1. Abstract (200 words)
2. Introduction and related work (2 pages)
3. Methods (ROS 2 setup, VLA training, simulation config) (3-4 pages)
4. Results (tables, graphs, statistical analysis) (3-4 pages)
5. Discussion (sim-to-real gap, failure analysis) (2 pages)
6. Conclusion and future work (1 page)
7. References (APA format, minimum 15 sources)

## Example Project: "Warehouse Restocking Assistant"

**Task**: "Move all red boxes from the conveyor to shelf A3"

**System Components**:
1. **Perception**: RGB-D camera detects red boxes, estimates poses
2. **VLA Model**: OpenVLA fine-tuned on box manipulation dataset
3. **Navigation**: Nav2 navigates between conveyor and shelf
4. **Manipulation**: MoveIt2 plans arm trajectories, gripper control
5. **Coordination**: State machine sequences pick-place-navigate loops

**Evaluation**:
- **Simulation**: 20 boxes, randomized poses, 95% success rate
- **Physical Robot**: 10 boxes, 85% success rate (10% sim-to-real gap)
- **Failure Modes**: Grasp slippage (5%), collision with shelf (5%), localization drift (5%)

## Common Pitfalls and Solutions

### Pitfall 1: Overambitious Scope

**Problem**: Teams propose multi-step tasks requiring hierarchical planning (e.g., "make coffee")

**Solution**: Limit to single-step VLA commands. Use state machines for sequencing, not expecting VLA to plan multi-step tasks.

### Pitfall 2: Insufficient Simulation Testing

**Problem**: Teams rush to physical robot, encounter failures due to untested edge cases

**Solution**: Enforce 90%+ simulation success before allowing physical deployment.

### Pitfall 3: Ignoring Safety

**Problem**: VLA commands unsafe actions, risking robot damage

**Solution**: Implement MoveIt2 collision checking, joint limit validation as mandatory pre-execution checks.

## Resources

**Hardware Access**:
- GPU workstations: Available 24/7 in lab
- Physical robots: Sign up for 2-hour time slots (max 6 hrs/week per team)

**Software Support**:
- Pre-trained VLA models: OpenVLA-7B, RT-2-Small checkpoints provided
- Isaac Sim templates: Warehouse, kitchen, office scenes available
- ROS 2 packages: Nav2, MoveIt2 pre-configured for Unitree H1

**Instructor Support**:
- Office hours: 4 hours/week for debugging assistance
- Slack channel: Real-time Q&A with TAs

## Grading Example

**Team "Robotic Restock"**:
- **Proposal**: 9/10 (clear task, realistic timeline)
- **Simulation Demo**: 23/25 (92% success, good failure analysis)
- **Physical Demo**: 13/15 (88% of sim performance)
- **Presentation**: 26/30 (solid technical content, weak Q&A responses)
- **Report**: 17/20 (good methods, limited discussion of sim-to-real gap)

**Total**: 88/100 (B+ grade)

## Next Steps

- Review the [Week-by-Week Schedule](/appendices/week-by-week) for capstone timeline
- Explore [VLA Deployment](/modules/module4-vla/vla-deployment) for integration patterns
- Consult [Lab Infrastructure](/category/lab-infrastructure) for hardware specifications

**Questions?** Open an issue on the [course GitHub](https://github.com/your-organization/physical-ai-course/issues).
