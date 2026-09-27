# slide12.py — Demo C: Web Scraping and Automated Scheduling without Code

from pptx.util import Inches, Pt
import theme as T
import primitives as P

def build(prs, slide):
    P.add_background(slide)
    P.add_eyebrow(slide, 3, "DEMO")

    title_segments = [
        ("示範 C：公開網站資訊抓取與排程，", {}),
        ("免寫程式碼", {"color": T.ORANGE}),
        ("也能定期追蹤", {}),
    ]
    P.add_argument_title(slide, title_segments, y=T.TITLE_Y)

    support_segments = [
        ("以", {}),
        ("政府公開資料網站", {"color": T.INK, "bold": True}),
        ("為例，自動擷取公告清單並設定每週定時更新，告別手動複製貼上。", {}),
    ]
    P.add_supporting_sentence(slide, support_segments, y=Inches(1.58))
    P.add_hairline(slide, Inches(2.2))

    steps = [
        {
            "num": "STEP 01",
            "title": "目標與欄位定義",
            "prompt": "「抓取政府採購公開網站最新 10 筆公告標題、日期與連結」",
            "details": [
                "指定目標公開網址與所需資料欄位",
                "AI 自主檢核網站架構與 robots.txt 合規",
                "確認資料來源公開合法，杜絕版權疑慮",
            ],
            "accent": False,
        },
        {
            "num": "STEP 02",
            "title": "沙箱工具自主執行",
            "prompt": "「使用終端工具取得網頁內容並解析指定標籤」",
            "details": [
                "AI 自主撰寫輕量提取程式碼並於沙箱執行",
                "使用者全程無需學習 Python 或 HTML 標籤",
                "終端面板即時顯示執行指令與回傳狀態",
            ],
            "accent": False,
        },
        {
            "num": "STEP 03",
            "title": "結構表格呈現",
            "prompt": "「將提取到的資料整理成欄位分明的 CSV 與 Markdown 表格」",
            "details": [
                "非結構化網頁文字自動清洗轉為標準表格",
                "右側 Artifacts 面板即時預覽抓取成果",
                "一鍵匯出 Excel 或直接貼入內部報告",
            ],
            "accent": True,
        },
        {
            "num": "STEP 04",
            "title": "背景定時自動化",
            "prompt": "「設定每週一早上 09:00 自動執行抓取，並比對新公告」",
            "details": [
                "利用 Scheduled Tasks 註冊定時任務",
                "背景自動化運作，有新異動主動發送通知",
                "徹底將週期性繁瑣查核轉化為無人值守",
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
