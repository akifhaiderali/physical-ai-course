# Physical AI Course - Content Data Model

**Version**: 1.0.0
**Last Updated**: 2025-12-07
**Purpose**: Define structured schemas for all content entities in the Physical AI & Humanoid Robotics Course

---

## Overview

This data model defines 10 core content entities used throughout the course specification. All entities follow YAML frontmatter + Markdown body structure for consistency with Docusaurus.

**Design Principles**:
1. **Separation of Concerns**: Metadata (YAML frontmatter) vs Content (Markdown body)
2. **Consistency**: All chapters follow same frontmatter schema
3. **Traceability**: IDs link to learning objectives, exercises, and references
4. **Validation**: Schemas enforce required fields and data types
5. **Flexibility**: Optional fields allow module-specific extensions

---

## Entity 1: Module Chapter

**Path**: `docs/modules/<module-id>/<chapter-id>.md`

**Purpose**: Detailed topic exposition for one of 10 module chapters

**Schema**:
```yaml
---
id: <chapter-id>                    # Required: Unique identifier (e.g., "ros2-fundamentals")
title: <chapter-title>              # Required: Display title (e.g., "ROS 2 Fundamentals")
sidebar_position: <number>          # Required: Order in sidebar (1-10)
module: <module-number>             # Required: Module number (1-4)
learning_objectives:                # Required: 3-5 measurable learning outcomes
  - "<objective-1>"
  - "<objective-2>"
  - "<objective-3>"
related_exercises:                  # Optional: Links to exercises
  - <exercise-id>
related_references:                 # Optional: BibTeX citation keys
  - <citation-key-1>
  - <citation-key-2>
word_count: <number>                # Required: Target 800-1500 words
last_updated: <YYYY-MM-DD>          # Required: ISO 8601 date
---

# <chapter-title>

## Introduction
[Overview paragraph establishing context and relevance]

## Learning Objectives
By the end of this chapter, you will be able to:
1. [Measurable objective using Bloom's taxonomy verbs]
2. [Another measurable objective]
...

## Topic 1: <topic-name>
[Detailed exposition with code examples, diagrams, and references]

### Subtopic 1.1
[Subsection content]

## Topic 2: <topic-name>
[Detailed exposition]

## Summary
[Recap of key concepts and connection to next chapter]

## References
[APA 7th edition citations for all sources cited in chapter]
```

**Validation Rules**:
- `id` matches filename (e.g., `ros2-fundamentals.md` → `id: ros2-fundamentals`)
- `learning_objectives` has 3-5 items
- `word_count` is 800-1500
- `module` is 1-4
- All citations in body match `related_references` keys

**Example**:
```yaml
---
id: ros2-fundamentals
title: ROS 2 Fundamentals
sidebar_position: 1
module: 1
learning_objectives:
  - "Design multi-node ROS 2 systems using publishers and subscribers"
  - "Implement custom ROS 2 services for request-response communication"
  - "Explain the DDS middleware architecture underlying ROS 2"
related_exercises:
  - ros2-talker-listener
  - ros2-custom-service
related_references:
  - Macenski2020
  - Quigley2015
word_count: 1200
last_updated: 2025-12-07
---
```

---

## Entity 2: Exercise Chapter

**Path**: `docs/exercises/<exercise-id>.md`

**Purpose**: Hands-on lab exercise with setup, procedure, and assessment

**Schema**:
```yaml
---
id: <exercise-id>                   # Required: Unique identifier
title: <exercise-title>             # Required: Display title
sidebar_position: <number>          # Required: Order in exercises category (1-4)
module: <module-number>             # Required: Related module (1-4)
duration: <minutes>                 # Required: Estimated completion time
difficulty: <level>                 # Required: "beginner" | "intermediate" | "advanced"
prerequisites:                      # Required: List of prerequisite exercises
  - <exercise-id>
learning_outcomes:                  # Required: 2-3 measurable outcomes
  - "<outcome-1>"
  - "<outcome-2>"
equipment_required:                 # Required: Hardware/software list
  hardware:
    - "<item-1>"
  software:
    - "<item-2>"
code_examples:                      # Optional: Links to code files
  - path: <relative-path>
    description: <description>
assessment_criteria:                # Required: Grading rubric
  - criterion: <criterion-name>
    weight: <percentage>
    description: <description>
last_updated: <YYYY-MM-DD>          # Required: ISO 8601 date
---

# <exercise-title>

## Overview
[Brief description of exercise goals and context]

## Prerequisites
[List of required knowledge and prior exercises]

## Setup
### Hardware Setup
[Step-by-step hardware assembly/connection instructions]

### Software Setup
[Environment configuration, package installation]

## Procedure
### Part 1: <part-name>
[Detailed step-by-step instructions with expected outputs]

### Part 2: <part-name>
[Continued procedure]

## Expected Results
[What students should observe upon successful completion]

## Troubleshooting
[Common errors and solutions]

## Assessment Criteria
[Rubric with point breakdown]

## Extensions (Optional)
[Advanced challenges for further exploration]

## References
[Cited sources]
```

**Validation Rules**:
- `duration` is 30-180 minutes
- `difficulty` is one of: beginner, intermediate, advanced
- `assessment_criteria` weights sum to 100%
- All `code_examples` paths exist in `static/code-examples/`

**Example**:
```yaml
---
id: ros2-talker-listener
title: "Exercise 1.1: Building a ROS 2 Talker-Listener System"
sidebar_position: 1
module: 1
duration: 60
difficulty: beginner
prerequisites: []
learning_outcomes:
  - "Create ROS 2 publisher and subscriber nodes in Python"
  - "Verify topic communication using ROS 2 CLI tools"
equipment_required:
  hardware:
    - "Ubuntu 22.04 workstation or VM"
  software:
    - "ROS 2 Humble"
    - "Python 3.10+"
code_examples:
  - path: "static/code-examples/module1-ros2/talker.py"
    description: "Publisher node sending string messages"
  - path: "static/code-examples/module1-ros2/listener.py"
    description: "Subscriber node receiving messages"
assessment_criteria:
  - criterion: "Nodes compile and run without errors"
    weight: 30
    description: "Both talker and listener execute successfully"
  - criterion: "Correct topic communication"
    weight: 40
    description: "Listener receives messages published by talker"
  - criterion: "Code quality and documentation"
    weight: 30
    description: "Code follows PEP 8 and includes docstrings"
last_updated: 2025-12-07
---
```

---

## Entity 3: Capstone Project

**Path**: `docs/capstone/capstone-project.md`

**Purpose**: Integrative final project specification

**Schema**:
```yaml
---
id: capstone-project
title: Capstone Project
sidebar_position: 1
duration: <weeks>                   # Required: Project duration in weeks
team_size: <number>                 # Required: Students per team
modules_integrated:                 # Required: List of modules (1-4)
  - <module-number>
learning_outcomes:                  # Required: 5-7 integrative outcomes
  - "<outcome-1>"
deliverables:                       # Required: List of required deliverables
  - name: <deliverable-name>
    due_week: <week-number>
    description: <description>
assessment:                         # Required: Rubric with weights
  - criterion: <criterion-name>
    weight: <percentage>
    description: <description>
last_updated: <YYYY-MM-DD>
---

# <title>

## Project Overview
[Description of capstone scope and goals]

## Learning Objectives
[Integrative learning outcomes across all modules]

## Project Requirements
### Functional Requirements
[What the system must do]

### Technical Requirements
[Technologies and platforms to use]

## Deliverables
[Timeline with milestones]

## Assessment Rubric
[Detailed grading criteria]

## Submission Guidelines
[How and when to submit]

## References
[Cited sources]
```

**Validation Rules**:
- `modules_integrated` includes all modules 1-4
- `assessment` weights sum to 100%
- `deliverables` cover all project phases

**Example**:
```yaml
---
id: capstone-project
title: Capstone Project - VLA-Driven Humanoid Task Execution
sidebar_position: 1
duration: 4
team_size: 3
modules_integrated: [1, 2, 3, 4]
learning_outcomes:
  - "Integrate ROS 2 navigation with VLA-based task planning"
  - "Generate synthetic training data using Isaac Sim domain randomization"
  - "Deploy and evaluate sim-to-real transfer on physical humanoid robots"
deliverables:
  - name: "Project Proposal"
    due_week: 1
    description: "2-page proposal with task specification and timeline"
  - name: "Simulation Demo"
    due_week: 2
    description: "Isaac Sim demo of VLA task execution"
  - name: "Final Presentation"
    due_week: 4
    description: "15-minute presentation with physical robot demo"
assessment:
  - criterion: "Technical Implementation"
    weight: 40
    description: "Correct integration of ROS 2, Isaac Sim, and VLA"
  - criterion: "Sim-to-Real Performance"
    weight: 30
    description: "Task success rate on physical robot"
  - criterion: "Documentation and Presentation"
    weight: 30
    description: "Clear technical report and presentation"
last_updated: 2025-12-07
---
```

---

## Entity 4: Lab Tier Specification

**Path**: `docs/infrastructure/<tier-id>.md`

**Purpose**: Hardware and software specification for one of 3 lab tiers

**Schema**:
```yaml
---
id: <tier-id>                       # Required: "proxy-tier" | "miniature-tier" | "premium-tier"
title: <tier-title>                 # Required: Display title
sidebar_position: <number>          # Required: Order (1-3)
tier_level: <level>                 # Required: 1 (Proxy) | 2 (Miniature) | 3 (Premium)
budget_range:                       # Required: Cost range
  min: <number>
  max: <number>
  currency: "USD"
student_capacity: <number>          # Required: Students supported
hardware_components:                # Required: List of equipment
  - name: <component-name>
    quantity: <number>
    unit_cost: <number>
    description: <description>
software_requirements:              # Required: Software stack
  - <software-name>
space_requirements:                 # Required: Lab space needs
  area_sqft: <number>
  description: <description>
pros:                               # Required: Advantages
  - "<advantage-1>"
cons:                               # Required: Limitations
  - "<limitation-1>"
use_cases:                          # Required: Ideal scenarios
  - "<use-case-1>"
last_updated: <YYYY-MM-DD>
---

# <tier-title>

## Overview
[Description of tier and target institutions]

## Budget Breakdown
[Itemized cost table]

## Hardware Specifications
[Detailed equipment descriptions]

## Software Stack
[Required software and licenses]

## Space and Facilities
[Lab layout and safety requirements]

## Strengths and Limitations
[Pros and cons analysis]

## Recommended Use Cases
[When to choose this tier]

## References
[Equipment vendor links and citations]
```

**Validation Rules**:
- `tier_level` matches `id` (Proxy=1, Miniature=2, Premium=3)
- `budget_range.min` < `budget_range.max`
- `hardware_components` total cost aligns with budget range

**Example**:
```yaml
---
id: miniature-tier
title: Miniature Tier Lab
sidebar_position: 2
tier_level: 2
budget_range:
  min: 50000
  max: 70000
  currency: "USD"
student_capacity: 12
hardware_components:
  - name: "GPU Workstation (NVIDIA RTX 4090)"
    quantity: 3
    unit_cost: 3500
    description: "For Isaac Sim and VLA training"
  - name: "Unitree H1 Humanoid Robot"
    quantity: 2
    unit_cost: 90000
    description: "Compact humanoid for hands-on exercises"
software_requirements:
  - "ROS 2 Humble"
  - "NVIDIA Isaac Sim (free)"
  - "Unity Pro (education license)"
space_requirements:
  area_sqft: 400
  description: "15x27 ft lab with safety barriers for robot operation"
pros:
  - "Real hardware experience without full-scale robot costs"
  - "GPU workstations support advanced AI training"
cons:
  - "Compact robots have limited payload and reach vs full-scale"
use_cases:
  - "Mid-sized universities with dedicated robotics programs"
  - "Research labs focusing on AI rather than heavy manipulation"
last_updated: 2025-12-07
---
```

---

## Entity 5: Week-by-Week Schedule

**Path**: `docs/appendices/week-by-week.md`

**Purpose**: Semester schedule mapping modules to weeks

**Schema**:
```yaml
---
id: week-by-week
title: Week-by-Week Schedule
sidebar_position: 2
semester_length: <weeks>            # Required: Total weeks (12-16)
schedule:                           # Required: Weekly breakdown
  - week: <number>
    module: <module-number>
    topics:
      - <topic-1>
      - <topic-2>
    exercises:
      - <exercise-id>
    assessments:
      - <assessment-name>
last_updated: <YYYY-MM-DD>
---

# <title>

## Semester Overview
[Introduction to course pacing]

## Weekly Breakdown

### Week <number>: <topic-name>
**Module**: <module-number>
**Topics**: [List]
**Exercises**: [List]
**Assessments**: [List]

[Repeat for all weeks]

## References
[Cited sources for pedagogy]
```

**Validation Rules**:
- `semester_length` is 12-16 weeks
- All weeks accounted for in `schedule`
- All `exercises` reference valid exercise IDs

**Example**:
```yaml
---
id: week-by-week
title: Week-by-Week Schedule
sidebar_position: 2
semester_length: 16
schedule:
  - week: 1
    module: 1
    topics:
      - "ROS 2 architecture and nodes"
      - "Publishers and subscribers"
    exercises:
      - ros2-talker-listener
    assessments: []
  - week: 2
    module: 1
    topics:
      - "Services and actions"
      - "Parameters and launch files"
    exercises:
      - ros2-custom-service
    assessments:
      - "Module 1 Quiz"
last_updated: 2025-12-07
---
```

---

## Entity 6: Reference Entry (BibTeX)

**Path**: `static/references.bib`

**Purpose**: Academic citations in BibTeX format for APA rendering

**Schema**:
```bibtex
@<entry-type>{<citation-key>,
  author    = {<author-list>},
  title     = {<title>},
  booktitle = {<conference-name>},  # For inproceedings
  journal   = {<journal-name>},     # For article
  year      = {<year>},
  pages     = {<page-range>},
  doi       = {<doi>},
  url       = {<url>},
  publisher = {<publisher>}         # For books
}
```

**Entry Types**:
- `@inproceedings` - Conference papers
- `@article` - Journal articles
- `@book` - Textbooks
- `@techreport` - Technical reports (e.g., NVIDIA whitepapers)
- `@online` - Web resources (documentation)

**Validation Rules**:
- `year` is 2015-2025
- `author` uses proper BibTeX escaping (e.g., `Mart{\\'i}n` for accents)
- All citation keys referenced in markdown files exist

**Example**:
```bibtex
@inproceedings{Macenski2020,
  author    = {Macenski, Steve and Mart{\\'i}n, Francisco and White, Ruffin and Clavero, Jonatan Gin{\\'e}s},
  title     = {The Marathon 2: A Navigation System},
  booktitle = {2020 IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS)},
  year      = {2020},
  pages     = {2718-2725},
  doi       = {10.1109/IROS45743.2020.9341207}
}

@article{Brohan2023,
  author  = {Brohan, Anthony and Brown, Noah and others},
  title   = {RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control},
  journal = {arXiv preprint arXiv:2307.15818},
  year    = {2023},
  url     = {https://arxiv.org/abs/2307.15818}
}
```

---

## Entity 7: Code Example

**Path**: `static/code-examples/<module-id>/<example-name>.<ext>`

**Purpose**: Executable code snippets for exercises

**Schema** (Metadata Comment Header):
```python
#!/usr/bin/env python3
"""
<example-title>

Module: <module-number>
Exercise: <exercise-id>
Author: Physical AI Course Contributors
License: Apache 2.0
Last Updated: <YYYY-MM-DD>

Description:
<multi-line-description>

Prerequisites:
- <prerequisite-1>
- <prerequisite-2>

Usage:
    python3 <example-name>.py [args]

Expected Output:
    <description-of-output>
"""

# Code implementation
```

**File Structure**:
```
static/code-examples/
├── module1-ros2/
│   ├── talker.py
│   ├── listener.py
│   ├── requirements.txt
│   └── tests/
│       └── test_talker_listener.py
├── module2-simulation/
│   ├── models/
│   │   └── unitree_h1.urdf
│   ├── worlds/
│   │   └── humanoid_lab.world
│   └── unity/
│       └── Scripts/
│           └── RobotController.cs
├── module3-isaac/
│   ├── synthetic_data_generation.py
│   └── domain_randomization.py
└── module4-vla/
    ├── openvla_inference.py
    └── rt2_manipulation.py
```

**Validation Rules**:
- All Python files have docstring header
- All code passes `flake8` linting
- All code has corresponding test in `tests/` directory
- All dependencies listed in `requirements.txt`

---

## Entity 8: Glossary Entry

**Path**: `docs/appendices/glossary.md`

**Purpose**: Technical term definitions

**Schema** (Per Entry):
```markdown
**<TERM>** - <definition-sentence>. <optional-elaboration>. <optional-example>.
```

**Formatting Rules**:
- **Term** in bold
- Definition starts with part of speech (if applicable)
- Keep definitions 1-3 sentences
- Include examples for complex concepts
- Link to relevant chapters (e.g., "See [ROS 2 Fundamentals](/modules/ros2-fundamentals) for details")

**Example**:
```markdown
**Sim-to-Real Transfer** - The process of applying policies or models trained in simulation to physical robots. This technique mitigates the reality gap through domain randomization and sim-to-sim validation. See [NVIDIA Isaac Sim](/modules/isaac-sim-synthetic-data) for implementation details.
```

---

## Entity 9: Diagram/Image Asset

**Path**: `static/img/<category>/<filename>.<ext>`

**Purpose**: Visual aids (architecture diagrams, lab layouts, robot photos)

**Categories**:
- `architecture/` - System diagrams (draw.io exports)
- `lab-setups/` - Lab layout diagrams
- `robots/` - Robot platform images (vendor photos or original)

**Metadata** (Embedded in Markdown):
```markdown
![<alt-text>](<path-to-image>)
*Figure <number>: <caption>. <source-attribution>.*
```

**File Naming Convention**:
```
<module-id>_<description>_<version>.<ext>

Examples:
- module1_ros2_architecture_v1.png
- lab_miniature_tier_layout_v2.png
- robot_unitree_h1_front_view.jpg
```

**Validation Rules**:
- All images referenced in markdown exist
- All images have alt text for accessibility
- All vendor images have attribution in caption

**Example**:
```markdown
![ROS 2 DDS Architecture](static/img/architecture/module1_ros2_dds_v1.png)
*Figure 1.1: ROS 2 Data Distribution Service (DDS) middleware architecture showing publisher-subscriber communication. Adapted from [Macenski et al., 2020].*
```

---

## Entity 10: Quickstart Guide

**Path**: `docs/quickstart.md`

**Purpose**: Contributor onboarding and local development setup

**Schema**:
```yaml
---
id: quickstart
title: Quickstart Guide
sidebar_position: 1
last_updated: <YYYY-MM-DD>
---

# <title>

## For Educators (Course Delivery)
[How to use this course in teaching]

## For Contributors (Content Development)
### Prerequisites
[Required tools and knowledge]

### Setup
[Step-by-step local development setup]

### Running Locally
[Commands to build and preview]

### Contributing Guidelines
[How to propose content changes]

## For Students (Self-Study)
[How to navigate the course independently]

## References
[Links to documentation]
```

**Validation Rules**:
- All setup commands tested in CI/CD
- All links verified by link checker

---

## Data Model Summary Table

| Entity                  | Path Pattern                          | Frontmatter | Body     | Validation Schema         |
|-------------------------|---------------------------------------|-------------|----------|---------------------------|
| Module Chapter          | `docs/modules/<module>/<id>.md`       | Yes         | Markdown | chapter-schema.yaml       |
| Exercise Chapter        | `docs/exercises/<id>.md`              | Yes         | Markdown | exercise-schema.yaml      |
| Capstone Project        | `docs/capstone/capstone-project.md`   | Yes         | Markdown | (inline validation)       |
| Lab Tier Spec           | `docs/infrastructure/<tier-id>.md`    | Yes         | Markdown | lab-tier-table-schema.md  |
| Week-by-Week Schedule   | `docs/appendices/week-by-week.md`     | Yes         | Markdown | (inline validation)       |
| Reference Entry         | `static/references.bib`               | No          | BibTeX   | BibTeX syntax             |
| Code Example            | `static/code-examples/<module>/<id>`  | No          | Code     | Linters (flake8, pylint)  |
| Glossary Entry          | `docs/appendices/glossary.md`         | No          | Markdown | (inline validation)       |
| Diagram/Image Asset     | `static/img/<category>/<id>.<ext>`    | No          | Binary   | Link checker              |
| Quickstart Guide        | `docs/quickstart.md`                  | Yes         | Markdown | (inline validation)       |

---

## Contract Enforcement

**Pre-Commit Hooks**:
1. Validate all YAML frontmatter against schemas
2. Run flake8 on all Python code
3. Check all markdown links
4. Verify all BibTeX citations have corresponding keys

**CI/CD Validation** (GitHub Actions):
1. Build Docusaurus site (fails on broken links)
2. Run Docker tests for all code examples
3. Validate citation keys match references.bib
4. Check word counts against targets

**Manual Review**:
1. Content accuracy against peer-reviewed sources
2. Pedagogical soundness of learning objectives
3. Consistency of tone and style across chapters

---

## References

- [Docusaurus Frontmatter](https://docusaurus.io/docs/api/plugins/@docusaurus/plugin-content-docs#markdown-frontmatter)
- [YAML Schema Validator](https://json-schema-everywhere.github.io/yaml)
- [BibTeX Format Guide](https://www.bibtex.org/Format/)
- [APA 7th Edition](https://apastyle.apa.org/style-grammar-guidelines)
