---
name: brand-strategist-lite
description: A human-in-the-loop brand positioning tool that separates data extraction, human scoring, mechanical analysis, and strategic options into four transparent layers.
version: 2.0.0
---

# Brand Strategist Lite

This skill guides the user through a four-layer brand strategy process where AI handles structuring and the human handles all scoring and decisions.

## Capabilities

- **Layer 1 — JTBD Extraction**: AI extracts Jobs to be Done from interviews; user confirms and selects top 3-5 Jobs.
- **Layer 2 — Bain 30 Scoring**: AI suggests relevant value elements; user scores importance ($W_u$) and delivery ($S_c$, $S_{corp}$) with evidence.
- **Layer 3 — 3C Matrix Computation**: Deterministic gap analysis with no AI involvement. Same inputs always produce same outputs.
- **Layer 4 — Positioning Options**: AI generates 2-3 positioning options with evidence, archetypes, and risks; user chooses direction.

## Design Principles

1. **AI structures, human judges**: All scores and decisions come from the user.
2. **Traceable**: Every score links to at least one evidence source.
3. **Reproducible**: Layer 3 is pure math — deterministic and verifiable.
4. **Options, not answers**: Final output is 2-3 choices, not a single conclusion.

## Usage

### Step 1: Input Data

- **/add-interview**: Import user interview notes (minimum 3, covering ≥2 customer segments).
- **/add-competitor**: Add competitor name and information sources.
- **/add-brand-info**: Define your brand mission, values, and product description.

### Step 2: Execute Analysis

- **/brand-run**: Full guided workflow (with human confirmation at each layer).

Or run individual layers:

- **/brand-user**: Layer 1 — JTBD extraction and confirmation.
- **/brand-comp**: Layer 2 — Dimension selection and human scoring.
- **/brand-strat**: Layers 3-4 — Matrix computation and positioning options.
- **/archive-reports**: Archive current reports.

## Quality Gates

| Layer | Gate Condition |
| :--- | :--- |
| 1 | ≥3 interviews; each Job must appear in ≥2 different interviews |
| 2 | Every score requires evidence; empty evidence marks score as "unverified" |
| 3 | None (deterministic math) |
| 4 | User must explicitly choose a direction before strategy is expanded |

## Output

- `stage_2_market_analysis/User_Insights_Report.md` — Confirmed JTBD with source quotes
- `stage_2_market_analysis/Scoring_Matrix.md` — Human-scored matrix with evidence
- `stage_3_strategy_generation/Positioning_Options.md` — 2-3 options with tradeoffs
- `stage_3_strategy_generation/Final_Strategy.md` — Expanded strategy for chosen direction

## Directory Structure

- `config/`: Configuration files.
- `brand-strategist-lite/scripts/`: Python automation scripts.
- `brand-strategist-lite/references/`: Framework definitions and templates.
- `stage_1_user_insights/`: Input directory for user interviews.
- `stage_2_market_analysis/`: Scoring matrices and analysis reports.
- `stage_3_strategy_generation/`: Positioning options and final strategy.
