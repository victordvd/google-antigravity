# slide17.py — Extensibility Ecosystem: Agent Skills, MCP, and Plugins

from pptx.util import Inches, Pt
import theme as T
import primitives as P

def build(prs, slide):
    P.add_background(slide)
    P.add_eyebrow(slide, 4, "BEST PRACTICES")

    title_segments = [
        ("超越單次對話：以 ", {}),
        ("Skills、MCP 與 Plugins", {"color": T.ORANGE}),
        (" 打造長期專屬生產力", {}),
    ]
    P.add_argument_title(slide, title_segments, y=T.TITLE_Y)

    support_segments = [
        ("擺脫單次重複下指令的繁瑣，透過", {}),
        ("技能沉澱流程、協議連接外部工具、外掛模組化分發", {"color": T.INK, "bold": True}),
        ("，將 AI 升級為組織級的專屬專家。", {}),
    ]
    P.add_supporting_sentence(slide, support_segments, y=Inches(1.58))
    P.add_hairline(slide, Inches(2.2))

    cards = [
        {
            "num": "架構 01",
            "tag": "流程沉澱",
            "title": "Agent Skills (技能庫)",
            "subtitle": "多步驟 SOP 封裝為標準 Runbook",
            "points": [
                ("漸進加載機制", "平時僅加載名稱與描述，按需喚醒完整指令，大幅節省 Token。"),
                ("結構化流程包", "包含 SKILL.md 指引、輔助 scripts、範例與自訂驗證步驟。"),
                ("版本控制共用", "存放於 .agents/skills/，隨專案 Git 簽入，團隊成員開箱即用。"),
            ],
            "accent": False,
        },
        {
            "num": "架構 02",
            "tag": "工具擴充",
            "title": "MCP 外部協議",
            "subtitle": "開放標準通訊連接外部資料與系統",
            "points": [
                ("通用開放協議", "支援本機 Stdio 進程與遠端 SSE 串流，安全開放外部工具調用。"),
                ("串接內部資源", "透過 mcp_config.json 介接院內資料庫、私有 API 或本機系統。"),
                ("動態工具探索", "啟動自動註冊 Tools 到 AI 工具箱，擺脫手動複製貼上。"),
            ],
            "accent": True,  # Highlighting MCP as the critical integration bridge
        },
        {
            "num": "架構 03",
            "tag": "生態分發",
            "title": "Plugins (外掛套件)",
            "subtitle": "模組化整合與團隊一鍵分發大禮包",
            "points": [
                ("全功能打包袋", "以 plugin.json 為核心，整合 Skills、Rules、MCP 與 Hooks。"),
                ("獨立命名空間", "有效防止跨專案工具與規則命名衝突，權限清晰獨立。"),
                ("彈性開關管理", "可透過設定介面或 CLI 自由啟用/停用，依專案需求抽換。"),
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
        pill_bg = T.ORANGE if c["accent"] else T.INK
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
