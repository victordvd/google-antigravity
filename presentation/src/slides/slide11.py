# slide09.py — Section 3 Divider: 實務示範

import theme as T
import primitives as P

def build(prs, slide):
    title_segments = [
        ("實務示範：日常行政與研究的", {}),
        ("三大落地場景", {"color": T.ORANGE}),
    ]
    bullets = [
        "示範 A：雜亂檔案智慧歸檔，先預覽清單再執行，杜絕誤刪風險",
        "示範 B：原始資料直接生成多頁簡報，以對話持續微調語氣與圖表",
        "示範 C：公開網站資訊抓取與排程，免寫程式碼也能定期追蹤更新",
    ]
    nav = ["觀念建立", "介面導覽", "實務示範", "最佳實踐"]

    P.add_section_slide(
        slide,
        3,
        "PART 03",
        title_segments,
        bullets,
        nav,
        active_idx=2,
        corner_badge="UNIT 03",
        context=T.DECK_CONTEXT,
    )
