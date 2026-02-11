---
description: Import your own brand's mission, values, and product description. Supports file import.
---

# Workflow: Add Brand Info

1.  **Ask User**: "Do you have a brand document (Mission, Values, Product) to import? (Yes/No)"
2.  **Branch - Yes (File Import)**:
    -   Ask: "Please provide the absolute file path."
    -   **Read File**: Use the `view_file` tool to read the content of the provided path.
    -   **Extract & Convert**: extract key information (Mission, Values, Product Description) and format it into Markdown.
3.  **Branch - No (Interview)**:
    -   Ask: "What is your Brand Mission?"
    -   Ask: "What are your Core Values?"
    -   Ask: "Describe your Product/Service."
    -   Combine these answers into a Markdown format.
4.  **Save**:
    -   Create directory if not exists: `stage_2_market_analysis/own_brand/`
    -   Write the content to: `stage_2_market_analysis/own_brand/brand_info.md`
5.  **Confirm**: Tell the user "Brand info saved. You can now run `/brand-strat` to generate your strategy."
