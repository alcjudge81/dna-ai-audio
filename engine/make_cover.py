import os, random
from PIL import Image, ImageDraw, ImageFont
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
W = 1400; im = Image.new("RGB", (W, W), "#0B3F45"); d = ImageDraw.Draw(im); random.seed(7)
cols = ["#55C4CF", "#F1A75B", "#E5ECF2", "#2A8C96"]
for i in range(40):
    x = 110 + i * 30; h = 60 + int(150 * abs(((i * 37) % 17) / 17 - 0.5) * 2)
    d.rounded_rectangle([x, 1080 - h, x + 14, 1080], 6, fill=cols[i % 4]); d.rounded_rectangle([x, 1100, x + 14, 1100 + h], 6, fill=cols[(i + 2) % 4])
def font(sz):
    for p in ["/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf"]:
        if os.path.exists(p): return ImageFont.truetype(p, sz)
    return ImageFont.load_default()
d.text((110, 150), "DNA", font=font(250), fill="#E5ECF2"); d.text((110, 430), "Computing", font=font(190), fill="#E5ECF2")
d.text((110, 690), "Audio Course", font=font(110), fill="#55C4CF")
im.save(f"{ROOT}/cover.jpg", quality=88); print("cover ok")
