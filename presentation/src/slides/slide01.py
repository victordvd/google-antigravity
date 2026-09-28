# slide01.py — Opening Cover Slide (editorial-light)

from pptx.util import Inches
import theme as T
import primitives as P

def build(prs, slide):
    title_segments = [
        ("自然語言驅動", {"color": T.ORANGE}),
        ("的日常", {}),
        ("工作自動化\n", {"color": T.ORANGE}),
        ("Google Antigravity 2.0 與 Vibe Coding 實務", {}),
    ]
    P.add_cover_slide(
        slide,
        title_segments,
        variant="editorial-light",
        context=T.DECK_CONTEXT,
        subtitle="中央研究院職員實務工作坊 · 90 分鐘全流程解析與三大工作場景示範",
        presenter="資訊處 / 專題分享",
        date="2026-09",
        title_size=36,
    )

    icon_path = str(T.ASSETS_DIR / "antigravity-icon.png")
    pic = slide.shapes.add_picture(icon_path, T.MARGIN_X, Inches(1.22), height=Inches(0.85))
    P.no_shadow(pic)
