---
id: ros2-fundamentals
title: ROS 2 Fundamentals
sidebar_position: 1
module: 1
learning_objectives:
  - "Design multi-node ROS 2 systems using publishers and subscribers for asynchronous communication"
  - "Implement custom ROS 2 services and actions for synchronous request-response patterns"
  - "Explain the Data Distribution Service (DDS) middleware architecture underlying ROS 2"
  - "Configure ROS 2 parameters and launch files for scalable robot system deployment"
related_exercises:
  - ros2-talker-listener
  - ros2-custom-service
related_references:
  - Macenski2020
word_count: 1350
last_updated: 2025-12-07
---

# ROS 2 Fundamentals

## Introduction

The Robot Operating System 2 (ROS 2) represents a fundamental shift in robot middleware design, addressing the limitations of ROS 1 through real-time capabilities, improved security, and native support for distributed multi-robot systems. Unlike its predecessor, ROS 2 leverages the Data Distribution Service (DDS) standard for inter-process communication, enabling deterministic behavior critical for safety-critical applications in humanoid robotics and autonomous systems (Macenski et al., 2020).

This chapter establishes the foundational concepts required to architect ROS 2 systems for Physical AI applications. You will learn to design communication patterns, implement service-oriented architectures, and deploy scalable robot systems using industry-standard middleware. These skills form the basis for autonomous navigation, multi-robot coordination, and integration with vision-language-action models explored in later modules.

## Learning Objectives

By the end of this chapter, you will be able to:

1. **Design multi-node ROS 2 systems** using publishers and subscribers for asynchronous communication
2. **Implement custom ROS 2 services and actions** for synchronous request-response patterns
3. **Explain the Data Distribution Service (DDS) middleware architecture** underlying ROS 2
4. **Configure ROS 2 parameters and launch files** for scalable robot system deployment

## ROS 2 Architecture and Design Philosophy

### From ROS 1 to ROS 2: Key Improvements

ROS 2 was designed to address three critical limitations of ROS 1: lack of real-time guarantees, single-master architecture bottlenecks, and insufficient security for production deployments. By adopting the Object Management Group's DDS specification, ROS 2 achieves:

- **Deterministic communication**: Quality of Service (QoS) policies enable predictable message delivery for safety-critical control loops
- **Peer-to-peer discovery**: No central master node eliminates single points of failure in distributed robot fleets
- **Native security**: DDS Security extends authentication, encryption, and access control to all communication channels

These improvements make ROS 2 suitable for commercial humanoid robotics platforms where ROS 1's reliability constraints were prohibitive.

### The DDS Middleware Layer

ROS 2's abstraction over DDS provides portability across multiple DDS vendors (e.g., eProsima Fast DDS, RTI Connext, Eclipse Cyclone DDS) while exposing QoS controls essential for robot behavior. Each ROS 2 node creates DDS participants that discover peers through multicast or static configuration, establishing data readers and writers for topics.

**QoS Policies**: Unlike ROS 1's best-effort TCP/UDP transport, ROS 2 allows per-topic configuration of:
- **Reliability**: Best-effort (UDP-like) vs. reliable (TCP-like) delivery
- **Durability**: Transient-local storage of historical messages for late-joining subscribers
- **Liveliness**: Automatic detection of failed nodes through heartbeat mechanisms
- **History**: Queue depth for message buffering during high-throughput bursts

Understanding QoS tuning is critical for balancing latency, bandwidth, and reliability in multi-robot scenarios explored in Chapter 3.

## ROS 2 Communication Patterns

### Publishers and Subscribers: Asynchronous Data Flow

The publish-subscribe pattern decouples data producers from consumers, enabling many-to-many communication through named topics. A publisher sends messages without knowledge of subscriber count or identity, while subscribers register callbacks invoked asynchronously upon message arrival.

**Example Use Case**: A humanoid robot's joint state publisher broadcasts current joint angles at 100 Hz. Multiple subscribers (motion planner, visualization tool, data logger) consume this stream independently without blocking the publisher.

**Code Pattern** (Python):
```python
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import JointState

class JointStatePublisher(Node):
    def __init__(self):
        super().__init__('joint_state_publisher')
        self.publisher = self.create_publisher(JointState, 'joint_states', 10)
        self.timer = self.create_timer(0.01, self.publish_joint_states)  # 100 Hz

    def publish_joint_states(self):
        msg = JointState()
        msg.name = ['hip', 'knee', 'ankle']
        msg.position = [0.1, 0.5, -0.3]
        self.publisher.publish(msg)
```

### Services: Synchronous Request-Response

Services implement RPC (remote procedure call) semantics for operations requiring acknowledgment or computation results. Unlike topics, service calls block until the server responds or a timeout occurs. This pattern suits discrete commands like "compute inverse kinematics" or "capture RGB-D image."

**Service Definition** (.srv file):
```
# Request
geometry_msgs/Pose target_pose
---
# Response
bool success
float64[] joint_angles
string message
```

Services guarantee single-response semantics, making them unsuitable for long-running operations. For tasks like "navigate to goal" that require progress feedback, ROS 2 provides actions.

### Actions: Long-Running Tasks with Feedback

Actions extend services with three components:
1. **Goal**: Initial request (e.g., target navigation waypoint)
2. **Feedback**: Periodic updates during execution (e.g., distance remaining)
3. **Result**: Final outcome upon completion or preemption

The ROS 2 Navigation Stack (Nav2) extensively uses actions for goal-driven behaviors, allowing clients to monitor progress and cancel operations mid-execution.

## Building Your First ROS 2 System

### Node Lifecycle and Execution

ROS 2 nodes follow a managed lifecycle for deterministic startup and shutdown:
1. **Unconfigured**: Node constructed but not ready
2. **Inactive**: Resources allocated, awaiting activation
3. **Active**: Fully operational, processing messages
4. **Finalized**: Graceful shutdown initiated

Lifecycle management prevents race conditions in multi-node systems where initialization order affects behavior.

### Parameters: Runtime Configuration

Parameters provide dynamic reconfiguration without code changes. A humanoid robot's gait controller might expose parameters for step length, frequency, and balance tolerance, allowing operators to tune behavior through command-line tools or configuration files.

**Parameter Declaration**:
```python
self.declare_parameter('step_length', 0.3)  # meters
step_length = self.get_parameter('step_length').value
```

Parameters support type validation (int, float, string, arrays) and can trigger callbacks when modified at runtime, enabling adaptive behavior in response to environmental changes.

### Launch Files: Orchestrating Complex Systems

Launch files (Python or XML) coordinate multi-node startup with parameter passing, namespace remapping, and conditional logic. A typical humanoid robot launch might start:
- Joint state publisher and robot state publisher (URDF kinematics)
- Camera and LiDAR drivers
- Navigation stack (costmap, planner, controller)
- High-level task manager

**Launch File Example** (Python):
```python
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            parameters=[{'robot_description': ...}]
        ),
        Node(
            package='nav2_bringup',
            executable='bt_navigator',
            parameters=[{'default_bt_xml': ...}]
        )
    ])
```

## Practical Considerations for Humanoid Robotics

### Real-Time Performance

Humanoid balance control requires sub-10ms control loops. ROS 2's DDS layer supports real-time scheduling with appropriate QoS (reliable, deadline policies), but Linux kernel tuning (PREEMPT_RT patches) and careful memory management (lock-free queues) remain necessary for hard real-time guarantees.

### Network Topologies for Multi-Robot Fleets

DDS discovery scales to dozens of robots through domain ID partitioning and static peer configuration. For large-scale deployments (e.g., warehouse fleets), cloud-based discovery servers reduce multicast traffic, though this reintroduces partial centralization.

### Security Considerations

DDS Security (SROS2) integrates X.509 certificate-based authentication and AES encryption. While overhead is acceptable for sensor data (~5% latency increase), encrypting high-bandwidth streams (4K video) may require hardware acceleration or selective security policies.

## Summary

This chapter introduced ROS 2's architecture, focusing on DDS-based communication, QoS policies, and the three primary interaction patterns: topics, services, and actions. You learned to structure nodes with lifecycle management, configure parameters for runtime adaptability, and orchestrate systems with launch files.

The subsequent chapters build on these foundations: Chapter 2 applies ROS 2 to autonomous navigation with Nav2, while Chapter 3 explores multi-robot coordination using the communication patterns established here. Mastery of ROS 2 fundamentals is essential for integrating vision-language-action models (Module 4) with physical robot platforms.

## Next Steps

- **Hands-On**: Complete [Exercise 1.1: Building a ROS 2 Talker-Listener System](/exercises/ros2-talker-listener) to implement publishers and subscribers
- **Deep Dive**: Explore [ROS 2 DDS tuning](https://docs.ros.org/en/humble/Concepts/About-Quality-of-Service-Settings.html) for performance optimization
- **Continue**: Proceed to [Chapter 2: ROS 2 Navigation with Nav2](/modules/module1-ros2/ros2-navigation) for autonomous mobility

## References

Macenski, S., Martín, F., White, R., & Clavero, J. G. (2020). The Marathon 2: A navigation system. In *2020 IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS)* (pp. 2718-2725). IEEE. https://doi.org/10.1109/IROS45743.2020.9341207

*Additional references from ROS 2 documentation, DDS specifications, and real-time robotics literature will be added during Phase 2 research tasks (T011-T016).*
