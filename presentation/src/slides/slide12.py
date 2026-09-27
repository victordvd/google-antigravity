# slide10.py — Demo A: Intelligent File & Storage Cleanup

from pptx.util import Inches, Pt
import theme as T
import primitives as P

def build(prs, slide):
    P.add_background(slide)
    P.add_eyebrow(slide, 3, "DEMO")

    title_segments = [
        ("示範 A：雜亂檔案智慧歸檔，", {}),
        ("變更前一律先看清單", {"color": T.ORANGE}),
    ]
    P.add_argument_title(slide, title_segments, y=T.TITLE_Y)

    support_segments = [
        ("以 Downloads 資料夾為例，依據", {}),
        ("檔案類型與年份", {"color": T.INK, "bold": True}),
        ("建立結構，並透過清單確認杜絕誤刪風險。", {}),
    ]
    P.add_supporting_sentence(slide, support_segments, y=Inches(1.58))
    P.add_hairline(slide, Inches(2.2))

    steps = [
        {
            "num": "STEP 01",
            "title": "容量與類型盤點",
            "prompt": "「請掃描 Downloads 目錄，列出各副檔名數量與大於 1GB 檔案」",
            "details": [
                "AI 自主調用本機目錄讀取工具",
                "產出 PDF、ZIP、影像各佔容量統計",
                "標記出長期佔用空間的巨型安裝檔",
            ],
            "accent": False,
        },
        {
            "num": "STEP 02",
            "title": "建議架構確認",
            "prompt": "「請依 年份/月份 與類別規劃子目錄，先列清單讓我確認」",
            "details": [
                "AI 擬定建議搬遷對照路徑表",
                "強制設定確認關卡，等待人類審核",
                "可隨時要求調整規則（如特定專案留存）",
            ],
            "accent": False,
        },
        {
            "num": "STEP 03",
            "title": "安全批次歸檔",
            "prompt": "「計畫已核可，請開始執行分類移動」",
            "details": [
                "AI 於本機自動建立分類資料夾",
                "自動批次搬移檔案至對應目錄",
                "在 Files Changed 面板即時核對異動",
            ],
            "accent": True,
        },
        {
            "num": "STEP 04",
            "title": "重複檔清理釋放",
            "prompt": "「比對重複下載的舊版檔案，列出清單供我勾選刪除」",
            "details": [
                "透過雜湊值（Hash）精準找出重複檔案",
                "人工勾選確認後執行清理",
                "安全釋出磁碟空間，留下完整紀錄",
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
