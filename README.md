# 🚀 Vibe Coding 開發課程：自然語言驅動的日常工作自動化
### Google Antigravity 2.0 實務應用（中央研究院職員專屬工作坊）

本專案為準備給**中央研究院（Academia Sinica）**全體同仁（涵蓋研究人員、研究助理、專案經理與行政同仁）之內部教育訓練教材庫。透過「純白話、免安裝、看示範」的設計，帶領學員跨越傳統程式語法門檻，掌握以自然語言指揮 AI 代理人（Autonomous Agent）完成日常行政與研究自動化任務的核心技能。

---

## 📌 課程基本資訊

| 項目 | 說明 |
|---|---|
| **課程名稱** | **Vibe Coding 開發課程**（自然語言驅動的日常工作自動化：Google Antigravity 2.0 與 Vibe Coding 實務） |
| **課程時長** | **1.5 小時（90 分鐘）** |
| **授課對象** | 中央研究院全院職員（無程式背景者至具基本程式概念者均適用） |
| **授課方式** | 線上遠端授課（Google Meet 螢幕示範 + 講師解說，學員全程觀摩無須事前安裝） |
| **核心工具** | Google Antigravity 2.0（以 Gemini 3.8 Flash / Pro 為核心大語言模型） |
| **主要產出** | 全套 20 頁可編輯簡報（PPTX / PDF）、90 分鐘教學時程規劃表、示範操作腳本 |

---

## 🎯 課程核心目標

1. **思維翻轉（Mindset Shift）**：理解 Vibe Coding 本質——「用自然語言描述成果，而非記憶瑣碎語法」，建立由「單輪問答」升級為「主動代理人（Agentic Workflow）」的協作認知。
2. **工具駕馭（Tool Mastery）**：熟悉 Antigravity 2.0 三大工作區（左側專案導航、中央對話畫布、右側輔助窗格），掌握 `/` 斜線指令與 `@` 本機資料引用技巧。
3. **場景落地（Real-world Applications）**：透過三大生活化且貼近中研院日常的現場 Live Demo，見證 AI 在檔案管理、數據簡報、定時網路爬蟲上的自動化威力。
4. **資安把關（Security & Governance）**：落實中研院資安與合規底線，堅持 `Plan Review Policy: Always Ask`（動手前先看計畫）與 `Security Preset: Default`（沙箱手動授權），杜絕非預期檔案異動與機密外洩。

---

## ⏱️ 90 分鐘教學節奏規劃 (1.5H)

```
00:00 ─── 引言開場 (Hook)       ( 2 min)  以「擺脫重複機械性工作」切入，免寒暄直接聚焦
02:00 ─── 單元一：觀念建立      (13 min)  什麼是 Vibe Coding？AI 代理人 vs 傳統單輪問答
15:00 ─── 單元二：介面導覽      (12 min)  Antigravity 2.0 工作環境全貌、快捷指令與算力設定
27:00 ─── ☕ 中場微休息         ( 2 min)  緩衝吸收與連線檢查
29:00 ─── 單元三：實務示範      (43 min)  三大日常行政與研究場景 Live 實機操作
          ├─ 示範 A：電腦檔案智慧歸檔 (12 min)
          ├─ 示範 B：問卷 CSV 直出多頁簡報 (15 min)
          └─ 示範 C：政府公開資訊抓取與定時排程 (16 min)
72:00 ─── 單元四：最佳實踐      ( 8 min)  Prompt 四大要素公式（角色+背景+格式+限制）與資安防線
80:00 ─── Q&A 與課後行動總結   (10 min)  本週即可嘗試的一件小工作、交流與諮詢管道
90:00 ─── 課程圓滿結束
```

---

## 📂 專案架構與教材清單

```
c:\workspaces\agy\
├── README.md                           # 本課程總覽與指引文件（本檔）
├── course_plan.md                      # 完整 90 分鐘教學計畫、開場腳本與示範逐字提示詞
├── slide_story.md                      # ⭐️ 20 頁全套簡報逐頁演講故事與講師口述腳本（Slide Story）
├── ui-img/                             # Antigravity 2.0 原生高解析介面截圖庫（10 張）
│   ├── antigravity.png                 # 桌面視窗全景（左欄、中央畫布、輸入框）
│   ├── settings-models.png             # 後台模型配額、Gemini 使用進度與超額防護
│   ├── settings-general2.png           # 計畫審核機制（Plan Review Policy: Always Ask）
│   ├── settings-general-security-preset.png # 沙箱防護等級（Security Preset: Default）
│   └── ...                             # 其他設定、MCP、終端授權截圖
├── demos/                              # ⭐️ 三大實務示範完整測試包與 Prompt 指南
│   ├── demo_a_cleanup/                 # 示範 A：電腦空間清理與檔案整理
│   │   ├── prompt_guide.md             # 講師逐字 Prompt 指南與操作步驟
│   │   └── mock_downloads/             # 內建 17 個涵蓋 2024-2025 年、多副檔名與重複檔之假資料
│   ├── demo_b_slides/                  # 示範 B：簡報製作（Antigravity 原生工作流）
│   │   ├── prompt_guide.md             # 講師逐字 Prompt 指南（大綱規劃 → Python 構建 → 視覺驗收）
│   │   └── sinica_staff_survey.csv     # 150 筆中研院同仁日常痛點與自動化需求調查真實問卷數據
│   └── demo_c_scraper/                 # 示範 C：公開網站資訊抓取與排程
│       ├── prompt_guide.md             # 講師逐字 Prompt 指南（爬取、CSV 匯出與 /schedule 排程）
│       └── mock_portal/                # 本機安全演練網站（10 筆徵件與公告，離線亦可穩定示範）
└── presentation/                       # 課程簡報專案目錄
    ├── presentation.pptx               # ⭐️ 核心交付物：全套 20 頁原生可編輯投影片
    ├── presentation.pdf                # ⭐️ 核心交付物：高解析 20 頁匯出 PDF
    ├── preview-contact-sheet.png       # ⭐️ 20 頁全簡報縮圖聯絡單（供快速審閱）
    ├── slide_story.md                  # ⭐️ 20 頁簡報逐頁演講故事與切換指南
    ├── outline.md                      # 簡報 20 頁大綱架構與各頁視覺規範說明書
    ├── edit-impact.md                  # 簡報修改歷程與架構演進紀錄
    ├── preview/                        # 各頁 high-dpi 獨立 PNG 預覽（slide-01 ~ slide-20）
    ├── assets/ui-img/                  # 簡報內部引用之介面截圖資產庫
    └── src/                            # 簡報原始碼（基於 python-pptx 之工程化架構）
        ├── theme.py                    # 設計系統常數（2pt 格線、中研院暖白配色 #FAF8F4）
        ├── primitives.py               # 向量形狀、文字框與高亮加框組件庫
        ├── build.py                    # 簡報構建主腳本
        └── slides/                     # 模組化投影片程式碼（slide01.py ~ slide20.py）
```

---

## 🖥️ 簡報亮點設計（針對 Google Meet 遠端視認性優化）

為克服遠端視訊會議（Google Meet）常見的模糊與字體過小問題，本簡報遵循「**總覽 + 詳解**」的 20 頁專業工程敘事結構：

1. **重點控制項大圖化展示（獨立 Slide）**：
   - 包含 **原生介面全景 (Slide 08)**、**算力配額監控 (Slide 10)**、**計畫審核設定 (Slide 18)** 與 **安全沙箱等級 (Slide 19)**。
   - 單張截圖佔據投影片 60%~65% 面積，控制項標籤清晰可辨。
2. **高對比向量標註加框**：
   - 以高明度橘色與紅色原生線條框選目標按鈕與設定卡片，並搭配微章指示（如 `★ 關鍵設定：Plan Review Policy = Always Ask`），引導學員視覺焦點。
3. **伴隨式解析面板**：
   - 截圖右側搭配暖象牙白（`#F4EFE6`）說明卡片，透過原生單一文字流自動排版，層次分明、無文字擠壓與穿透現象。
4. **真實 Antigravity 原生簡報工作流 (Slide 13)**：
   - 示範 B 完整解構「資料脈絡注入 (`@資料`) → 大綱規格規劃 (`/plan outline.md`) → Python 程式原生構建 (`python-pptx`) → 視覺彩現全覽驗收 (PNG 預覽 + 聯絡單 + PDF)」的專業級工程代理人流程。

---

## 🛠️ 講師快速上手與操作指引

### 1. 簡報投影與觀摩
- **開課前**：建議直接以 PowerPoint 開啟 `presentation/presentation.pptx` 或使用 PDF 閱讀器開啟 `presentation/presentation.pdf` 進入全螢幕播放模式。
- **螢幕分享建議**：在 Google Meet 中以「**單一視窗（Window）**」方式分享簡報，切換至 Antigravity 2.0 實機操作時則切換至 Antigravity 主應用程式視窗，確保文字串流清晰度最高。

### 2. 實機操作（Live Demo）即用示範包
本專案已為講師備妥隨開即用的完整測試數據與示範腳本，位於 `demos/` 目錄：
- **示範 A（電腦空間清理）**：參考 [demos/demo_a_cleanup/prompt_guide.md](file:///C:/workspaces/agy/demos/demo_a_cleanup/prompt_guide.md)，對象為內建 17 個假檔案的 `mock_downloads/` 目錄。
- **示範 B（簡報製作工作流）**：參考 [demos/demo_b_slides/prompt_guide.md](file:///C:/workspaces/agy/demos/demo_b_slides/prompt_guide.md)，注入 150 筆真實同仁問卷 `sinica_staff_survey.csv`。
- **示範 C（公開資訊爬取與排程）**：參考 [demos/demo_c_scraper/prompt_guide.md](file:///C:/workspaces/agy/demos/demo_c_scraper/prompt_guide.md)，可直接讀取本機離線安全入口 `mock_portal/bulletin_portal.html`，展示爬取與 `/schedule` 自動化排程。

### 3. 本地維護與重新構建
若日後需調整簡報內容或字體配色，可在安裝相依套件後執行：
```powershell
# 重新構建 PPTX 簡報
python presentation/src/build.py

# 匯出各頁高解析預覽圖（需本機 Microsoft PowerPoint）
powershell -ExecutionPolicy Bypass -File "presentation/render_ppt_com.ps1"

# 重新匯出 PDF
powershell -ExecutionPolicy Bypass -File "presentation/convert_ppt_to_pdf.ps1" -Deck "presentation/presentation.pptx" -Pdf "presentation/presentation.pdf"
```

---

## 📋 課後資源與支援

- **官方文件**：[Google Antigravity Documentation](https://antigravity.google/docs)
- **實務 Prompt 範本**：參考 `course_plan.md` 中的四大要素示範句型
- **諮詢交流**：中研院內部技術與 AI 自動化交流社群
