---
id: 002
title: Physical AI Course Specification
stage: spec
date: 2025-12-06
surface: agent
model: claude-sonnet-4-5
feature: 001-physical-ai-course
branch: 001-physical-ai-course
user: unknown
command: /sp.specify
labels: ["specification", "physical-ai", "robotics", "education", "curriculum"]
links:
  spec: specs/001-physical-ai-course/spec.md
  ticket: null
  adr: null
  pr: null
files:
  - specs/001-physical-ai-course/spec.md
  - specs/001-physical-ai-course/checklists/requirements.md
tests:
  - All 16 checklist items PASSED
  - Zero [NEEDS CLARIFICATION] markers
  - 17 functional requirements testable
  - 10 measurable success criteria
  - 5 user stories with 15+ acceptance scenarios
---

## Prompt

```text
Detailed Specifications for Physical AI & Humanoid Robotics Course

Target audience: Robotics educators, curriculum designers, university program coordinators, and advanced students evaluating Physical AI and humanoid robotics curricula.

Focus: Develop a detailed specification for a 4-module Physical AI course (ROS 2, Gazebo & Unity, NVIDIA Isaac, Vision-Language-Action) culminating in a capstone project that integrates simulation, AI perception, navigation, and conversational robotics.

Success criteria:

Each module includes: clear learning objectives, high-level content, key exercises, and expected outcomes.

Capstone project specifications show integration of all modules and real-world deployment on humanoid robots.

Hardware and software requirements are listed for student workstations, Edge AI kits, and robot lab setups (Proxy, Miniature, Premium).

Provides week-by-week course overview and suggested exercises for hands-on learning.

Demonstrates feasibility, cost, and ROI for lab infrastructure (On-Premise vs Cloud-Native).

All technical claims and recommendations supported by peer-reviewed sources or industry-standard references (published within the past 10 years).

Constraints:

Word count: 3000–5000 words

Format: Markdown with APA citations

Sources: Peer-reviewed journals or conference papers within the last 10 years

Timeline: Complete within 2 weeks

Not included:

Full vendor/product comparisons (only high-level lab recommendations).

Implementation guides with complete code (conceptual workflows only).

Broad AI literature reviews unrelated to Physical AI education.

Ethical discussions (to be addressed separately).
```

## Response snapshot

Created comprehensive course specification with 5 prioritized user stories covering educational stakeholder needs:

**User Story 1 (P1)**: Course Structure Evaluation
- Target: Curriculum designers assessing accreditation fit
- Deliverables: Learning objectives, content outlines, assessment methods per module
- Test: Verify against ABET robotics engineering criteria

**User Story 2 (P1)**: Lab Infrastructure Planning
- Target: Program coordinators estimating costs for 20-30 students
- Deliverables: 3 lab tiers (Proxy $10-20K, Miniature $50-70K, Premium $120-180K)
- Test: Validate itemized hardware, software, space requirements enable budget proposals

**User Story 3 (P2)**: Hands-On Exercise Design
- Target: Educators creating weekly labs
- Deliverables: Progressive exercises per module (ROS 2 → Gazebo/Unity → Isaac → VLA)
- Test: Each module provides 2+ exercises with objectives, time, deliverables

**User Story 4 (P2)**: Capstone Project Assessment
- Target: Educators grading integrated final projects
- Deliverables: Rubric (30% integration, 25% real-world deployment, 15% VLA interface)
- Test: Specification defines integration requirements and deployment targets

**User Story 5 (P3)**: ROI and Feasibility Analysis
- Target: University decision-makers evaluating long-term sustainability
- Deliverables: On-premise vs cloud-native cost-benefit comparison
- Test: Includes capital expenditure, recurring costs, scalability, educational impact

**17 Functional Requirements** grouped by:
- Course Content (FR-001 to FR-005): Modules, capstone, week-by-week structure
- Infrastructure (FR-006 to FR-010): Lab tiers, hardware/software, cost estimates, deployment options
- Academic Rigor (FR-011 to FR-013): Peer-reviewed sources, APA citations, Markdown format
- Scope Boundaries (FR-014 to FR-017): Explicit exclusions (vendor comparisons, implementation guides, ethics)

**10 Measurable Success Criteria**:
- SC-001: Educators map course to semester in 2 hours
- SC-002: Coordinators generate budget proposal in 4 hours
- SC-003: 90% requirements verifiable without clarification
- SC-004: All claims supported by 2015-2025 peer-reviewed sources
- SC-005: Capstone demonstrates 4-module integration with measurable metrics
- SC-006: 8+ hands-on exercises identifiable (2 per module)
- SC-007: 2+ real-world curriculum case studies provided
- SC-008: ROI analysis covers 4+ dimensions (cost, scalability, accessibility, recurring)
- SC-009: Accessible to non-robotics experts (administrators, IT)
- SC-010: 3000-5000 word constraint met

**Assumptions Documented**: 10 explicit assumptions (semester structure, cohort size, robot platforms, VLA frameworks, simulation primacy, cloud options, safety protocols, prerequisites, deployment timeline)

**Out of Scope Defined**: 7 exclusions (vendor comparisons, implementation guides, AI literature reviews, ethics deep-dives, accreditation paperwork, assessment tools, industry partnerships)

**Edge Cases Addressed**: Limited budgets (<$30K), remote learning, heterogeneous robot platforms, prerequisite gaps, safety/ethics integration

**Validation Checklist Created**: specs/001-physical-ai-course/checklists/requirements.md
- 16/16 items PASSED
- Zero [NEEDS CLARIFICATION] markers
- Ready for `/sp.plan`

## Outcome

- ✅ Impact: Comprehensive educational specification enabling Physical AI course adoption decisions
- 🧪 Tests: Automated validation checklist PASSED (16/16 items), zero clarification markers, all requirements testable
- 📁 Files: Created spec.md (main specification), checklists/requirements.md (validation checklist)
- 🔁 Next prompts: `/sp.plan` to design detailed 4-module outlines and week-by-week lesson plans, `/sp.tasks` to break down into actionable writing tasks (literature review, hardware tables, cost analysis)
- 🧠 Reflection: Specification balances educational stakeholder needs (educators, coordinators, decision-makers) with concrete infrastructure requirements (3 lab tiers, hardware/software specs, cost estimates). Zero clarification markers achieved through informed assumptions documented transparently.

## Evaluation notes (flywheel)

- Failure modes observed: None - specification completed with full validation checklist passing
- Graders run and results (PASS/FAIL): PASS - All 16 checklist items validated (content quality, requirement completeness, feature readiness)
- Prompt variant (if applicable): Educational course specification adapted from standard feature spec template
- Next experiment (smallest change to try): Monitor `/sp.plan` phase to verify module outlines and week-by-week breakdown align with FR-001 to FR-005 requirements; validate peer-reviewed source gathering meets FR-011 citation needs
