# 📋 Google Antigravity 2.0 實務工作坊待辦清單 (TODO)

> **課程名稱**：自然語言驅動的日常工作自動化：Google Antigravity 2.0 與 Vibe Coding 實務  
> **受眾對象**：中央研究院行政人員、研究助理、技術人員（約 60 人，遠端 Google Meet）  
> **課程時長**：90 分鐘（含 43 分鐘實機操作示範與 Q&A）  
> **最後更新**：2026-09-28  

---

## 📌 進度總覽 (Progress Overview)

- [x] **課程整體規劃**：`course_plan.md` 大綱、時間分配、教學目標與講義結構完成。
- [x] **21 頁演講逐字講稿**：`slide_story.md` 四大樂章、21 頁講稿、焦點指引與轉場詞完備。
- [x] **投影片程式化架構**：`presentation/src/slides/slide01~21.py` 全數建置完成。
- [x] **4 大核心設定截圖**：主介面、模型配額、Always Ask、Default 沙箱已配置並高亮標註。
- [x] **三大 Demo 實戰腳本**：清理、做簡報、爬蟲之資料集與 Prompt 指引全數就位。
- [ ] **選配素材與備援強化**：產出中介面全景、快捷選單特寫、Demo 靜態成果備援圖。
- [ ] **課前演練與環境測試**：時間控制測試（43 分鐘 Demo）、Meet 錄音/分享測試。

---

## 🎨 1. 簡報製作與視覺素材 (Presentation & Assets)

### 投影片核心架構
- [x] 建立 21 頁 Slide 原始碼檔案（`presentation/src/slides/slide01.py` ~ `slide21.py`）
- [x] 納入 Slide 17「能力擴充生態（Skills、MCP、Plugins）」架構卡片
- [x] 重新調整章節結構與頁碼，確保編號與大綱一致（`presentation/outline.md`）
- [x] 編譯產出最新版 `presentation/presentation.pptx` 與 `presentation/presentation.pdf`

### 現有核心截圖配置
- [x] **Slide 01（封面）**：向量標誌與原生 Icon（`presentation/assets/antigravity-icon.png`）
- [x] **Slide 08（介面導覽）**：桌面軟體全景視窗（`ui-img/antigravity.png` + 雙原生標籤）
- [x] **Slide 10（模型額度）**：Gemini 算力與配額防線（`ui-img/settings-models.png` + 高亮紅框標籤）
- [x] **Slide 19（防線一）**：計畫審核設定（`ui-img/settings-general2.png` + Always Ask 高亮框）
- [x] **Slide 20（防線二）**：沙箱防護隔離（`ui-img/settings-general-security-preset.png` + Default 高亮框）

### 🌟 選配加分素材（進度追蹤）
- [x] **Slide 08 替換昇華**：已收到 `ui-img/antigravity-right-pane.png`（對話進行中＋右側同時展開 Artifacts 簡報預覽與 Files Changed 異動面板，完美展示三大工作區）。
- [x] **Demo C / Slide 14 排程實機佐證**：已收到 `ui-img/schedule.png`（Scheduled Tasks 建立定時任務「晨間新聞」對話框，可直接作為排程功能實機展示）。
- [ ] **Slide 09 圖文補充**：在對話輸入框輸入 `/`（跳出 `/plan`、`/goal` 等快捷選單）或 `@`（跳出檔案引用選單）的特寫截圖（選配）。
- [ ] **Slide 17 實體佐證**：截取 `Settings` ➔ `Customizations` 分頁畫面（或 `Tool Permissions` ➔ `MCP Tools` 視窗），強化生態落地感（選配）。
- [ ] **Slide 21 課後行動**：製作並置入課後回放錄影／雲端資料夾的 **QR Code 圖檔**（選配）。
- [ ] **更新預覽圖冊**：將 `presentation/preview/slide-01~21.png` 全數重新導出為最新 21 頁高解析預覽圖。

---

## 💻 2. 三大實務示範準備 (Live Demos & Fallback)

### Demo A：雜亂檔案智慧歸檔（時長：5–6 min）
- [x] 準備假資料目錄：`demos/demo_a_cleanup/mock_downloads/`（含各式 PDF、Excel、大型壓縮檔、圖片、雜項快取）
- [x] 撰寫提示詞操作指引：`demos/demo_a_cleanup/prompt_guide.md`
- [ ] **實機預演**：演練「先列清單確認再搬移」的節奏，確保 AI 在沙箱中執行順暢。
- [ ] **備援截圖**：截取整理完成後的檔案樹與異動對照表，作為網路延遲時的備用投影片。

### Demo B：問卷 CSV 產出多頁簡報（時長：20 min · 核心重頭戲）
- [x] 準備脫敏調查資料：`demos/demo_b_slides/sinica_staff_survey.csv`（中研院職員 AI 工具使用調查）
- [x] 撰寫分步提詞指引：`demos/demo_b_slides/prompt_guide.md`（資料探索 ➔ 交叉分析 ➔ 產出 Artifacts 簡報 ➔ 樣式微調）
- [ ] **實機預演**：測試由 Antigravity 2.0 自主撰寫程式碼並渲染 Artifacts 預覽視窗的時間。
- [ ] **備援產出檔**：先在本地保留一份生成好的投影片檔案或截圖，以防生成超時。

### Demo C：公開網站爬蟲與排程追蹤（時長：17 min）
- [x] 準備本機模擬網站：`demos/demo_c_scraper/mock_portal/bulletin_portal.html`（避免外網連線受阻或政府網站改版）
- [x] 撰寫爬蟲提示詞引導：`demos/demo_c_scraper/prompt_guide.md`（結構解析 ➔ 抓取 ➔ 排程 `/schedule`）
- [ ] **實機預演**：測試 Agent 內建瀏覽器（Browser Tool）解析本機 HTML 與定時排程指令。
- [ ] **備援截圖**：截取爬蟲整理出的摘要表格與排程設定畫面。

---

## 🎙️ 3. 講師課前技術與行政清單 (Pre-Flight Checklist)

### 課前 1 天準備
- [ ] **Google Meet 測試**：
  - [ ] 確認 Meet 會議室已開啟錄影權限（已關聯 Google Drive）。
  - [ ] 測試螢幕分享（確認可清晰顯示 Antigravity 視窗與投影片字體）。
  - [ ] 螢幕解析度調整：建議切換為 1080p 並設定 125%~150% 系統縮放，確保遠端學員看清程式碼與終端文字。
- [ ] **Antigravity 軟體環境**：
  - [ ] 確認軟體已更新至 2.0 最新版本且登入正常。
  - [ ] 檢查 Gemini 模型配額可用狀態（避免課中觸發 Quota Exceeded）。
  - [ ] 檢查本機沙箱權限：確認已設定為 `Security Preset: Default` 與 `Plan Review: Always Ask`。
- [ ] **示範環境還原**：
  - [ ] 確認 `mock_downloads` 處於未整理的初始雜亂狀態。
  - [ ] 清理上一輪測試留下的暫存檔案與快取。

### 課前 30 分鐘（上線前）
- [ ] 關閉無關應用程式、個人通訊軟體（Line、Slack、Email），避免彈出隱私通知。
- [ ] 開啟 Google Meet 提早 15 分鐘進場，確認麥克風音質與視訊背景。
- [ ] 在投影螢幕左側放置 Antigravity 2.0 視窗，右側放置示範指引或講稿備忘錄。
- [ ] 開啟 Google Meet 聊天室發言權限，提示同仁可在示範過程中隨時留言提問。

---

## 📦 4. 課後學員交付資源包 (Post-Workshop Delivery Package)

- [ ] **講義導出**：提供學員無動畫之完整版簡報 PDF（`presentation/presentation.pdf`）。
- [ ] **Prompt 快速手冊**：將 `course_plan.md` 的「四大要素公式」與 3 個場景模板整理為單頁 PDF/Markdown 範本卡。
- [ ] **錄影連結發布**：將 Google Meet 錄製之影片上傳至院內共用雲端硬碟，並設定同仁存取權限。
- [ ] **課後滿意度與需求問卷**：收集同仁對於後續進階課程（如 Skills 撰寫、MCP 整合）之意願反饋。

---

## 🔄 5. 專案版本控制 (Repository Hygiene)

- [ ] 檢查目前的 Git 暫存區（Staged changes）：確認 21 頁 PPTX/PDF、`slide_story.md`、`course_plan.md` 與新素材皆已妥善追蹤。
- [ ] 執行 Commit 提交（訊息建議：`docs: update presentation to 21 slides, add slide story and todo checklist`）。
- [ ] 推送最新進度至遠端儲存庫（`git push origin main`）。
