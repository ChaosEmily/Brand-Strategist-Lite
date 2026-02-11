---
name: brand-strategist-lite
description: A lightweight brand positioning tool for startups, automating competitor analysis and guiding users through JTBD, Bain 30, and Brand Archetypes frameworks.
---

# Brand Strategist Lite

This skill guides the user through a brand strategy process.

## Capabilities
- **3C Framework Integration**: Holistic brand strategy covering Customer (Demand), Competitor (Supply), and Corporation (Capability).
- **Expanded 3C Competitive Matrix**: Quantitative side-by-side comparison of up to 3 competitors with **Max Gap** and Opportunity Score ($O$) calculation.
- **Functional Moat Identification**: Prioritizing product/service specs over personality to find true differentiation.
- **Psychological Archetype Mapping**: Deriving brand personality directly from 3C interaction (The "Wise Butler" logic).
- **Report Archiving**: Systematic storage of historical analysis iterations.

## Usage

### Step 1: Configuration
1. Edit `config/targets.json` to include competitor URLs.
2. Place user interview notes in `stage_1_user_insights/interviews/` (text or markdown files).

### Step 2: Input Data (Interactive Workflows)
Start by telling the AI about your brand, users, and competitors. Use these commands to add data:

- 🆕 **/add-competitor**: Add a new competitor website to analyze.
- 🆕 **/add-interview**: Add user interview notes (supports text paste or file import).
- 🆕 **/add-brand-info**: Add your own brand mission/values (supports text or file).

### Step 3: Execute Analysis (Slash Commands)
To generate the full strategy report, simply type the following command in the chat:

> **/brand-run**

Alternatively, you can run individual steps:
- **User Analysis**: `/brand-user`
- **Competitor Analysis**: `/brand-comp`
- **Strategy Generation**: `/brand-strat`
- **Archive Reports**: `/archive-reports`

## Output
The analysis results will be saved in `stage_2_market_analysis/`:
- `User_Insights_Report.md`
- `Competitor_Analysis.md`
- `Final_Brand_Strategy.md`

## Directory Structure
- `config/`: Configuration files.
- `brand-strategist-lite/scripts/`: Python scripts for automation.
- `branded-strategist-lite/references/`: Framework definitions and templates.
- `stage_1_user_insights/`: Input directory for user interviews.
- `stage_2_market_analysis/`: Output directory for competitor data and final reports.
- `brand-strategist-lite/`: Skill definition and documentation.
