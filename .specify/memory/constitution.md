# Book Creation Constitution

<!--
Sync Impact Report:
Version change: [NEW CONSTITUTION] → 1.0.0
Modified principles: Initial creation with 7 core principles
Added sections: Core Principles, Content Standards, Development Workflow, Governance
Removed sections: None
Templates requiring updates:
  ✅ plan-template.md - Aligned with book creation structure and Docusaurus requirements
  ✅ spec-template.md - Aligned with chapter specification requirements
  ✅ tasks-template.md - Aligned with chapter development workflow
Follow-up TODOs: None - all placeholders filled
-->

## Core Principles

### I. Spec-First Writing Workflow

Every chapter MUST originate from a feature specification created using Spec-Kit Plus workflows. No chapter content may be written without a corresponding spec.md file that defines:
- Chapter scope and learning objectives
- Target audience and prerequisites
- Key concepts and examples required
- Success criteria for the chapter

**Rationale**: Spec-first approach ensures consistency, prevents scope creep, and maintains alignment between planned and delivered content. Each chapter becomes a testable unit of educational value.

### II. Clarity and Accessibility

All content MUST be written for general technical learners without assuming deep specialized knowledge. Technical concepts MUST be:
- Introduced with plain-language definitions before diving into implementation details
- Supported by concrete, verifiable examples
- Free of jargon unless explicitly defined in context
- Structured with clear headings and progressive difficulty

**Rationale**: The book serves learners at various skill levels. Accessibility maximizes reach and educational impact while maintaining technical rigor.

### III. Technical Accuracy (NON-NEGOTIABLE)

Zero tolerance for hallucinations or fabricated information. All technical claims, code examples, and tool capabilities MUST be:
- Verified through actual testing or authoritative documentation
- Based on real, reproducible examples
- Clearly marked when hypothetical or illustrative
- Updated when underlying tools or technologies change

**Rationale**: Educational credibility depends entirely on accuracy. A single fabricated example undermines reader trust and learning outcomes.

### IV. Consistent Tone and Structure

All chapters MUST follow a unified structure and maintain consistent:
- Voice (instructional, friendly, professional)
- Terminology (defined once, used consistently throughout)
- Code formatting and style conventions
- Section organization (introduction → concepts → examples → practice → summary)
- Docusaurus metadata and navigation structure

**Rationale**: Consistency reduces cognitive load, enables readers to focus on content rather than adapting to format changes, and creates a cohesive learning experience.

### V. Iterative Improvement Through Claude Code

Claude Code is the primary tool for:
- Drafting initial chapter content from specifications
- Refining based on review feedback
- Ensuring Docusaurus build compliance
- Maintaining consistency across chapters
- Generating and validating code examples

All chapter updates MUST be performed through Claude Code using established workflows (`/sp.specify`, `/sp.plan`, `/sp.tasks`, `/sp.implement`).

**Rationale**: Claude Code provides consistent execution of the spec-driven workflow, maintains quality standards, and enables rapid iteration with traceability.

### VI. Version Control and Traceability

Every content change MUST be committed with:
- Meaningful commit messages explaining the "why" (e.g., "docs: clarify installation steps in chapter 2 based on reader feedback")
- Reference to the spec or task being addressed
- Atomic commits (one logical change per commit)
- Branch naming convention: `###-feature-name` for new chapters/features

**Rationale**: Version control provides audit trail, enables rollback, facilitates collaboration, and documents the evolution of the book's content.

### VII. Build Validation and Deployment

Before any chapter is considered complete, it MUST:
- Pass `npm run build` without errors or warnings
- Render correctly in Docusaurus local preview (`npm start`)
- Include all required Docusaurus frontmatter (id, title, sidebar_position)
- Have working internal links and navigation
- Deploy successfully to GitHub Pages

**Rationale**: A book that doesn't build or deploy is unusable. Build validation is the final quality gate ensuring content reaches readers in working condition.

## Content Standards

### Chapter Requirements

Each chapter MUST:
- Contain 800–1,500 words of substantive content (excluding code blocks)
- Include at least one complete, runnable code example
- Have clear learning objectives stated in the introduction
- End with a summary of key takeaways
- Be self-contained while building on previous chapters

### Markdown/MDX Format

All chapters MUST:
- Use GitHub-flavored Markdown or MDX compatible with Docusaurus
- Include proper Docusaurus frontmatter:
  ```yaml
  ---
  id: chapter-slug
  title: Chapter Title
  sidebar_position: N
  ---
  ```
- Use code fences with language identifiers for syntax highlighting
- Include alt text for all images
- Use relative links for internal navigation

### Code Examples

All code examples MUST:
- Be complete and executable (not fragments unless explicitly teaching concepts)
- Include necessary context (imports, setup, teardown)
- Be tested before inclusion
- Follow the language's established style conventions
- Include comments explaining non-obvious logic

## Development Workflow

### Chapter Creation Process

1. **Specification** (`/sp.specify`):
   - Create spec.md defining chapter scope, learning objectives, examples
   - Define acceptance criteria for the chapter
   - Identify dependencies on previous chapters

2. **Planning** (`/sp.plan`):
   - Design chapter structure and flow
   - Identify code examples and exercises
   - Plan Docusaurus integration (navigation, metadata)
   - Create research.md if needed for complex topics

3. **Task Generation** (`/sp.tasks`):
   - Break chapter creation into actionable tasks
   - Include tasks for: content drafting, code examples, build validation, review

4. **Implementation** (`/sp.implement`):
   - Draft chapter content following the spec
   - Create and test all code examples
   - Validate build and preview
   - Iterate based on review feedback

5. **Review and Refinement**:
   - Verify against spec acceptance criteria
   - Run build validation
   - Check consistency with existing chapters
   - Update terminology glossary if needed

### Quality Gates

Before merging any chapter:
- [ ] Spec acceptance criteria met
- [ ] Word count within 800–1,500 range
- [ ] All code examples tested and working
- [ ] `npm run build` passes
- [ ] Docusaurus preview renders correctly
- [ ] Internal links validated
- [ ] No technical inaccuracies (peer review or self-review required)
- [ ] Consistent with book tone and terminology

## Governance

### Amendment Process

This constitution may be amended when:
- Book scope expands beyond 8–18 chapters
- New tooling or platforms are adopted (e.g., alternative to Docusaurus)
- Quality issues reveal gaps in principles or standards

Amendments require:
1. Documentation of the problem or limitation in current constitution
2. Proposed change with rationale
3. Impact analysis on existing chapters and workflows
4. Update to this document with version bump
5. Migration plan for existing content if needed

### Compliance

All contributions MUST comply with this constitution. Non-compliance requires one of:
- Immediate correction
- Documented exception with rationale and time-bound plan to comply
- Constitution amendment if the principle is overly restrictive

### Version Control

- This constitution follows semantic versioning (MAJOR.MINOR.PATCH)
- MAJOR: Breaking changes to core principles or workflow
- MINOR: New principles or significant expansions
- PATCH: Clarifications, wording improvements, typo fixes

### Review Cycle

Constitution MUST be reviewed:
- After every 5 chapters completed
- When build or deployment processes change
- When feedback reveals systematic quality issues
- At project milestones (e.g., first draft complete, beta release)

**Version**: 1.0.0 | **Ratified**: 2025-12-06 | **Last Amended**: 2025-12-06
