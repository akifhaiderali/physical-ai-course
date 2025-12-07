---
id: ros2-navigation
title: ROS 2 Navigation with Nav2
sidebar_position: 2
module: 1
learning_objectives:
  - "Configure the Nav2 navigation stack for autonomous mobile robot path planning and obstacle avoidance"
  - "Implement behavior trees for task-level navigation control with recovery behaviors"
  - "Analyze costmap representations and their role in safe trajectory generation"
  - "Deploy SLAM algorithms for simultaneous localization and mapping in unknown environments"
related_exercises:
  - ros2-navigation
related_references:
  - Macenski2020
word_count: 1420
last_updated: 2025-12-07
---

# ROS 2 Navigation with Nav2

## Introduction

Autonomous navigation represents one of the most critical capabilities for mobile robots, enabling them to traverse environments safely while avoiding obstacles and reaching goal locations. The ROS 2 Navigation Stack (Nav2) provides a production-ready framework for autonomous mobility, supporting applications from warehouse logistics robots to humanoid platforms navigating cluttered human environments.

Nav2 builds upon the lessons learned from ROS 1's navigation stack, introducing behavior trees for hierarchical task control, improved costmap algorithms for dynamic obstacle handling, and robust recovery mechanisms for failure scenarios. This chapter explores the Nav2 architecture, configuration strategies, and integration with humanoid robot platforms where bipedal locomotion adds complexity beyond wheeled mobile robots.

Understanding Nav2 is essential for Physical AI systems that must navigate real-world environments autonomously—a prerequisite for completing tasks specified through vision-language commands explored in Module 4.

## Learning Objectives

By the end of this chapter, you will be able to:

1. **Configure the Nav2 navigation stack** for autonomous mobile robot path planning and obstacle avoidance
2. **Implement behavior trees** for task-level navigation control with recovery behaviors
3. **Analyze costmap representations** and their role in safe trajectory generation
4. **Deploy SLAM algorithms** for simultaneous localization and mapping in unknown environments

## Nav2 Architecture Overview

### Core Components and Data Flow

The Nav2 stack consists of seven primary servers that collaborate to achieve autonomous navigation:

1. **Planner Server**: Computes global paths from start to goal using algorithms like NavFn (Dijkstra's) or Theta* (any-angle planning)
2. **Controller Server**: Generates velocity commands to follow planned paths, with plugins like DWB (Dynamic Window Approach) or TEB (Timed Elastic Band)
3. **Recoveries Server**: Executes fallback behaviors when navigation fails (e.g., rotate in place, back up)
4. **BT Navigator**: Coordinates servers through behavior tree logic, enabling complex task sequences
5. **Waypoint Follower**: Manages sequential navigation through multiple goal poses
6. **Smoother Server**: Refines paths for smoothness and kinematic feasibility
7. **Velocity Smoother**: Applies acceleration limits to controller outputs for safe execution

**Data Flow**: A navigation request triggers the BT Navigator, which calls the Planner Server for a global path. The Controller Server tracks this path while monitoring costmaps for obstacles, publishing velocity commands to the robot's mobile base. If the controller fails (e.g., local minimum), the BT invokes recovery behaviors before replanning.

### Behavior Trees: Hierarchical Task Control

Unlike ROS 1's state machine approach, Nav2 uses behavior trees (BTs) for navigation logic. BTs provide composability, allowing complex behaviors from simple reusable nodes:

- **Sequence Nodes**: Execute children in order until one fails (e.g., "compute path, then follow path")
- **Fallback Nodes**: Try children until one succeeds (e.g., "follow path, else execute recovery")
- **Decorator Nodes**: Modify child behavior (e.g., retry N times, run until condition)

**Default Navigation BT**:
```
Fallback (NavigateWithReplanning)
├─ Sequence
│  ├─ ComputePathToPose
│  └─ FollowPath
└─ RecoveryFallback
   ├─ ClearCostmap
   ├─ Rotate
   └─ BackUp
```

This structure encodes robust navigation: attempt path following, and if it fails, clear stale obstacles from the costmap, rotate to reorient sensors, or back away from tight spaces before replanning.

Behavior trees can be customized for humanoid-specific scenarios, such as adding "request human assistance" recovery when all autonomous strategies fail—critical for safe deployment in public spaces.

## Costmaps: Representing the Environment

### Layered Costmap Architecture

Nav2 costmaps represent the environment as 2D grids where each cell stores a cost from 0 (free space) to 254 (lethal obstacle), with 255 reserved for unknown regions. Costmaps fuse data from multiple sources through layered plugins:

1. **Static Layer**: Loads pre-built maps from SLAM or CAD drawings, marking known permanent obstacles
2. **Obstacle Layer**: Integrates real-time sensor data (LiDAR, depth cameras) for dynamic obstacles
3. **Inflation Layer**: Expands obstacles by robot radius plus safety margin, creating cost gradients
4. **Voxel Layer**: Extends obstacle tracking to 3D for robots with vertical sensors (humanoids looking down stairs)

**Configuration Trade-offs**: Large costmaps (20m x 20m at 5cm resolution = 160,000 cells) consume memory and CPU but provide lookahead for fast robots. Humanoid platforms often use smaller rolling costmaps (10m x 10m) centered on the robot, balancing computational constraints with bipedal walking speeds (~1 m/s).

### Global vs. Local Costmaps

Nav2 maintains two costmaps with distinct purposes:

- **Global Costmap**: Large, static or slowly-updating map for long-range path planning. Typically uses static layer + inflation, updated at 1-5 Hz.
- **Local Costmap**: Small, frequently-updated map for reactive obstacle avoidance. Includes obstacle layer, updated at 5-10 Hz to track pedestrians or dynamic objects.

This separation allows computationally expensive global planning (A*, Theta*) to run infrequently while the local controller (DWB) rapidly adjusts trajectories in response to sensor data.

## Path Planning Algorithms

### Global Planners: NavFn vs. Smac Planners

**NavFn (Navigation Function)**: Implements Dijkstra's algorithm over the costmap grid, guaranteeing optimal paths in configuration space. Efficient for simple environments but produces grid-aligned paths with unnecessary turns.

**Smac Planners** (State Lattice): Hybrid A* planners that search over both position and heading, generating smooth paths respecting non-holonomic constraints (differential drive, car-like steering). The Smac Hybrid planner suits humanoid robots where turning in place has a cost.

**Selection Criteria**: Use NavFn for initial prototyping, then switch to Smac planners when path quality affects task performance (e.g., VLA-driven manipulation requires precise final poses).

### Local Trajectory Control

The **DWB (Dynamic Window Approach) controller** samples velocity commands within the robot's dynamic constraints (max speed, acceleration), simulating forward trajectories and scoring them against:
- **Path alignment**: Distance to global plan
- **Obstacle proximity**: Clearance from lethal/inflated costs
- **Goal heading**: Alignment with final target orientation

The highest-scoring feasible trajectory is executed. Tuning DWB parameters (simulation time, velocity sampling granularity) balances safety (conservative) vs. efficiency (aggressive).

For humanoid platforms, DWB requires custom footprint definitions (bounding box or polygon) representing the robot's swept volume during walking, plus careful tuning of rotation-in-place costs to prefer smooth turning over abrupt stops.

## SLAM: Simultaneous Localization and Mapping

### SLAM-Toolbox for Unknown Environments

When pre-built maps are unavailable, SLAM algorithms build maps while estimating the robot's pose within them. **SLAM-Toolbox** (Macenski, 2020) provides ROS 2-native SLAM with:
- **Graph-based optimization**: Corrects accumulated drift through loop closure detection
- **Lifelong SLAM**: Updates maps over multiple sessions, handling environment changes
- **Serialization**: Saves/loads maps for reuse across deployments

**Configuration**: SLAM-Toolbox requires tuning scan matching parameters (correlation search space, resolution) and loop closure thresholds. Humanoid robots with head-mounted LiDAR benefit from IMU fusion to stabilize scans during walking vibrations.

### Localization with AMCL

Once a map exists, **AMCL (Adaptive Monte Carlo Localization)** estimates the robot's pose by matching sensor data to the map. AMCL uses particle filters to track pose uncertainty, converging through sensor updates and odometry predictions.

**Humanoid Considerations**: Bipedal odometry is noisier than wheeled robots due to foot slip and terrain compliance. Increasing AMCL's particle count (2000-5000) and tuning motion noise parameters improves localization accuracy at the cost of CPU usage.

## Integrating Nav2 with Humanoid Robots

### Footprint and Kinematic Constraints

Unlike wheeled robots with circular footprints, humanoids have rectangular swept volumes during walking. Nav2 supports polygon footprints defined in YAML:

```yaml
footprint: [[-0.3, -0.2], [0.3, -0.2], [0.3, 0.2], [-0.3, 0.2]]  # 0.6m x 0.4m
```

Additionally, humanoid gait controllers impose constraints:
- **Minimum turning radius**: Some gaits cannot pivot in place
- **Step frequency limits**: Acceleration bounds differ from wheeled platforms
- **Terrain awareness**: Nav2's 2D costmaps must integrate with 3D terrain analysis for stairs/ramps

Advanced integrations replace Nav2's default velocity commands with footstep planners that compute discrete foot placements respecting balance and collision constraints.

### Recovery Behaviors for Bipedal Locomotion

Standard Nav2 recoveries (rotate, back up) assume instantaneous velocity changes. Humanoid adaptations include:
- **Rebalance**: Pause navigation to regain stability before retrying
- **Sidestep**: Lateral motion when forward path is blocked
- **Request assistance**: Trigger operator notification when autonomous recovery fails

These behaviors are implemented as custom BT nodes loaded via Nav2's plugin architecture.

## Practical Deployment Considerations

### Sensor Selection and Placement

Nav2 supports multiple sensor types through the `sensor_msgs/LaserScan` and `sensor_msgs/PointCloud2` interfaces:
- **2D LiDAR**: 10-30m range, 270-360° coverage, robust for planar navigation
- **3D LiDAR**: Detects overhanging obstacles (tables, shelves) critical for humanoids
- **Depth Cameras**: Lower cost, shorter range (~5m), dense 3D data for manipulation zones

**Mounting**: Humanoid head mounts provide elevated viewpoints over clutter but introduce scan distortion from walking motion, requiring IMU-based stabilization.

### Performance Optimization

Nav2's computational footprint scales with costmap size and update frequency. Profiling typical scenarios:
- **Global planner**: 50-200ms per call (acceptable at 1 Hz)
- **Local controller**: 10-50ms per cycle (requires 10-20 Hz for reactive control)
- **Costmap updates**: 5-20ms (dominated by raytracing laser scans)

GPU acceleration (NVIDIA Jetson Orin) can offload costmap raytracing and DWB trajectory simulation, achieving real-time performance for large maps.

## Summary

This chapter explored the ROS 2 Navigation Stack (Nav2), covering its modular architecture, behavior tree coordination, and costmap-based planning. You learned to configure global and local planners, deploy SLAM for unknown environments, and adapt Nav2 for humanoid robot constraints.

Nav2 provides the autonomous mobility foundation for Physical AI systems. The next chapter extends these concepts to multi-robot coordination, where multiple humanoids share maps and negotiate paths collaboratively. Later modules integrate Nav2 with vision-language-action models, enabling navigation to semantically-defined goals ("go to the kitchen") rather than geometric waypoints.

## Next Steps

- **Hands-On**: Complete [Exercise 1.2: Autonomous Navigation with Nav2](/exercises/ros2-navigation) to configure and tune the navigation stack
- **Deep Dive**: Explore [Nav2 behavior tree XML](https://navigation.ros.org/behavior_trees/index.html) for custom task logic
- **Continue**: Proceed to [Chapter 3: Multi-Robot Coordination](/modules/module1-ros2/multi-robot-systems) for fleet management

## References

Macenski, S., Martín, F., White, R., & Clavero, J. G. (2020). The Marathon 2: A navigation system. In *2020 IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS)* (pp. 2718-2725). IEEE. https://doi.org/10.1109/IROS45743.2020.9341207

*Additional references covering behavior trees, SLAM-Toolbox, DWB controller, and humanoid navigation will be added during Phase 2 research tasks (T011-T016).*
