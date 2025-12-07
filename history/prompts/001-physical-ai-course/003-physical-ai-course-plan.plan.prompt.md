---
id: 003
title: Physical AI Course Implementation Plan
stage: plan
date: 2025-12-06
surface: agent
model: claude-sonnet-4-5
feature: 001-physical-ai-course
branch: 001-physical-ai-course
user: unknown
command: /sp.plan
labels: ["planning", "architecture", "docusaurus", "book-creation", "physical-ai"]
links:
  spec: specs/001-physical-ai-course/spec.md
  ticket: null
  adr: null
  pr: null
files:
  - specs/001-physical-ai-course/plan.md
tests:
  - Constitution check PASSED (all 7 principles compliant)
  - Technical context defined (Docusaurus 3.x, GitHub Pages, Node.js 18+)
  - Project structure documented (14 chapters, 4 module groups)
  - Phase 0 research tasks defined (8 research areas)
  - Phase 1 data model designed (10 entities with relationships)
---

## Prompt

```text
Create:
- Architecture sketch: Define the technical architecture for the Spec-Driven Book project, including:
    - Docusaurus project structure (chapters, navigation, assets)
    - Integration of Spec-Kit Plus for generating structured content
    - Integration of Claude Code for automated content drafting and iteration
    - GitHub Pages deployment workflow and CI/CD automation
    - Module-to-chapter mapping (Modules 1–4, Capstone, hardware/lab appendices)
- Section structure: Organize the book into chapters and sub-sections aligned with course modules, lab setups, capstone, and appendices.
- Research approach: Use a research-concurrent approach to gather references, academic sources, and technical guides while drafting content.
- Quality validation: Define validation checks for module completeness, content alignment with specs, APA citations, Docusaurus rendering, and deployment correctness.

Decisions needing documentation:
- Book framework choices: Docusaurus version, theming, plugins
- Deployment strategy: GitHub Pages branch and CI/CD workflow
- Content generation pipeline: Spec-Kit Plus vs Claude Code usage, iterative content updates
- Chapter/module structure: granularity, sequence, and mapping to learning outcomes
- Lab and hardware representation: depth of detail and imagery

Testing strategy:
- Validate Spec-Kit Plus outputs against module objectives and expected learning outcomes
- Verify Claude Code generates coherent, spec-aligned content
- Check Docusaurus build locally and deployed on GitHub Pages
- Test all navigation links, chapter rendering, and formatting consistency
- Confirm APA citations are correct and sources properly referenced

Technical details:
- Research-concurrent approach: iterate research, content generation, and validation simultaneously
- Follow APA citation style consistently across all content
- Organize plan by phases:
    1. Research – collect references, technical guides for Docusaurus, Spec-Kit Plus, and Claude Code
    2. Foundation – setup Docusaurus project, GitHub repo, initial chapter scaffolds, and Spec-Kit Plus structure
    3. Analysis – evaluate content pipelines, module-to-chapter mapping, lab representation, and deployment strategy
    4. Synthesis – generate full book content, integrate modules, validate formatting and APA references, deploy to GitHub Pages
```

## Response snapshot

Created comprehensive implementation plan for Physical AI & Humanoid Robotics Course Book:

**Technical Architecture**:
- **Framework**: Docusaurus 3.x (latest stable) for static site generation
- **Content Pipeline**: Spec-Kit Plus (planning) → Claude Code (drafting) → Human Review (quality)
- **Deployment**: GitHub Actions CI/CD → GitHub Pages (gh-pages branch)
- **Testing**: Docker-based code validation, link checking, APA citation verification
- **Project Type**: Documentation/Book (Markdown/MDX, Node.js 18+)

**Project Structure**:
- **14 Chapters Total** (~1,400 words avg, 800-1,500 range):
  - Module 1 (ROS 2): 3 chapters
  - Module 2 (Simulation): 2 chapters
  - Module 3 (Isaac Sim): 2 chapters
  - Module 4 (VLA): 3 chapters
  - Capstone: 1 chapter
  - Infrastructure: 2 chapters
  - Appendices: 1 chapter
- **Directory Structure**: `/docs/` (chapters), `/static/` (assets), `/src/` (React components), `.github/workflows/` (CI/CD)
- **Total Word Count**: 14 × ~1,400 = ~19,600 words (meets ~20,000 target)

**Phase 0: Research & Architecture** (8 research areas):
1. Docusaurus Framework Decisions (v3.x, plugins, theming)
2. GitHub Pages Deployment Strategy (gh-pages branch, GitHub Actions)
3. Content Generation Pipeline (Spec-Kit Plus + Claude Code workflow)
4. APA Citation Management (BibTeX + remark plugin)
5. Peer-Reviewed Source Gathering (50-100 sources, 2015-2025)
6. Code Example Testing Infrastructure (Docker containers per module)
7. Chapter/Module Structure Granularity (14 chapters mapped to 4 modules)
8. Lab and Hardware Representation (diagrams + vendor photos)

**Phase 1: Data Model & Contracts** (10 entities):
1. **Module**: 4 core instructional units (ROS 2, Simulation, Isaac, VLA)
2. **Topic**: Detailed topic breakdowns with learning outcomes (2-3 pages per module)
3. **Exercise**: Hands-on activities with setup, procedure, assessment (~1 page each)
4. **Chapter**: Markdown/MDX chapters (800-1,500 words, code examples, citations)
5. **CodeExample**: Executable code with testing status and validation
6. **LabTier**: Infrastructure configurations (Proxy, Miniature, Premium)
7. **HardwareComponent**: Workstations, robots, edge AI kits, network gear
8. **SoftwareRequirement**: ROS 2, Gazebo, Unity, Isaac Sim, VLA frameworks
9. **Citation**: BibTeX entries with APA 7th edition formatting
10. **CapstoneMilestone**: Integrative project deliverables (4-module integration)

**Contracts (Content Schemas)**:
- `chapter-schema.yaml`: Docusaurus frontmatter + content structure (learning objectives, introduction, sections, code examples, summary, references)
- `exercise-schema.yaml`: Exercise specifications (prerequisites, setup, procedure, assessment, deliverables)
- `lab-tier-table-schema.md`: Comparative table format for 3 lab tiers
- `quickstart.md`: Contributor onboarding guide (local dev setup, chapter creation, testing, deployment)

**Constitution Check**: All 7 principles COMPLIANT ✅
- I. Spec-First Workflow: Maintained (plan derived from spec)
- II. Clarity: Chapter schemas ensure consistent structure
- III. Technical Accuracy: Code testing infrastructure enforces verification
- IV. Consistent Tone: Templates and quality gates ensure uniformity
- V. Claude Code Integration: Agent context update planned
- VI. Version Control: Quickstart documents Git workflow
- VII. Build Validation: CI/CD enforces `npm run build` success

**Quality Gates** (before merging any chapter):
- [ ] Spec acceptance criteria met
- [ ] Word count 800-1,500 range
- [ ] All code examples tested and working
- [ ] `npm run build` passes
- [ ] Docusaurus preview renders correctly
- [ ] Internal links validated
- [ ] No technical inaccuracies (peer/self-review)
- [ ] Consistent with book tone and terminology

**Content Generation Workflow**:
1. Spec-Kit Plus: Structure planning (this plan)
2. Claude Code: Draft chapter content from spec
3. Human Review: Technical accuracy, citation verification
4. Iteration: 2-3 cycles typical per chapter
5. Merge: After quality gates pass

**Next Steps**:
1. Generate `research.md` (Phase 0 execution)
2. Generate `data-model.md` and `contracts/` (Phase 1 execution)
3. Update agent context (`update-agent-context.ps1`)
4. Run `/sp.tasks` for actionable task breakdown
5. Begin content generation following established workflow

## Outcome

- ✅ Impact: Comprehensive architectural plan for ~20,000-word educational book using Docusaurus, Spec-Kit Plus, and Claude Code
- 🧪 Tests: Constitution check PASSED (all 7 principles compliant), 14-chapter structure validated, quality gates defined
- 📁 Files: Created plan.md (920+ lines, comprehensive architecture and Phase 0/1 specifications)
- 🔁 Next prompts: Generate `research.md` (Phase 0), `data-model.md` and `contracts/` (Phase 1), run `/sp.tasks` for task breakdown
- 🧠 Reflection: Plan successfully adapts software development template to educational book creation, maintaining constitution compliance while addressing unique documentation project needs (Docusaurus, APA citations, pedagogical content structure)

## Evaluation notes (flywheel)

- Failure modes observed: None - plan successfully generated with full Phase 0 and Phase 1 design
- Graders run and results (PASS/FAIL): PASS - Constitution check validates all 7 principles, technical context defined, project structure documented
- Prompt variant (if applicable): Documentation/book project adapted from software development plan template
- Next experiment (smallest change to try): Monitor `/sp.tasks` execution to verify task breakdown aligns with 14-chapter structure and Phase 0/1 specifications; validate research.md and data-model.md generation completeness
