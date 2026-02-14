---
description: Synthesize Customer and Competitor data into a Final Brand Strategy (Corporation aspect of 3C).
---

# Workflow: Brand Strategy Synthesis

// turbo-all
1.  Check previous reports:
    ```bash
    python brand-strategist-lite/scripts/state_manager.py check strategy_generation
    ```
2.  Synthesize findings:
    -   Read `stage_2_market_analysis/User_Insights_Report.md`.
    -   Read `stage_2_market_analysis/Competitor_Analysis.md`.
    -   Find the 3C Intersection (Max Gap).
    -   Map the Brand Archetype (e.g., Sage, Creator) based on the intersection.
    -   Save final strategy to `stage_3_strategy_generation/Final_Brand_Strategy.md`.
 vs competitors.
3.  **Expanded 3C Competitive Matrix ($O$ & Max Gap)**: 
    -   Evaluate our own functional performance ($S_{corp}$).
    -   Calculate $\text{Avg}(S_c)$ across all active competitors for $O$ score.
    -   Calculate $\text{Max}(S_c)$ to find the **Max Gap** ($S_{corp} - \text{Max}(S_c)$).
    -   Identify "Win Zones" where both $W_u$ and Max Gap are high.
4.  **3C Sweet Spot Synthesis**: 
    -   **Customer Want**: Top unmet $W_u$ scores.
    -   **Competitor Own**: Top $S_c$ elements.
    -   **Our Strategic Pivot**: Intersection of our high $S_{corp}$ (Functional Moat) and Customer Want.
5.  **Archetype Implementation**: 
    -   Derived a Target Archetype based on the **Strategic Pivot** (not just random preference).
    -   Define Tone of Voice, Content Pillars, and Taglines.
6.  **Action Plan**: Draft next steps for Product, Marketing, and Community.
7.  **Output**: Save to `stage_3_strategy_generation/Final_Brand_Strategy.md`.
