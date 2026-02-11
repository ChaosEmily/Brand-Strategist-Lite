---
description: Add a new user interview to the insights database. Supports direct text input or file import.
---

# Workflow: Add User Interview

1.  **Ask User**: "What is the Interviewee Name or ID? (e.g., User_01)"
2.  **Ask User**: "Do you have a file to import, or would you like to paste the text directly?"
3.  **Branch - File Import**:
    -   If user says **File**:
        -   Ask: "Please provide the absolute file path."
        -   **Read File**: Use the `view_file` tool to read the content of the provided path.
        -   **Convert**: If the file is not Markdown, format the content into clean Markdown.
4.  **Branch - Paste Text**:
    -   If user says **Paste**:
        -   Ask: "Please paste the interview notes here."
        -   Wait for user input.
5.  **Save**:
    -   Create a new file: `stage_1_user_insights/interviews/[Interviewee_Name].md`
    -   Write the content (converted Markdown or pasted text) into this file.
6.  **Confirm**: Tell the user "Interview for [Name] saved. You can now run `/brand-user` to analyze insights."
