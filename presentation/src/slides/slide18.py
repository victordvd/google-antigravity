# slide18.py — Governance Deep Dive 1: Plan Review Policy (Always Ask)

from pptx.util import Inches, Pt
from pptx.enum.shapes import MSO_SHAPE
import theme as T
import primitives as P

def build(prs, slide):
    P.add_background(slide)
    P.add_eyebrow(slide, 4, "BEST PRACTICES")

    title_segments = [
        ("防線一實體設定：計畫審核機制", {"color": T.ORANGE}),
        ("：以 Always Ask 阻斷非預期檔案異動", {}),
    ]
    P.add_argument_title(slide, title_segments, y=T.TITLE_Y)

    support_segments = [
        ("在動手前先看計畫：將", {}),
        ("Plan Review Policy 設為 Always Ask", {"color": T.INK, "bold": True}),
        ("，杜絕任何未經確認的本機檔案覆蓋與刪除。", {}),
    ]
    P.add_supporting_sentence(slide, support_segments, y=Inches(1.58))
    P.add_hairline(slide, Inches(2.2))

    card_y = Inches(2.45)
    card_h = Inches(4.55)
    img_w = Inches(7.2)
    col_gap = Inches(0.28)
    info_w = Inches(4.61)

    # ------------------------------------------------------------- Left: Large Annotated Screenshot
    img_x = T.MARGIN_X
    img_path = T.ASSETS_DIR / "ui-img" / "settings-general2.png"
    # settings-general2.png is 1257 x 802 -> scale = 0.005673 -> placed w = 7.13", h = 4.55"
    P.add_screenshot(slide, str(img_path), img_x, card_y, max_w=img_w, max_h=card_h, frame=True)

    # --- Callout: Plan Review Policy Highlight Box (y ~ 105..220 in 802, x ~ 350..1115 in 1257)
    box_x = img_x + Inches(1.98)
    box_y = card_y + Inches(0.60)
    box_w = Inches(4.35)
    box_h = Inches(0.65)
    box = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, box_x, box_y, box_w, box_h)
    box.fill.background()
    box.line.color.rgb = T.ORANGE
    box.line.width = Pt(2.25)
    P.no_shadow(box)
    P.add_status_pill(slide, box_x + box_w - Inches(3.40), box_y - Inches(0.28), "★ 關鍵設定：Plan Review Policy = Always Ask",
                      bg=T.ORANGE, fg=T.ON_DARK, w=Inches(3.35), h=Inches(0.24), size=10)

    # ------------------------------------------------------------- Right: Companion Explanation Panel
    info_x = img_x + img_w + col_gap
    P.add_panel(slide, info_x, card_y, info_w, card_h, fill=T.PANEL_BG, line=T.PANEL_LN)

    # Header
    tb_h, tf_h = P.textbox(slide, info_x + Inches(0.2), card_y + Inches(0.18), info_w - Inches(0.4), Inches(0.28))
    P.rich_par(tf_h, [
        ("EXECUTION SAFEGUARD  ·  ", {"color": T.ORANGE, "mono": True, "bold": True, "size": 11}),
        ("執行把關防線", {"color": T.MUTED, "size": 11}),
    ], first=True)

    tb_t, tf_t = P.textbox(slide, info_x + Inches(0.2), card_y + Inches(0.48), info_w - Inches(0.4), Inches(0.38))
    P.rich_par(tf_t, [("堅持「先看計畫再放行」的操作原則", {"color": T.INK, "bold": True, "size": 16})], first=True)

    P.add_hairline(slide, card_y + Inches(0.92), x=info_x + Inches(0.2), w=info_w - Inches(0.4))

    # Notes inside a single contiguous TextFrame to prevent overlapping
    sections = [
        ("① Always Ask 的防護機制", [
            ("強制中斷等待批准", "遇批次檔案移動、刪除或覆蓋，AI 必須停手呈報計畫。"),
            ("點選 Proceed 始得執行", "只有使用者在介面確認計畫無誤後，代理人才獲准動手。"),
        ]),
        ("② 善用 /plan 斜線指令", [
            ("主動啟動規劃模式", "複雜任務前輸入 /plan，要求 AI 先梳理步驟清單與邊界。"),
            ("消除 95% 溝通落差", "在投入實際修改前釐清目錄、格式與邏輯，大幅降低試錯成本。"),
        ]),
        ("③ 中研院職員最佳實踐", [
            ("禁止切換為 Never Ask", "日常行政與學術研究嚴禁關閉計畫確認，保持操作透明可稽。"),
        ]),
    ]

    tb_notes, tf_notes = P.textbox(slide, info_x + Inches(0.2), card_y + Inches(1.04),
                                   info_w - Inches(0.4), card_h - Inches(1.15))
    first_par = True
    for s_idx, (s_title, s_points) in enumerate(sections):
        p_title = P.rich_par(tf_notes, [(s_title, {"color": T.ORANGE, "bold": True, "size": 12.5})],
                             first=first_par, space_after=4)
        if s_idx > 0:
            p_title.space_before = Pt(8)
        first_par = False

        for j, (pname, pdesc) in enumerate(s_points):
            P.rich_par(tf_notes, [
                (f"▸ {pname}：", {"color": T.INK, "bold": True, "size": 10.5}),
                (pdesc, {"color": T.INK_SOFT, "size": 10.5}),
            ], space_after=3 if j < len(s_points) - 1 else 0, line=1.18)
