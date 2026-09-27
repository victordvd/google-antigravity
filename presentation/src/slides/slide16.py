# slide14.py — Guideline Table: 4 Key Elements of Effective Prompting

from pptx.util import Inches
import theme as T
import primitives as P

def build(prs, slide):
    P.add_background(slide)
    P.add_eyebrow(slide, 4, "BEST PRACTICES")

    title_segments = [
        ("提示詞四大關鍵要素：", {}),
        ("給足角色、背景、格式與限制", {"color": T.ORANGE}),
    ]
    P.add_argument_title(slide, title_segments, y=T.TITLE_Y)

    support_segments = [
        ("擺脫「幫我整理資料」的模糊指令，用", {}),
        ("四維度結構", {"color": T.INK, "bold": True}),
        ("讓 AI 第一次就能精準交付符合預期的成果。", {}),
    ]
    P.add_supporting_sentence(slide, support_segments, y=Inches(1.58))
    P.add_hairline(slide, Inches(2.2))

    headers = ["要素", "核心意義", "不佳示範", "推薦示範"]
    rows = [
        [
            "角色 (Role)",
            "設定專業視角、思考深度與專案標準",
            "（未設定角色）",
            [("「你是一位資深的", {}), ("學術專案資料分析師", {"color": T.ORANGE, "bold": True}), ("」", {})],
        ],
        [
            "背景 (Context)",
            "提供任務情境、資料規模與業務目標",
            "「整理這份資料」",
            [("「這是院內 2026 年問卷調查結果，", {}), ("共 500 筆紀錄", {"color": T.ORANGE, "bold": True}), ("」", {})],
        ],
        [
            "格式 (Format)",
            "明確指定輸出結構、載體與段落編排",
            "「給我摘要」",
            [("「請整理成 Markdown 表格，並依重要性", {}), ("條列 3 點具體結論", {"color": T.ORANGE, "bold": True}), ("」", {})],
        ],
        [
            "限制 (Constraint)",
            "劃定不可逾越的安全邊界與過濾條件",
            "（未設定限制條件）",
            [("「不要更動原始檔案，大於 500MB 者", {}), ("僅列清單勿逕行移動", {"color": T.ORANGE, "bold": True}), ("」", {})],
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
        col_widths=[1.8, 3.2, 2.4, 4.6],
        row_label_col=0,
    )
