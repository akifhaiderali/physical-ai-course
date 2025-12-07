---
id: 004
title: Physical AI Course Tasks Generation
stage: tasks
date: 2025-12-06
surface: agent
model: claude-sonnet-4-5
feature: 001-physical-ai-course
branch: 001-physical-ai-course
user: unknown
command: /sp.tasks
labels: ["tasks", "task-breakdown", "user-stories", "docusaurus", "book-creation"]
links:
  spec: specs/001-physical-ai-course/spec.md
  ticket: null
  adr: null
  pr: null
files:
  - specs/001-physical-ai-course/tasks.md
tests:
  - 97 tasks generated across 8 phases
  - All tasks follow checklist format (checkbox, ID, labels, file paths)
  - 5 user stories mapped to independent phases
  - Parallel opportunities identified for 60+ tasks
  - MVP strategy defined (US1 + US2)
---

## Prompt

```text
Generate actionable task breakdown for Physical AI & Humanoid Robotics Course Book based on:
- plan.md (14-chapter structure, Docusaurus architecture)
- spec.md (5 user stories with priorities P1, P2, P3)
```

## Response snapshot

Generated comprehensive tasks.md with **97 tasks** organized across **8 phases**:

### Phase Structure

**Phase 1: Setup** (9 tasks)
- Initialize Node.js project and Docusaurus 3.x
- Setup GitHub Actions CI/CD for GitHub Pages
- Create directory structure and configuration files
- Parallel opportunities: 7 tasks (T003-T009)

**Phase 2: Foundational** (15 tasks)
- Generate research.md and data-model.md
- Gather 50-100 peer-reviewed references (2015-2025) across 6 research areas
- Create contracts (chapter, exercise, lab tier schemas)
- Setup Docker test environments for code examples
- Parallel opportunities: 14 tasks (T011-T024)
- **CRITICAL**: Blocks all user story work

**Phase 3: User Story 1 - Course Structure Evaluation** (P1, 15 tasks)
- Create all 10 module chapters (ROS 2, Simulation, Isaac, VLA)
- Create week-by-week semester schedule
- Update references and glossary
- Build validation and review
- **Independent Test**: Curriculum committee can evaluate course structure
- Parallel opportunities: 10 chapter creation tasks (T025-T034)

**Phase 4: User Story 2 - Lab Infrastructure Planning** (P1, 12 tasks)
- Create 5 infrastructure chapters (lab tiers overview, 3 tier specs, deployment options)
- Create diagrams (lab layouts, network topology)
- Source robot platform images
- Build validation and review
- **Independent Test**: Coordinator can select tier, estimate costs, plan space
- Parallel opportunities: 8 content/diagram tasks (T040-T047)

**Phase 5: User Story 3 - Hands-On Exercise Design** (P2, 16 tasks)
- Create 4 exercise chapters (ROS 2, simulation, Isaac, VLA)
- Write code examples for each module
- Create Docker tests for code validation
- Run all tests and verify passing
- **Independent Test**: Educator finds progressive exercises, can setup labs
- Parallel opportunities: 8 content/code tasks (T052-T059)

**Phase 6: User Story 4 - Capstone Project Assessment** (P2, 8 tasks)
- Create capstone project chapter
- Define milestones with 4-module integration
- Create evaluation rubric (30% integration, 25% deployment, etc.)
- Write example scenario and code skeleton
- **Independent Test**: Students receive spec, educators can grade, program can showcase

**Phase 7: User Story 5 - ROI and Feasibility Analysis** (P3, 8 tasks)
- Create ROI analysis section
- On-premise vs cloud cost comparison tables
- Document 5-year growth scenarios
- Add case studies of 2+ universities
- **Independent Test**: CFO can compare costs, department head can assess scalability

**Phase 8: Polish & Cross-Cutting Concerns** (14 tasks)
- Create link checker and citation validator
- Verify word counts (800-1,500 per chapter, ~20,000 total)
- Run build and deployment validations
- Constitution compliance check
- Deploy to GitHub Pages

### Task Organization by User Story

**Mapping**:
- **US1 (P1)**: 10 module chapters + week-by-week schedule + appendices (T025-T039)
- **US2 (P1)**: 5 infrastructure chapters + diagrams + images (T040-T051)
- **US3 (P2)**: 4 exercise chapters + 4 code examples + Docker tests (T052-T067)
- **US4 (P2)**: 1 capstone chapter + rubric + example (T068-T075)
- **US5 (P3)**: 1 ROI analysis + cost tables + case studies (T076-T083)

**All tasks follow required checklist format**:
- ✅ Checkbox: `- [ ]`
- ✅ Task ID: T001-T097 sequential
- ✅ [P] marker: 60+ parallelizable tasks
- ✅ [Story] label: US1, US2, US3, US4, US5 for user story phases
- ✅ File paths: Exact paths for all content/code/config files

### Dependencies & Execution Order

**Critical Path**:
1. Setup (Phase 1) → Foundational (Phase 2) → [BLOCKS all user stories]
2. After Foundational complete:
   - US1 (P1): Independent, can start immediately
   - US2 (P1): Independent, can start immediately
   - US3 (P2): Independent (references US1 but testable separately)
   - US4 (P2): Independent (integrates US1/US3 but testable separately)
   - US5 (P3): Independent (references US2 but testable separately)

**Parallel Opportunities**:
- 7 Setup tasks can run in parallel
- 14 Foundational tasks can run in parallel
- All 5 user stories can be worked on simultaneously by different team members
- Within US1: 10 module chapters can be written in parallel
- Within US2: 8 infrastructure chapters/diagrams can be created in parallel
- Within US3: 8 exercise chapters/code examples can be developed in parallel

### Implementation Strategies Defined

**MVP First** (US1 + US2 only):
- Educators can evaluate course structure
- Coordinators can plan lab budgets
- Deploy to GitHub Pages for stakeholder review

**Incremental Delivery**:
- Each user story adds value without breaking previous deliverables
- Can stop after any story and have working subset

**Parallel Team Strategy**:
- 5 team members can work on 5 user stories simultaneously after Foundational phase

### Validation Criteria

**Per Chapter**:
- Word count 800-1,500
- Docusaurus frontmatter (id, title, sidebar_position)
- Learning objectives + summary
- ≥1 code example (if applicable)
- APA 7th edition citations
- Internal links working
- `npm run build` passes

**Complete Book**:
- 14 chapters total
- ~19,600-20,000 words
- 5 user stories independently deliverable
- 50-100 peer-reviewed references (2015-2025)
- All code examples tested
- GitHub Pages deployment successful
- Constitution compliance verified

## Outcome

- ✅ Impact: Comprehensive actionable task breakdown for ~20,000-word book creation
- 🧪 Tests: All 97 tasks validate checklist format, dependencies clear, parallel opportunities maximized
- 📁 Files: Created tasks.md (420+ lines, 8 phases, 5 user stories, dependency graph, implementation strategies)
- 🔁 Next prompts: Begin implementation with Phase 1 (Setup), then Phase 2 (Foundational), then parallel user story execution
- 🧠 Reflection: Task breakdown successfully maps 14-chapter book structure to 5 user stories, enabling independent development and incremental delivery. MVP scope (US1+US2) provides immediate value to educators and coordinators.

## Evaluation notes (flywheel)

- Failure modes observed: None - tasks generated successfully with complete coverage
- Graders run and results (PASS/FAIL): PASS - All tasks follow checklist format, dependencies documented, parallel opportunities identified
- Prompt variant (if applicable): Documentation project adapted from software development task template
- Next experiment (smallest change to try): Monitor Phase 1-2 execution to verify setup and foundational tasks produce expected artifacts (Docusaurus config, research.md, references.bib); validate parallel execution efficiency in Phase 3-7
