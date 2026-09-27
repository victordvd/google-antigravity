# slide07.py — Layout Slide: Three Core Workspaces in Antigravity 2.0 (Architecture Overview)

from pptx.util import Inches, Pt
import theme as T
import primitives as P

def build(prs, slide):
    P.add_background(slide)
    P.add_eyebrow(slide, 2, "INTERFACE")

    title_segments = [
        ("三大核心工作區", {"color": T.ORANGE}),
        ("：管理、對話與產出歷程完全透明", {}),
    ]
    P.add_argument_title(slide, title_segments, y=T.TITLE_Y)

    support_segments = [
        ("不需開啟終端機或編輯器，所有操作在", {}),
        ("單一桌面視窗", {"color": T.INK, "bold": True}),
        ("內即可完整掌控與監控。", {}),
    ]
    P.add_supporting_sentence(slide, support_segments, y=Inches(1.58))
    P.add_hairline(slide, Inches(2.2))

    columns = [
        {
            "num": "01",
            "name": "左側邊欄",
            "en": "Sidebar · 導航與專案",
            "desc": "管理工作空間、歷史任務與系統權限設定",
            "features": [
                ("新對話", "快速啟動獨立任務，避免上下文互相污染"),
                ("Projects", "自由切換不同的本機工作目錄與研究資料夾"),
                ("Scheduled Tasks", "設定定時自動化背景排程（Cron）"),
                ("Settings", "靈活切換 Gemini 模型並設定終端沙箱安全等級"),
            ],
            "highlight": False,
        },
        {
            "num": "02",
            "name": "中央畫布",
            "en": "Chat Canvas · 對話與規劃",
            "desc": "使用者發布目標與審核 AI 計畫的主要溝通窗口",
            "features": [
                ("繁中自然語言", "直接輸入目標與驗收標準，由 AI 拆解步驟"),
                ("Slash Commands", "鍵入「/」快速調用 /plan、/goal 專業模式"),
                ("@ Mention 引用", "直接掛載本機檔案、目錄或終端紀錄為上下文"),
                ("多模態拖曳", "支援直接貼上研究圖表截圖與問卷 PDF 供分析"),
            ],
            "highlight": True,  # Main interaction hub
        },
        {
            "num": "03",
            "name": "右側輔助窗格",
            "en": "Auxiliary Pane · 歷程與成果",
            "desc": "即時驗證 AI 產出成果並把關每一次本機檔案異動",
            "features": [
                ("Artifacts 面板", "即時預覽 AI 產出的獨立報告、簡報與試算表"),
                ("Files Changed", "視覺化列出被新增、編輯或移動的本機檔案清單"),
                ("Terminal 面板", "完全透明檢視 AI 於沙箱環境執行的每一條指令"),
                ("Subagents 監控", "觀察後台背景多代理人協同運作的即時狀態"),
            ],
            "highlight": False,
        },
    ]

    col_w = Inches(3.84)
    col_gap = Inches(0.28)
    card_y = Inches(2.45)
    card_h = Inches(4.55)

    for i, col in enumerate(columns):
        x = T.MARGIN_X + i * (col_w + col_gap)
        bg = T.ORANGE_SOFT if col["highlight"] else T.PANEL_BG
        border = T.ORANGE if col["highlight"] else T.PANEL_LN
        line_w = Pt(1.5) if col["highlight"] else Pt(1.0)
        P.add_panel(slide, x, card_y, col_w, card_h, fill=bg, line=border, line_w=line_w)

        # Header tag
        tb, tf = P.textbox(slide, x + Inches(0.24), card_y + Inches(0.22), col_w - Inches(0.48), Inches(0.32))
        P.rich_par(tf, [
            (f"ZONE {col['num']}  ·  ", {"color": T.ORANGE, "mono": True, "bold": True, "size": 11}),
            (col["en"], {"color": T.MUTED, "mono": True, "size": 11}),
        ], first=True)

        # Title
        tb_t, tf_t = P.textbox(slide, x + Inches(0.24), card_y + Inches(0.62), col_w - Inches(0.48), Inches(0.6))
        P.rich_par(tf_t, [(col["name"], {"color": T.INK, "bold": True, "size": 22})], first=True, space_after=3)
        P.rich_par(tf_t, [(col["desc"], {"color": T.INK_SOFT, "size": 12})], first=False)

        P.add_hairline(slide, card_y + Inches(1.42), x=x + Inches(0.24), w=col_w - Inches(0.48),
                       color=T.ORANGE if col["highlight"] else T.HAIRLINE)

        # Features list
        tb_f, tf_f = P.textbox(slide, x + Inches(0.24), card_y + Inches(1.56), col_w - Inches(0.48), Inches(2.7))
        for j, (fname, fdesc) in enumerate(col["features"]):
            P.rich_par(tf_f, [
                (f"▸ {fname}：", {"color": T.ORANGE if col["highlight"] else T.INK, "bold": True, "size": 13}),
                (fdesc, {"color": T.INK_SOFT, "size": 12}),
            ], first=(j == 0), space_after=8, line=1.18)
