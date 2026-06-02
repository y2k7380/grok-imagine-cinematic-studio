# Changelog

All notable changes to Grok Imagine Cinematic Studio will be documented in this file.

## [3.5.1] - 2026-06-02

### Added
- Complete **22-agent Role Card system** in `references/agents/` with full structure:
  - Core Mission
  - v3.5 / v4.0 Upgrades
  - Key Responsibilities
  - Specialized Protocols
  - Decision Frameworks
  - Output Formats
  - Activation Triggers
  - Integration Notes
- Comprehensive `AGENT_INDEX.md` in `references/agents/`
- Improved CI workflow (`cinematic-agent-workflow-ci.yml` v3.5) with:
  - Role Card structure validation
  - `references/agents/` directory checking
  - Configurable `validation_mode` (standard / strict / full)
  - Better agent detection logic
- Updated documentation:
  - Revised `README.md` (accurate 22-agent count, Role Card emphasis)
  - Updated `Quick_Start_Guide.md` v2.0 with improved workflow and specialist table
- Full `grok-imagine-cinematic-studio` skill pulled with latest `MASTER_PROMPT_v3.5.md`

### Changed
- Standardized all agent files to `*_v3.5.txt` naming
- Expanded and refined all 22 agent Role Cards to full detailed format
- Improved consistency across agent activation commands
- Better alignment between project structure and documentation

### Fixed
- Broken filename in agents directory (`Continuity_Consistency_Guardian`)
- Outdated agent counts and references in documentation
- Missing references to the new `references/agents/` Role Card system

---

## [3.5.0] - 2026-06

### Added
- Full 22-agent cinematic production system
- ErosForge NSFW Director with artistic standards
- Cinematic Sequence Extender for long-form content
- Native audio design integration
- Production Bible system
- Modular prompt template architecture
- Comprehensive agent personality versioning
- Streamlit Web UI
- Python CLI toolkit

### Changed
- Major reorganization of agent folder structure by production department
- Improved continuity and identity lock systems

## [3.4.0] - Previous

- Initial multi-agent orchestration
- Core leadership agents (Studio Director + Mega Production Architect)
- Basic Production Bible support