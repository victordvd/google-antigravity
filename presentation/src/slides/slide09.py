# slide08.py — Mechanism Slide: Slash Commands and Context Mentions

from pptx.util import Inches, Pt
import theme as T
import primitives as P

def build(prs, slide):
    P.add_background(slide)
    P.add_eyebrow(slide, 2, "INTERFACE")

    title_segments = [
        ("斜線指令與 @ 引用：", {}),
        ("精準傳遞上下文", {"color": T.ORANGE}),
        ("是成功協作的關鍵", {}),
    ]
    P.add_argument_title(slide, title_segments, y=T.TITLE_Y)

    support_segments = [
        ("善用內建快捷語法，將", {}),
        ("特定作業流程", {"color": T.INK, "bold": True}),
        ("與", {}),
        ("本地檔案資訊", {"color": T.INK, "bold": True}),
        ("無縫送入模型，大幅減少反覆說明成本。", {}),
    ]
    P.add_supporting_sentence(slide, support_segments, y=Inches(1.58))
    P.add_hairline(slide, Inches(2.2))

    panel_w = Inches(5.88)
    panel_gap = Inches(0.33)
    panel_y = Inches(2.55)
    panel_h = Inches(4.35)

    # Left Panel: Slash Commands
    left_x = T.MARGIN_X
    P.add_panel(slide, left_x, panel_y, panel_w, panel_h, fill=T.PANEL_BG, line=T.PANEL_LN)

    P.add_status_pill(slide, left_x + Inches(0.24), panel_y + Inches(0.24), "流程加速器",
                      bg=T.BLUE, fg=T.ON_DARK, w=Inches(1.2), h=Inches(0.28), size=11)

    tb_lt, tf_lt = P.textbox(slide, left_x + Inches(0.24), panel_y + Inches(0.68), panel_w - Inches(0.48), Inches(0.55))
    P.rich_par(tf_lt, [("Slash Commands 「 / 」 快速流程", {"color": T.INK, "bold": True, "size": 18})], first=True, space_after=3)
    P.rich_par(tf_lt, [("輸入斜線調用預設的高階代理人行為模式", {"color": T.MUTED, "size": 12})], first=False)

    P.add_hairline(slide, panel_y + Inches(1.35), x=left_x + Inches(0.24), w=panel_w - Inches(0.48))

    slash_cmds = [
        ("/goal", "交付長時間非同步任務，指示代理人持續工作直至徹底達成目標"),
        ("/plan", "啟動規劃模式，要求 AI 在動手前先產出可審閱的完整步驟"),
        ("/browser", "調用安全瀏覽器，進行公開網站互動、資料抓取或驗證"),
        ("/schedule", "將重複性質高的指令設定為定時定週自動執行的背景任務"),
    ]
    tb_ls, tf_ls = P.textbox(slide, left_x + Inches(0.24), panel_y + Inches(1.5), panel_w - Inches(0.48), Inches(2.6))
    for i, (cmd, desc) in enumerate(slash_cmds):
        P.rich_par(tf_ls, [
            (f"{cmd}  ", {"color": T.BLUE, "mono": True, "bold": True, "size": 13}),
            (desc, {"color": T.INK_SOFT, "size": 12}),
        ], first=(i == 0), space_after=9, line=1.18)

    # Right Panel: Context Mentions
    right_x = left_x + panel_w + panel_gap
    P.add_panel(slide, right_x, panel_y, panel_w, panel_h, fill=T.PANEL_BG, line=T.PANEL_LN)

    P.add_status_pill(slide, right_x + Inches(0.24), panel_y + Inches(0.24), "脈絡注入",
                      bg=T.ORANGE, fg=T.ON_DARK, w=Inches(1.2), h=Inches(0.28), size=11)

    tb_rt, tf_rt = P.textbox(slide, right_x + Inches(0.24), panel_y + Inches(0.68), panel_w - Inches(0.48), Inches(0.55))
    P.rich_par(tf_rt, [("Context Mentions 「 @ 」 本地脈絡", {"color": T.INK, "bold": True, "size": 18})], first=True, space_after=3)
    P.rich_par(tf_rt, [("輸入 @ 精準注入本機檔案與環境資料，杜絕 AI 憑空捏造", {"color": T.MUTED, "size": 12})], first=False)

    P.add_hairline(slide, panel_y + Inches(1.35), x=right_x + Inches(0.24), w=panel_w - Inches(0.48))

    mention_items = [
        ("@檔案 / 資料夾", "直接選取桌面上的資料表格（CSV/Excel）、PDF 或研究草稿"),
        ("@Terminal", "將終端機目前執行的日誌與系統錯誤資訊即時注入對話"),
        ("@Rules", "載入專屬作業規範，如中研院公文格式或院內特定排版指引"),
        ("@Conversations", "跨對話調用過去討論歷程與分析結論，保持工作連貫性"),
    ]
    tb_rs, tf_rs = P.textbox(slide, right_x + Inches(0.24), panel_y + Inches(1.5), panel_w - Inches(0.48), Inches(2.6))
    for i, (m, desc) in enumerate(mention_items):
        P.rich_par(tf_rs, [
            (f"{m}  ", {"color": T.ORANGE, "mono": True, "bold": True, "size": 13}),
            (desc, {"color": T.INK_SOFT, "size": 12}),
        ], first=(i == 0), space_after=9, line=1.18)
