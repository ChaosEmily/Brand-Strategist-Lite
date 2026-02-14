---
description: Analyze competitor data to generate the Competitor Analysis Report (Competitor aspect of 3C).
---

# Workflow: Competitor Analysis

// turbo-all
1.  Check input data (Competitor URLs):
    ```bash
    python brand-strategist-lite/scripts/state_manager.py check competitor_analysis
    ```
2.  Crawl competitor websites (if check passed):
    ```bash
    python brand-strategist-lite/scripts/competitor_crawler.py state
    ```
3.  Analyze the data and generate the report:
    -   Read `stage_2_market_analysis/competitors/*.json`.
    -   Compare features using the 3C expanded matrix.
    -   Calculate Opportunity Score ($O$).
    -   Save to `stage_2_market_analysis/Competitor_Analysis.md` following the Master Template in `framework_details.md`.
```
