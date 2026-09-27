# slide05.py — Mechanism Slide: Single-turn Chat vs. Agentic Workflow

from pptx.util import Inches, Pt
from pptx.enum.text import PP_ALIGN
import theme as T
import primitives as P

def build(prs, slide):
    P.add_background(slide)
    P.add_eyebrow(slide, 1, "CONCEPT")

    title_segments = [
        ("從單輪問答到", {}),
        ("主動代理人", {"color": T.ORANGE}),
        ("：AI 負責拆解步驟與執行", {}),
    ]
    P.add_argument_title(slide, title_segments, y=T.TITLE_Y)

    support_segments = [
        ("代理人模式具備", {}),
        ("感知、規劃、執行與修正", {"color": T.INK, "bold": True}),
        ("的完整循環，將單純諮詢轉化為具體行動。", {}),
    ]
    P.add_supporting_sentence(slide, support_segments, y=Inches(1.58))
    P.add_hairline(slide, Inches(2.2))

    panel_w = Inches(5.88)
    panel_gap = Inches(0.33)
    panel_y = Inches(2.55)
    panel_h = Inches(4.35)

    # Left Panel: 傳統問答式 AI
    left_x = T.MARGIN_X
    P.add_panel(slide, left_x, panel_y, panel_w, panel_h, fill=T.PANEL_BG, line=T.PANEL_LN)

    P.add_status_pill(slide, left_x + Inches(0.24), panel_y + Inches(0.24), "傳統問答式 AI",
                      bg=T.MUTED, fg=T.ON_DARK, w=Inches(1.6), h=Inches(0.28), size=11)

    tb_lt, tf_lt = P.textbox(slide, left_x + Inches(0.24), panel_y + Inches(0.68), panel_w - Inches(0.48), Inches(0.55))
    P.rich_par(tf_lt, [("「只說不做」的諮詢顧問模式", {"color": T.INK, "bold": True, "size": 18})], first=True, space_after=3)
    P.rich_par(tf_lt, [("AI 僅在瀏覽器內產生文字，後續執行全由人工承擔", {"color": T.MUTED, "size": 12})], first=False)

    P.add_hairline(slide, panel_y + Inches(1.35), x=left_x + Inches(0.24), w=panel_w - Inches(0.48))

    steps_left = [
        ("步驟 1：輸入指令", "使用者用文字提問，AI 提供程式碼或處理建議文字"),
        ("步驟 2：手動搬移", "使用者自行複製程式碼，切換至本機終端或文書軟體貼上"),
        ("步驟 3：人工除錯", "指令失敗或報錯時，使用者手動截圖或複製日誌回問"),
        ("核心瓶頸", "繁重的資料搬移、執行與環境除錯仍由人類肉身承擔"),
    ]
    tb_ls, tf_ls = P.textbox(slide, left_x + Inches(0.24), panel_y + Inches(1.5), panel_w - Inches(0.48), Inches(2.6))
    for i, (st, desc) in enumerate(steps_left):
        color_tag = T.RED if i == 3 else T.INK
        P.rich_par(tf_ls, [
            (f"{st}  ", {"color": color_tag, "bold": True, "size": 13}),
            (desc, {"color": T.INK_SOFT, "size": 12}),
        ], first=(i == 0), space_after=9, line=1.18)

    # Right Panel: Antigravity 2.0 代理人模式
    right_x = left_x + panel_w + panel_gap
    P.add_panel(slide, right_x, panel_y, panel_w, panel_h, fill=T.ORANGE_SOFT, line=T.ORANGE, line_w=Pt(1.5))

    P.add_status_pill(slide, right_x + Inches(0.24), panel_y + Inches(0.24), "主動代理人模式",
                      bg=T.ORANGE, fg=T.ON_DARK, w=Inches(1.6), h=Inches(0.28), size=11)

    tb_rt, tf_rt = P.textbox(slide, right_x + Inches(0.24), panel_y + Inches(0.68), panel_w - Inches(0.48), Inches(0.55))
    P.rich_par(tf_rt, [("「目標導向」的數位實習生模式", {"color": T.INK, "bold": True, "size": 18})], first=True, space_after=3)
    P.rich_par(tf_rt, [("AI 自行規劃步驟、調用系統工具並回報透明變更", {"color": T.INK_SOFT, "size": 12})], first=False)

    P.add_hairline(slide, panel_y + Inches(1.35), x=right_x + Inches(0.24), w=panel_w - Inches(0.48), color=T.ORANGE)

    steps_right = [
        ("步驟 1：定義目標", "使用者用日常繁中下達目標（如整理某資料夾、抓取公告）"),
        ("步驟 2：自主規劃", "AI 拆解子任務清單，主動說明預計執行的步驟與路徑"),
        ("步驟 3：工具執行", "AI 在本機沙箱讀取檔案、執行腳本、生成結構化成果"),
        ("核心價值", "人類轉變為「需求定義者與驗收者」，省下 80% 機械工時"),
    ]
    tb_rs, tf_rs = P.textbox(slide, right_x + Inches(0.24), panel_y + Inches(1.5), panel_w - Inches(0.48), Inches(2.6))
    for i, (st, desc) in enumerate(steps_right):
        color_tag = T.ORANGE if i == 3 else T.INK
        P.rich_par(tf_rs, [
            (f"{st}  ", {"color": color_tag, "bold": True, "size": 13}),
            (desc, {"color": T.INK_SOFT, "size": 12}),
        ], first=(i == 0), space_after=9, line=1.18)
