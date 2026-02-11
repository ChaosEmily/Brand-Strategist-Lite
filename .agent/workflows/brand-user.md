---
description: Analyze user interview data to generate the User Insight Report (Customer aspect of 3C).
---

# Workflow: User Insight Analysis

1.  **Data Collection**: Read all files in `stage_1_user_insights/interviews/`.
2.  **JTBD Extraction**: 
    -   Identify Functional Jobs (practical tasks).
    -   Identify Emotional Jobs (inner feelings).
    -   Identify Social Jobs (external perception).
    -   Draft a JTBD Statement: "When I [context], I want to [motivation], so I can [outcome]."
3.  **Bain 30 Mapping ($W_u$)**:
    -   Refer to `brand-strategist-lite/references/framework_details.md` for elements.
    -   Map user statements to elements.
    -   Assign **User Weight ($W_u$)** (1-10) based on emotion and frequency.
4.  **Customer Persona**: 
    -   Summarize "Who they are".
    -   Identify the **Expected Brand Archetype**: What personality should a provider have to satisfy these users' emotional jobs?
5.  **Output**: Save to `stage_2_market_analysis/User_Insights_Report.md` following the Master Template in `framework_details.md`.
