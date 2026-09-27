# slide19.py — Governance Deep Dive 2: Security Preset (Default Sandbox)

from pptx.util import Inches, Pt
from pptx.enum.shapes import MSO_SHAPE
import theme as T
import primitives as P

def build(prs, slide):
    P.add_background(slide)
    P.add_eyebrow(slide, 4, "BEST PRACTICES")

    title_segments = [
        ("防線二實體設定：安全沙箱等級", {"color": T.ORANGE}),
        ("：堅守 Default 預設沙箱防護隔離", {}),
    ]
    P.add_argument_title(slide, title_segments, y=T.TITLE_Y)

    support_segments = [
        ("把守資安邊界：將", {}),
        ("Security Preset 維持為 Default", {"color": T.INK, "bold": True}),
        ("，所有終端指令與跨目錄檔案存取皆需人工逐條審查。", {}),
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
    img_path = T.ASSETS_DIR / "ui-img" / "settings-general-security-preset.png"
    # settings-general-security-preset.png is 1245 x 812 -> scale = 0.005603 -> placed w = 6.98", h = 4.55"
    P.add_screenshot(slide, str(img_path), img_x, card_y, max_w=img_w, max_h=card_h, frame=True)

    # --- Callout: Security Preset Dropdown Highlight Box (x ~ 620..1135, y ~ 313..669 in 1245x812)
    box_x = img_x + Inches(3.47)
    box_y = card_y + Inches(1.75)
    box_w = Inches(2.88)
    box_h = Inches(2.00)
    box = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, box_x, box_y, box_w, box_h)
    box.fill.background()
    box.line.color.rgb = T.RED
    box.line.width = Pt(2.25)
    P.no_shadow(box)
    P.add_status_pill(slide, box_x + Inches(0.06), box_y - Inches(0.28), "★ 核心防護：Default (終端與目錄外存取強制審查)",
                      bg=T.RED, fg=T.ON_DARK, w=Inches(3.35), h=Inches(0.24), size=10)

    # ------------------------------------------------------------- Right: Companion Explanation Panel
    info_x = img_x + img_w + col_gap
    P.add_panel(slide, info_x, card_y, info_w, card_h, fill=T.PANEL_BG, line=T.PANEL_LN)

    # Header
    tb_h, tf_h = P.textbox(slide, info_x + Inches(0.2), card_y + Inches(0.18), info_w - Inches(0.4), Inches(0.28))
    P.rich_par(tf_h, [
        ("DATA ISOLATION  ·  ", {"color": T.RED, "mono": True, "bold": True, "size": 11}),
        ("資安紅線防護", {"color": T.MUTED, "size": 11}),
    ], first=True)

    tb_t, tf_t = P.textbox(slide, info_x + Inches(0.2), card_y + Inches(0.48), info_w - Inches(0.4), Inches(0.38))
    P.rich_par(tf_t, [("四種安全預設與院內合規底線", {"color": T.INK, "bold": True, "size": 16})], first=True)

    P.add_hairline(slide, card_y + Inches(0.92), x=info_x + Inches(0.2), w=info_w - Inches(0.4))

    # Notes inside a single contiguous TextFrame to prevent overlapping
    sections = [
        ("① Default（推薦 · 院內唯一規範）", [
            ("手動審查指令", "所有涉及系統終端機之操作，皆需人工檢視並按確認。"),
            ("目錄外隔離", "嚴格禁止 AI 自主讀寫工作專案資料夾外的任何本機檔案。"),
        ]),
        ("② Full Machine 與 Turbo 之危害", [
            ("Full Machine 風險", "允許跨全機所有磁區讀寫，容易誤觸個人隱私或系統檔。"),
            ("Turbo Mode 嚴禁啟用", "完全解除一切安全審查屏障，院內環境一律嚴禁使用。"),
        ]),
        ("③ 遵循中研院資安守則", [
            ("敏感資料不落地", "涉及未公開學術數據或個資，切勿開啟任意存取許可權。"),
        ]),
    ]

    tb_notes, tf_notes = P.textbox(slide, info_x + Inches(0.2), card_y + Inches(1.04),
                                   info_w - Inches(0.4), card_h - Inches(1.15))
    first_par = True
    for s_idx, (s_title, s_points) in enumerate(sections):
        p_title = P.rich_par(tf_notes, [(s_title, {"color": T.RED if "Default" in s_title else T.INK, "bold": True, "size": 12.5})],
                             first=first_par, space_after=4)
        if s_idx > 0:
            p_title.space_before = Pt(8)
        first_par = False

        for j, (pname, pdesc) in enumerate(s_points):
            P.rich_par(tf_notes, [
                (f"▸ {pname}：", {"color": T.INK, "bold": True, "size": 10.5}),
                (pdesc, {"color": T.INK_SOFT, "size": 10.5}),
            ], space_after=3 if j < len(s_points) - 1 else 0, line=1.18)
