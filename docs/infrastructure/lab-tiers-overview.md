---
id: lab-tiers-overview
title: Lab Tiers Overview
sidebar_position: 1
last_updated: 2025-12-07
---

# Lab Tiers Overview

This course offers **three lab infrastructure tiers** to accommodate varying institutional budgets, student capacities, and program goals. Each tier provides a complete learning experience while optimizing for different constraints.

## Tier Comparison Table

| Tier           | Budget Range (USD) | Student Capacity | Robots         | GPU Workstations | Space (sq ft) | Use Case                                      |
|----------------|--------------------|-----------------:|----------------|:----------------:|--------------:|-----------------------------------------------|
| **Proxy**      | $10,000 - $20,000  | 12-15            | None           | 3-5              | 150-250       | Budget-constrained programs, simulation-only  |
| **Miniature**  | $50,000 - $70,000  | 10-12            | 1-2 compact    | 3-4              | 300-400       | Mid-sized universities, hands-on AI focus     |
| **Premium**    | $120,000 - $180,000| 8-10             | 3-5 full-scale | 5-7              | 500-800       | Flagship programs, research-grade robotics    |

## Tier Descriptions

### Proxy Tier ($10-20K)

**Philosophy**: Simulation-first approach using GPU workstations for Gazebo, Unity, and NVIDIA Isaac Sim. Students complete all learning objectives through virtual environments, with optional field trips to partner institutions for physical robot exposure.

**Strengths**:
- Lowest cost barrier to entry
- Rapid iteration (no hardware setup/maintenance)
- Scalable to larger class sizes (15+ students)
- Zero safety risk from physical robots

**Limitations**:
- No hands-on physical robot experience
- Sim-to-real transfer concepts taught theoretically
- Capstone projects limited to simulation demonstrations

**Best For**: Community colleges, online programs, initial curriculum pilots

[View Detailed Specification →](/infrastructure/proxy-tier)

---

### Miniature Tier ($50-70K)

**Philosophy**: Balance simulation and physical experience using compact humanoid robots (Unitree H1, G1) alongside GPU workstations. Most development in simulation, validation on real hardware.

**Strengths**:
- Real hardware manipulation experience
- Affordable compared to full-scale humanoids ($90K vs. $150K+)
- GPU workstations support advanced AI training
- Sufficient for manipulation and navigation research

**Limitations**:
- Compact robots have limited payload (2-5 kg vs. 10-20 kg)
- Reduced reach and workspace compared to full-scale
- Battery life constraints (1-2 hours vs. 3-4 hours)

**Best For**: Mid-sized universities, robotics minors, AI research labs

[View Detailed Specification →](/infrastructure/miniature-tier)

---

### Premium Tier ($120-180K)

**Philosophy**: Research-grade infrastructure with multiple full-scale humanoid robots (Boston Dynamics Atlas, Agility Robotics Digit, Tesla Optimus) and extensive GPU compute for fleet-scale experiments.

**Strengths**:
- Full-scale humanoids for realistic task execution
- Multiple robots enable multi-robot coordination research
- Publication-quality results for conferences/journals
- Industry partnership opportunities

**Limitations**:
- High upfront and maintenance costs
- Requires dedicated lab space and safety infrastructure
- Smaller student capacity (8-10 due to supervision needs)

**Best For**: Flagship robotics programs, PhD-granting institutions, industry-sponsored labs

[View Detailed Specification →](/infrastructure/premium-tier)

---

## Decision Framework

### Budget Constraints

**&lt;$25K Available**: Proxy Tier (simulation-only)
**$40-80K Available**: Miniature Tier (1-2 compact robots)
**$100K+ Available**: Premium Tier (3-5 full-scale robots)

### Program Goals

**Goal: Introduce robotics to undergraduates** → Proxy or Miniature
**Goal: Train industry-ready engineers** → Miniature or Premium
**Goal: Conduct publishable research** → Premium

### Student Capacity

**15+ students** → Proxy (scalable simulation)
**10-15 students** → Miniature (limited robot access, rotate teams)
**8-10 students** → Premium (intensive hands-on supervision)

### Institutional Context

**No existing robotics lab** → Start with Proxy, upgrade to Miniature after 2-3 years
**Existing wheeled robot lab** → Add Miniature tier for humanoid experience
**Established robotics program** → Premium tier for flagship differentiation

---

## Phased Adoption Strategy

Many institutions start small and expand over 3-5 years:

**Year 1**: Proxy Tier ($15K)
- Validate curriculum with simulation-only delivery
- Build student enrollment to justify hardware investment

**Year 2**: Add Miniature Tier ($60K incremental)
- Purchase 1-2 compact humanoids
- Pilot physical robot exercises with subset of students

**Year 3**: Upgrade to Premium Tier ($100K incremental)
- Add 2-3 full-scale humanoids
- Launch graduate-level research track

**Total 3-Year Investment**: $175K (vs. $150K upfront for immediate Premium tier)

**Advantage**: De-risk investment, allow curriculum iteration, demonstrate ROI for funding stakeholders

---

## Software and Licensing Costs

All tiers share common software requirements:

| Software                | License Type   | Annual Cost | Notes                          |
|-------------------------|----------------|------------:|--------------------------------|
| ROS 2 Humble            | Open Source    | $0          | Apache 2.0 license             |
| Gazebo Fortress         | Open Source    | $0          | Apache 2.0 license             |
| NVIDIA Isaac Sim        | Free           | $0          | Requires NVIDIA account        |
| Unity Pro (Educational) | Educational    | $0          | Free for accredited programs   |
| GitHub Team (10 users)  | Commercial     | $400        | Version control and CI/CD      |
| **Total Annual**        |                | **$400**    | Negligible compared to hardware|

**Note**: Unity Pro Educational license requires institutional accreditation verification. Commercial use requires paid license ($2,040/year).

---

## Next Steps

1. **Review Detailed Tier Specifications**:
   - [Proxy Tier →](/infrastructure/proxy-tier)
   - [Miniature Tier →](/infrastructure/miniature-tier)
   - [Premium Tier →](/infrastructure/premium-tier)

2. **Assess Deployment Options**:
   - [On-Premise vs. Cloud Infrastructure →](/infrastructure/deployment-options)

3. **Evaluate Return on Investment**:
   - [ROI Analysis and Feasibility →](/appendices/roi-analysis)

4. **Plan Implementation**:
   - Contact vendors for quotes (Unitree, Boston Dynamics, Agility Robotics)
   - Secure lab space and electrical/network infrastructure
   - Budget for safety training and lab supervision

---

## Support Resources

- **Hardware Vendors**: See [Deployment Options](/infrastructure/deployment-options) for vendor contacts
- **Funding Opportunities**: NSF MRI, industry partnerships, alumni donations
- **Peer Institutions**: Join Physical AI Educators Network for shared resources

**Questions?** Contact course maintainers at [GitHub Issues](https://github.com/your-organization/physical-ai-course/issues).
