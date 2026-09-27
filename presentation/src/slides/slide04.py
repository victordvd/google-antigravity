# slide04.py — Contrast Slide: Traditional vs. Vibe Coding (Native Table)

from pptx.util import Inches
import theme as T
import primitives as P

def build(prs, slide):
    P.add_background(slide)
    P.add_eyebrow(slide, 1, "CONCEPT")

    title_segments = [
        ("Vibe Coding 的本質：用", {}),
        ("自然語言描述", {"color": T.ORANGE}),
        ("「成果」而非「步驟」", {}),
    ]
    P.add_argument_title(slide, title_segments, y=T.TITLE_Y)

    support_segments = [
        ("傳統開發要求", {}),
        ("精確語法", {"color": T.INK, "bold": True}),
        ("；對話式編程只需給予", {}),
        ("目標限制與驗收標準", {"color": T.INK, "bold": True}),
        ("。", {}),
    ]
    P.add_supporting_sentence(slide, support_segments, y=Inches(1.58))
    P.add_hairline(slide, Inches(2.2))

    headers = ["工作維度", "傳統工作方式", "Vibe Coding 模式"]
    rows = [
        [
            "核心要求",
            "自行學習程式語言語法與工具設定",
            [("用日常繁體中文描述", {}), ("最終需要的文件或表格", {"color": T.ORANGE, "bold": True})],
        ],
        [
            "卡關處理",
            "查閱技術論壇、逐行偵錯與修改",
            [("直接告知 AI 錯誤訊息，", {}), ("要求重新規劃調整", {"color": T.ORANGE, "bold": True})],
        ],
        [
            "角色定位",
            "執行者：自行搬運資料與編排格式",
            [("指導者：", {"bold": True}), ("檢閱 AI 規劃步驟並驗收成品", {"color": T.ORANGE, "bold": True})],
        ],
        [
            "門檻與效益",
            "學習曲線陡峭，非技術同仁難以跨越",
            [("具備清晰邏輯與需求，", {}), ("任何人皆能驅動自動化", {"color": T.ORANGE, "bold": True})],
        ],
    ]

    P.add_native_table(
        slide,
        T.MARGIN_X,
        Inches(2.52),
        T.CONTENT_W,
        Inches(4.35),
        headers=headers,
        rows=rows,
        col_widths=[1.6, 5.2, 5.2],
        row_label_col=0,
    )
