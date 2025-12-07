# Lab Tier Table Schema

**Version**: 1.0.0
**Last Updated**: 2025-12-07
**Purpose**: Define structured format for lab infrastructure comparison tables

---

## Overview

This schema defines the standard format for lab tier comparison tables used in Physical AI course infrastructure documentation. All lab tier tables must follow this structure for consistency and comparison.

---

## Table Structure

### Required Columns

| Column Name            | Data Type | Description                                      | Validation Rules                        |
|------------------------|-----------|--------------------------------------------------|-----------------------------------------|
| **Tier Name**          | String    | Name of lab tier                                 | "Proxy Tier" \| "Miniature Tier" \| "Premium Tier" |
| **Budget Range (USD)** | Currency  | Cost range for tier setup                        | Format: "$X,XXX - $XX,XXX"             |
| **Student Capacity**   | Integer   | Maximum students supported                       | 6-30 students                           |
| **Robots**             | String    | Physical robots included                         | "None" \| "1-2 compact" \| "3-5 full-scale" |
| **GPU Workstations**   | Integer   | Number of GPU-equipped workstations              | 0-10                                    |
| **Space (sq ft)**      | Integer   | Required lab floor area                          | 150-800 sq ft                           |
| **Use Case**           | String    | Ideal scenario for this tier                     | 50-200 characters                       |

### Optional Columns (Context-Specific)

| Column Name              | Data Type | Description                                    | When to Include                         |
|--------------------------|-----------|------------------------------------------------|-----------------------------------------|
| **GPU Model**            | String    | Specific GPU models included                   | When comparing GPU capabilities         |
| **Robot Models**         | String    | Specific robot platform models                 | When detailing hardware options         |
| **Software Licenses**    | String    | Required commercial software licenses          | When discussing costs                   |
| **Setup Time**           | String    | Estimated installation/setup time              | When planning implementation timeline   |
| **Maintenance Cost/Year**| Currency  | Annual maintenance and consumables cost        | When discussing TCO (total cost of ownership) |

---

## Standard Lab Tier Comparison Table

**Canonical Format** (used in `docs/infrastructure/lab-tiers-overview.md`):

```markdown
| Tier           | Budget Range (USD) | Student Capacity | Robots         | GPU Workstations | Space (sq ft) | Use Case                                      |
|----------------|--------------------|-----------------:|----------------|:----------------:|--------------:|-----------------------------------------------|
| **Proxy**      | $10,000 - $20,000  | 12-15            | None           | 3-5              | 150-250       | Budget-constrained programs, simulation-only  |
| **Miniature**  | $50,000 - $70,000  | 10-12            | 1-2 compact    | 3-4              | 300-400       | Mid-sized universities, hands-on AI focus     |
| **Premium**    | $120,000 - $180,000| 8-10             | 3-5 full-scale | 5-7              | 500-800       | Flagship programs, research-grade robotics    |
```

**Rendering Guidelines**:
- Use Markdown table syntax for Docusaurus compatibility
- Right-align numeric columns (`:---` for left, `---:` for right, `:---:` for center)
- Bold tier names in first column
- Use thousand separators for currency ($10,000 not $10000)
- Include units in column headers (USD, sq ft)

---

## Detailed Lab Tier Specification Schema

**Used in individual tier pages** (`docs/infrastructure/proxy-tier.md`, etc.):

### YAML Frontmatter

```yaml
---
id: <tier-id>                       # "proxy-tier" | "miniature-tier" | "premium-tier"
title: <tier-title>                 # "Proxy Tier Lab" | "Miniature Tier Lab" | "Premium Tier Lab"
sidebar_position: <number>          # 1-3
tier_level: <level>                 # 1 (Proxy) | 2 (Miniature) | 3 (Premium)
budget_range:                       # Required: Cost range
  min: <number>                     # Minimum cost in USD (integer)
  max: <number>                     # Maximum cost in USD (integer)
  currency: "USD"                   # Currency code
student_capacity: <number>          # Maximum students (6-30)
hardware_components:                # Required: Itemized equipment list
  - name: <component-name>
    quantity: <number>
    unit_cost: <number>
    total_cost: <number>            # quantity × unit_cost
    description: <description>
software_requirements:              # Required: Software stack
  - name: <software-name>
    license_type: <type>            # "Open Source" | "Commercial" | "Educational"
    cost: <number>                  # Annual cost (0 for free)
space_requirements:                 # Required: Lab space
  area_sqft: <number>
  description: <description>
pros:                               # Required: 3-5 advantages
  - "<advantage-1>"
cons:                               # Required: 3-5 limitations
  - "<limitation-1>"
use_cases:                          # Required: 2-4 ideal scenarios
  - "<use-case-1>"
last_updated: <YYYY-MM-DD>
---
```

### Markdown Body Structure

```markdown
# <tier-title>

## Overview
[1-2 paragraph description of tier and target institutions]

## Budget Breakdown

### Hardware Components

| Component                | Quantity | Unit Cost (USD) | Total Cost (USD) | Description                          |
|--------------------------|:--------:|----------------:|-----------------:|--------------------------------------|
| <component-1>            | <qty>    | <unit>          | <total>          | <description>                        |
| <component-2>            | <qty>    | <unit>          | <total>          | <description>                        |
| **Total Hardware**       |          |                 | **<sum>**        |                                      |

### Software Requirements

| Software                 | License Type   | Annual Cost (USD) | Description                          |
|--------------------------|----------------|------------------:|--------------------------------------|
| <software-1>             | <type>         | <cost>            | <description>                        |
| <software-2>             | <type>         | <cost>            | <description>                        |
| **Total Software**       |                | **<sum>**         |                                      |

### Total Budget Range: $<min> - $<max>

## Hardware Specifications

### Workstations
[Detailed specs for GPU workstations]

### Robots (if applicable)
[Detailed specs for robot platforms]

## Software Stack
[Description of required software and setup]

## Space and Facilities

**Required Area**: <area> sq ft

**Layout**:
[Description of lab layout, safety barriers, workstation placement]

**Power and Cooling**:
[Electrical and HVAC requirements]

## Strengths and Limitations

### Advantages
- <advantage-1>
- <advantage-2>
- <advantage-3>

### Limitations
- <limitation-1>
- <limitation-2>
- <limitation-3>

## Recommended Use Cases
- <use-case-1>
- <use-case-2>
- <use-case-3>

## Setup Timeline

| Phase                    | Duration      | Description                          |
|--------------------------|---------------|--------------------------------------|
| <phase-1>                | <duration>    | <description>                        |
| <phase-2>                | <duration>    | <description>                        |
| **Total Setup Time**     | **<total>**   |                                      |

## Maintenance and TCO

**Annual Maintenance Cost**: $<amount>

**5-Year Total Cost of Ownership (TCO)**: $<amount>

[Breakdown of recurring costs: consumables, software licenses, repairs]

## References
[Vendor links, equipment datasheets, ROI studies]
```

---

## Validation Rules

### Frontmatter Validation

1. **Budget consistency**: `budget_range.min < budget_range.max`
2. **Hardware totals**: Sum of `hardware_components[].total_cost` should fall within `budget_range`
3. **Component costs**: `total_cost = quantity × unit_cost` for all components
4. **Tier levels**:
   - Proxy (tier_level=1): budget_range.max < $25,000
   - Miniature (tier_level=2): budget_range.min >= $40,000, max < $80,000
   - Premium (tier_level=3): budget_range.min >= $100,000
5. **Student capacity realism**:
   - Proxy: 12-15 students
   - Miniature: 10-12 students
   - Premium: 8-10 students

### Table Validation

1. **Column completeness**: All required columns present
2. **Numeric formatting**: Currency uses thousand separators ($10,000)
3. **Alignment**: Numeric columns right-aligned
4. **Units**: All units specified in column headers
5. **Totals**: Bold "Total" rows with accurate sums

### Cross-Tier Consistency

Validation across all three tier pages:

1. **Budget ordering**: Proxy < Miniature < Premium
2. **Robot count ordering**: Proxy (0) < Miniature (1-2) < Premium (3-5)
3. **Space ordering**: Proxy area < Miniature area < Premium area
4. **Use case differentiation**: Each tier has distinct use cases with no overlap

---

## Example: Miniature Tier Hardware Table

```markdown
| Component                          | Quantity | Unit Cost (USD) | Total Cost (USD) | Description                                    |
|------------------------------------|:--------:|----------------:|-----------------:|------------------------------------------------|
| GPU Workstation (NVIDIA RTX 4090)  | 3        | $3,500          | $10,500          | Isaac Sim and VLA training                     |
| Unitree H1 Humanoid Robot          | 2        | $90,000         | $180,000         | Compact humanoid for hands-on exercises        |
| Workstation (CPU-only)             | 2        | $1,200          | $2,400           | ROS 2 development without GPU requirements     |
| Network Switch (10GbE)             | 1        | $500            | $500             | High-speed data transfer for Isaac Sim         |
| Safety Barriers                    | 4        | $300            | $1,200           | Physical barriers for robot operation zones    |
| Tool Kit (assembly/maintenance)    | 1        | $400            | $400             | Basic tools for robot maintenance              |
| **Total Hardware**                 |          |                 | **$195,000**     |                                                |
```

**Validation Checks**:
- ✅ Sum of Total Cost = $195,000
- ✅ Each row: `total_cost = quantity × unit_cost`
- ✅ Currency formatted with thousand separators
- ✅ Numeric columns right-aligned (`:---`)
- ✅ Total row in bold

---

## Software License Table Example

```markdown
| Software                           | License Type   | Annual Cost (USD) | Description                                    |
|------------------------------------|----------------|------------------:|------------------------------------------------|
| ROS 2 Humble                       | Open Source    | $0                | Robot middleware (Apache 2.0 license)          |
| NVIDIA Isaac Sim                   | Free           | $0                | Robot simulation (free with NVIDIA account)    |
| Unity Pro (Educational)            | Educational    | $0                | Game engine for visualization (free for edu)   |
| Gazebo Fortress                    | Open Source    | $0                | Physics simulation (Apache 2.0 license)        |
| GitHub Team (10 users)             | Commercial     | $400              | Version control and CI/CD                      |
| **Total Annual Software Cost**     |                | **$400**          |                                                |
```

---

## TCO (Total Cost of Ownership) Table Example

Used in ROI analysis and budget planning sections:

```markdown
| Cost Category              | Year 1    | Year 2    | Year 3    | Year 4    | Year 5    | 5-Year Total |
|----------------------------|----------:|----------:|----------:|----------:|----------:|-------------:|
| Initial Hardware           | $195,000  | $0        | $0        | $0        | $0        | $195,000     |
| Software Licenses          | $400      | $400      | $400      | $400      | $400      | $2,000       |
| Maintenance & Repairs      | $0        | $5,000    | $5,000    | $8,000    | $8,000    | $26,000      |
| Consumables (cables, etc.) | $500      | $500      | $500      | $500      | $500      | $2,500       |
| Facility Costs (power)     | $1,200    | $1,200    | $1,200    | $1,200    | $1,200    | $6,000       |
| **Total Annual Cost**      | **$197,100** | **$7,100** | **$7,100** | **$10,100** | **$10,100** | **$231,500** |
```

**Validation**:
- ✅ All costs right-aligned
- ✅ 5-Year Total = sum of Year 1-5 for each category
- ✅ Total Annual Cost = sum of all categories per year
- ✅ Currency formatted consistently

---

## CI/CD Validation Script

**Validation Command** (to be run in GitHub Actions):

```bash
# Check all lab tier pages have complete tables
./scripts/validate-lab-tiers.sh

# Verify budget ordering (Proxy < Miniature < Premium)
python3 tests/validate-tier-budgets.py
```

**Python Validation Example**:

```python
import yaml
from pathlib import Path

tier_files = [
    "docs/infrastructure/proxy-tier.md",
    "docs/infrastructure/miniature-tier.md",
    "docs/infrastructure/premium-tier.md"
]

budgets = {}
for tier_file in tier_files:
    frontmatter = extract_frontmatter(Path(tier_file))
    tier_id = frontmatter['id']
    budgets[tier_id] = frontmatter['budget_range']

    # Validate hardware totals
    hardware_total = sum(
        component['total_cost']
        for component in frontmatter['hardware_components']
    )

    assert frontmatter['budget_range']['min'] <= hardware_total <= frontmatter['budget_range']['max'], \
        f"{tier_id}: Hardware total ${hardware_total} outside budget range"

# Validate budget ordering
assert budgets['proxy-tier']['max'] < budgets['miniature-tier']['min'], \
    "Proxy tier max must be less than Miniature tier min"
assert budgets['miniature-tier']['max'] < budgets['premium-tier']['min'], \
    "Miniature tier max must be less than Premium tier min"

print("✅ All lab tier validations passed")
```

---

## References

- [Markdown Tables Guide](https://www.markdownguide.org/extended-syntax/#tables)
- [Docusaurus Markdown Features](https://docusaurus.io/docs/markdown-features)
- [YAML Schema Validation](https://json-schema-everywhere.github.io/yaml)
- Cost data sources: Vendor quotes, academic procurement records (2023-2025)
