---
name: brand-strategist-lite
description: A lightweight brand positioning tool for startups, automating competitor analysis and guiding users through JTBD, Bain 30, and Brand Archetypes frameworks.
version: 1.0.0
---

# Brand Strategist Lite

Brand Strategist Lite is a specialized AI agent skill designed to help startups and personal brands define their strategic positioning. It utilizes the **3C Framework** (Customer, Competitor, Corporation) to create a comprehensive brand strategy that is actionable and defensible.

## 🚀 Key Features

- **3C Framework Integration**: Systematically analyzes User Insights (Customer), Market Landscape (Competitor), and Internal Capabilities (Corporation).
- **Quantitative Competitive Matrix**: Compares your brand against up to 3 competitors using a scoring system to identify **Max Gap** and Opportunity Score ($O$).
- **Functional Moat Identification**: Focuses on finding differentiation in product specifications and service levels, not just "brand vibes".
- **Automated Archetype Mapping**: Derives the most suitable Brand Archetype (e.g., Sage, Hero, Creator) based on the analytical results.
- **Automated Reporting**: Generates structured Markdown reports for every stage of the analysis.

## 📂 System Structure

The skill is organized as follows:

```text
d:\Projects\Brand Strategist Lite\
├── brand-strategist-lite/      # Core skill definitions and scripts
│   ├── scripts/                # Python automation scripts
│   │   ├── competitor_crawler.py # Basic web scraper
│   │   └── archive_reports.py    # Archiving utility
│   ├── COMMANDS.md             # Detailed command reference
│   └── SKILL.md                # Internal reference
├── config/                     # Configuration files
│   └── targets.json            # Competitor URLs and settings
├── stage_1_user_insights/      # Input: User interview notes & raw data
├── stage_2_market_analysis/    # Output: Generated analysis reports
├── stage_3_strategy_generation/# Output: Final strategy documents
├── stage_3_strategy_generation/# Output: Final strategy documents
├── archive/                    # Archived historical reports
├── project_state.json          # [NEW] Central state file required for analysis
├── README.md                   # General project info
└── SKILL.md                    # This documentation file
```

## 🛠️ Installation & Setup

1.  **Prerequisites**:
    -   Python 3.8+ installed.
    -   Required Python packages: `playwright`.
    -   (Install via: `pip install playwright`, then `playwright install chromium`)

2.  **Configuration**:
    -   Edit `config/targets.json` to define your competitor list if you wish to bypass the interactive commands.

## 💻 Usage Guide (Slash Commands)

This skill is operated primarily through **Slash Commands** in the chat interface.

### 1. Data Collection Phase
Before running the full analysis, you need to feed the system with data.

| Command | Description |
| :--- | :--- |
| **/add-competitor** | Interactive guide to add a competitor's name and URL. Updates `config/targets.json`. |
| **/add-interview** | Import user interview notes. You can paste text directly or provide a file path to a transcript. Saved to `stage_1_user_insights/`. |
| **/add-brand-info** | Define your brand's mission, values, and core product offerings. Crucial for the "Corporation" aspect of the 3C analysis. |

### 1. **全自動分析 (One-Click Strategy)**
- **指令**: `/brand-run`
- **功能**: **自動檢查資料完整性**，然後依序執行：使用者分析 $\rightarrow$ 競品分析 $\rightarrow$ 策略生成。
- **Output**: 產生三份完整報告。
- **注意**: 若缺少訪談或競品資料，系統會自動停止並提示補齊。

### 2. **單項分析 (Modular Analysis)**
- **`/brand-user`**: **檢查訪談資料** $\rightarrow$ 分析 Pain/Gain/Jobs $\rightarrow$ 產出 `User_Insights_Report.md`。
- **`/brand-comp`**: **檢查競品網址** $\rightarrow$ 自動爬蟲 $\rightarrow$ 3C 分析 $\rightarrow$ 產出 `Competitor_Analysis.md`。
- **`/brand-strat`**: **檢查前兩份報告** $\rightarrow$ 尋找策略缺口 $\rightarrow$ 產出 `Final_Brand_Strategy.md`。

### 3. Maintenance
| Command | Description |
| :--- | :--- |
| **/archive-reports** | Moves current markdown reports to a timestamped folder in `archive/` to clear the workspace for a new iteration. |

## 📊 Output Artifacts

The skill generates the following markdown reports:

1.  **User_Insights_Report.md** (`stage_2_market_analysis/`)
    -   Summary of user pains and gains (JTBD).
    -   Key purchasing drivers.

2.  **Competitor_Analysis.md** (`stage_2_market_analysis/`)
    -   Feature-by-feature comparison matrix.
    -   Scoring of competitors on key attributes.

3.  **Final_Brand_Strategy.md** (`stage_3_strategy_generation/`)
    -   **3C Intersection**: Where your strengths meet customer needs and competitor weaknesses.
    -   **Brand Archetype**: The persona that best communicates this position.
    -   **Action Plan**: Strategic roadmap.

## 🔗 Recommended Integration Scenarios

Once the strategy is generated, you can combine this skill with other workflows for maximum impact:

### 1. **Content Marketing Engine**
-   **Goal**: Generate high-quality, on-brand content.
-   **How**: Use `Final_Brand_Strategy.md` as the "Brand Voice" input for an AI copywriter.
-   **Prompt**: "Act as the [Archetype] defined in the strategy. Write 5 social posts about [Topic] using the identified [Brand Voice]."

### 2. **Visual Identity Prototyping**
-   **Goal**: Visualize the brand's look and feel.
-   **How**: Extract "Mood Board Keywords" from the strategy to drive image generation.
-   **Prompt**: "Create a landing page hero section. Style: [Keywords from Strategy]. Emphasize: [Functional Moat]."

### 3. **Product Roadmap Planning**
-   **Goal**: Prioritize features that matter.
-   **How**: Use the "Max Gap" and "Opportunity Score" from `Competitor_Analysis.md` to feed into a Product Manager skill. focus on features where competitors are weak ($S_c$ is low) but user demand is high ($W_u$ is high).

### 4. **Pitch Deck Generation**
-   **Goal**: Create a compelling investor story.
-   **How**: Map the 3C outputs directly to slide decks:
    -   **Problem**: User Pain Points (`User_Insights_Report.md`)
    -   **Competition**: Comparative Matrix (`Competitor_Analysis.md`)
    -   **Solution**: Value Proposition (`Final_Brand_Strategy.md`)

## ⚠️ Current Limitations & Roadmap

-   **Crawler**: The crawler (`competitor_crawler.py`) uses Playwright to handle dynamic websites, but may still be blocked by strict anti-bot measures (e.g., Cloudflare).
-   **Data Persistence**: Relies on file-based storage. Ensure you do not manually delete files in `stage_X` folders while an analysis is in progress.
-   **Context Limit**: Very large interview transcripts may need to be summarized before import.

---
*Documentation updated on: 2026-02-14*