"""Resize and compress all JPEGs in public/images/ to max 1200px wide, quality 82."""
from PIL import Image
import os, glob

src_dir = r"C:\Users\Xiangyu.Cityus\Downloads\lab-equipment\public\images"
before_total = after_total = 0

for path in sorted(glob.glob(f"{src_dir}/*.jpg")):
    before = os.path.getsize(path)
    before_total += before
    img = Image.open(path)
    w, h = img.size
    if w > 1200:
        img = img.resize((1200, int(h * 1200 / w)), Image.LANCZOS)
    img.save(path, "JPEG", quality=82, optimize=True)
    after = os.path.getsize(path)
    after_total += after
    print(f"  {os.path.basename(path):45s}  {before//1024:4d}KB -> {after//1024:4d}KB")

print(f"\nTotal: {before_total//1024//1024:.1f}MB -> {after_total//1024//1024:.1f}MB  "
      f"(saved {(before_total-after_total)//1024//1024:.1f}MB, "
      f"{100*(before_total-after_total)//before_total}% reduction)")
