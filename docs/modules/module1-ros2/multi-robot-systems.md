---
id: multi-robot-systems
title: Multi-Robot Coordination with ROS 2
sidebar_position: 3
module: 1
learning_objectives:
  - "Design namespace-based architectures for isolating multiple robots within shared ROS 2 networks"
  - "Implement multi-robot task allocation algorithms using action servers and coordination protocols"
  - "Configure DDS domain IDs and discovery mechanisms for scalable robot fleet communication"
  - "Analyze bandwidth and latency trade-offs in centralized vs. distributed multi-robot systems"
related_exercises:
  - multi-robot-coordination
related_references:
  - Macenski2020
word_count: 1380
last_updated: 2025-12-07
---

# Multi-Robot Coordination with ROS 2

## Introduction

Multi-robot systems enable capabilities beyond single-agent limitations: parallel task execution, spatial coverage, redundancy for fault tolerance, and collective behaviors like formation control or collaborative manipulation. Applications range from warehouse logistics fleets to search-and-rescue teams of humanoid robots coordinating in disaster zones.

ROS 2's DDS-based architecture provides native support for multi-robot communication without central bottlenecks, contrasting with ROS 1's master-slave design that struggled at fleet scales beyond 10-15 robots. By leveraging namespace isolation, domain partitioning, and distributed discovery, ROS 2 enables systems of dozens to hundreds of coordinating robots.

This chapter explores architectural patterns for multi-robot ROS 2 systems, task allocation strategies, and network optimization techniques. These concepts culminate in the capstone project, where multiple humanoid robots collaborate on manipulation tasks guided by vision-language commands (Module 4).

## Learning Objectives

By the end of this chapter, you will be able to:

1. **Design namespace-based architectures** for isolating multiple robots within shared ROS 2 networks
2. **Implement multi-robot task allocation algorithms** using action servers and coordination protocols
3. **Configure DDS domain IDs and discovery mechanisms** for scalable robot fleet communication
4. **Analyze bandwidth and latency trade-offs** in centralized vs. distributed multi-robot systems

## Namespace Isolation and Topic Remapping

### Namespaces: Logical Separation of Robot State

ROS 2 namespaces prefix topic, service, and action names with robot identifiers, preventing naming conflicts in multi-robot systems. For example, three robots `robot1`, `robot2`, `robot3` each publish joint states:

```
/robot1/joint_states
/robot2/joint_states
/robot3/joint_states
```

Launch files assign namespaces through the `namespace` parameter:

```python
Node(
    package='robot_state_publisher',
    executable='robot_state_publisher',
    namespace='robot1',
    parameters=[{'robot_description': urdf_robot1}]
)
```

**Benefits**:
- **Modularity**: Identical launch files for each robot, differing only in namespace
- **Debugging**: Clear attribution of messages to specific robots
- **Selective subscription**: Nodes subscribe only to relevant robot namespaces

**Trade-offs**: Global coordination nodes (fleet managers) must subscribe to all robot namespaces or use topic aggregation patterns (discussed below).

### Topic Remapping for Cross-Robot Communication

When robots need to share data (e.g., shared map from SLAM), topic remapping exposes selected topics outside namespaces:

```python
Node(
    package='slam_toolbox',
    executable='sync_slam_toolbox_node',
    namespace='robot1',
    remappings=[('/map', '/shared_map')]  # Publish to global topic
)
```

All robots subscribe to `/shared_map`, receiving map updates from the designated SLAM leader. This pattern centralizes mapping while distributing localization.

## DDS Domain IDs and Network Partitioning

### Domain Isolation for Multi-Team Deployments

DDS domains partition robots into non-communicating groups, useful for:
- **Testing**: Isolate development robots from production fleet
- **Multi-tenant facilities**: Separate customer fleets in shared warehouses
- **Bandwidth management**: Prevent cross-talk in high-density deployments

Domain IDs (0-232, typically 0-99 used) are set via environment variable:

```bash
export ROS_DOMAIN_ID=42
ros2 run my_package my_node
```

**Recommendation**: Use domain 0 for single-robot development, unique domains per robot team in multi-team scenarios. Note that domain isolation is network-level; robots in different domains cannot communicate even if namespaces align.

### Discovery Mechanisms: Multicast vs. Static Peers

**Multicast Discovery** (default): Robots broadcast presence on multicast addresses (239.255.0.1), enabling automatic peer detection. Simple but generates background traffic proportional to robot count × topic count.

**Static Peer Discovery**: Manually specify peer IP addresses in DDS XML configuration, eliminating multicast overhead. Required for networks blocking multicast (some enterprise WiFi, VPNs) or large fleets (50+ robots) where discovery traffic saturates bandwidth.

**Configuration Example** (Cyclone DDS):
```xml
<CycloneDDS>
  <Discovery>
    <Peers>
      <Peer Address="192.168.1.10"/>
      <Peer Address="192.168.1.11"/>
    </Peers>
  </Discovery>
</CycloneDDS>
```

Static discovery trades configuration complexity for network efficiency—critical for humanoid robot fleets where high-bandwidth sensor streams (RGB-D cameras) compete for wireless capacity.

## Multi-Robot Task Allocation

### Centralized vs. Distributed Coordination

**Centralized**: A fleet manager node receives task requests, allocates them to robots based on availability and proximity, and monitors progress. Simple to reason about but creates a single point of failure.

**Distributed**: Robots negotiate task assignments through consensus protocols (e.g., auction-based bidding). Resilient to node failures but requires more complex coordination logic.

**Hybrid**: Common in practice—centralized high-level planning with distributed low-level execution. For example, a fleet manager assigns "inspect area A" to robot 1, which then autonomously navigates and avoids other robots without central coordination.

### Auction-Based Task Allocation

Robots bid on tasks based on cost functions (distance to task, battery level, current workload):

1. **Announcement**: Fleet manager broadcasts new task (e.g., "pick object at pose X")
2. **Bidding**: Each idle robot computes its cost and publishes a bid
3. **Award**: Fleet manager selects lowest-cost bidder and assigns task
4. **Execution**: Winner confirms acceptance and begins task

**Implementation** (simplified):
```python
class AuctionBidder(Node):
    def __init__(self):
        super().__init__('auction_bidder')
        self.subscription = self.create_subscription(
            TaskAnnouncement, '/tasks/new', self.bid_on_task, 10)
        self.bid_publisher = self.create_publisher(Bid, '/tasks/bids', 10)

    def bid_on_task(self, task_msg):
        cost = self.compute_cost(task_msg.pose)  # Distance + workload
        bid = Bid(robot_id=self.get_namespace(), cost=cost, task_id=task_msg.id)
        self.bid_publisher.publish(bid)
```

Auction protocols balance efficiency (tasks go to closest robots) with simplicity (no complex optimization).

### Conflict Resolution: Path Planning and Deadlock

Multiple robots navigating shared spaces require collision avoidance and deadlock prevention:

**Trajectory Deconfliction**: Robots share planned paths, and a central coordinator or distributed protocol resolves conflicts by re-timing or re-routing. Tools like **Multi-Robot Path Planning (MRPP)** libraries extend Nav2 for fleets.

**Priority Systems**: Assign priorities (e.g., based on task urgency) where higher-priority robots have right-of-way. Lower-priority robots pause or reroute when paths intersect.

**Deadlock Detection**: Circular wait conditions (robot A waiting for B, B for C, C for A) are detected through timeout heuristics. Recovery involves backing up the lowest-priority robot.

## Shared vs. Distributed Mapping

### Centralized SLAM with Distributed Localization

One robot (SLAM leader) builds and broadcasts a map while others localize within it using AMCL. Advantages:
- **Consistency**: Single map source avoids conflicts from independent SLAM
- **Efficiency**: Only one robot runs computationally expensive SLAM

Limitations:
- **Scalability**: SLAM leader becomes bottleneck for large environments
- **Single point of failure**: If SLAM robot fails, fleet cannot update map

### Distributed SLAM with Map Merging

Each robot runs SLAM independently, periodically exchanging maps for merging. Approaches:
- **Feature matching**: Align maps by matching landmarks (corners, doors)
- **Multi-robot loop closure**: Robots detect when they observe same regions and fuse maps

**Tools**: Extensions to SLAM-Toolbox support distributed mapping, though map merging remains an active research area with limited production deployments.

**Humanoid Context**: Distributed SLAM suits scenarios where robots explore disconnected areas (different floors of a building), while centralized SLAM fits tightly-coupled tasks (collaborative manipulation in shared workspace).

## Network Bandwidth and QoS Optimization

### Bandwidth Profiling for Multi-Robot Fleets

Each robot in a 5-robot fleet might publish:
- Joint states: 1 KB/s
- LiDAR scans: 100 KB/s
- RGB-D camera: 10 MB/s (uncompressed depth + color at 30 Hz)
- Nav2 costmaps: 500 KB/s

**Total per robot**: ~10 MB/s → **Fleet**: ~50 MB/s. On a 100 Mbps WiFi network shared with other traffic, this approaches saturation, causing latency spikes and packet loss.

### QoS Strategies for Bandwidth Management

1. **Best-Effort for High-Bandwidth Streams**: Camera feeds use best-effort reliability (UDP-like), tolerating occasional frame drops for lower latency
2. **Reliable for Critical Commands**: Task assignments and safety stops use reliable QoS (TCP-like)
3. **Transient-Local for Maps**: Costmaps use transient-local durability, allowing late-joining robots to retrieve historical data without retransmission requests

**Compression**: Apply ROS 2 image transport compression (JPEG, H.264) to reduce camera bandwidth by 10-20×, at the cost of increased CPU usage and latency (10-50 ms).

### Network Topology: Wired vs. Wireless

**Wired Ethernet**: Preferred for stationary multi-robot labs (e.g., manipulation cells) due to guaranteed bandwidth and low latency (< 1 ms). Requires tethers limiting mobility.

**WiFi 5/6**: Typical for mobile fleets. WiFi 6 (802.11ax) provides better performance in dense deployments through OFDMA (orthogonal frequency-division multiple access). Still susceptible to interference and range limits.

**5G/LTE**: Emerging for outdoor fleets with cellular connectivity. Higher latency (20-50 ms) than WiFi but broader coverage. Requires edge computing or cloud integration.

## Practical Deployment Examples

### Warehouse Logistics Fleet

**Scenario**: 20 mobile robots transporting goods in a 10,000 m² facility.

**Architecture**:
- **Domain**: Single domain (0) with static peer discovery
- **Mapping**: Centralized static map (pre-built), no SLAM
- **Task allocation**: Centralized fleet manager assigns pick/delivery tasks via auctions
- **Collision avoidance**: Distributed via Nav2's obstacle layer, with priority rules for loaded robots

**Network**: Wired Ethernet at charging stations for map updates, WiFi 6 for operational zones.

### Humanoid Search-and-Rescue Team

**Scenario**: 5 humanoid robots coordinate to search a collapsed building.

**Architecture**:
- **Domain**: Single domain with multicast discovery (limited scale)
- **Mapping**: Distributed SLAM with periodic map sharing
- **Task allocation**: Distributed via frontier-based exploration (robots autonomously select unexplored regions)
- **Collision avoidance**: Coarse-grained zones ("robot 1 explores east wing") due to sparse environment

**Network**: WiFi 5 mesh with mobile relay nodes to maintain connectivity in obstructed areas.

## Summary

This chapter examined multi-robot coordination in ROS 2, covering namespace isolation, DDS domain configuration, and task allocation strategies. You learned to design centralized and distributed architectures, optimize network bandwidth through QoS tuning, and resolve conflicts in shared navigation spaces.

Multi-robot systems amplify the capabilities demonstrated in Modules 1-3, enabling parallel exploration, collaborative manipulation, and fleet-scale deployments. The subsequent modules build on these foundations: Module 2 simulates multi-robot scenarios in Gazebo and Unity, Module 3 generates synthetic training data for perception in multi-robot contexts, and Module 4 integrates vision-language-action models for natural language task assignment across fleets.

## Next Steps

- **Hands-On**: Complete [Exercise 1.3: Multi-Robot Task Coordination](/exercises/multi-robot-coordination) to implement auction-based allocation
- **Deep Dive**: Explore [ROS 2 multicast tuning](https://docs.ros.org/en/humble/How-To-Guides/DDS-tuning.html) for fleet optimization
- **Continue**: Proceed to [Module 2: Gazebo Simulation](/modules/module2-simulation/gazebo-simulation) for testing multi-robot systems in simulation

## References

Macenski, S., Martín, F., White, R., & Clavero, J. G. (2020). The Marathon 2: A navigation system. In *2020 IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS)* (pp. 2718-2725). IEEE. https://doi.org/10.1109/IROS45743.2020.9341207

*Additional references covering multi-robot task allocation, DDS scalability, and fleet management will be added during Phase 2 research tasks (T011-T016).*
