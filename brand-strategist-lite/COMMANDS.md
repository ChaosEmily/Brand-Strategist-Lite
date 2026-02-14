# Brand Strategist Lite - Command Reference (指令速查表)

此文件列出了所有可用的 AI 指令及其功能。您可以在對話框中直接輸入這些指令（Slash Command）來操作系統。

## 📥 資料輸入指令 (Data Input)

| 指令 | 功能 | 說明 |
| :--- | :--- | :--- |
| **/add-competitor** | **新增競品** | 引導您輸入競爭對手的名稱與網址，並自動更新設定檔。 |
| **/add-interview** | **匯入訪談** | 上傳用戶訪談資料。支援直接貼上文字或讀取檔案（Word/Text/Markdown）。 |
| **/add-brand-info** | **匯入品牌資訊** | 設定您自己的品牌使命、價值觀與產品介紹。支援檔案匯入。 |

---

## ⚡ 分析與生成指令 (Analysis & Strategy)

| 指令 | 功能 | 說明 |
| :--- | :--- | :--- |
| **/brand-run** | **🚀 一鍵全自動生成** | **推薦使用**。**自動檢查資料完整性**，執行 3C 全流程：用戶分析($W_u$) -> 競品分析($S_c$) -> 策略生成。 |
| **/brand-user** | 用戶洞察分析 | **自動檢查訪談資料**。僅執行第一階段：分析訪談筆記，產出 User Insights Report ($W_u$)。 |
| **/brand-comp** | 競品分析 | **自動檢查競品網址**。僅執行第二階段：支援最多 3 個品牌並行給分，產出 Competitor Analysis Matrix。 |
| **/brand-strat** | 策略制定 | **自動檢查前兩份報告**。僅執行第三階段：根據 3C 交點，產出 Final Brand Strategy。 |
| **/archive-reports** | **存檔報告** | 將目前的分析報告移動到帶有時間戳記的 `archive/` 資料夾中。 |

---

## 💡 使用小技巧 (Tips)

1.  **檔案路徑**：在使用 `/add-interview` 或 `/add-brand-info` 時，如果 AI 詢問檔案路徑，請提供完整的絕對路徑（例如：`d:/files/my_interview.docx`）。
2.  **自動檢查**：現在執行上述分析指令前，系統會自動檢查資料是否齊全。如果不齊全（例如沒加競品），系統會提示您先去補資料，不用擔心白跑一趟。
