# slide18.py — Governance Slide: 3 Lines of Defense in Agentic Collaboration (Clean Architecture Overview)

from pptx.util import Inches, Pt
import theme as T
import primitives as P

def build(prs, slide):
    P.add_background(slide)
    P.add_eyebrow(slide, 4, "BEST PRACTICES")

    title_segments = [
        ("代理人協作的", {}),
        ("三大防線", {"color": T.ORANGE}),
        ("：計畫審核、資料隔離與結果查驗", {}),
    ]
    P.add_argument_title(slide, title_segments, y=T.TITLE_Y)

    support_segments = [
        ("在充分享受自動化便利的同時，必須確保", {}),
        ("資安合規", {"color": T.INK, "bold": True}),
        ("與", {}),
        ("學術資料嚴謹性", {"color": T.INK, "bold": True}),
        ("，築牢風險防線。", {}),
    ]
    P.add_supporting_sentence(slide, support_segments, y=Inches(1.58))
    P.add_hairline(slide, Inches(2.2))

    cards = [
        {
            "num": "防線 01",
            "tag": "執行把關",
            "title": "永遠先確認計畫再放行",
            "subtitle": "特別防範涉及檔案移動、覆蓋與刪除的操作",
            "points": [
                ("先列清單原則", "下達破壞性或搬遷指令時，要求 AI 先提供預計變更對照表。"),
                ("善用異動面板", "在 Files Changed 輔助窗格逐一核對異動路徑，確認無誤再放行。"),
                ("保留原始備份", "執行批次整理前，建議將原始資料夾進行本機封存或快照備份。"),
            ],
            "accent": False,
        },
        {
            "num": "防線 02",
            "tag": "資安紅線",
            "title": "機密與個人隱私嚴格隔離",
            "subtitle": "未公開的學術研究資料與個資不上傳雲端",
            "points": [
                ("敏感資料不上傳", "涉及人體受試者個資、人事隱私、未公開論文草稿禁止直接上傳。"),
                ("脫敏演練習慣", "教學與日常測試一律使用脫敏假資料或公開資料集進行演練。"),
                ("遵循院內規範", "遵循中研院資通安全管理作業準則，確認模型與外網通訊權限。"),
            ],
            "accent": True,  # High risk emphasis
        },
        {
            "num": "防線 03",
            "tag": "嚴謹驗收",
            "title": "產出資料與引用人工查驗",
            "subtitle": "AI 擔任提速實習生，最終成果責任在人類",
            "points": [
                ("查驗數字統計", "LLM 可能存在計算或幻覺風險，簡報內的關鍵統計務必二次覆核。"),
                ("點選外部連結", "AI 爬蟲或整理之文獻連結與法規條文，發布前手動抽驗有效性。"),
                ("人類負責任簽核", "AI 產出之公文簽呈與專案報告，由承辦與研究同仁承擔簽定責任。"),
            ],
            "accent": False,
        },
    ]

    card_w = Inches(3.84)
    card_gap = Inches(0.28)
    card_y = Inches(2.45)
    card_h = Inches(4.55)

    for i, c in enumerate(cards):
        x = T.MARGIN_X + i * (card_w + card_gap)
        bg = T.ORANGE_SOFT if c["accent"] else T.PANEL_BG
        border = T.ORANGE if c["accent"] else T.PANEL_LN
        line_w = Pt(1.5) if c["accent"] else Pt(1.0)
        P.add_panel(slide, x, card_y, card_w, card_h, fill=bg, line=border, line_w=line_w)

        # Header tag
        pill_bg = T.RED if c["accent"] else T.INK
        P.add_status_pill(slide, x + Inches(0.24), card_y + Inches(0.22), c["tag"],
                          bg=pill_bg, fg=T.ON_DARK, w=Inches(1.1), h=Inches(0.26), size=11)

        tb_n, tf_n = P.textbox(slide, x + Inches(1.45), card_y + Inches(0.22), card_w - Inches(1.7), Inches(0.3))
        P.rich_par(tf_n, [(c["num"], {"color": T.ORANGE if c["accent"] else T.MUTED, "mono": True, "bold": True, "size": 12})], first=True)

        # Title
        tb_t, tf_t = P.textbox(slide, x + Inches(0.24), card_y + Inches(0.62), card_w - Inches(0.48), Inches(0.65))
        P.rich_par(tf_t, [(c["title"], {"color": T.INK, "bold": True, "size": 20})], first=True, space_after=3)
        P.rich_par(tf_t, [(c["subtitle"], {"color": T.INK_SOFT, "size": 12})], first=False)

        P.add_hairline(slide, card_y + Inches(1.48), x=x + Inches(0.24), w=card_w - Inches(0.48),
                       color=T.ORANGE if c["accent"] else T.HAIRLINE)

        # Points
        tb_p, tf_p = P.textbox(slide, x + Inches(0.24), card_y + Inches(1.62), card_w - Inches(0.48), Inches(2.7))
        for j, (pname, pdesc) in enumerate(c["points"]):
            P.rich_par(tf_p, [
                (f"▸ {pname}：", {"color": T.ORANGE if c["accent"] else T.INK, "bold": True, "size": 13}),
                (pdesc, {"color": T.INK_SOFT, "size": 12}),
            ], first=(j == 0), space_after=12, line=1.20)
