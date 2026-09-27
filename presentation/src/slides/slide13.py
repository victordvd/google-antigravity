# slide13.py — Demo B: Raw Data to Presentation via Antigravity Agent Workflow

from pptx.util import Inches, Pt
import theme as T
import primitives as P

def build(prs, slide):
    P.add_background(slide)
    P.add_eyebrow(slide, 3, "DEMO")

    title_segments = [
        ("示範 B：從原始資料到多頁簡報，以", {}),
        ("代理人工作流", {"color": T.ORANGE}),
        ("自動構建", {}),
    ]
    P.add_argument_title(slide, title_segments, y=T.TITLE_Y)

    support_segments = [
        ("體驗 Antigravity 原生簡報製作：", {}),
        ("大綱規劃 → Python 構建 → 視覺驗收", {"color": T.INK, "bold": True}),
        ("，一氣呵成產出可編輯簡報與聯絡單。", {}),
    ]
    P.add_supporting_sentence(slide, support_segments, y=Inches(1.58))
    P.add_hairline(slide, Inches(2.2))

    steps = [
        {
            "num": "STEP 01",
            "title": "資料脈絡注入",
            "prompt": "「@問卷調查.csv 這是中研院同仁反饋，請分析痛點並規劃 5 頁簡報」",
            "details": [
                "鍵入 @ 直接引用本機數據與參考文件",
                "AI 自主統計回覆筆數、平均分與關鍵詞",
                "免開 Excel 即可萃取宏觀洞察與趨勢",
            ],
            "accent": False,
        },
        {
            "num": "STEP 02",
            "title": "結構大綱規劃",
            "prompt": "「/plan 請擬定 outline.md，明確定義各頁標題、論點與視覺形式」",
            "details": [
                "啟動規劃模式先出具章節結構與規格",
                "嚴格依據黃金圈與敘事邏輯排列頁面",
                "使用者確認大綱無誤後才批准動手",
            ],
            "accent": False,
        },
        {
            "num": "STEP 03",
            "title": "Python 原生構建",
            "prompt": "「請調用 python-pptx 構建簡報，嚴格遵循 2pt 格線與暖白配色」",
            "details": [
                "AI 自動撰寫 Python 腳本生成可編輯物件",
                "非死板截圖，文字、圖表均可手動微調",
                "完全符合中研院簡報設計規範與色系",
            ],
            "accent": True,
        },
        {
            "num": "STEP 04",
            "title": "視覺彩現驗收",
            "prompt": "「導出各頁 PNG 預覽與全覽聯絡單，並轉存 presentation.pdf」",
            "details": [
                "自動產生單頁預覽圖與 20 頁總覽聯絡單",
                "免開啟 PowerPoint 即可即時檢驗排版",
                "支援匯入 Google Slides 供團隊線上協作",
            ],
            "accent": False,
        },
    ]

    card_w = Inches(2.84)
    card_gap = Inches(0.24)
    card_y = Inches(2.55)
    card_h = Inches(4.35)

    for i, s in enumerate(steps):
        x = T.MARGIN_X + i * (card_w + card_gap)
        bg = T.ORANGE_SOFT if s["accent"] else T.PANEL_BG
        border = T.ORANGE if s["accent"] else T.PANEL_LN
        line_w = Pt(1.5) if s["accent"] else Pt(1.0)
        P.add_panel(slide, x, card_y, card_w, card_h, fill=bg, line=border, line_w=line_w)

        # Step tag
        tb, tf = P.textbox(slide, x + Inches(0.2), card_y + Inches(0.22), card_w - Inches(0.4), Inches(0.32))
        P.rich_par(tf, [(s["num"], {"color": T.ORANGE, "mono": True, "bold": True, "size": 11})], first=True)

        # Title
        tb_t, tf_t = P.textbox(slide, x + Inches(0.2), card_y + Inches(0.55), card_w - Inches(0.4), Inches(0.5))
        P.rich_par(tf_t, [(s["title"], {"color": T.INK, "bold": True, "size": 18})], first=True)

        # Prompt Box
        P.add_hairline(slide, card_y + Inches(1.15), x=x + Inches(0.2), w=card_w - Inches(0.4))
        tb_p, tf_p = P.textbox(slide, x + Inches(0.2), card_y + Inches(1.28), card_w - Inches(0.4), Inches(1.1))
        P.rich_par(tf_p, [("指示範例：\n", {"color": T.MUTED, "mono": True, "size": 11}),
                          (s["prompt"], {"color": T.INK, "size": 11.5, "italic": True})], first=True, line=1.15)

        P.add_hairline(slide, card_y + Inches(2.45), x=x + Inches(0.2), w=card_w - Inches(0.4))

        # Details
        tb_d, tf_d = P.textbox(slide, x + Inches(0.2), card_y + Inches(2.58), card_w - Inches(0.4), Inches(1.6))
        for j, item in enumerate(s["details"]):
            P.rich_par(tf_d, [
                ("▸ ", {"color": T.ORANGE if s["accent"] else T.MUTED, "bold": True, "size": 12}),
                (item, {"color": T.INK_SOFT, "size": 11.5}),
            ], first=(j == 0), space_after=6, line=1.15)
