# Brand Strategist Lite

A lightweight brand positioning tool designed for startup teams. It integrates **Jobs to be Done (JTBD)**, **Bain 30 Value Elements**, and **Brand Archetypes** to help you build a differentiated brand strategy.

## Features
- **3C Framework Generator**: One-click strategy generation covering Customer, Competitor, and Corporation.
- **Multi-Competitor Matrix**: Side-by-side comparison of up to 3 rivals with automatic **Max Gap** detection.
- **Functional Moat Analysis**: Precision identification of product-based competitive advantages.
- **Auto-Crawler**: Fetches competitor website content for supply-side ($S_c$) analysis.

## Getting Started

1.  **Install Dependencies**:
    ```bash
    pip install requests beautifulsoup4
    ```

2.  **Setup Competitors**:
    Add URLs to `config/targets.json`.

3.  **Run Crawler**:
    ```bash
    python brand-strategist-lite/scripts/competitor_crawler.py config/targets.json
    ```

4.  **Analyze (One-Click)**:
    Just type the slash command:
    > **/brand-run**

    This will generate your User Insights, Competitor Matrix, and Final Strategy.

## Structure
- `brand-strategist-lite/scripts/`: Automation tools.
- `stage_1_user_insights/`: User interview data.
- `stage_2_market_analysis/`: Competitor data and Analysis reports.
- `brand-strategist-lite/references/`: Theory and templates.
