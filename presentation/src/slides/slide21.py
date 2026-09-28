# slide21.py — Next Steps: Practical Checklist and Follow-up Resources

from pptx.util import Inches, Pt
import theme as T
import primitives as P

def build(prs, slide):
    P.add_background(slide)
    P.add_eyebrow(slide, 4, "ACTION")

    title_segments = [
        ("從", {}),
        ("一件小工作開始", {"color": T.ORANGE}),
        ("嘗試：課後資源與實踐清單", {}),
    ]
    P.add_argument_title(slide, title_segments, y=T.TITLE_Y)

    support_segments = [
        ("AI 代理人的協作技能唯有在", {}),
        ("實際操作中內化", {"color": T.INK, "bold": True}),
        ("；善用院內資源與提示詞模板，本週就能啟動第一次嘗試。", {}),
    ]
    P.add_supporting_sentence(slide, support_segments, y=Inches(1.58))
    P.add_hairline(slide, Inches(2.2))

    panel_w = Inches(5.88)
    panel_gap = Inches(0.33)
    panel_y = Inches(2.55)
    panel_h = Inches(4.35)

    # Left Panel: Action Checklist
    left_x = T.MARGIN_X
    P.add_panel(slide, left_x, panel_y, panel_w, panel_h, fill=T.ORANGE_SOFT, line=T.ORANGE, line_w=Pt(1.5))

    P.add_status_pill(slide, left_x + Inches(0.24), panel_y + Inches(0.24), "實踐清單",
                      bg=T.ORANGE, fg=T.ON_DARK, w=Inches(1.2), h=Inches(0.28), size=11)

    tb_lt, tf_lt = P.textbox(slide, left_x + Inches(0.24), panel_y + Inches(0.68), panel_w - Inches(0.48), Inches(0.55))
    P.rich_par(tf_lt, [("本週即可落地的三步行動", {"color": T.INK, "bold": True, "size": 18})], first=True, space_after=3)
    P.rich_par(tf_lt, [("不需要翻新整套工作流程，先挑一件枯燥重複的小任務開始", {"color": T.INK_SOFT, "size": 12})], first=False)

    P.add_hairline(slide, panel_y + Inches(1.35), x=left_x + Inches(0.24), w=panel_w - Inches(0.48), color=T.ORANGE)

    actions = [
        ("第 1 步：挑選低風險標的", "找一個平時疏於整理的 Downloads 資料夾，或一份剛收集好的問卷 CSV 表格。"),
        ("第 2 步：套用四要素開局", "用「角色＋背景＋格式＋限制」清晰描述需求，並註明「先列清單讓我核可」。"),
        ("第 3 步：檢閱產出與歷程", "觀察右側 Artifacts 生成成果與 Files Changed 變更清單，體驗 Vibe Coding 節奏。"),
    ]
    tb_la, tf_la = P.textbox(slide, left_x + Inches(0.24), panel_y + Inches(1.5), panel_w - Inches(0.48), Inches(2.6))
    for i, (act, desc) in enumerate(actions):
        P.rich_par(tf_la, [
            (f"{act}\n", {"color": T.ORANGE, "bold": True, "size": 13}),
            (desc, {"color": T.INK_SOFT, "size": 12}),
        ], first=(i == 0), space_after=12, line=1.18)

    # Right Panel: Resources & Support
    right_x = left_x + panel_w + panel_gap
    P.add_panel(slide, right_x, panel_y, panel_w, panel_h, fill=T.PANEL_BG, line=T.PANEL_LN)

    P.add_status_pill(slide, right_x + Inches(0.24), panel_y + Inches(0.24), "課後資源",
                      bg=T.INK, fg=T.ON_DARK, w=Inches(1.2), h=Inches(0.28), size=11)

    tb_rt, tf_rt = P.textbox(slide, right_x + Inches(0.24), panel_y + Inches(0.68), panel_w - Inches(0.48), Inches(0.55))
    P.rich_par(tf_rt, [("延伸學習文件與諮詢管道", {"color": T.INK, "bold": True, "size": 18})], first=True, space_after=3)
    P.rich_par(tf_rt, [("院內提供完整錄影回放與提示詞範本卡，陪伴後續實踐", {"color": T.MUTED, "size": 12})], first=False)

    P.add_hairline(slide, panel_y + Inches(1.35), x=right_x + Inches(0.24), w=panel_w - Inches(0.48))

    resources = [
        ("官方技術文件", "https://antigravity.google/docs", "涵蓋完整介面指令、設定檔與進階功能導覽"),
        ("工作坊全程錄影", "Google Meet 自動錄製存檔", "已同步上傳院內共用雲端硬碟，供同仁隨時回放複習"),
        ("Prompt 範本卡", "實務場景模板 (PDF 單頁)", "彙整檔案整理、簡報分析、網站抓取 3 大現成指令範本"),
        ("內部技術支援", "資訊處技術諮詢窗口", "若在安裝或連線遇到技術障礙，歡迎向團隊諮詢協助"),
    ]
    tb_rr, tf_rr = P.textbox(slide, right_x + Inches(0.24), panel_y + Inches(1.48), panel_w - Inches(0.48), Inches(2.6))
    for i, (rname, rsub, rdesc) in enumerate(resources):
        P.rich_par(tf_rr, [
            (f"▸ {rname} ", {"color": T.INK, "bold": True, "size": 13}),
            (f"({rsub})\n", {"color": T.MUTED, "size": 11, "mono": True if "http" in rsub else False}),
            (f"  {rdesc}", {"color": T.INK_SOFT, "size": 12}),
        ], first=(i == 0), space_after=7, line=1.15)
