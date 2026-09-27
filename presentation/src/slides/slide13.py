# slide11.py — Demo B: Raw Data to Presentation via Conversational Iteration

from pptx.util import Inches, Pt
import theme as T
import primitives as P

def build(prs, slide):
    P.add_background(slide)
    P.add_eyebrow(slide, 3, "DEMO")

    title_segments = [
        ("示範 B：從原始資料到多頁簡報，以", {}),
        ("對話迭代", {"color": T.ORANGE}),
        ("格式與視覺", {}),
    ]
    P.add_argument_title(slide, title_segments, y=T.TITLE_Y)

    support_segments = [
        ("將問卷分析與專案報告轉化為", {}),
        ("結構化簡報", {"color": T.INK, "bold": True}),
        ("，直接在對話中微調圖表並匯出至辦公軟體。", {}),
    ]
    P.add_supporting_sentence(slide, support_segments, y=Inches(1.58))
    P.add_hairline(slide, Inches(2.2))

    steps = [
        {
            "num": "STEP 01",
            "title": "資料脈絡載入",
            "prompt": "「@滿意度調查.csv 這是本季同仁反饋，請先梳理出主要的資料分佈」",
            "details": [
                "使用 @ 功能精準載入原始資料表格",
                "AI 自主統計回覆筆數、平均分與關鍵詞",
                "免開 Excel 即可掌握整體統計輪廓",
            ],
            "accent": False,
        },
        {
            "num": "STEP 02",
            "title": "結構大綱生成",
            "prompt": "「提煉 3 項核心發現，製作 5 頁正式簡報大綱（摘要/現況/建議）」",
            "details": [
                "AI 依據資料自動擬定章節邏輯架構",
                "右側 Artifacts 面板即時預覽簡報內容",
                "將原始數字轉化為清晰的分析論點",
            ],
            "accent": False,
        },
        {
            "num": "STEP 03",
            "title": "對話持續迭代",
            "prompt": "「第 2 頁改用圓餅圖呈現各單位佔比，語氣改為正式行政風格」",
            "details": [
                "無需從頭重做，直接用中文指定修改頁面",
                "動態調整圖表形式、行文語氣與強調重點",
                "每一次修改即時在輔助面板呈現差異",
            ],
            "accent": True,
        },
        {
            "num": "STEP 04",
            "title": "原生格式匯出",
            "prompt": "「將這份簡報轉換為可編輯的 PPTX 格式，並保留原始文字區塊」",
            "details": [
                "產出原生 PowerPoint 檔案，非死板截圖",
                "支援匯入 Google Slides 供團隊線上協作",
                "節省 80% 手動排版與格式複製貼上工時",
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
                          (s["prompt"], {"color": T.INK, "size": 12, "italic": True})], first=True, line=1.15)

        P.add_hairline(slide, card_y + Inches(2.45), x=x + Inches(0.2), w=card_w - Inches(0.4))

        # Details
        tb_d, tf_d = P.textbox(slide, x + Inches(0.2), card_y + Inches(2.58), card_w - Inches(0.4), Inches(1.6))
        for j, item in enumerate(s["details"]):
            P.rich_par(tf_d, [
                ("▸ ", {"color": T.ORANGE if s["accent"] else T.MUTED, "bold": True, "size": 12}),
                (item, {"color": T.INK_SOFT, "size": 12}),
            ], first=(j == 0), space_after=7, line=1.15)
