# slide02.py — Agenda (Horizontal Process Flow)

from pptx.util import Inches, Pt
from pptx.enum.text import PP_ALIGN
import theme as T
import primitives as P

def build(prs, slide):
    P.add_background(slide)
    P.add_eyebrow(slide, 0, "AGENDA")

    title_segments = [
        ("從思維翻轉到實務落地的", {}),
        ("90 分鐘節奏", {"color": T.ORANGE}),
    ]
    P.add_argument_title(slide, title_segments, y=T.TITLE_Y)

    support_segments = [
        ("跳過繁瑣環境設定，以", {}),
        ("即時螢幕操作示範", {"color": T.INK, "bold": True}),
        ("為核心，完整走過需求發布至成果驗收。", {}),
    ]
    P.add_supporting_sentence(slide, support_segments, y=Inches(1.58))
    P.add_hairline(slide, Inches(2.2))

    # 4 sequential stages
    stages = [
        {
            "num": "01",
            "time": "15 min",
            "title": "觀念建立",
            "subtitle": "思維翻轉與代理人本質",
            "items": [
                "傳統程式設計 vs. Vibe Coding",
                "單輪問答升級為主動代理人",
                "白話描述結果取代手寫步驟",
            ],
            "highlight": False,
        },
        {
            "num": "02",
            "time": "12 min",
            "title": "介面導覽",
            "subtitle": "Antigravity 2.0 儀表板",
            "items": [
                "三大工作區：管理、對話與變更",
                "Slash Commands 快速工作流",
                "@ Mention 脈絡注入本機檔案",
            ],
            "highlight": False,
        },
        {
            "num": "03",
            "time": "43 min",
            "title": "實務示範",
            "subtitle": "三大日常辦公與研究場景",
            "items": [
                "示範 A：磁碟空間與智慧檔案歸檔",
                "示範 B：研究資料摘要與簡報生成",
                "示範 C：公開網站爬蟲與定時排程",
            ],
            "highlight": True,  # Core focus
        },
        {
            "num": "04",
            "time": "20 min",
            "title": "最佳實踐",
            "subtitle": "Prompt 公式與資安防線",
            "items": [
                "提示詞 4 大要素（角色/背景/格式/限制）",
                "三大防線：計畫審核與資料隔離",
                "即時 Q&A 互動與課後行動資源",
            ],
            "highlight": False,
        },
    ]

    card_w = Inches(2.84)
    card_gap = Inches(0.24)
    card_y = Inches(2.55)
    card_h = Inches(4.35)

    for i, s in enumerate(stages):
        x = T.MARGIN_X + i * (card_w + card_gap)
        bg = T.ORANGE_SOFT if s["highlight"] else T.PANEL_BG
        border = T.ORANGE if s["highlight"] else T.PANEL_LN
        line_w = Pt(1.5) if s["highlight"] else Pt(1.0)
        P.add_panel(slide, x, card_y, card_w, card_h, fill=bg, line=border, line_w=line_w)

        # Stage number & time tag
        tb, tf = P.textbox(slide, x + Inches(0.2), card_y + Inches(0.22), card_w - Inches(0.4), Inches(0.35))
        P.rich_par(tf, [
            (f"PART {s['num']}", {"color": T.ORANGE, "mono": True, "bold": True, "size": 12}),
            (f"  ·  {s['time']}", {"color": T.MUTED, "mono": True, "size": 12}),
        ], first=True)

        # Stage Title
        tb_t, tf_t = P.textbox(slide, x + Inches(0.2), card_y + Inches(0.65), card_w - Inches(0.4), Inches(0.75))
        P.rich_par(tf_t, [(s["title"], {"color": T.INK, "bold": True, "size": 20})], first=True, space_after=3)
        P.rich_par(tf_t, [(s["subtitle"], {"color": T.MUTED, "size": 12})], first=False)

        # Hairline inside card
        P.add_hairline(slide, card_y + Inches(1.52), x=x + Inches(0.2), w=card_w - Inches(0.4))

        # Items
        tb_b, tf_b = P.textbox(slide, x + Inches(0.2), card_y + Inches(1.68), card_w - Inches(0.4), Inches(2.4))
        for j, item in enumerate(s["items"]):
            P.rich_par(
                tf_b,
                [("▸ ", {"color": T.ORANGE if s["highlight"] else T.MUTED, "bold": True, "size": 12}),
                 (item, {"color": T.INK_SOFT, "size": 13})],
                first=(j == 0),
                space_after=10,
                line=1.2,
            )
