---
description: Add a new competitor website to the analysis target list.
---

# Workflow: Add Competitor

1.  **Ask User**: "Please provide the Competitor Name and their Website URL."
2.  **Validate**: Ensure the provided URL is valid.
3.  **Update Config**:
    -   Read `config/targets.json`.
    -   Add the new competitor (name and url) to the `urls` list.
    -   Save the updated `config/targets.json`.
4.  **Confirm**: Tell the user "Competitor [Name] added. You can now run `/brand-comp` to analyze them."
