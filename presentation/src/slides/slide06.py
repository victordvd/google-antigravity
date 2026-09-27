# slide06.py — Section 2 Divider: 介面導覽

import theme as T
import primitives as P

def build(prs, slide):
    title_segments = [
        ("工具駕馭：", {}),
        ("Antigravity 2.0", {"color": T.ORANGE}),
        ("核心介面導覽", {}),
    ]
    bullets = [
        "三大核心工作區：左側邊欄、中央對話畫布與右側輔助窗格",
        "Slash Commands：輸入斜線「/」快速叫出專業代理人工作流程",
        "@ Mention 引用：精準將本地檔案、資料夾與終端紀錄注入對話",
    ]
    nav = ["觀念建立", "介面導覽", "實務示範", "最佳實踐"]

    P.add_section_slide(
        slide,
        2,
        "PART 02",
        title_segments,
        bullets,
        nav,
        active_idx=1,
        corner_badge="UNIT 02",
        context=T.DECK_CONTEXT,
    )
