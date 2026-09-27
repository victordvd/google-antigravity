# Presentation Specification

## Presentation Brief

- Working Title: 自然語言驅動的日常工作自動化：Google Antigravity 2.0 與 Vibe Coding 實務
- User Request: /make-ppt (中研院職員 90 分鐘遠端授課簡報規劃，結合真實 Antigravity UI 大圖高亮解析)
- Cost Mode: standard
- Direction Lock: 面向中研院多元背景職員，以「自然語言驅動 AI 代理人」為主軸，透過免安裝觀摩與三大日常工作場景（檔案整理、簡報生成、網路爬蟲）示範 Vibe Coding 即學即用能力；UI 環節採「總覽卡片 + 獨立大圖高亮解析」雙層結構，確保遠端會議清晰易讀。
- Audience: 中央研究院職員（包含研究員、研究助理、專案助理與行政人員，技術背景涵蓋無程式經驗至具基本基礎者）
- Presentation Goal: 建立學員對 Vibe Coding 與 AI 代理人的實務認知，掌握 Antigravity 2.0 介面與功能，並建立在日常研究與行政工作中嘗試使用 AI 代理人的信心
- Presentation Context: 線上遠端授課（Google Meet），講師螢幕示範，學員觀摩（簡報投影需極高字體與控制項辨識度）
- Language: 台灣繁體中文（zh-TW；保留自然英文技術詞）
- Expected Duration: 90 min（含 43 分鐘螢幕操作示範）
- User Requested Slide Count: 未指定（由 90 分鐘時長與「一張圖一個 slide」遠端易讀性要求推定）
- Actual Planned Slide Count: 20
- Assumptions: 學員不需事前安裝環境，簡報作為觀念鋪陳、示範情境引導與規範提示，核心操作以即時螢幕分享進行；簡報需具備清晰的步驟感與高可讀性提示作用
- Source Inventory: `course_plan.md` → 核心授課大綱、教學目標與示範腳本 · 權威最高
- Source Conflicts: 無衝突

## Narrative Strategy

Start directly with the friction of repetitive administrative and research tasks. Introduce Vibe Coding not as a programmer-only paradigm, but as natural language delegation to an autonomous agent. Tour the Antigravity 2.0 workspace to demystify how the agent plans, executes, and confirms changes, backed by dedicated large-scale screenshots with native callout badges. Anchor learning in three progressive live demonstrations (file management, slide deck creation, automated web scraping). Conclude with practical prompt formulas and essential governance rules (data safety, plan review) backed by direct settings screenshots so attendees leave equipped to experiment safely.

## Golden Circle Lens

- Why: 院內研究與行政同仁每日耗費大量時間於檔案整理、格式調整、重複資料搜集等機械性工作，傳統寫程式門檻高，而單問單答式 AI 無法跨步驟執行複雜任務。
- How: 透過 Vibe Coding 與 Antigravity 2.0 代理人模式，以自然語言描述目標，由 AI 主動拆解步驟、調用工具並回報透明歷程，將人機協作轉為「指示與檢閱」。
- What: 掌握 Antigravity 2.0 三大工作區與指令技巧，落地應用於電腦檔案整理、簡報大綱製作、公開資料爬蟲與排程，並落實 4 大 Prompt 要件與資安檢核。
- Natural Engineering Angle: 清楚劃分「委託給 AI」與「人工驗收確認」的責任邊界，強調計畫確認與安全沙箱，拒絕未經審查的檔案變更與敏感資料外洩。

## Core Narrative

機械性日常工作耗時 → 傳統學程式門檻高、傳統 AI 只能問答 → Vibe Coding 轉換為「用白話描述結果」→ Antigravity 2.0 提供代理人規劃與執行平台（總覽 + 大圖導覽 + 配額設定）→ 三大實務示範驗證日常可行性 → 掌握 Prompt 技巧與防護邊界（總覽 + 計畫審核實體設定 + 沙箱隔離實體設定）→ 立即上手提升效率

## Narrative Review

- Status: Pass

## Content Tone

technical · factual · concise · evidence-oriented · direct · implementation-grounded · natural engineering language · register: sharing with 同仁 — plain declarative, never a hosted session

## Deck Context Line

中研院職員訓練 / Antigravity 2.0 & Vibe Coding

## Cover Variant

`editorial-light` — technical/practical workshop share. Subtitle included, Footer Highlight omitted.

## Design System

- Canvas: 16:9 (13.333" × 7.5")
- Background: #FAF8F4 warm off-white; dark slides #1A1714
- Primary Text: #1A1714 / body #4A443D
- Primary Accent: #D75F00 orange (emphasis device only)
- Success Semantic: #3E8E5A · Risk Semantic: #C13227 · Information Semantic: #3972DA
- Muted Semantic: #8A8177
- Eyebrow Style: `// NN    label`, mono, orange, upper-left
- Title Style: bold editorial argument, phrase-level orange emphasis
- Supporting Sentence Style: muted gray, key phrase bolded in ink
- Body Typography: Noto Sans TC / Microsoft JhengHei
- Mono Typography: Consolas / Courier New
- Line Style: hairline #DED8CE 1pt; accent rules #D75F00 2.25pt
- Takeaway Line Style: optional and default-off; orange rule + bold concrete implication
- Spacing Principles: 0.62" page margins; header zone ends with hairline ~2.2–2.3"; working area extends to bottom margin
- Native Table Style: one editable PowerPoint table object; dark header, warm-white body, 1pt hairlines, 16pt header / 14pt body, no shadow
- Cover Style: `editorial-light` via `add_cover_slide()`

## Global Content Constraints

- Visible content in Taiwan Traditional Chinese (`zh-TW`); follow `taiwan-language-guide.md` and preserve natural technical English (Antigravity, Vibe Coding, Artifacts, Terminal, Mention, Slash Commands, Prompt, CSV, PDF, Google Meet, Google Slides).
- No marketing slogans, decorative filler, or empty visionary claims.
- Concrete nouns, active verbs, process-oriented framing.

## Slide Architecture

01 — Opening — 建立主題：自然語言驅動日常工作自動化
02 — Agenda — 90 分鐘架構：觀念、介面、實務示範到最佳實踐
03 — Section Divider — 單元一：觀念建立：從手刻語法到對話式編程
04 — Contrast — Vibe Coding 本質：描述「成果」而非「步驟」
05 — Mechanism — 協作典範轉移：從單輪問答到主動代理人
06 — Section Divider — 單元二：介面導覽：Antigravity 2.0 核心工作環境
07 — Layout — 三大核心工作區：管理、對話與產出歷程完全透明（架構總覽卡片）
08 — Interface Deep Dive — 原生介面全貌導覽：導航側欄、對話畫布與提示詞輸入框（大圖高亮解析：antigravity.png）
09 — Mechanism — 斜線指令與 @ 引用：精準傳遞上下文是成功協作的關鍵
10 — Settings Deep Dive — 後台設定：模型配額與算力掌控：掌握 Gemini 週期額度與費用邊界（大圖高亮解析：settings-models.png）
11 — Section Divider — 單元三：實務示範：日常行政與研究的三大落地場景
12 — Process — 示範 A：雜亂檔案智慧歸檔，變更前一律先看清單
13 — Process — 示範 B：從原始資料到多頁簡報，以對話迭代格式與視覺
14 — Process — 示範 C：公開網站資訊抓取與排程，免寫程式碼也能定期追蹤
15 — Section Divider — 單元四：最佳實踐：下好 Prompt 與防護安全邊界
16 — Guideline Table — 提示詞四大關鍵要素：給足角色、背景、格式與限制
17 — Governance — 代理人協作的三大防線：計畫審核、資料隔離與結果查驗（防禦架構卡片）
18 — Governance Deep Dive 1 — 防線一實體設定：計畫審核機制：以 Always Ask 阻斷非預期檔案異動（大圖高亮解析：settings-general2.png）
19 — Governance Deep Dive 2 — 防線二實體設定：安全沙箱等級：堅守 Default 預設沙箱防護隔離（大圖高亮解析：settings-general-security-preset.png）
20 — Next Steps — 從一件小工作開始嘗試：課後資源與實踐清單

---

## Slide 01 — 自然語言驅動日常工作自動化

### Slide Role
Title Slide

### Purpose
Establish the session identity, core theme, and practical perspective for Academia Sinica colleagues.

### Eyebrow
中研院職員訓練 / Antigravity 2.0 & Vibe Coding

### Title
自然語言驅動的日常工作自動化：Google Antigravity 2.0 與 Vibe Coding 實務

### Title Emphasis
`日常工作自動化`

### Supporting Sentence
中央研究院職員實務工作坊 · 90 分鐘全流程解構與三大工作場景示範

### Visual Form
editorial-light (Title Slide)

---

## Slide 02 — 從思維翻轉到實務落地的 90 分鐘節奏

### Slide Role
Agenda

### Purpose
Lay out the four clear units of the workshop with estimated durations.

### Eyebrow
// 00    AGENDA

### Title
從思維翻轉到實務落地的 90 分鐘節奏

### Title Emphasis
`90 分鐘節奏`

### Supporting Sentence
跳過繁瑣環境設定，以**即時螢幕操作示範**為核心，完整走過觀念理解至成果驗收。

### Visual Form
four-column-process-cards

---

## Slide 03 — 單元一：觀念建立

### Slide Role
Section Divider

### Purpose
Transition into Unit 1: understanding the shift from manual coding to conversational delegation.

### Eyebrow
// 01    CONCEPT

### Title
觀念建立：從手刻語法到對話式編程

### Title Emphasis
`從手刻語法`、`對話式編程`

### Supporting Sentence
Vibe Coding 核心思維：用自然語言描述成果而非死背語法；人機協作典範轉移：從單純問答文字建議升級為主動代理人。

### Visual Form
section-divider

---

## Slide 04 — Vibe Coding 本質：描述「成果」而非「步驟」

### Slide Role
Contrast

### Purpose
Dispel fear of programming among non-technical staff by defining Vibe Coding clearly.

### Eyebrow
// 01    CONCEPT

### Title
Vibe Coding 的本質：用自然語言描述「成果」而非「步驟」

### Title Emphasis
`自然語言描述`

### Supporting Sentence
傳統開發要求**精確語法**；對話式編程只需給予**目標限制與驗收標準**。

### Visual Form
two-column-comparison-table (Traditional Coding vs Vibe Coding)

---

## Slide 05 — 協作典範轉移：從單輪問答到主動代理人

### Slide Role
Mechanism

### Purpose
Differentiate simple LLM chat assistants from autonomous AI agents.

### Eyebrow
// 01    CONCEPT

### Title
從單輪問答到主動代理人：AI 負責拆解步驟與執行

### Title Emphasis
`主動代理人`

### Supporting Sentence
代理人模式具備**感知、規劃、執行與修正**的完整循環，將單純諮詢轉化為具體行動。

### Visual Form
two-column-contrast-cards (Chat Assistant vs Autonomous Agent)

---

## Slide 06 — 單元二：介面導覽

### Slide Role
Section Divider

### Purpose
Transition into Unit 2: walking through Antigravity 2.0 interface components.

### Eyebrow
// 02    INTERFACE

### Title
工具駕馭：Antigravity 2.0 核心介面導覽

### Title Emphasis
`核心介面導覽`

### Supporting Sentence
在動手前先看清儀表板：側邊欄管理專案、主畫布進行對話、輔助窗格掌控所有真實變更。

### Visual Form
section-divider

---

## Slide 07 — 三大核心工作區：管理、對話與產出歷程完全透明

### Slide Role
Layout Overview

### Purpose
Provide a clean structural overview of the 3 major functional zones before diving into screenshots.

### Eyebrow
// 02    INTERFACE

### Title
三大核心工作區：管理、對話與產出歷程完全透明

### Title Emphasis
`三大核心工作區`

### Supporting Sentence
不需開啟終端機或編輯器，所有操作在**單一桌面視窗**內即可完整監控。

### Visual Form
three-column-cards (Sidebar / Chat Canvas / Auxiliary Pane)

---

## Slide 08 — 原生介面全貌導覽：導航側欄、對話畫布與提示詞輸入框

### Slide Role
Interface Deep Dive

### Purpose
Present a high-resolution, large-scale view of the real Antigravity 2.0 desktop workspace (`antigravity.png`) with orange highlight boxes and companion explanation notes.

### Eyebrow
// 02    INTERFACE

### Title
原生介面全貌導覽：導航側欄、對話畫布與提示詞輸入框

### Title Emphasis
`原生介面全貌導覽`

### Supporting Sentence
真實桌面環境一覽：**左側專案管理、中央發布目標**，底部輸入列直接調用快捷指令與切換模型。

### Visual Form
annotated-large-screenshot + companion explanation panel

### Layout
- Left (65% width): `antigravity.png` large screenshot
  - Callout ①: Orange highlight box around Left Sidebar (`New Conversation`, `Projects`, `Scheduled Tasks`)
  - Callout ②: Orange highlight box around Prompt Input Bar (`/`, `@`, Model Selector)
- Right (35% width): Warm ivory companion card (`UI BREAKDOWN`) mapping control positions and practical usage.

---

## Slide 09 — 斜線指令與 @ 引用：精準傳遞上下文是成功協作的關鍵

### Slide Role
Mechanism

### Purpose
Detail how to leverage `/` (Slash Commands) and `@` (Context Mentions) to streamline prompt workflows.

### Eyebrow
// 02    INTERFACE

### Title
斜線指令與 @ 引用：精準傳遞上下文是成功協作的關鍵

### Title Emphasis
`精準傳遞上下文`

### Supporting Sentence
善用內建快捷語法，將**特定作業流程**與**本地檔案資訊**無縫送入模型。

### Visual Form
two-column-cards (Slash Commands `/` vs Context Mentions `@`)

---

## Slide 10 — 後台設定：模型配額與算力掌控：掌握 Gemini 週期額度與費用邊界

### Slide Role
Settings Deep Dive

### Purpose
Examine real backend settings (`settings-models.png`) for Gemini quotas and billing protections at full scale.

### Eyebrow
// 02    INTERFACE

### Title
後台設定：模型配額與算力掌控：掌握 Gemini 週期額度與費用邊界

### Title Emphasis
`模型配額與算力掌控`

### Supporting Sentence
依任務複雜度切換模型，透過後台即時掌握**5 小時與每週使用額度**，並開啟超額防護避免額外費用。

### Visual Form
annotated-large-screenshot + companion explanation panel

### Layout
- Left (58% width): `settings-models.png` large screenshot
  - Callout ②: Red highlight box around `Enable AI Credit Overages` toggle switch with badge pill
  - Callout ①: Orange highlight box around `Gemini Models` 5-hour and weekly quota meters with badge pill
- Right (42% width): Companion explanation card detailing quota cycles, Flash vs Pro division, and billing safeguards.

---

## Slide 11 — 單元三：實務示範

### Slide Role
Section Divider

### Purpose
Transition into Unit 3: three live demonstrations in Academia Sinica scenarios.

### Eyebrow
// 03    DEMO

### Title
實務示範：日常行政與研究的三大落地場景

### Title Emphasis
`三大落地場景`

### Supporting Sentence
示範 A：電腦檔案智慧歸檔 · 示範 B：原始資料直接生成多頁簡報 · 示範 C：公開網站資訊抓取與定時排程。

### Visual Form
section-divider

---

## Slide 12 — 示範 A：雜亂檔案智慧歸檔，變更前一律先看清單

### Slide Role
Process Demo

### Purpose
Showcase automated sorting of Downloads/desktop files by extension and year, enforcing plan inspection before moving.

### Eyebrow
// 03    DEMO

### Title
示範 A：雜亂檔案智慧歸檔，變更前一律先看清單

### Title Emphasis
`雜亂檔案智慧歸檔`

### Supporting Sentence
以 Downloads 資料夾為例，依據**檔案類型與年份**建立結構，並透過審查確認杜絕誤刪風險。

### Visual Form
four-step-horizontal-pipeline (容量類型盤點 → 結構架構確認 → 安全批次歸檔 → 重複清理釋放)

---

## Slide 13 — 示範 B：從原始資料到多頁簡報，以對話迭代格式與視覺

### Slide Role
Process Demo

### Purpose
Demonstrate transforming CSV survey data into a multi-slide presentation via conversational iterations.

### Eyebrow
// 03    DEMO

### Title
示範 B：從原始資料到多頁簡報，以對話迭代格式與視覺

### Title Emphasis
`從原始資料到多頁簡報`

### Supporting Sentence
將問卷分析與專案報告轉化為**結構化簡報**，直接在對話中微調圖表並匯出至投影片。

### Visual Form
four-step-horizontal-pipeline (資料脈絡輸入 → 結構大綱生成 → 對話持續迭代 → 原生格式匯出)

---

## Slide 14 — 示範 C：公開網站資訊抓取與排程，免寫程式碼也能定期追蹤

### Slide Role
Process Demo

### Purpose
Demonstrate building an automated web scraping workflow targeting public government open data without writing code.

### Eyebrow
// 03    DEMO

### Title
示範 C：公開網站資訊抓取與排程，免寫程式碼也能定期追蹤

### Title Emphasis
`公開網站資訊抓取與排程`

### Supporting Sentence
以**政府公開資料網站**為例，自動擷取公告清單並設定每週定時更新，告別手動複製貼上。

### Visual Form
four-step-horizontal-pipeline (目標與欄位定義 → 爬蟲工具自主執行 → 結構表格呈現 → 背景定時自動化)

---

## Slide 15 — 單元四：最佳實踐與安全防護

### Slide Role
Section Divider

### Purpose
Transition into Unit 4: prompt engineering standards and human-in-the-loop security governance.

### Eyebrow
// 04    BEST PRACTICES

### Title
治理守則：下好 Prompt 與防護安全邊界

### Title Emphasis
`治理守則`、`安全邊界`

### Supporting Sentence
Prompt 四大關鍵要素：給足角色、背景、格式與限制；代理人協作的三大防線：計畫審核、機密資料隔離與結果人工覆核。

### Visual Form
section-divider

---

## Slide 16 — 提示詞四大關鍵要素：給足角色、背景、格式與限制

### Slide Role
Guideline Table

### Purpose
Provide a concrete, actionable prompt formula that staff can apply immediately across administrative and research tasks.

### Eyebrow
// 04    BEST PRACTICES

### Title
提示詞四大關鍵要素：給足角色、背景、格式與限制

### Title Emphasis
`四大關鍵要素`

### Supporting Sentence
擺脫「幫我整理資料」的無效指令，用**四維度結構**讓 AI 第一次就能精準交付合規成果。

### Visual Form
native-table (4 columns: 要素, 核心意義, 不佳示範, 推薦示範)

---

## Slide 17 — 代理人協作的三大防線：計畫審核、資料隔離與結果查驗

### Slide Role
Governance Architecture

### Purpose
Introduce the three structural defense lines protecting data integrity and system safety before deep diving into physical UI settings.

### Eyebrow
// 04    BEST PRACTICES

### Title
代理人協作的三大防線：計畫審核、資料隔離與結果查驗

### Title Emphasis
`三大防線`

### Supporting Sentence
在充分享受自動化便利的同時，必須確保**資安合規**與**學術資料嚴謹性**，築牢風險防線。

### Visual Form
three-column-cards (防線 01 永遠先確認計畫再放行 / 防線 02 機密與個人隱私嚴格隔離 / 防線 03 產出資料引用人工查驗)

---

## Slide 18 — 防線一實體設定：計畫審核機制：以 Always Ask 阻斷非預期檔案異動

### Slide Role
Governance Deep Dive 1

### Purpose
Present a high-resolution, annotated view of `settings-general2.png` proving how to enforce `Plan Review Policy = Always Ask` in the software.

### Eyebrow
// 04    BEST PRACTICES

### Title
防線一實體設定：計畫審核機制：以 Always Ask 阻斷非預期檔案異動

### Title Emphasis
`計畫審核機制`

### Supporting Sentence
在動手前先看計畫：將**Plan Review Policy 設為 Always Ask**，杜絕任何未經確認的本機檔案覆蓋與刪除。

### Visual Form
annotated-large-screenshot + companion explanation panel

### Layout
- Left (58% width): `settings-general2.png` large screenshot
  - Callout: Orange highlight box around `Plan Review Policy: Always Ask` setting card with badge pill on top right
- Right (42% width): Companion explanation panel detailing `Always Ask` safeguards, `/plan` command best practices, and Academia Sinica compliance rules.

---

## Slide 19 — 防線二實體設定：安全沙箱等級：堅守 Default 預設沙箱防護隔離

### Slide Role
Governance Deep Dive 2

### Purpose
Present a high-resolution, annotated view of `settings-general-security-preset.png` highlighting the `Security Preset: Default` dropdown menu and danger of unrestricted execution.

### Eyebrow
// 04    BEST PRACTICES

### Title
防線二實體設定：安全沙箱等級：堅守 Default 預設沙箱防護隔離

### Title Emphasis
`安全沙箱等級`

### Supporting Sentence
把守資安邊界：將**Security Preset 維持為 Default**，所有終端指令與跨目錄檔案存取皆需人工逐條審查。

### Visual Form
annotated-large-screenshot + companion explanation panel

### Layout
- Left (58% width): `settings-general-security-preset.png` large screenshot
  - Callout: Red highlight box around the `[Default, Full machine, Turbo mode, Custom]` popup menu with badge pill aligned cleanly above
- Right (42% width): Companion explanation panel highlighting the 4 presets, the dangers of Full Machine / Turbo mode, and strict prohibition under Academia Sinica IT guidelines.

---

## Slide 20 — 從一件小工作開始嘗試：課後資源與實踐清單

### Slide Role
Next Steps & Practical Checklist

### Purpose
Provide immediate, concrete next steps and official references for colleagues to begin experimenting safely post-workshop.

### Eyebrow
// 04    ACTION

### Title
從一件小工作開始嘗試：課後資源與實踐清單

### Title Emphasis
`一件小工作開始`

### Supporting Sentence
AI 代理人的協作技能唯有在**實際操作中內化**；善用院內資源與提示詞模板，本週就能啟動第一次嘗試。

### Visual Form
two-column-cards (左欄：本週即可落地的三步行動 / 右欄：延伸學習文件與諮詢管道)
