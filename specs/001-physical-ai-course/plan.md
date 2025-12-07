# Implementation Plan: Physical AI & Humanoid Robotics Course Book

**Branch**: `001-physical-ai-course` | **Date**: 2025-12-06 | **Spec**: [spec.md](./spec.md)
**Input**: Feature specification from `/specs/001-physical-ai-course/spec.md`

## Summary

This plan outlines the technical architecture and implementation strategy for creating a comprehensive ~20,000-word educational book on Physical AI and Humanoid Robotics using a spec-driven approach. The book will be built using Docusaurus, deployed to GitHub Pages, and generated through an integrated workflow combining Spec-Kit Plus (for structured content planning) and Claude Code (for automated content drafting and iteration). The book covers four main modules (ROS 2, Gazebo & Unity, NVIDIA Isaac, Vision-Language-Action), a capstone project, hardware/lab infrastructure guidance, and comprehensive appendices with APA-cited references.

**Primary Requirements**:
- Spec-driven book creation workflow (constitution principle I)
- Docusaurus-based static site with GitHub Pages deployment
- ~20,000 words total across 8-18 chapters
- Each chapter: 800-1,500 words, runnable code examples, APA citations
- Module-to-chapter mapping with detailed topic breakdowns and exercises
- Lab infrastructure documentation (3 tiers: Proxy, Miniature, Premium)
- Build validation and deployment automation

**Technical Approach** (from research):
- **Framework**: Docusaurus v3.x (latest stable) for static site generation
- **Content Pipeline**: Spec-Kit Plus for planning → Claude Code for drafting → iterative refinement
- **Deployment**: GitHub Actions CI/CD → GitHub Pages (gh-pages branch)
- **Quality Assurance**: Automated build checks, link validation, APA citation verification
- **Research-Concurrent**: Gather peer-reviewed sources (2015-2025) while drafting content

## Technical Context

**Language/Version**: Markdown/MDX, Node.js 18+, Docusaurus 3.x
**Primary Dependencies**: Docusaurus, React (for MDX components), remark/rehype plugins for citations
**Storage**: Git repository (GitHub), static assets in `/static/`, chapters in `/docs/`
**Testing**: Docusaurus build validation (`npm run build`), link checker, citation format validator
**Target Platform**: GitHub Pages (static hosting), accessible via modern web browsers
**Project Type**: Documentation/Book (static site generation)
**Performance Goals**: Build time <60 seconds, page load <2 seconds, lighthouse score >90
**Constraints**:
- Chapters must be 800-1,500 words each (per constitution)
- Total book ~20,000 words (revised from 3,000-5,000)
- All code examples must be tested and executable
- APA 7th edition citations required
- Build must pass `npm run build` without errors
**Scale/Scope**:
- 8-18 chapters total
- 4 core module chapters + capstone + infrastructure + appendices
- ~50-100 peer-reviewed references (2015-2025)
- 10-15 code examples across modules
- 3 lab tier specifications with detailed hardware/software tables

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

### I. Spec-First Writing Workflow ✅

**Status**: COMPLIANT

- Specification exists: `specs/001-physical-ai-course/spec.md`
- All chapters will originate from this spec
- User stories define educational stakeholder needs (P1: Course Structure, Lab Planning; P2: Exercise Design, Capstone; P3: ROI)
- Success criteria mapped to measurable outcomes (SC-001 through SC-010)

### II. Clarity and Accessibility ✅

**Status**: COMPLIANT

- Target audience explicitly defined (educators, coordinators, students)
- Prerequisites documented (programming, robotics basics, ML fundamentals)
- Technical terms will be introduced with plain-language definitions
- Progressive difficulty through module sequence (ROS 2 → Simulation → Isaac → VLA)
- Glossary planned for specialized terms (ROS 2, Isaac Sim, VLA, sim-to-real transfer)

### III. Technical Accuracy (NON-NEGOTIABLE) ✅

**Status**: COMPLIANT with VERIFICATION REQUIRED

- FR-011: All claims must cite peer-reviewed sources (2015-2025)
- FR-012: APA format citations required
- Code examples must be tested before inclusion (per constitution)
- Research phase will gather authoritative sources
- **Action Required**: Implement citation verification in build process

### IV. Consistent Tone and Structure ✅

**Status**: COMPLIANT

- Unified chapter structure planned: introduction → concepts → examples → practice → summary
- Docusaurus frontmatter standardized (id, title, sidebar_position)
- Code formatting conventions will be enforced (language identifiers, comments)
- Terminology consistency tracked via glossary
- Voice: instructional, friendly, professional (per constitution)

### V. Iterative Improvement Through Claude Code ✅

**Status**: COMPLIANT

- This plan created via `/sp.plan` (Spec-Kit Plus workflow)
- Content drafting will use Claude Code
- Refinement loops planned for review feedback
- Build compliance checks automated
- Agent context updates integrated (Phase 1)

### VI. Version Control and Traceability ✅

**Status**: COMPLIANT

- Branch: `001-physical-ai-course`
- Commit message convention documented
- Atomic commits planned (one chapter/logical change per commit)
- Spec references in commit messages
- Git hooks considered for pre-commit checks

### VII. Build Validation and Deployment ✅

**Status**: COMPLIANT

- `npm run build` required before merge (quality gate)
- `npm start` for local preview during development
- Docusaurus frontmatter validation planned
- Link checker integration planned
- GitHub Actions CI/CD for deployment to GitHub Pages

### Content Standards - Chapter Requirements ✅

**Status**: COMPLIANT with EXPANSION

- Word count: 800-1,500 per chapter (constitution) → ~20,000 total (revised spec)
- Runnable code examples required (minimum 1 per chapter)
- Learning objectives stated in introduction
- Summary of key takeaways
- Self-contained chapters building on previous content

### Content Standards - Markdown/MDX Format ✅

**Status**: COMPLIANT

- GitHub-flavored Markdown/MDX compatible with Docusaurus
- Frontmatter structure defined
- Code fences with language identifiers
- Alt text for images
- Relative links for internal navigation

### Content Standards - Code Examples ✅

**Status**: COMPLIANT with TESTING GATE

- Complete, executable examples (not fragments)
- Context provided (imports, setup, teardown)
- Testing required before inclusion
- Language style conventions (Python PEP 8, C++ Google Style)
- Comments for non-obvious logic

### Development Workflow - Quality Gates ✅

**Status**: GATES DEFINED

Before merging any chapter:
- [ ] Spec acceptance criteria met
- [ ] Word count 800-1,500 range
- [ ] All code examples tested and working
- [ ] `npm run build` passes
- [ ] Docusaurus preview renders correctly
- [ ] Internal links validated
- [ ] No technical inaccuracies (peer review or self-review)
- [ ] Consistent with book tone and terminology

**Gate Evaluation**: All constitutional requirements align with feature specification. No violations identified. Proceed to Phase 0.

## Project Structure

### Documentation (this feature)

```text
specs/001-physical-ai-course/
├── plan.md              # This file (/sp.plan command output)
├── spec.md              # Feature specification
├── research.md          # Phase 0 output: technical decisions, references
├── data-model.md        # Phase 1 output: content structure entities
├── quickstart.md        # Phase 1 output: getting started guide for contributors
├── contracts/           # Phase 1 output: chapter schemas, APIs (if applicable)
├── checklists/          # Validation checklists
│   └── requirements.md  # Spec quality checklist (already created)
└── tasks.md             # Phase 2 output (/sp.tasks command - NOT created by /sp.plan)
```

### Source Code (repository root) - Documentation Project

```text
docs/                    # Docusaurus content directory
├── intro.md             # Book introduction/landing page
├── modules/             # Core module chapters
│   ├── module-1-ros2.md
│   ├── module-2-gazebo-unity.md
│   ├── module-3-nvidia-isaac.md
│   └── module-4-vla.md
├── exercises/           # Detailed exercise specifications
│   ├── ros2-exercises.md
│   ├── simulation-exercises.md
│   ├── isaac-exercises.md
│   └── vla-exercises.md
├── capstone/            # Capstone project chapter
│   └── capstone-project.md
├── infrastructure/      # Lab setup and hardware
│   ├── lab-tiers-overview.md
│   ├── proxy-tier.md
│   ├── miniature-tier.md
│   ├── premium-tier.md
│   └── deployment-options.md
├── appendices/          # Supporting materials
│   ├── glossary.md
│   ├── references.md    # APA citations
│   ├── week-by-week.md  # Semester schedule
│   └── roi-analysis.md
└── _category_.json      # Docusaurus category metadata

static/                  # Static assets
├── img/                 # Images, diagrams
│   ├── architecture/    # System architecture diagrams
│   ├── lab-setups/      # Lab tier photos/diagrams
│   └── robots/          # Humanoid robot images
└── downloads/           # Downloadable resources (optional)

src/                     # Docusaurus React components (if needed)
├── components/          # Custom MDX components
│   ├── LabTierTable.js  # Comparative lab tier table
│   └── CodeSandbox.js   # Embedded code examples (if applicable)
├── css/                 # Custom styling
│   └── custom.css       # Docusaurus theme overrides
└── pages/               # Custom pages (landing, about)

docusaurus.config.js     # Docusaurus configuration
sidebars.js              # Navigation sidebar structure
package.json             # Node.js dependencies
.github/
└── workflows/
    └── deploy.yml       # GitHub Actions CI/CD

tests/                   # Build and content validation
├── link-checker.js      # Internal link validation
├── citation-validator.js # APA format checker
└── code-examples/       # Test harness for code examples
    ├── test-ros2.py
    ├── test-gazebo.py
    └── test-vla.py
```

**Structure Decision**:

This is a **documentation project** using Docusaurus static site generator. The structure follows Docusaurus conventions:

- **`/docs/`**: Primary content directory containing all Markdown/MDX chapters
- **`/static/`**: Images, assets, downloadable resources
- **`/src/`**: Custom React components for enhanced MDX functionality
- **`/.github/workflows/`**: CI/CD automation for GitHub Pages deployment
- **`/tests/`**: Validation scripts for build quality (links, citations, code examples)

The directory organization mirrors the book's logical structure:
1. **Modules** (core educational content)
2. **Exercises** (hands-on practice detailed specifications)
3. **Capstone** (integrative final project)
4. **Infrastructure** (lab setup guidance for institutions)
5. **Appendices** (references, glossary, schedule, ROI analysis)

This structure supports:
- Clear navigation via Docusaurus sidebar
- Modular content updates (chapters can be edited independently)
- Scalability (8-18 chapters within consistent organization)
- Automated deployment (GitHub Actions builds and publishes to `gh-pages`)

## Complexity Tracking

> **No constitutional violations identified. This section remains empty.**

## Phase 0: Research & Architecture

**Objective**: Resolve all technical decisions, gather peer-reviewed references, and establish architectural patterns for book generation and deployment.

### Research Tasks

1. **Docusaurus Framework Decisions**
   - **Decision**: Docusaurus version, theming, essential plugins
   - **Rationale**: Must support Markdown/MDX, APA citations, code syntax highlighting, GitHub Pages deployment
   - **Research Required**:
     - Docusaurus 3.x vs 2.x (latest stable features, migration path)
     - Plugin ecosystem: remark-citation, rehype-citation-plugin, or custom solution
     - Theme selection: classic (default) vs custom for academic/educational content
     - Math equation support (if needed for robotics formulas)

2. **GitHub Pages Deployment Strategy**
   - **Decision**: Branch structure, CI/CD workflow, custom domain (if applicable)
   - **Rationale**: Automated deployment on every merge to main, preview builds for PRs
   - **Research Required**:
     - GitHub Actions workflow for Docusaurus build and deploy
     - `gh-pages` branch management vs `docs/` folder approach
     - Build caching strategies for faster CI/CD
     - Environment secrets for deployment tokens

3. **Content Generation Pipeline**
   - **Decision**: Division of labor between Spec-Kit Plus and Claude Code
   - **Rationale**: Spec-Kit provides structure; Claude Code drafts content; human review refines
   - **Research Required**:
     - Spec-Kit Plus integration points (specs → chapter outlines → task breakdowns)
     - Claude Code prompts for consistent chapter drafting
     - Iteration loops: draft → review → refine → validate
     - Version control for multi-iteration chapters

4. **APA Citation Management**
   - **Decision**: Citation storage format, inline citation syntax, bibliography generation
   - **Rationale**: FR-011 and FR-012 require peer-reviewed sources with APA formatting
   - **Research Required**:
     - Markdown citation syntax compatible with Docusaurus (e.g., `[@AuthorYear]`)
     - BibTeX/CSL JSON bibliography files
     - Remark/Rehype plugins for citation rendering
     - Manual vs automated citation validation

5. **Peer-Reviewed Source Gathering**
   - **Decision**: Search strategy for ROS 2, NVIDIA Isaac, VLA, humanoid robotics education literature (2015-2025)
   - **Rationale**: SC-004 requires all technical claims supported by peer-reviewed or industry-standard references
   - **Research Required**:
     - Databases: IEEE Xplore, ACM Digital Library, arXiv (robotics section), Google Scholar
     - Keywords: "ROS 2 education", "Isaac Sim robotics", "vision-language-action", "humanoid robot curriculum", "Physical AI pedagogy"
     - Minimum 50-100 references needed for ~20,000 words
     - Case studies: universities with Physical AI programs (for SC-007)

6. **Code Example Testing Infrastructure**
   - **Decision**: Test harness for ROS 2, Gazebo, Isaac Sim, VLA code snippets
   - **Rationale**: Constitution III (technical accuracy) and quality gate require tested code
   - **Research Required**:
     - Docker-based test environments for ROS 2, Gazebo, Unity, Isaac Sim
     - CI/CD integration for code example validation
     - Test frameworks: pytest for Python, gtest for C++
     - Mocking strategies for hardware-dependent code (e.g., humanoid robot APIs)

7. **Chapter/Module Structure Granularity**
   - **Decision**: Number of chapters, mapping to 4 modules, depth per topic
   - **Rationale**: Spec defines 8-18 chapters total, ~20,000 words, 800-1,500 per chapter
   - **Research Required**:
     - Module 1 (ROS 2): 2-3 chapters? (intro, navigation, advanced topics)
     - Module 2 (Gazebo & Unity): 2 chapters? (Gazebo, Unity separately or combined)
     - Module 3 (NVIDIA Isaac): 1-2 chapters? (Isaac Sim intro, sim-to-real transfer)
     - Module 4 (VLA): 2-3 chapters? (VLA concepts, integration, manipulation)
     - Capstone: 1 chapter
     - Infrastructure: 2 chapters? (overview, detailed tier specs)
     - Appendices: 2-3 chapters (glossary, references, week-by-week, ROI)
     - **Preliminary Breakdown**: 12-16 chapters (fits 8-18 range, ~1,250-1,667 words avg)

8. **Lab and Hardware Representation**
   - **Decision**: Depth of hardware specs, imagery, vendor examples
   - **Rationale**: FR-006 to FR-010 require detailed lab tier specifications
   - **Research Required**:
     - Table formats for hardware comparisons (CPU, GPU, RAM, cost)
     - Diagrams: lab layout, network topology, robot platforms
     - Image sourcing: royalty-free or vendor permissions for robot photos
     - FR-014 constraint: high-level recommendations, NOT full vendor comparisons

### Research Deliverables (research.md)

The `research.md` file will document:

1. **Docusaurus Configuration**
   - Decision: Docusaurus 3.x (latest stable)
   - Rationale: Better MDX support, modern React components, active maintenance
   - Plugins: `@docusaurus/plugin-content-docs`, `remark-math`, `rehype-katex` (for equations), custom citation plugin
   - Theme: Classic with custom CSS for academic styling

2. **Deployment Workflow**
   - Decision: GitHub Actions → `gh-pages` branch
   - Rationale: Standard Docusaurus deployment, free hosting, automated on push to main
   - Workflow file: `.github/workflows/deploy.yml`
   - Branch protection: main branch requires passing build

3. **Content Pipeline**
   - Decision: Spec-Kit Plus (planning) + Claude Code (drafting) + Human (review)
   - Rationale: Combines structured planning with AI efficiency and human quality control
   - Iteration: 2-3 draft cycles per chapter expected
   - Version control: One branch per chapter, PR for merge to main

4. **Citation System**
   - Decision: BibTeX file (`references.bib`) + remark-bibtex plugin (or manual Markdown rendering)
   - Rationale: Industry standard for academic citations, compatible with Markdown
   - Inline syntax: `(Author, Year)` or `[AuthorYear]` depending on plugin
   - Bibliography: Auto-generated from BibTeX, rendered in `docs/appendices/references.md`

5. **Reference Library (50-100 sources)**
   - ROS 2 Education: 10-15 papers (e.g., Macenski et al. 2020 on Nav2)
   - Gazebo/Unity Simulation: 8-10 papers (robotics pedagogy, sim-to-real)
   - NVIDIA Isaac: 5-8 sources (Isaac Sim whitepapers, research applications)
   - VLA Frameworks: 10-15 papers (RT-2, OpenVLA, vision-language-action architectures)
   - Humanoid Robotics: 10-15 papers (platforms, education, deployment)
   - Curriculum Design: 5-10 papers (ABET standards, robotics education outcomes)
   - Lab Infrastructure: 5-10 sources (cost-benefit analyses, case studies)

6. **Code Testing Strategy**
   - Decision: Docker containers for each module's environment
   - Rationale: Reproducible, isolated testing without requiring full hardware
   - Containers: `ros2-test` (Humble/Jazzy), `gazebo-test`, `isaac-sim-test` (via Omniverse), `vla-test` (Python VLA libs)
   - CI Integration: GitHub Actions runs Docker tests on code example changes
   - Mocking: Hardware-specific APIs mocked with reasonable defaults

7. **Chapter Structure (Final)**
   - **Total: 14 chapters** (~1,428 words avg, range 800-1,500 compliant)
   - **Module 1 (ROS 2)**: 3 chapters (Intro & Basics, Navigation Stack, Advanced Multi-Robot)
   - **Module 2 (Simulation)**: 2 chapters (Gazebo for Robotics, Unity Robotics Integration)
   - **Module 3 (Isaac Sim)**: 2 chapters (Isaac Sim Intro & Synthetic Data, Sim-to-Real Transfer)
   - **Module 4 (VLA)**: 3 chapters (VLA Concepts, Integration with Robots, Manipulation Tasks)
   - **Capstone**: 1 chapter (Integrated VLA-Driven Humanoid Task)
   - **Infrastructure**: 2 chapters (Lab Tiers Overview, Detailed Tier Specifications)
   - **Appendices**: 1 combined chapter (Glossary, Week-by-Week Schedule, ROI Analysis, References as subsections)
   - **Total Word Count**: 14 × ~1,400 = ~19,600 words (meets ~20,000 target)

8. **Lab Hardware Imagery**
   - Decision: Combination of diagrams (created in Lucidchart/draw.io) and vendor photos (with attribution)
   - Rationale: Diagrams for abstract concepts (network topology), photos for tangible hardware
   - Sourcing: Vendor press kits (NVIDIA, Unitree, Figure), Creative Commons robotics images
   - Alt text: Descriptive for accessibility (per constitution)

## Phase 1: Data Model & Contracts

**Prerequisites**: `research.md` complete with all decisions documented

### Data Model (data-model.md)

**Purpose**: Define the logical entities and relationships that structure the book's content. This is NOT a software data model, but a **content structure model** for educational material.

#### Entities

1. **Module**
   - **Attributes**:
     - `module_id` (integer): 1-4
     - `title` (string): e.g., "ROS 2 Fundamentals"
     - `learning_objectives` (list of strings): What students will be able to do
     - `topics` (list of Topic entities): Detailed topic breakdowns
     - `exercises` (list of Exercise entities): Hands-on practice activities
     - `estimated_weeks` (integer): Time allocation in semester
     - `prerequisite_knowledge` (list of strings): Required background
   - **Relationships**:
     - One Module has many Topics
     - One Module has many Exercises
     - Modules have sequential dependencies (Module 1 → 2 → 3 → 4)
   - **Validation Rules**:
     - Each module must have ≥5 learning objectives (per FR-001)
     - Topics must sum to 2-3 pages of content per module (per clarification #1)
     - Exercises must have 2+ per module (per SC-006)

2. **Topic**
   - **Attributes**:
     - `topic_id` (string): Unique identifier (e.g., "ros2-pub-sub")
     - `module_id` (integer): Parent module
     - `title` (string): e.g., "Publisher/Subscriber Pattern"
     - `learning_outcome` (string): Specific measurable outcome for this topic
     - `content_outline` (list of strings): Bullet points of subtopics
     - `estimated_pages` (float): 0.25-0.75 pages typically
   - **Relationships**:
     - Many Topics belong to one Module
   - **Validation Rules**:
     - Learning outcome must be measurable/testable
     - Content outline must have ≥3 subtopics for clarity

3. **Exercise**
   - **Attributes**:
     - `exercise_id` (string): Unique identifier
     - `module_id` (integer): Parent module
     - `title` (string): e.g., "Autonomous Navigation Challenge"
     - `learning_objective` (string): What skill this exercise builds
     - `prerequisites` (list of strings): Topics/knowledge required
     - `setup_requirements` (object): Hardware, software, environment
     - `procedure_outline` (list of strings): Step-by-step guidance (NOT full solution)
     - `assessment_criteria` (list of strings): How to evaluate success
     - `estimated_time_hours` (float): 2-4 hours typical
     - `deliverables` (list of strings): Code repo, simulation video, report, etc.
     - `difficulty_level` (enum): "introductory", "intermediate", "advanced"
   - **Relationships**:
     - Many Exercises belong to one Module
   - **Validation Rules**:
     - Per clarification #2: must include setup, procedure, assessment (~1 page each)
     - Estimated time must be 2-4 hours per FR-003
     - Deliverables must be specific and measurable

4. **Chapter**
   - **Attributes**:
     - `chapter_id` (string): Filename slug (e.g., "module-1-ros2-intro")
     - `title` (string): Full chapter title
     - `sidebar_position` (integer): Navigation order
     - `word_count` (integer): Must be 800-1,500
     - `learning_objectives` (list of strings): Introduced at chapter start
     - `summary` (string): Key takeaways at chapter end
     - `code_examples` (list of CodeExample entities): Minimum 1 per chapter
     - `citations` (list of Citation entities): APA references used
     - `related_modules` (list of integers): Which modules this chapter covers
   - **Relationships**:
     - One Chapter may cover one or more Modules (for module chapters)
     - One Chapter may reference multiple Exercises
     - One Chapter has many CodeExamples
     - One Chapter cites many Citations
   - **Validation Rules**:
     - Word count 800-1,500 (per constitution)
     - Must have ≥1 runnable code example (per constitution)
     - Learning objectives stated in introduction (per quality gate)
     - Summary at end (per quality gate)

5. **CodeExample**
   - **Attributes**:
     - `example_id` (string): Unique identifier
     - `chapter_id` (string): Parent chapter
     - `title` (string): Description of what the code does
     - `language` (string): Python, C++, Bash, etc.
     - `code_content` (string): Full executable code
     - `context` (object): Imports, setup, teardown needed
     - `explanation` (string): Comments/narrative explaining non-obvious logic
     - `test_status` (enum): "untested", "passing", "failing"
     - `test_command` (string): How to run the test (e.g., "pytest test_example.py")
   - **Relationships**:
     - Many CodeExamples belong to one Chapter
   - **Validation Rules**:
     - Must be complete and executable (per constitution)
     - `test_status` must be "passing" before chapter merge (per quality gate)
     - Comments required for non-obvious logic (per constitution)

6. **LabTier**
   - **Attributes**:
     - `tier_name` (enum): "Proxy", "Miniature", "Premium"
     - `cost_range_usd` (object): `{min: 10000, max: 20000}` example
     - `hardware_components` (list of HardwareComponent entities)
     - `software_requirements` (list of SoftwareRequirement entities)
     - `student_capacity` (integer): Number of students supported
     - `use_cases` (list of strings): Teaching-only, teaching+research, flagship
     - `space_requirements_sqft` (integer): Lab footprint
   - **Relationships**:
     - One LabTier has many HardwareComponents
     - One LabTier has many SoftwareRequirements
   - **Validation Rules**:
     - Cost range must align with FR-009 estimates
     - Hardware/software lists must be itemized per FR-007 and FR-008

7. **HardwareComponent**
   - **Attributes**:
     - `component_id` (string): Unique identifier
     - `tier_name` (enum): Which tier(s) include this component
     - `component_type` (enum): "workstation", "robot", "edge_ai_kit", "network_gear"
     - `specifications` (object): CPU, GPU, RAM, storage (for workstations); model, DOF, payload (for robots)
     - `cost_estimate_usd` (integer): Per-unit cost
     - `quantity` (integer): Number needed for the tier
     - `vendor_examples` (list of strings): Non-exhaustive suggestions (per FR-014)
   - **Relationships**:
     - Many HardwareComponents belong to one or more LabTiers
   - **Validation Rules**:
     - Specifications must be detailed enough for procurement (per FR-007)
     - Vendor examples are suggestions, not comparisons (per FR-014)

8. **SoftwareRequirement**
   - **Attributes**:
     - `software_id` (string): Unique identifier
     - `tool_name` (string): e.g., "ROS 2 Humble"
     - `version` (string): e.g., "Humble Hawksbill"
     - `purpose` (string): Simulation, ROS middleware, VLA framework
     - `deployment_method` (enum): "local_install", "docker", "cloud"
     - `licensing` (enum): "open_source", "academic", "commercial"
     - `compatible_tiers` (list of enums): ["Proxy", "Miniature", "Premium"]
   - **Relationships**:
     - Many SoftwareRequirements apply to one or more LabTiers
   - **Validation Rules**:
     - Must list version/distribution per FR-008
     - Deployment method specified per FR-008

9. **Citation**
   - **Attributes**:
     - `citation_id` (string): BibTeX key (e.g., "Macenski2020")
     - `authors` (list of strings): Author names
     - `year` (integer): Publication year (2015-2025 per FR-011)
     - `title` (string): Publication title
     - `venue` (string): Journal, conference, or source
     - `doi` (string): Digital Object Identifier
     - `apa_formatted` (string): Full APA 7th edition citation
     - `cited_in_chapters` (list of strings): Chapter IDs that reference this
   - **Relationships**:
     - Many Citations are referenced by many Chapters (many-to-many)
   - **Validation Rules**:
     - Year must be 2015-2025 (per FR-011)
     - APA format must validate against APA 7th edition (per FR-012)

10. **CapstoneMilestone**
    - **Attributes**:
      - `milestone_id` (string): e.g., "capstone-ros2-architecture"
      - `title` (string): e.g., "ROS 2 System Architecture Design"
      - `module_integration` (list of integers): Which modules this milestone integrates (1-4)
      - `deliverable` (string): What students submit
      - `evaluation_weight_percent` (integer): Portion of capstone grade (sum to 100%)
      - `rubric_criteria` (list of strings): How this milestone is graded
    - **Relationships**:
      - Many CapstoneMilestones collectively define the Capstone project
    - **Validation Rules**:
      - Sum of `evaluation_weight_percent` across all milestones must equal 100
      - Must integrate all 4 modules (per FR-004)

#### State Transitions

- **Chapter Lifecycle**: Draft → In Review → Revision → Approved → Published
- **CodeExample Lifecycle**: Untested → Testing → Passing/Failing → (if passing) Included
- **Citation Lifecycle**: Candidate → Verified → Cited → (if unused) Archived

### Contracts (contracts/)

**Purpose**: Define the "API" for content generation—standardized schemas for how chapters, exercises, and other entities are structured in Markdown/YAML.

#### Chapter Schema (`chapter-schema.yaml`)

```yaml
# Docusaurus frontmatter + content structure
---
id: string                  # Unique chapter ID (kebab-case)
title: string               # Full chapter title
sidebar_position: integer   # Navigation order (1, 2, 3, ...)
description: string         # Brief chapter summary for SEO
tags: [string]              # Categorization tags (e.g., ["ROS 2", "Module 1"])
---

# {title}

## Learning Objectives

- LO1: Students will be able to...
- LO2: Students will be able to...
- [minimum 3 objectives]

## Introduction

[Motivate the topic, provide context, preview what will be covered]

## {Section 1 Title}

[Content with subsections as needed]

### {Subsection if needed}

[Content]

## {Section 2 Title}

[Content]

## Code Example: {Example Title}

```{language}
# Full executable code with comments
```

**Explanation**: [What the code does, why it's structured this way]

**Testing**: Run with `{test command}`

## Summary

- Key Takeaway 1
- Key Takeaway 2
- [3-5 takeaways]

## References

- (Author, Year) inline citations throughout
- Full bibliography in appendices/references.md
```

#### Exercise Schema (`exercise-schema.yaml`)

```yaml
# Exercise specification structure (per clarification #2)

## Exercise: {Title}

**Module**: {Module Number and Name}
**Learning Objective**: {Specific skill built by this exercise}
**Difficulty**: {introductory | intermediate | advanced}
**Estimated Time**: {X hours}

### Prerequisites

- Topic/knowledge required 1
- Topic/knowledge required 2
- [list all prerequisites]

### Setup Requirements

**Hardware**:
- Component 1 (or simulation equivalent)
- Component 2

**Software**:
- Tool 1 (version)
- Tool 2 (version)
- [Docker image if applicable]

**Environment**:
- Operating system requirements
- Network configuration (if applicable)

### Procedure Outline

1. **Step 1**: {High-level action}
   - Substep guidance (not full solution code)
2. **Step 2**: {Next action}
   - Substep guidance
3. [Continue for all major steps]

### Assessment Criteria

- [ ] Criterion 1 (e.g., "Robot navigates to goal without collisions")
- [ ] Criterion 2 (e.g., "Code follows ROS 2 best practices")
- [ ] [3-5 measurable criteria]

### Deliverables

- Deliverable 1 (e.g., "GitHub repository with ROS 2 package")
- Deliverable 2 (e.g., "Screen recording of simulation run")
- [List all expected submissions]
```

#### Lab Tier Table Schema (`lab-tier-table-schema.md`)

```markdown
# Lab Tier Comparison

| Aspect | Proxy Tier | Miniature Tier | Premium Tier |
|--------|------------|----------------|--------------|
| **Cost Range** | $10-20K | $50-70K | $120-180K |
| **Student Capacity** | 20-30 (simulation only) | 20-30 (limited physical) | 20-30 (full physical) |
| **Robot Platforms** | None (simulation) | 1-2 compact humanoids | 3-5 full-scale humanoids |
| **Workstations** | 10-15 GPU workstations | 10-15 GPU + 2-3 edge AI | 15-20 GPU + 5-8 edge AI |
| **Use Case** | Teaching-only, budget-constrained | Teaching + limited research | Teaching + research + showcase |
| **Space Requirements** | 500-800 sqft | 800-1200 sqft | 1500-2500 sqft |

[Detailed specifications follow in dedicated tier chapters]
```

### Quickstart Guide (quickstart.md)

**Purpose**: Provide contributors (educators adapting the book, or future content updaters) with a rapid onboarding guide to the project structure and workflow.

```markdown
# Quickstart: Physical AI Book Contribution Guide

## Prerequisites

- Node.js 18+ installed
- Git configured
- Familiarity with Markdown and Docusaurus (optional but helpful)

## Local Development Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/{org}/physical-ai-book.git
   cd physical-ai-book
   ```

2. **Install dependencies**:
   ```bash
   npm install
   ```

3. **Start local development server**:
   ```bash
   npm start
   ```
   Opens browser to `http://localhost:3000` with live reload.

4. **Build for production** (to test deployment):
   ```bash
   npm run build
   npm run serve
   ```

## Project Structure Overview

- **`/docs/`**: All book content (Markdown/MDX chapters)
- **`/static/`**: Images, assets, downloadable resources
- **`/src/`**: Custom React components (if needed for MDX)
- **`docusaurus.config.js`**: Site configuration (title, URL, navbar, footer)
- **`sidebars.js`**: Navigation structure

## Adding a New Chapter

1. **Create Markdown file** in `/docs/{category}/` (e.g., `/docs/modules/new-chapter.md`)
2. **Add frontmatter**:
   ```yaml
   ---
   id: new-chapter
   title: New Chapter Title
   sidebar_position: 10
   ---
   ```
3. **Write content** following `chapter-schema.yaml` (see `specs/001-physical-ai-course/contracts/`)
4. **Update `/sidebars.js`** if creating a new category
5. **Test locally** with `npm start`
6. **Commit and push** to feature branch
7. **Create PR** for review

## Code Example Testing

Before merging a chapter with code examples:

1. **Navigate to `/tests/code-examples/`**
2. **Run the relevant test**:
   ```bash
   docker-compose up ros2-test  # For ROS 2 examples
   pytest tests/code-examples/test_ros2.py
   ```
3. **Ensure all tests pass** (green checkmarks in CI)

## Citation Management

- **Add new source** to `/references.bib` (BibTeX format)
- **Cite in chapter** with inline format: `(Author, Year)`
- **Verify APA format** with `npm run validate:citations`

## Deployment

- **Automatic**: Merging to `main` triggers GitHub Actions → builds → deploys to `gh-pages`
- **Manual**: Run `npm run deploy` (requires write access to `gh-pages` branch)

## Troubleshooting

- **Build fails**: Check `npm run build` output for Markdown syntax errors or broken links
- **Citation not rendering**: Verify BibTeX entry in `references.bib` and inline citation format
- **Code example failing**: Run Docker test locally to debug

## Constitution Compliance

All contributions must adhere to `.specify/memory/constitution.md`:
- Spec-first workflow (no content without a spec)
- Technical accuracy (all code tested, all claims cited)
- Word count per chapter: 800-1,500 words
- APA citations for all sources (2015-2025)

## Contact

For questions, open an issue or contact the maintainers.
```

### Agent Context Update

**Action**: Run `.specify/scripts/powershell/update-agent-context.ps1 -AgentType claude`

**Purpose**: Update the `CLAUDE.md` agent-specific file with technology decisions from this plan, enabling Claude Code to maintain context for future content generation and iteration.

**Expected Updates to `CLAUDE.md`**:

```markdown
## Project-Specific Context

**Project Type**: Educational Book (Docusaurus static site)

**Technology Stack**:
- **Framework**: Docusaurus 3.x
- **Language**: Markdown/MDX, Node.js 18+
- **Build**: npm scripts, GitHub Actions CI/CD
- **Deployment**: GitHub Pages (gh-pages branch)
- **Testing**: Jest (link validation), pytest (code examples in Docker)
- **Citations**: BibTeX + APA 7th edition formatting

**Content Structure**:
- 14 chapters total (~1,400 words avg, 800-1,500 range)
- 4 module groups: ROS 2 (3 ch), Simulation (2 ch), Isaac (2 ch), VLA (3 ch)
- Additional: Capstone (1 ch), Infrastructure (2 ch), Appendices (1 ch)

**Quality Gates** (per constitution):
- Spec acceptance criteria met
- Word count 800-1,500 per chapter
- All code examples tested (Docker environments)
- `npm run build` passes without errors
- APA citations verified (sources 2015-2025)

**Content Generation Workflow**:
1. Spec-Kit Plus: Structure planning (this plan)
2. Claude Code: Draft chapter content from spec
3. Human Review: Technical accuracy, citation verification
4. Iteration: 2-3 cycles typical
5. Merge: After quality gates pass
```

## Phase 0 & Phase 1 Outputs Summary

**Phase 0 Output** (`research.md`):
- Docusaurus 3.x configuration decisions
- GitHub Actions deployment workflow design
- Content generation pipeline (Spec-Kit + Claude Code division of labor)
- APA citation system (BibTeX + remark plugin or manual)
- Peer-reviewed reference library (50-100 sources, 2015-2025)
- Code testing infrastructure (Docker containers per module)
- Final chapter structure (14 chapters, mapping to modules)
- Lab hardware imagery strategy (diagrams + vendor photos)

**Phase 1 Outputs**:
- `data-model.md`: 10 entities (Module, Topic, Exercise, Chapter, CodeExample, LabTier, HardwareComponent, SoftwareRequirement, Citation, CapstoneMilestone) with attributes, relationships, validation rules
- `contracts/chapter-schema.yaml`: Markdown/YAML template for chapters
- `contracts/exercise-schema.yaml`: Markdown template for exercises
- `contracts/lab-tier-table-schema.md`: Table format for lab tier comparisons
- `quickstart.md`: Contributor onboarding guide
- **Agent context updated**: `CLAUDE.md` modified with Docusaurus stack, quality gates, workflow

## Re-Evaluation of Constitution Check

After Phase 1 design, all constitutional requirements remain compliant:

- **Spec-First Workflow**: Maintained (this plan derived from spec)
- **Clarity**: Chapter schemas ensure consistent structure
- **Technical Accuracy**: Code testing infrastructure enforces this
- **Consistent Tone**: Templates and quality gates ensure uniformity
- **Claude Code Integration**: Agent context updated for iterative drafting
- **Version Control**: Quickstart documents Git workflow
- **Build Validation**: CI/CD enforces `npm run build` success

**No new violations introduced. Proceed to Phase 2 (tasks generation) via `/sp.tasks`.**

## Next Steps

1. **Review this plan** (`specs/001-physical-ai-course/plan.md`) for completeness
2. **Generate `research.md`** by executing Phase 0 research tasks (agent-assisted or manual)
3. **Generate `data-model.md`** and `contracts/` per Phase 1 specifications
4. **Update agent context** with `update-agent-context.ps1` script
5. **Run `/sp.tasks`** to break this plan into actionable implementation tasks
6. **Begin content generation** following Spec-Kit Plus → Claude Code → Review workflow

**Branch**: `001-physical-ai-course`
**Plan Path**: `D:\TypeScript\claude\Project1\Project-Book\specs\001-physical-ai-course\plan.md`
**Status**: Phase 1 design complete, ready for task generation
