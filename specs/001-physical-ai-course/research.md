# Research: Physical AI & Humanoid Robotics Course Book

**Date**: 2025-12-06
**Purpose**: Document all technical decisions and research findings for the book implementation

## Overview

This document captures research decisions for creating a ~20,000-word educational book on Physical AI and Humanoid Robotics using Docusaurus, deployed to GitHub Pages, with content generated through Spec-Kit Plus and Claude Code workflows.

---

## 1. Docusaurus Framework Configuration

### Decision

**Docusaurus 3.x (3.1.0)** with classic theme and custom CSS for academic styling

### Rationale

- **Modern MDX support**: Docusaurus 3.x provides enhanced MDX capabilities for embedding React components in Markdown
- **Active maintenance**: Latest stable version with ongoing support and security updates
- **GitHub Pages integration**: Native support for static site deployment
- **Educational content optimization**: Classic theme provides clean, distraction-free reading experience suitable for technical education

### Implementation Details

**Core Dependencies**:
- `@docusaurus/core`: ^3.1.0
- `@docusaurus/preset-classic`: ^3.1.0
- `@mdx-js/react`: ^3.0.0
- `react`: ^18.2.0
- `react-dom`: ^18.2.0

**Plugins** (future additions as needed):
- `remark-math` + `rehype-katex`: For mathematical equations in robotics formulas
- Custom citation plugin or manual Markdown rendering for APA references

**Theme Customization**:
- Classic theme as base
- Custom CSS (`src/css/custom.css`) for academic styling:
  - Larger font size (1.05rem) for readability
  - Enhanced heading hierarchy with color differentiation
  - Table styling for lab specification comparisons
  - Code block styling with syntax highlighting for Python, C++, Bash, YAML, XML
  - Blockquote styling for important notes and callouts

### Alternatives Considered

- **Docusaurus 2.x**: Rejected due to inferior MDX support and approaching end-of-life
- **VuePress**: Rejected due to smaller community, less GitHub Pages integration
- **MkDocs**: Rejected as Python-based system doesn't align with Node.js project structure

---

## 2. GitHub Pages Deployment Strategy

### Decision

**GitHub Actions CI/CD** deploying to `gh-pages` branch on every push to `main`

### Rationale

- **Automation**: Zero-touch deployment on merge to main branch
- **Free hosting**: GitHub Pages provides free static site hosting for public repositories
- **Standard workflow**: Aligns with Docusaurus best practices and community patterns
- **Preview builds**: Can extend to build PR previews for review before merge

### Implementation Details

**Workflow File**: `.github/workflows/deploy.yml`

**Trigger Events**:
- Push to `main` branch → Build and deploy
- Pull requests to `main` → Build only (validate, no deploy)

**Build Process**:
1. Checkout repository
2. Setup Node.js 18 with npm caching
3. Install dependencies (`npm ci`)
4. Build Docusaurus site (`npm run build`)
5. Deploy to `gh-pages` branch using `peaceiris/actions-gh-pages@v3`

**Branch Protection**:
- `main` branch requires passing build before merge
- `gh-pages` branch auto-generated, no direct commits

**Deployment URL**: `https://[organization].github.io/physical-ai-course/`

### Alternatives Considered

- **`docs/` folder approach**: Rejected due to mixing source and build artifacts
- **Netlify/Vercel**: Rejected to minimize external dependencies and cost
- **Manual deployment**: Rejected due to error-prone nature and lack of automation

---

## 3. Content Generation Pipeline

### Decision

**Spec-Kit Plus (planning)** → **Claude Code (drafting)** → **Human Review (validation)**

### Rationale

- **Structured planning**: Spec-Kit Plus provides consistent specification and task breakdown
- **AI efficiency**: Claude Code accelerates content drafting while maintaining quality
- **Human validation**: Technical accuracy (constitution principle III) requires expert review
- **Iteration support**: 2-3 draft cycles per chapter expected for refinement

### Implementation Details

**Phase 1: Specification** (`/sp.specify`):
- Define chapter scope, learning objectives, examples
- Create acceptance criteria for the chapter
- Identify dependencies on previous chapters

**Phase 2: Planning** (`/sp.plan`):
- Design chapter structure and flow
- Identify code examples and exercises
- Plan Docusaurus integration (navigation, metadata)
- Create research.md for complex topics

**Phase 3: Task Generation** (`/sp.tasks`):
- Break chapter creation into actionable tasks
- Tasks include: content drafting, code examples, build validation, review

**Phase 4: Implementation** (`/sp.implement`):
- Claude Code drafts initial content from spec
- Human reviews for technical accuracy and citation correctness
- Iterate 2-3 times based on feedback
- Validate build and preview

**Phase 5: Review and Refinement**:
- Verify against spec acceptance criteria
- Run build validation (`npm run build`)
- Check consistency with existing chapters
- Update terminology glossary

**Version Control Strategy**:
- One feature branch per chapter (e.g., `001-physical-ai-course`)
- Atomic commits (one logical change per commit)
- Pull request for merge to main with build validation
- Commit message format: `docs: [chapter-name] - [change description]`

### Iteration Example

**Chapter Draft Cycle**:
1. **Initial Draft** (Claude Code): Generate 800-1,500 words following chapter schema
2. **Review 1** (Human): Check technical accuracy, citations, code examples
3. **Revision 1** (Claude Code): Address review feedback, refine content
4. **Review 2** (Human): Verify fixes, check consistency with other chapters
5. **Final Polish** (Claude Code): Minor edits, ensure word count compliance
6. **Merge**: After `npm run build` passes

---

## 4. APA Citation Management

### Decision

**BibTeX file (`static/references.bib`)** with **manual Markdown rendering** for citations

### Rationale

- **Industry standard**: BibTeX is widely used in academic publishing
- **Compatibility**: Works with Markdown/MDX without requiring complex plugins
- **APA 7th edition**: Supports required citation format (FR-012)
- **Manual control**: Ensures accurate citations without plugin quirks

### Implementation Details

**BibTeX File Structure**:
```bibtex
@inproceedings{AuthorYear,
  author    = {Last, First and Last2, First2},
  title     = {Paper Title},
  booktitle = {Conference/Journal Name},
  year      = {2020},
  pages     = {123-145},
  doi       = {10.1109/EXAMPLE.2020.12345}
}
```

**Inline Citation Format** (manual Markdown):
- Narrative: `Macenski et al. (2020) demonstrated...`
- Parenthetical: `Navigation systems have improved (Macenski et al., 2020).`

**Bibliography Generation**:
- Stored in `docs/appendices/references.md`
- Manually formatted from BibTeX entries in APA 7th edition
- Organized by category: ROS 2, Simulation, Isaac, VLA, Humanoid Robotics, Curriculum Design, Infrastructure

**Citation Validation**:
- Script: `tests/citation-validator.js`
- Checks: APA format compliance, year range (2015-2025), DOI presence
- Run via: `npm run validate:citations`

### Alternatives Considered

- **remark-bibtex plugin**: Rejected due to limited Docusaurus 3.x support and APA formatting issues
- **Zotero integration**: Rejected as over-engineered for static site
- **CSL JSON**: Rejected in favor of more widely-used BibTeX format

---

## 5. Peer-Reviewed Source Gathering Strategy

### Decision

**50-100 peer-reviewed sources** (2015-2025) gathered from **IEEE Xplore, ACM Digital Library, arXiv, Google Scholar**

### Rationale

- **FR-011 compliance**: All technical claims require peer-reviewed or industry-standard references
- **SC-004 requirement**: Every technical claim supported by citations
- **Recent relevance**: 2015-2025 ensures sources reflect current state of technology
- **Credibility**: Peer-reviewed sources ensure educational accuracy (constitution principle III)

### Source Allocation

**Total: 50-100 sources distributed as**:
- **ROS 2 Education**: 10-15 papers
  - Keywords: "ROS 2 education", "Robot Operating System pedagogy", "Nav2 stack", "ROS 2 Humble/Jazzy"
  - Example: Macenski et al. (2020) - Marathon 2 Navigation System
- **Gazebo/Unity Simulation**: 8-10 papers
  - Keywords: "Gazebo robotics pedagogy", "Unity robotics simulation", "sim-to-real transfer"
- **NVIDIA Isaac Sim**: 5-8 sources
  - Keywords: "Isaac Sim robotics", "NVIDIA Omniverse", "synthetic data generation", "sim-to-real"
  - Sources: NVIDIA technical reports, research papers using Isaac Sim
- **VLA Frameworks**: 10-15 papers
  - Keywords: "vision-language-action", "RT-1", "RT-2", "OpenVLA", "robotic manipulation"
  - Example: Brohan et al. (2023) - RT-2: Vision-Language-Action Models
- **Humanoid Robotics**: 10-15 papers
  - Keywords: "humanoid robot education", "bi-pedal locomotion", "Unitree", "Boston Dynamics", "humanoid manipulation"
- **Curriculum Design/ABET**: 5-10 papers
  - Keywords: "ABET robotics curriculum", "engineering education outcomes", "robotics program accreditation"
  - Example: ACM (2019) - Curriculum Guidelines for Robotics Engineering
- **Lab Infrastructure & ROI**: 5-10 sources
  - Keywords: "robotics lab cost-benefit", "university robotics infrastructure", "Physical AI education"
  - **SC-007**: 2+ case studies of universities with Physical AI programs

### Research Databases

**Primary Sources**:
- **IEEE Xplore**: Robotics conferences (IROS, ICRA, Humanoids), IEEE Transactions on Robotics
- **ACM Digital Library**: HRI conferences, educational technology, curriculum design
- **arXiv**: Robotics section (cs.RO), recent VLA and humanoid robotics preprints
- **Google Scholar**: Broader search, cross-reference validation

**Search Strategy**:
1. Start with known landmark papers (e.g., RT-2, Nav2)
2. Use "Cited by" to find recent applications
3. Filter by publication year (2015-2025)
4. Prioritize peer-reviewed conferences/journals over preprints
5. Validate relevance to educational context (not just research novelty)

### Quality Criteria

**Accept if**:
- Peer-reviewed (conference, journal, or industry whitepaper from reputable source)
- Published 2015-2025
- Directly relevant to robotics education, Physical AI, or course infrastructure
- Available in English
- Accessible (not paywalled or institutional access required)

**Reject if**:
- Preprint without peer review (unless seminal work like RT-2)
- Published before 2015 (unless foundational reference still widely cited)
- Tangential relevance (e.g., general ML theory not applied to robotics)
- Paywalled without institutional access

---

## 6. Code Example Testing Infrastructure

### Decision

**Docker containers** for each module's environment with **pytest (Python)** and **gtest (C++)** test frameworks

### Rationale

- **Reproducibility**: Docker ensures consistent testing environment across machines
- **Isolation**: Separate containers per module prevent dependency conflicts
- **Constitution compliance**: Technical accuracy (principle III) requires tested code
- **Quality gate**: All code examples must pass tests before chapter merge

### Implementation Details

**Docker Compose Configuration** (`docker-compose.yml`):
```yaml
version: '3.8'
services:
  ros2-test:
    image: ros:humble
    volumes:
      - ./tests/code-examples:/tests
      - ./static/code-examples:/code
    command: pytest /tests/test-ros2.py

  gazebo-test:
    image: osrf/gazebo:latest
    volumes:
      - ./tests/code-examples:/tests
      - ./static/code-examples:/code
    command: pytest /tests/test-gazebo.py

  isaac-sim-test:
    image: nvcr.io/nvidia/isaac-sim:latest
    volumes:
      - ./tests/code-examples:/tests
      - ./static/code-examples:/code
    command: pytest /tests/test-isaac.py

  vla-test:
    image: python:3.10
    volumes:
      - ./tests/code-examples:/tests
      - ./static/code-examples:/code
    command: |
      pip install torch transformers && pytest /tests/test-vla.py
```

**Test Frameworks**:
- **Python examples**: pytest with ROS 2 client libraries
- **C++ examples**: gtest for ROS 2 C++ nodes
- **Launch files**: XML validation, roslaunch-check equivalent

**CI Integration**:
- GitHub Actions runs `docker-compose up` on code example changes
- Fail PR if any test fails
- Report test results in PR comments

**Mocking Strategy**:
- **Hardware APIs**: Mock Jetson Orin, humanoid robot APIs with reasonable defaults
- **Sensors**: Mock LiDAR, camera data with sample datasets
- **Simulation**: Use headless Gazebo/Isaac Sim for CI compatibility

### Test Coverage Requirements

**Per Code Example**:
- Syntax validation (code compiles/runs without errors)
- Functional test (example achieves stated objective)
- Output verification (expected behavior confirmed)

**Example Test** (ROS 2 publisher/subscriber):
```python
def test_ros2_pubsub():
    # Start ROS 2 nodes
    pub = subprocess.Popen(['python3', 'ros2-pubsub.py', '--publisher'])
    sub = subprocess.Popen(['python3', 'ros2-pubsub.py', '--subscriber'])

    time.sleep(2)  # Allow nodes to communicate

    # Verify subscriber received messages
    output = sub.stdout.read()
    assert b"Received message" in output

    pub.kill()
    sub.kill()
```

---

## 7. Chapter/Module Structure (Final Decision)

### Decision

**14 chapters** organized across 5 categories: Modules (10), Exercises (4), Capstone (1), Infrastructure (2), Appendices (1)

### Rationale

- **Word count compliance**: 14 chapters × ~1,400 words avg = ~19,600 words (meets ~20,000 target)
- **Chapter range**: Falls within 8-18 chapter specification
- **Pedagogical flow**: Progressive difficulty from ROS 2 basics through VLA integration
- **Independent chapters**: Each 800-1,500 words, self-contained with cross-references

### Detailed Breakdown

**Module 1: ROS 2 (3 chapters, ~4,200 words)**
1. **ROS 2 Intro & Basics** (~1,400 words)
   - Learning objectives: Understand ROS 2 architecture, create publisher/subscriber nodes
   - Topics: Nodes, topics, services, parameters, workspaces
   - Exercise: Simple publisher/subscriber communication
2. **ROS 2 Navigation Stack** (~1,400 words)
   - Learning objectives: Implement autonomous navigation using Nav2
   - Topics: Costmaps, path planning, behavior trees
   - Exercise: Autonomous navigation in Gazebo simulation
3. **Advanced Multi-Robot Systems** (~1,400 words)
   - Learning objectives: Coordinate multiple robots, implement distributed systems
   - Topics: Namespaces, multi-robot coordination, distributed ROS 2
   - Exercise: Multi-robot coordination task

**Module 2: Simulation (2 chapters, ~2,800 words)**
4. **Gazebo for Robotics** (~1,400 words)
   - Learning objectives: Create robot models, simulate sensors, test algorithms
   - Topics: URDF/SDF, sensor plugins, world files
   - Exercise: Custom robot simulation with sensors
5. **Unity Robotics Integration** (~1,400 words)
   - Learning objectives: Use Unity for high-fidelity visualization
   - Topics: Unity Robotics Hub, ROS-Unity bridge, visualization
   - Exercise: Unity visualization of ROS 2 robot

**Module 3: NVIDIA Isaac Sim (2 chapters, ~2,800 words)**
6. **Isaac Sim Intro & Synthetic Data** (~1,400 words)
   - Learning objectives: Generate synthetic training data for perception models
   - Topics: Omniverse platform, synthetic data generation, domain randomization
   - Exercise: Generate labeled dataset for object detection
7. **Sim-to-Real Transfer** (~1,400 words)
   - Learning objectives: Validate sim-to-real transfer for robot policies
   - Topics: Reality gap, transfer learning, validation strategies
   - Exercise: Train policy in Isaac Sim, validate metrics

**Module 4: VLA (3 chapters, ~4,200 words)**
8. **VLA Concepts** (~1,400 words)
   - Learning objectives: Understand vision-language-action architectures
   - Topics: Transformer models, multimodal learning, action spaces
   - Exercise: Analyze RT-2 architecture and capabilities
9. **VLA Integration with Robots** (~1,400 words)
   - Learning objectives: Integrate pre-trained VLA models with robot systems
   - Topics: OpenVLA, model deployment, inference optimization
   - Exercise: Deploy VLA model for object recognition
10. **VLA Manipulation Tasks** (~1,400 words)
    - Learning objectives: Execute manipulation tasks via natural language commands
    - Topics: Grasp planning, task execution, language grounding
    - Exercise: "Pick up the red cup" natural language task

**Capstone (1 chapter, ~1,400 words)**
11. **Integrated VLA-Driven Humanoid Task** (~1,400 words)
    - Learning objectives: Demonstrate mastery of all 4 modules
    - Integration: ROS 2 architecture + simulation validation + Isaac Sim + VLA task execution
    - Evaluation rubric: 30% integration, 25% deployment, 20% simulation, 15% VLA, 10% docs

**Infrastructure (2 chapters, ~2,800 words)**
12. **Lab Tiers Overview** (~1,400 words)
    - Proxy tier ($10-20K, simulation-only)
    - Miniature tier ($50-70K, compact humanoids)
    - Premium tier ($120-180K, full-scale humanoids)
13. **Detailed Tier Specifications** (~1,400 words)
    - Itemized hardware/software for each tier
    - On-premise vs cloud-native comparison
    - Space requirements and deployment options

**Appendices (1 combined chapter, ~1,400 words)**
14. **Appendices** (~1,400 words as combined)
    - Glossary: ROS 2, Isaac Sim, VLA, sim-to-real, etc.
    - Week-by-Week Schedule: 12-16 week semester mapping
    - ROI Analysis: Cost-benefit, case studies, educational impact
    - References: 50-100 APA-formatted sources

**Additional Exercise Chapters** (not counted in 14, but included in sidebar):
- Detailed exercise specifications for each module (1 page each)
- Total 4 exercise chapters providing implementation guidance

---

## 8. Lab and Hardware Representation

### Decision

**Combination approach**: Diagrams (draw.io/Lucidchart) for abstract concepts + Vendor photos (attributed) for hardware

### Rationale

- **FR-006 to FR-010**: Detailed lab tier specifications required
- **FR-014 constraint**: High-level recommendations, not full vendor comparisons
- **Accessibility**: All images require descriptive alt text (constitution principle IV)
- **Visual learning**: Diagrams aid understanding of complex lab setups

### Implementation Details

**Diagram Types** (created in draw.io, exported as SVG/PNG):
1. **Lab Layout Diagrams** (`static/img/lab-setups/`)
   - Proxy tier: 10-15 GPU workstations layout
   - Miniature tier: Workstations + 1-2 compact humanoids
   - Premium tier: Workstations + 3-5 full-scale humanoids with safety zones
2. **Network Topology** (`static/img/architecture/`)
   - ROS 2 distributed system architecture
   - Workstation-robot communication
   - Cloud vs on-premise networking
3. **System Architecture**
   - ROS 2 node graph
   - VLA integration architecture
   - Sim-to-real workflow diagram

**Robot Platform Images** (`static/img/robots/`):
- **Sourcing**: Vendor press kits (NVIDIA, Unitree, Figure), Creative Commons
- **Attribution**: `"Image courtesy of [Vendor]"` in caption
- **Examples (non-exhaustive per FR-014)**:
  - Unitree H1, G1 (compact humanoids)
  - Figure 01 (full-scale humanoid)
  - Boston Dynamics Atlas (reference for capabilities)
  - NVIDIA Jetson Orin (edge AI compute)

**Hardware Tables**:
| Component | Proxy | Miniature | Premium |
|-----------|-------|-----------|---------|
| Workstations | 10-15 GPU | 10-15 GPU + edge AI | 15-20 GPU + edge AI |
| Humanoid Robots | None | 1-2 compact | 3-5 full-scale |
| Cost Range | $10-20K | $50-70K | $120-180K |
| Space (sqft) | 500-800 | 800-1200 | 1500-2500 |

**Alt Text Standards** (accessibility):
- Descriptive, not decorative: "Diagram showing ROS 2 node communication architecture"
- Include key information: "Lab layout for Premium tier with 3 humanoid robots, 15 workstations, and safety zones"
- Avoid redundancy with caption

---

## References

This research document references decisions from:
- **plan.md**: Implementation plan with technical context and architecture
- **spec.md**: Feature specification with user stories and requirements
- **constitution.md**: 7 core principles governing book creation

**Next Steps**:
1. Gather peer-reviewed sources per Section 5 strategy
2. Generate data-model.md defining 10 content entities
3. Create contracts (chapter schema, exercise schema, lab tier table)
4. Generate quickstart.md for contributor onboarding
