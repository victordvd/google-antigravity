# slide03.py — Section 1 Divider: 觀念建立

import theme as T
import primitives as P

def build(prs, slide):
    title_segments = [
        ("觀念建立：從", {}),
        ("手刻語法", {"color": T.ORANGE}),
        ("到對話式編程", {}),
    ]
    bullets = [
        "Vibe Coding 核心思維：用自然語言描述成果而非死背語法",
        "人機協作典範轉移：從單純諮詢文字建議升級為主動代理人",
        "免安裝觀摩模式：先看懂 AI 如何規劃，再決定日常落地策略",
    ]
    nav = ["觀念建立", "介面導覽", "實務示範", "最佳實踐"]

    P.add_section_slide(
        slide,
        1,
        "PART 01",
        title_segments,
        bullets,
        nav,
        active_idx=0,
        corner_badge="UNIT 01",
        context=T.DECK_CONTEXT,
    )
