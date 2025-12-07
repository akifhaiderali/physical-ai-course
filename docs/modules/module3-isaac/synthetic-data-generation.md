---
id: synthetic-data-generation
title: Synthetic Data Generation and Domain Randomization
sidebar_position: 2
module: 3
learning_objectives:
  - "Implement domain randomization techniques for textures, lighting, and object properties in Isaac Sim"
  - "Generate large-scale annotated datasets (RGB-D images, bounding boxes, segmentation masks) for ML training"
  - "Evaluate sim-to-real transfer performance using synthetic training data on physical robots"
  - "Design data collection pipelines with automated scene variation and quality validation"
related_exercises:
  - isaac-synthetic-data
related_references:
  - Macenski2020
word_count: 1250
last_updated: 2025-12-07
---

# Synthetic Data Generation and Domain Randomization

## Introduction

The data bottleneck represents one of the greatest barriers to deploying vision-based AI in robotics: collecting and labeling thousands of images across diverse environments is expensive, time-consuming, and often infeasible for rare scenarios (e.g., humanoid robot failures). Synthetic data generation addresses this by creating unlimited labeled training data in simulation, with automatic annotations for object detection, segmentation, and pose estimation.

Domain randomization—the systematic variation of simulation parameters—is the key technique enabling models trained on synthetic data to generalize to real-world conditions. By exposing models to extreme lighting, texture, and geometry variations during training, domain randomization forces learning of robust features that transfer across the "reality gap."

This chapter explores Isaac Sim's synthetic data tools, domain randomization strategies, and validation methods for measuring sim-to-real transfer quality. These techniques directly enable Module 4's vision-language-action models, which require diverse training data to understand commands like "pick up the red mug."

## Learning Objectives

By the end of this chapter, you will be able to:

1. **Implement domain randomization techniques** for textures, lighting, and object properties in Isaac Sim
2. **Generate large-scale annotated datasets** (RGB-D images, bounding boxes, segmentation masks) for ML training
3. **Evaluate sim-to-real transfer performance** using synthetic training data on physical robots
4. **Design data collection pipelines** with automated scene variation and quality validation

## Domain Randomization Fundamentals

### The Reality Gap Problem

Models trained in static simulation often fail on physical robots due to:

- **Visual mismatch**: Simulated materials lack real-world wear, lighting differs from lab conditions
- **Physics discrepancies**: Friction, contact dynamics approximated in simulation
- **Sensor noise**: Real cameras have lens distortion, motion blur absent in perfect renders

**Example Failure**: Object detector trained on pristine Isaac Sim renders (100% accuracy in sim) achieves 40% accuracy on real robot camera due to unexpected shadows and reflections.

### Domain Randomization Solution

Instead of perfecting simulation realism, domain randomization **expands the training distribution** to encompass reality as one of many possibilities:

**Randomized Parameters**:
1. **Textures**: Randomly sample materials for objects (wood, metal, plastic variants)
2. **Lighting**: Vary HDRI skyboxes (sunny, overcast, indoor) and light intensities
3. **Camera**: Add noise, blur, color shifts simulating sensor variability
4. **Object Poses**: Randomize positions, orientations within reachable workspace
5. **Distractors**: Add irrelevant objects (clutter) to prevent overfitting to clean scenes

**Training Protocol**: Generate 10,000-100,000 images with extreme randomization. Models learn invariant features (object shape, color boundaries) robust to sim-to-real gaps.

## Implementing Domain Randomization in Isaac Sim

### Texture Randomization

Isaac Sim's **Replicator** API automates material swapping:

```python
import omni.replicator.core as rep

# Randomize object materials
objects = rep.get.prims(path_pattern="/World/Objects/*")
with objects:
    rep.randomizer.materials(
        materials=rep.get.materials(semantics=[("class", "diffuse")]),
        project_uvw=True
    )
```

**Strategy**: Maintain semantic consistency (don't apply metal texture to cloth napkins) while maximizing visual diversity.

### Lighting Randomization

Cycle through HDRI environments and vary light intensities:

```python
import omni.isaac.core.utils.stage as stage_utils

hdri_paths = [
    "omniverse://localhost/NVIDIA/Assets/Skies/Clear/noon.hdr",
    "omniverse://localhost/NVIDIA/Assets/Skies/Overcast/cloudy.hdr",
    "omniverse://localhost/NVIDIA/Assets/Skies/Indoor/warehouse.hdr"
]

# Randomize per scene generation
for i in range(1000):
    stage_utils.set_dome_light(hdri_path=random.choice(hdri_paths))
    stage_utils.set_dome_light_intensity(random.uniform(500, 2000))
    # Capture camera images
```

**Advanced**: Use area lights with randomized positions to simulate portable lamps, windows.

### Camera Pose Randomization

Vary camera viewpoints to train models robust to robot head motion:

```python
from pxr import UsdGeom, Gf

camera_prim = stage.GetPrimAtPath("/World/Camera")
xform = UsdGeom.Xformable(camera_prim)

# Randomize camera position in hemisphere around object
theta = random.uniform(0, 2*math.pi)
phi = random.uniform(0, math.pi/3)
radius = random.uniform(0.5, 2.0)

x = radius * math.sin(phi) * math.cos(theta)
y = radius * math.sin(phi) * math.sin(theta)
z = radius * math.cos(phi)

xform.ClearXformOpOrder()
xform.AddTranslateOp().Set(Gf.Vec3d(x, y, z))
xform.AddOrientOp().Set(Gf.Quatd(...))  # Look at target
```

## Generating Annotated Datasets

### Semantic Segmentation and Bounding Boxes

Isaac Sim's **Synthetic Data Recorder** outputs:

- **RGB Images**: Standard camera view
- **Semantic Segmentation**: Pixel-wise class labels (13 classes: person, chair, table, etc.)
- **Instance Segmentation**: Each object instance uniquely colored
- **Bounding Boxes**: 2D (image space) and 3D (world space) boxes
- **Depth Maps**: Per-pixel distance for RGB-D training

**Configuration**:
```python
import omni.syntheticdata as sd

# Enable annotators
sd.sensors.enable_sensors(
    sensors=[
        sd.SensorType.RGB,
        sd.SensorType.SEMANTIC_SEGMENTATION,
        sd.SensorType.BOUNDING_BOX_2D,
        sd.SensorType.DEPTH
    ],
    camera_path="/World/Camera"
)

# Capture frame
rgb = sd.sensors.get_rgb()
seg = sd.sensors.get_semantic_segmentation()
bbox = sd.sensors.get_bounding_box_2d()  # COCO format JSON
```

### Data Pipeline Design

**Automated Collection Loop**:
1. **Scene Setup**: Load base environment (warehouse, kitchen, etc.)
2. **Randomization**: Apply texture, lighting, object pose variations
3. **Capture**: Render RGB, depth, segmentation, bounding boxes
4. **Validation**: Filter low-quality images (occlusion > 80%, lighting too dark)
5. **Save**: Write to disk in training framework format (COCO, YOLO, TensorFlow Records)

**Performance**: Isaac Sim generates ~100 annotated images/minute on RTX 4090, enabling 10K-image datasets in ~2 hours (vs. weeks for manual real-world collection).

## Dataset Quality and Validation

### Diversity Metrics

Measure dataset coverage using:

- **Lighting Histogram**: Ensure uniform distribution of brightness levels
- **Viewpoint Distribution**: Visualize camera poses on unit sphere (avoid clustering)
- **Object Co-occurrence**: Track which objects appear together (ensure realism)

**Tool**: Use dimensionality reduction (t-SNE) on image embeddings to visualize dataset diversity in 2D space. Clusters indicate redundant data.

### Sim-to-Real Validation Protocol

1. **Baseline**: Train object detector on synthetic data only
2. **Real-World Test**: Evaluate on 500 real robot camera images (hand-labeled)
3. **Metrics**: Compare mAP (mean average precision), per-class accuracy
4. **Iteration**: If real-world accuracy < 70%, increase randomization diversity or add real-world fine-tuning (10% real data often sufficient)

**Success Criteria**: Model trained on 50K synthetic images should achieve ≥80% of accuracy compared to model trained on 5K real images (10× data efficiency gain).

## Advanced Techniques

### Structured Domain Randomization

Not all parameters contribute equally—**structured randomization** focuses variation on high-impact factors:

**Study Example**: Vary lighting (±40% accuracy impact) more than texture (±5% impact) based on ablation studies.

**Implementation**: Use learned randomization policies where RL agents optimize randomization parameters to maximize real-world performance.

### Procedural Scene Generation

Combine domain randomization with procedural content generation:

```python
def generate_warehouse_scene():
    # Procedurally place shelves in grid
    for i in range(10):
        for j in range(5):
            shelf = spawn_shelf(position=(i*2.0, j*1.5, 0))
            # Randomize shelf contents
            populate_shelf(shelf, num_objects=random.randint(5, 15))

    # Add humanoid robot at random start position
    robot = spawn_humanoid(position=random_point_in_aisle())
```

**Application**: Generate infinite training environments for navigation policies, preventing overfitting to specific room layouts.

## Integration with VLA Training (Module 4)

Synthetic data from Isaac Sim feeds directly into VLA model training:

1. **Dataset Generation**: 100K images of humanoid arm interacting with objects, varying commands ("pick red mug", "place on shelf")
2. **Annotation**: Automatically label successful/failed grasps from simulation physics
3. **Training**: Fine-tune VLA model (e.g., RT-2) on synthetic dataset
4. **Deployment**: Test on physical humanoid executing natural language commands

**Chapter 9 Preview**: VLA models trained 80% on synthetic data + 20% real data achieve near-parity with 100% real data, dramatically reducing labeling costs.

## Summary

This chapter explored synthetic data generation and domain randomization as solutions to the data bottleneck in Physical AI. You learned to implement texture, lighting, and pose randomization in Isaac Sim, generate large-scale annotated datasets, and validate sim-to-real transfer quality. These techniques enable cost-effective training of vision-language-action models deployed to physical humanoid robots.

Domain randomization represents a paradigm shift: rather than perfecting simulation realism, embrace diversity to train robust models. This principle extends beyond vision to manipulation, navigation, and multi-robot coordination explored in Module 4.

## Next Steps

- **Hands-On**: [Exercise 3.1: Synthetic Data Pipeline](/exercises/isaac-synthetic-data)
- **Continue**: [Module 4: Vision-Language-Action Models](/modules/module4-vla/vla-introduction)

## References

*References for domain randomization (Tobin et al.), Isaac Sim Replicator, sim-to-real transfer, and synthetic data validation will be added during research tasks (T011-T016).*
