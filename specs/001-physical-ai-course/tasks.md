# Tasks: Physical AI & Humanoid Robotics Course Book

**Input**: Design documents from `/specs/001-physical-ai-course/`
**Prerequisites**: plan.md (required), spec.md (required for user stories)

**Note**: This is a documentation/book project. No traditional tests are needed - validation is through build success, citation verification, and content quality review.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each deliverable.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3, US4, US5)
- Include exact file paths in descriptions

## Path Conventions

This is a Docusaurus documentation project:
- **Content**: `docs/` at repository root
- **Static assets**: `static/` at repository root
- **Configuration**: Root-level config files
- **Specs**: `specs/001-physical-ai-course/` for planning documents

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic Docusaurus structure

- [X] T001 Initialize Node.js project with package.json at repository root
- [X] T002 Install Docusaurus 3.x dependencies via npm (docusaurus, react, react-dom)
- [X] T003 [P] Create Docusaurus configuration in docusaurus.config.js
- [X] T004 [P] Create sidebar navigation structure in sidebars.js
- [X] T005 [P] Create custom CSS for academic styling in src/css/custom.css
- [X] T006 [P] Setup GitHub Actions workflow in .github/workflows/deploy.yml for GitHub Pages deployment
- [X] T007 [P] Create directory structure: docs/, static/img/, src/components/
- [X] T008 [P] Initialize BibTeX references file at static/references.bib
- [X] T009 [P] Create .gitignore for Node.js and Docusaurus artifacts

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure and research that MUST be complete before ANY user story content can be written

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

- [ ] T010 Generate research.md in specs/001-physical-ai-course/ documenting all 8 research decisions from plan
- [ ] T011 [P] Gather 10-15 peer-reviewed ROS 2 education sources (2015-2025) and add to references.bib
- [ ] T012 [P] Gather 8-10 peer-reviewed Gazebo/Unity simulation sources (2015-2025) and add to references.bib
- [ ] T013 [P] Gather 5-8 NVIDIA Isaac Sim sources (2015-2025) and add to references.bib
- [ ] T014 [P] Gather 10-15 VLA framework sources (RT-2, OpenVLA) (2015-2025) and add to references.bib
- [ ] T015 [P] Gather 10-15 humanoid robotics education sources (2015-2025) and add to references.bib
- [ ] T016 [P] Gather 5-10 curriculum design/ABET sources (2015-2025) and add to references.bib
- [ ] T017 [P] Create book introduction/landing page in docs/intro.md with Docusaurus frontmatter
- [ ] T018 [P] Create glossary structure in docs/appendices/glossary.md
- [ ] T019 [P] Setup Docker test environments for code examples (docker-compose.yml at root)
- [ ] T020 Generate data-model.md in specs/001-physical-ai-course/ defining 10 content entities
- [ ] T021 [P] Create chapter schema contract in specs/001-physical-ai-course/contracts/chapter-schema.yaml
- [ ] T022 [P] Create exercise schema contract in specs/001-physical-ai-course/contracts/exercise-schema.yaml
- [ ] T023 [P] Create lab tier table schema in specs/001-physical-ai-course/contracts/lab-tier-table-schema.md
- [ ] T024 Generate quickstart.md in specs/001-physical-ai-course/ for contributor onboarding

**Checkpoint**: Foundation ready - user story content creation can now begin in parallel

---

## Phase 3: User Story 1 - Course Structure Evaluation (Priority: P1) 🎯 MVP

**Goal**: Educators can assess whether the 4-module course meets accreditation requirements by reviewing detailed module outlines, learning objectives, and exercises.

**Independent Test**: Curriculum committee can identify Module 1 learning objectives, map 4 modules to 12-16 week semester, and verify capstone integrates all modules.

### Content for User Story 1

- [ ] T025 [P] [US1] Create Module 1 Chapter 1: ROS 2 Intro & Basics in docs/modules/module-1-ros2-intro.md
- [ ] T026 [P] [US1] Create Module 1 Chapter 2: ROS 2 Navigation Stack in docs/modules/module-1-ros2-navigation.md
- [ ] T027 [P] [US1] Create Module 1 Chapter 3: Advanced Multi-Robot Systems in docs/modules/module-1-ros2-advanced.md
- [ ] T028 [P] [US1] Create Module 2 Chapter 1: Gazebo for Robotics in docs/modules/module-2-gazebo.md
- [ ] T029 [P] [US1] Create Module 2 Chapter 2: Unity Robotics Integration in docs/modules/module-2-unity.md
- [ ] T030 [P] [US1] Create Module 3 Chapter 1: Isaac Sim Intro & Synthetic Data in docs/modules/module-3-isaac-intro.md
- [ ] T031 [P] [US1] Create Module 3 Chapter 2: Sim-to-Real Transfer in docs/modules/module-3-sim-to-real.md
- [ ] T032 [P] [US1] Create Module 4 Chapter 1: VLA Concepts in docs/modules/module-4-vla-concepts.md
- [ ] T033 [P] [US1] Create Module 4 Chapter 2: VLA Integration with Robots in docs/modules/module-4-vla-integration.md
- [ ] T034 [P] [US1] Create Module 4 Chapter 3: VLA Manipulation Tasks in docs/modules/module-4-vla-manipulation.md
- [ ] T035 [US1] Create week-by-week semester schedule in docs/appendices/week-by-week.md mapping modules to 12-16 weeks
- [ ] T036 [US1] Add all Module 1-4 citations to docs/appendices/references.md with APA formatting
- [ ] T037 [US1] Update glossary in docs/appendices/glossary.md with all technical terms from modules
- [ ] T038 [US1] Run npm run build to validate all module chapters render correctly
- [ ] T039 [US1] Review all module chapters for 800-1,500 word count compliance and technical accuracy

**Checkpoint**: At this point, User Story 1 should be fully functional - educators can evaluate the complete 4-module course structure.

---

## Phase 4: User Story 2 - Lab Infrastructure Planning (Priority: P1)

**Goal**: Program coordinators can estimate cost, space, and technical requirements for labs supporting 20-30 students.

**Independent Test**: Coordinator with $50K budget can select Miniature tier, IT can provision software, facilities can determine space needs for Premium tier.

### Content for User Story 2

- [ ] T040 [P] [US2] Create lab tiers overview chapter in docs/infrastructure/lab-tiers-overview.md
- [ ] T041 [P] [US2] Create Proxy tier specification in docs/infrastructure/proxy-tier.md with hardware/software tables
- [ ] T042 [P] [US2] Create Miniature tier specification in docs/infrastructure/miniature-tier.md with hardware/software tables
- [ ] T043 [P] [US2] Create Premium tier specification in docs/infrastructure/premium-tier.md with hardware/software tables
- [ ] T044 [P] [US2] Create deployment options comparison in docs/infrastructure/deployment-options.md (on-premise vs cloud)
- [ ] T045 [P] [US2] Create lab layout diagrams for each tier using draw.io, export to static/img/lab-setups/
- [ ] T046 [P] [US2] Source and attribute robot platform images to static/img/robots/ (Unitree, Figure, vendor photos)
- [ ] T047 [P] [US2] Create network topology diagrams for lab setups, save to static/img/architecture/
- [ ] T048 [US2] Add lab infrastructure citations (cost-benefit analyses, case studies) to docs/appendices/references.md
- [ ] T049 [US2] Update glossary with lab tier and hardware terminology in docs/appendices/glossary.md
- [ ] T050 [US2] Run npm run build to validate all infrastructure chapters render correctly
- [ ] T051 [US2] Review infrastructure chapters for accuracy and budget estimate validation

**Checkpoint**: At this point, User Stories 1 AND 2 should both work independently - educators AND coordinators have complete information.

---

## Phase 5: User Story 3 - Hands-On Exercise Design (Priority: P2)

**Goal**: Educators can design weekly labs that scaffold from ROS 2 basics to advanced VLA tasks.

**Independent Test**: Educator finds progressive ROS 2 exercises (Weeks 1-6), TA can setup Isaac Sim environments, students can perform VLA manipulation exercises.

### Content for User Story 3

- [ ] T052 [P] [US3] Create ROS 2 exercises chapter in docs/exercises/ros2-exercises.md with detailed exercise specs
- [ ] T053 [P] [US3] Create simulation exercises chapter in docs/exercises/simulation-exercises.md for Gazebo/Unity
- [ ] T054 [P] [US3] Create Isaac Sim exercises chapter in docs/exercises/isaac-exercises.md with sim-to-real exercises
- [ ] T055 [P] [US3] Create VLA exercises chapter in docs/exercises/vla-exercises.md with manipulation tasks
- [ ] T056 [P] [US3] Write ROS 2 publisher/subscriber code example for Module 1 Chapter 1, save to static/code-examples/ros2-pubsub.py
- [ ] T057 [P] [US3] Write ROS 2 navigation example for Module 1 Chapter 2, save to static/code-examples/ros2-nav.py
- [ ] T058 [P] [US3] Write Gazebo simulation launch file for Module 2 Chapter 1, save to static/code-examples/gazebo-launch.xml
- [ ] T059 [P] [US3] Write VLA manipulation example for Module 4 Chapter 3, save to static/code-examples/vla-grasp.py
- [ ] T060 [US3] Create Docker test for ROS 2 examples in tests/code-examples/test-ros2.py
- [ ] T061 [US3] Create Docker test for Gazebo examples in tests/code-examples/test-gazebo.py
- [ ] T062 [US3] Create Docker test for VLA examples in tests/code-examples/test-vla.py
- [ ] T063 [US3] Run all code example tests via docker-compose up and verify passing
- [ ] T064 [US3] Add exercise-specific citations to docs/appendices/references.md
- [ ] T065 [US3] Update glossary with exercise-specific terminology in docs/appendices/glossary.md
- [ ] T066 [US3] Run npm run build to validate all exercise chapters render correctly
- [ ] T067 [US3] Review exercise chapters for 1-page specification compliance and clarity

**Checkpoint**: All user stories 1, 2, AND 3 should now be independently functional - complete course structure, lab planning, and exercises.

---

## Phase 6: User Story 4 - Capstone Project Assessment (Priority: P2)

**Goal**: Educators can design comprehensive capstone that assesses mastery across all 4 modules.

**Independent Test**: Students receive spec requiring ROS 2 + simulation + Isaac + VLA integration; educators can apply evaluation rubric; program can showcase deliverables.

### Content for User Story 4

- [ ] T068 [US4] Create capstone project chapter in docs/capstone/capstone-project.md
- [ ] T069 [US4] Define capstone milestones with module integration requirements in capstone chapter
- [ ] T070 [US4] Create evaluation rubric table (30% integration, 25% deployment, 20% simulation, 15% VLA, 10% docs)
- [ ] T071 [US4] Write example capstone scenario: "VLA-commanded humanoid navigation and object manipulation"
- [ ] T072 [US4] Create capstone code example skeleton showing ROS 2 + VLA integration, save to static/code-examples/capstone-skeleton.py
- [ ] T073 [US4] Add capstone project citations (portfolio assessment, integrative projects) to docs/appendices/references.md
- [ ] T074 [US4] Run npm run build to validate capstone chapter renders correctly
- [ ] T075 [US4] Review capstone chapter for integration requirements completeness and rubric clarity

**Checkpoint**: All user stories 1-4 should now work independently - full course with capstone.

---

## Phase 7: User Story 5 - ROI and Feasibility Analysis (Priority: P3)

**Goal**: Decision-makers can evaluate ROI by comparing on-premise vs cloud-native deployments.

**Independent Test**: CFO can compare cost data (on-premise vs cloud), department head can assess scalability, accreditation review finds educational impact evidence.

### Content for User Story 5

- [ ] T076 [US5] Create ROI analysis section in docs/appendices/roi-analysis.md
- [ ] T077 [US5] Create on-premise vs cloud cost comparison table (upfront, recurring, scalability, accessibility)
- [ ] T078 [US5] Document 5-year growth scenarios for both deployment options
- [ ] T079 [US5] Add case studies of 2+ universities with Physical AI programs (for SC-007 requirement)
- [ ] T080 [US5] Include student placement rates, industry partnerships, research publications metrics
- [ ] T081 [US5] Add ROI and case study citations (cost-benefit analyses, educational impact studies) to docs/appendices/references.md
- [ ] T082 [US5] Run npm run build to validate ROI analysis renders correctly
- [ ] T083 [US5] Review ROI analysis for data accuracy and completeness

**Checkpoint**: All user stories complete - full book with course structure, infrastructure, exercises, capstone, and ROI analysis.

---

## Phase 8: Polish & Cross-Cutting Concerns

**Purpose**: Final quality checks, build validation, and deployment

- [ ] T084 [P] Create link checker script in tests/link-checker.js to validate internal links
- [ ] T085 [P] Create citation validator script in tests/citation-validator.js to verify APA 7th edition format
- [ ] T086 [P] Run link checker across all chapters and fix broken links
- [ ] T087 [P] Run citation validator and fix any APA formatting errors
- [ ] T088 [P] Verify all 14 chapters meet 800-1,500 word count requirement
- [ ] T089 [P] Verify total word count is ~19,600-20,000 words (SC-010)
- [ ] T090 [P] Test local Docusaurus preview with npm start and verify navigation
- [ ] T091 [P] Run final npm run build and ensure zero errors/warnings
- [ ] T092 [P] Test GitHub Actions deployment workflow with dry-run
- [ ] T093 [P] Review all chapters for consistent tone (instructional, friendly, professional)
- [ ] T094 [P] Review all code examples for consistent formatting and comments
- [ ] T095 [P] Verify all images have descriptive alt text for accessibility
- [ ] T096 [P] Final constitution compliance check against all 7 principles
- [ ] T097 Deploy to GitHub Pages via GitHub Actions and verify live site

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories
- **User Stories (Phase 3-7)**: All depend on Foundational phase completion
  - User Story 1 (P1): Can start after Foundational - No dependencies on other stories
  - User Story 2 (P1): Can start after Foundational - No dependencies on other stories
  - User Story 3 (P2): Can start after Foundational - Integrates with US1 modules but independently testable
  - User Story 4 (P2): Can start after Foundational - Integrates with US1/US3 but independently testable
  - User Story 5 (P3): Can start after Foundational - References US2 infrastructure but independently testable
- **Polish (Phase 8)**: Depends on all desired user stories being complete

### User Story Dependencies

- **User Story 1 (P1)**: Can start after Foundational (Phase 2) - Creates core 4-module content
- **User Story 2 (P1)**: Can start after Foundational (Phase 2) - Creates infrastructure documentation
- **User Story 3 (P2)**: Can start after Foundational (Phase 2) - Creates exercises referencing modules from US1
- **User Story 4 (P2)**: Can start after Foundational (Phase 2) - Creates capstone integrating US1 modules
- **User Story 5 (P3)**: Can start after Foundational (Phase 2) - Creates ROI analysis referencing US2 infrastructure

### Within Each User Story

- Content creation tasks marked [P] can run in parallel (different chapter files)
- Build validation must run after all content for that story is complete
- Review must be final step before checkpoint

### Parallel Opportunities

- **Phase 1 (Setup)**: All tasks marked [P] can run in parallel (T003-T009)
- **Phase 2 (Foundational)**: Most tasks can run in parallel:
  - Research gathering (T011-T016): Parallel
  - Document generation (T017-T024): Parallel after T010
- **User Stories (Phase 3-7)**: Can run in parallel by different team members:
  - Developer A: User Story 1 (modules)
  - Developer B: User Story 2 (infrastructure)
  - Developer C: User Story 3 (exercises)
  - Developer D: User Story 4 (capstone)
  - Developer E: User Story 5 (ROI)
- **Within Each Story**: Chapter creation tasks marked [P] can run in parallel

---

## Parallel Example: User Story 1 (Module Content)

```bash
# All 10 module chapters can be written in parallel:
Task T025: docs/modules/module-1-ros2-intro.md
Task T026: docs/modules/module-1-ros2-navigation.md
Task T027: docs/modules/module-1-ros2-advanced.md
Task T028: docs/modules/module-2-gazebo.md
Task T029: docs/modules/module-2-unity.md
Task T030: docs/modules/module-3-isaac-intro.md
Task T031: docs/modules/module-3-sim-to-real.md
Task T032: docs/modules/module-4-vla-concepts.md
Task T033: docs/modules/module-4-vla-integration.md
Task T034: docs/modules/module-4-vla-manipulation.md
```

---

## Parallel Example: User Story 2 (Infrastructure)

```bash
# All infrastructure chapters and diagrams can be created in parallel:
Task T040: docs/infrastructure/lab-tiers-overview.md
Task T041: docs/infrastructure/proxy-tier.md
Task T042: docs/infrastructure/miniature-tier.md
Task T043: docs/infrastructure/premium-tier.md
Task T044: docs/infrastructure/deployment-options.md
Task T045: static/img/lab-setups/ (diagrams)
Task T046: static/img/robots/ (images)
Task T047: static/img/architecture/ (diagrams)
```

---

## Implementation Strategy

### MVP First (User Stories 1 + 2 Only)

1. Complete Phase 1: Setup
2. Complete Phase 2: Foundational (CRITICAL - blocks all stories)
3. Complete Phase 3: User Story 1 (Course Structure)
4. Complete Phase 4: User Story 2 (Lab Infrastructure)
5. **STOP and VALIDATE**: Educators can evaluate course, coordinators can plan labs
6. Deploy MVP to GitHub Pages for stakeholder review

### Incremental Delivery

1. Complete Setup + Foundational → Foundation ready
2. Add User Story 1 (Modules) → Educators can evaluate course structure (MVP!)
3. Add User Story 2 (Infrastructure) → Coordinators can plan budgets
4. Add User Story 3 (Exercises) → Educators can design weekly labs
5. Add User Story 4 (Capstone) → Complete course with assessment
6. Add User Story 5 (ROI) → Decision-makers have full analysis
7. Each story adds value without breaking previous deliverables

### Parallel Team Strategy

With multiple content creators:

1. Team completes Setup + Foundational together
2. Once Foundational is done:
   - Creator A: User Story 1 (10 module chapters)
   - Creator B: User Story 2 (5 infrastructure chapters + diagrams)
   - Creator C: User Story 3 (4 exercise chapters + code examples)
   - Creator D: User Story 4 (1 capstone chapter)
   - Creator E: User Story 5 (1 ROI analysis section)
3. Stories complete and integrate independently
4. Final polish phase validates all content together

---

## Notes

- **[P] tasks**: Different files, no dependencies, can run in parallel
- **[Story] label**: Maps task to specific user story for traceability
- **Each user story is independently deliverable**: Can stop after any story and have working subset
- **No traditional tests**: Book validation is through build success (`npm run build`), citation checks, link validation, and content review
- **Word count targets**: 800-1,500 per chapter, ~20,000 total
- **All code examples must be tested** before chapter merge (Docker tests in Phase 5)
- **Commit after each task or logical group** (e.g., all Module 1 chapters together)
- **Stop at any checkpoint** to validate story independently before proceeding

## Validation Checklist (Before Merge)

For each chapter:
- [ ] Word count 800-1,500
- [ ] Docusaurus frontmatter present (id, title, sidebar_position)
- [ ] Learning objectives stated in introduction
- [ ] At least 1 code example (if applicable to chapter)
- [ ] Summary with key takeaways
- [ ] All citations in APA 7th edition format
- [ ] All internal links working
- [ ] `npm run build` passes

For the complete book:
- [ ] All 14 chapters complete
- [ ] Total word count ~19,600-20,000
- [ ] All 5 user stories deliverable independently
- [ ] 50-100 peer-reviewed references (2015-2025)
- [ ] All code examples tested and passing
- [ ] GitHub Pages deployment successful
- [ ] Constitution compliance verified
