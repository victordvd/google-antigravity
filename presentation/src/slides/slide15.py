# slide13.py — Section 4 Divider: 最佳實踐與安全守則

import theme as T
import primitives as P

def build(prs, slide):
    title_segments = [
        ("治理守則：下好 Prompt 與", {}),
        ("防護安全邊界", {"color": T.ORANGE}),
    ]
    bullets = [
        "Prompt 四大關鍵要素：給足角色、背景、格式與限制，一次就做對",
        "代理人協作的三大防線：計畫審核、機密資料隔離與結果人工查驗",
        "從一件小工作開始嘗試：挑選日常低風險重複性任務展開第一步",
    ]
    nav = ["觀念建立", "介面導覽", "實務示範", "最佳實踐"]

    P.add_section_slide(
        slide,
        4,
        "PART 04",
        title_segments,
        bullets,
        nav,
        active_idx=3,
        corner_badge="UNIT 04",
        context=T.DECK_CONTEXT,
    )
