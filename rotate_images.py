"""Fix rotation for specific images."""
from PIL import Image
import os

BASE = r"C:\Users\Xiangyu.Cityus\Downloads\lab-equipment\public\images"

fixes = {
    "tektronix-tds2022c.jpg":    90,   # 顺时针旋了90° → 逆时针旋90°修正
    "danfoss-fc302.jpg":         180,
    "ti-boostxl-3phganinv.jpg":  180,
    "ti-launchxl-f28379d.jpg":   180,
    "raspberry-pi5-4gb.jpg":     180,
}

for fname, angle in fixes.items():
    path = os.path.join(BASE, fname)
    img = Image.open(path)
    img = img.rotate(angle, expand=True)
    img.save(path, "JPEG", quality=82, optimize=True)
    print(f"  {fname}: rotated {angle}°")

print("Done.")
