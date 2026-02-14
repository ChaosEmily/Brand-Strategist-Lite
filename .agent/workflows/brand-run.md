---
description: Execute the entire Brand Strategist workflow from raw data to final strategy.
---

# Workflow: One-Click Full Strategy Generation

// turbo-all
1.  Check data readiness:
    ```bash
    python brand-strategist-lite/scripts/state_manager.py check all
    ```
2.  Execute workflow: `.agent/workflows/brand-user.md`
3.  Execute workflow: `.agent/workflows/brand-comp.md`
4.  Execute workflow: `.agent/workflows/brand-strat.md`

---
**Goal**: Ensure all three reports are generated in `stage_2_market_analysis/`: `User_Insights_Report.md`, `Competitor_Analysis.md`, and `Final_Brand_Strategy.md`.
