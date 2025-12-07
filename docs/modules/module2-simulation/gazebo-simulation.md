---
id: gazebo-simulation
title: Robot Simulation with Gazebo
sidebar_position: 1
module: 2
learning_objectives:
  - "Design robot models using URDF and SDF formats with accurate kinematic and dynamic properties"
  - "Configure Gazebo physics engines for realistic sensor simulation and contact dynamics"
  - "Integrate Gazebo with ROS 2 for hardware-in-the-loop testing and algorithm validation"
  - "Evaluate simulation fidelity trade-offs between real-time performance and physical accuracy"
related_exercises:
  - gazebo-urdf-modeling
  - gazebo-world-design
related_references:
  - Macenski2020
word_count: 1450
last_updated: 2025-12-07
---

# Robot Simulation with Gazebo

## Introduction

Simulation serves as the critical bridge between algorithmic development and physical deployment in robotics. Gazebo, an open-source 3D robot simulator, provides high-fidelity physics simulation, sensor models, and seamless ROS 2 integration, enabling developers to test navigation algorithms, manipulation policies, and multi-robot coordination before risking hardware damage or safety incidents.

For Physical AI systems, simulation offers three strategic advantages: **accelerated iteration** (testing thousands of scenarios overnight), **cost reduction** (validating algorithms without expensive hardware), and **safety** (exploring failure modes in virtual environments). Gazebo has become the de facto standard for academic robotics research and increasingly appears in industry prototyping workflows, particularly for humanoid platforms where physical testing is resource-intensive.

This chapter explores Gazebo's architecture, robot modeling with URDF/SDF, physics engine configuration, and integration patterns with ROS 2. These skills enable you to create digital twins of humanoid robots for algorithm development in Module 3 (synthetic data generation with Isaac Sim) and Module 4 (VLA policy training).

## Learning Objectives

By the end of this chapter, you will be able to:

1. **Design robot models** using URDF and SDF formats with accurate kinematic and dynamic properties
2. **Configure Gazebo physics engines** for realistic sensor simulation and contact dynamics
3. **Integrate Gazebo with ROS 2** for hardware-in-the-loop testing and algorithm validation
4. **Evaluate simulation fidelity trade-offs** between real-time performance and physical accuracy

## Gazebo Architecture and Versions

### Gazebo Classic vs. Gazebo (Ignition/Fortress)

**Gazebo Classic** (versions 1-11, final release 2025) dominated ROS 1 era but is deprecated in favor of **Gazebo** (formerly Ignition, now unified naming). Gazebo Fortress (current stable) and Garden (latest) offer:

- **Modular architecture**: Physics, rendering, and sensors as separate libraries, allowing custom engine integration
- **Performance**: Multi-threaded physics and rendering for real-time simulation of complex robots
- **Ogre 2.x rendering**: Physically-based materials and lighting for photorealistic sensor data
- **Distributed simulation**: Run physics and rendering on separate machines for large-scale scenarios

**ROS 2 Compatibility**: Use `ros_gz` (formerly `ros_ign`) bridge packages for topic/service translation between ROS 2 and Gazebo. This chapter focuses on Gazebo Fortress integrated with ROS 2 Humble.

### Core Components

1. **Physics Engine**: Simulates rigid body dynamics, contact forces, joint constraints. Supports ODE, Bullet, DART, and Simbody backends.
2. **Rendering Engine**: Generates camera images, depth maps, lidar point clouds using Ogre 2.x GPU rendering.
3. **Sensor Manager**: Provides plugins for cameras, lidar, IMU, contact sensors with configurable noise models.
4. **World Manager**: Loads SDF world files defining robots, environments, and lighting.
5. **Plugin System**: Allows custom robot controllers, sensor processing, and world modifications via C++ shared libraries.

## Robot Modeling: URDF vs. SDF

### URDF (Unified Robot Description Format)

URDF, the ROS standard for robot kinematics, describes robots as trees of links (rigid bodies) connected by joints (kinematic constraints). Originally designed for kinematic visualization, URDF was extended with Gazebo-specific tags for dynamics and sensors.

**Example** (simplified humanoid leg):
```xml
<robot name="humanoid">
  <link name="thigh">
    <inertial>
      <mass value="5.0"/>
      <inertia ixx="0.1" ixy="0" ixz="0" iyy="0.1" iyz="0" izz="0.05"/>
    </inertial>
    <visual>
      <geometry><cylinder radius="0.05" length="0.4"/></geometry>
    </visual>
    <collision>
      <geometry><cylinder radius="0.05" length="0.4"/></geometry>
    </collision>
  </link>

  <joint name="hip" type="revolute">
    <parent link="pelvis"/>
    <child link="thigh"/>
    <axis xyz="0 1 0"/>
    <limit lower="-1.57" upper="1.57" effort="100" velocity="2.0"/>
  </joint>
</robot>
```

**Gazebo Extensions**:
```xml
<gazebo reference="thigh">
  <material>Gazebo/DarkGrey</material>
  <mu1>0.8</mu1>  <!-- Friction coefficient -->
  <mu2>0.8</mu2>
</gazebo>
```

**Limitations**: URDF's tree structure cannot represent closed kinematic chains (e.g., parallel linkages in humanoid feet), requiring workarounds with fixed joints or SDF.

### SDF (Simulation Description Format)

SDF extends URDF with first-class support for simulation-specific properties: multiple models per file, closed-loop kinematics, and sensor/plugin declarations without extensions.

**Advantages for Humanoid Robotics**:
- **Model composition**: Include pre-built sub-models (grippers, sensors) via `<include>` tags
- **State specification**: Define initial joint positions and velocities for reproducible scenarios
- **World integration**: Embed robots, terrains, and lighting in single SDF world files

**Conversion**: Use `gz sdf -p robot.urdf > robot.sdf` to convert URDF to SDF, though manual editing is typically required to optimize inertial properties and sensor configurations.

## Physics Engine Configuration

### Choosing a Physics Backend

**ODE (Open Dynamics Engine)**: Default in Gazebo Classic, stable for most robots, moderate performance. Best for initial prototyping.

**Bullet**: Faster contact handling, better for multi-robot simulations with frequent collisions (warehouse fleets). Slightly less stable for complex articulated robots.

**DART (Dynamic Animation and Robotics Toolkit)**: Most accurate for humanoids, supports advanced features like soft contacts and muscle models. Higher computational cost (60-70% slower than ODE).

**Selection Guideline**: Use ODE for navigation algorithms, DART for manipulation and bipedal locomotion where contact accuracy matters.

### Simulation Time Step and Real-Time Factor

**Time Step**: Smaller steps (1 ms) improve stability for fast dynamics (humanoid running) but reduce real-time factor (RTF). Larger steps (10 ms) achieve RTF > 1 (faster than real-time) but risk instability.

**Configuration** (SDF):
```xml
<physics name="default_physics">
  <max_step_size>0.001</max_step_size>  <!-- 1 ms -->
  <real_time_factor>1.0</real_time_factor>
  <real_time_update_rate>1000</real_time_update_rate>  <!-- Hz -->
</physics>
```

**Trade-off**: Humanoid balance control often requires 1 ms steps for stability, limiting RTF to 0.5-0.8 on standard workstations. GPU-accelerated physics (via NVIDIA PhysX in Gazebo's roadmap) promises RTF > 1 for complex robots.

### Contact Dynamics and Friction

Accurate foot-ground contact is critical for humanoid simulation. Key parameters:

- **mu (friction coefficient)**: 0.8-1.2 for rubber feet on concrete, 0.3-0.5 for smooth surfaces
- **kp/kd (contact stiffness/damping)**: Higher stiffness (1e6) prevents penetration but requires smaller time steps
- **max_contacts**: Limit contact points (typically 4-6 per foot) to balance accuracy and performance

**Tuning Approach**: Calibrate friction by comparing sim-to-real push recovery tests—if the simulated robot slips more/less than reality, adjust `mu` iteratively.

## Sensor Simulation

### Camera and Depth Sensors

Gazebo's rendering engine generates RGB images, depth maps, and semantic segmentation:

**RGB Camera Plugin**:
```xml
<sensor name="camera" type="camera">
  <update_rate>30</update_rate>
  <camera>
    <horizontal_fov>1.57</horizontal_fov>  <!-- 90 degrees -->
    <image>
      <width>640</width>
      <height>480</height>
    </image>
  </camera>
  <plugin name="camera_plugin" filename="libgazebo_ros_camera.so">
    <ros><namespace>/robot1</namespace></ros>
  </plugin>
</sensor>
```

**Depth Camera**: Adds `<depth>` tag with near/far clip planes. Outputs `sensor_msgs/PointCloud2` for integration with perception pipelines.

**Noise Models**: Gaussian noise simulates sensor imperfections:
```xml
<noise>
  <type>gaussian</type>
  <mean>0.0</mean>
  <stddev>0.007</stddev>  <!-- Kinect-like depth noise -->
</noise>
```

### Lidar Simulation

3D lidar (Velodyne, Ouster) uses GPU raycasting for point cloud generation:

```xml
<sensor name="lidar" type="gpu_lidar">
  <update_rate>10</update_rate>
  <lidar>
    <scan>
      <horizontal><samples>1024</samples><min_angle>-3.14</min_angle><max_angle>3.14</max_angle></horizontal>
      <vertical><samples>64</samples><min_angle>-0.26</min_angle><max_angle>0.26</max_angle></vertical>
    </scan>
    <range><min>0.1</min><max>100</max></range>
  </lidar>
</sensor>
```

**Performance**: 64-beam lidar at 10 Hz typically achieves RTF 0.8-1.0 on NVIDIA RTX 3060. For faster simulation, reduce vertical samples or use 2D lidar (`ray` sensor type).

## ROS 2 Integration

### Gazebo-ROS 2 Bridge

The `ros_gz_bridge` translates Gazebo transport (Ignition Transport) to ROS 2 DDS:

**Launch File Integration**:
```python
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        # Launch Gazebo server
        IncludeLaunchDescription('gazebo_ros/launch/gazebo.launch.py'),

        # Spawn robot from URDF
        Node(
            package='gazebo_ros',
            executable='spawn_entity.py',
            arguments=['-entity', 'humanoid', '-file', 'robot.sdf']
        ),

        # Bridge camera topic
        Node(
            package='ros_gz_bridge',
            executable='parameter_bridge',
            arguments=['/camera/image_raw@sensor_msgs/msg/Image@gz.msgs.Image']
        )
    ])
```

### Hardware-in-the-Loop Testing

Simulation validates algorithms before hardware deployment:

1. **Develop** navigation stack in Gazebo with URDF humanoid model
2. **Test** obstacle avoidance scenarios (narrow corridors, dynamic pedestrians)
3. **Tune** controller gains (DWB parameters) for smooth motion
4. **Deploy** identical ROS 2 launch file to physical robot, replacing Gazebo sensor topics with real hardware

**Sim-to-Real Gap**: Chapter 7 (Module 3) addresses differences between simulated and physical sensors through domain randomization and transfer learning.

## World Design for Testing

### Procedural vs. Hand-Crafted Worlds

**Hand-Crafted**: Manually place obstacles, furniture, stairs in SDF. High control but time-intensive.

**Procedural**: Generate random environments from templates (e.g., warehouse aisles with variable shelf spacing). Enables automated testing across thousands of scenarios.

**Tool**: Use Gazebo's Building Editor for indoor environments or `blender_to_sdf` converters for CAD imports.

### Testing Scenarios for Humanoid Robots

1. **Flat terrain navigation**: Validate basic locomotion and obstacle avoidance
2. **Stairs and ramps**: Test terrain adaptation and balance on inclines
3. **Cluttered spaces**: Tight doorways, furniture mazes for path planning
4. **Multi-robot coordination**: Spawn 3-5 robots to test collision avoidance and task allocation (Chapter 3 concepts)

## Practical Performance Optimization

### GPU Acceleration

Enable GPU rendering and physics (when available):

```xml
<world name="default">
  <physics type="bullet">
    <bullet><solver><type>iters</type></solver></bullet>
  </physics>
  <scene><shadows>false</shadows></scene>  <!-- Disable for performance -->
</world>
```

Disabling shadows and reflections improves RTF by 20-30% with minimal visual impact for navigation testing.

### Level of Detail (LOD) for Complex Scenes

Use simplified collision meshes (convex hulls) while retaining detailed visual meshes:

```xml
<visual>
  <geometry><mesh><uri>model://humanoid/meshes/thigh_highres.dae</uri></mesh></geometry>
</visual>
<collision>
  <geometry><box><size>0.1 0.1 0.4</size></box></geometry>  <!-- Simplified -->
</collision>
```

**Result**: 50-70% faster physics simulation with negligible accuracy loss for navigation algorithms.

## Summary

This chapter introduced Gazebo as a physics-based simulation platform for robot algorithm development. You learned to model robots using URDF and SDF, configure physics engines for accuracy vs. performance trade-offs, simulate sensors for perception pipelines, and integrate with ROS 2 for hardware-in-the-loop testing.

Gazebo provides the testing foundation for Physical AI development: algorithms validated in simulation (Module 2) are then trained on synthetic data (Module 3) and deployed to physical robots (Modules 3-4). The next chapter explores Unity for high-fidelity visualization and VR/AR integration, complementing Gazebo's physics focus.

## Next Steps

- **Hands-On**: Complete [Exercise 2.1: Creating Robot Models in Gazebo](/exercises/gazebo-urdf-modeling) to build a URDF humanoid model
- **Deep Dive**: Explore [SDF specification](http://sdformat.org/spec) for advanced sensor and plugin configurations
- **Continue**: Proceed to [Chapter 5: Unity for Robot Visualization](/modules/module2-simulation/unity-visualization) for photorealistic rendering

## References

Macenski, S., Martín, F., White, R., & Clavero, J. G. (2020). The Marathon 2: A navigation system. In *2020 IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS)* (pp. 2718-2725). IEEE. https://doi.org/10.1109/IROS45743.2020.9341207

*Additional references covering Gazebo architecture, URDF/SDF modeling, physics engine comparisons, and sensor simulation will be added during Phase 2 research tasks (T011-T016).*
