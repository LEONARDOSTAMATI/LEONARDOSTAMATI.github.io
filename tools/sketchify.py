#!/usr/bin/env python3
"""
Pencil-sketch filter for an image.
Usage: python tools/sketchify.py input_path output_path [intensity]
- intensity: 0.0–1.0 (default 0.6) controls sketch strength
"""
import sys
from PIL import Image, ImageOps, ImageFilter
import numpy as np

def to_sketch(img: Image.Image, intensity: float = 0.6) -> Image.Image:
    gray = ImageOps.grayscale(img)
    inv = ImageOps.invert(gray)
    blur_radius = max(2, int(round(min(img.size) * 0.01)))  # scale with image size
    blurred = inv.filter(ImageFilter.GaussianBlur(blur_radius))
    g = np.asarray(gray, dtype=np.float32)
    b = np.asarray(blurred, dtype=np.float32)
    # Color dodge: result = g * 255 / (255 - b)
    dodge = np.minimum(255, (g * 255.0) / (255.0 - b + 1e-5))
    # Blend original gray with dodge for controllable intensity
    out = (1.0 - intensity) * g + intensity * dodge
    out = np.clip(out, 0, 255).astype(np.uint8)
    return Image.fromarray(out)

def main():
    if len(sys.argv) < 3:
        print("Usage: python tools/sketchify.py input_path output_path [intensity]")
        sys.exit(1)
    inp = sys.argv[1]
    outp = sys.argv[2]
    intensity = float(sys.argv[3]) if len(sys.argv) > 3 else 0.6
    img = Image.open(inp).convert('RGB')
    sketch = to_sketch(img, intensity=intensity)
    # Optional paper texture overlay (soft noise)
    noise = Image.effect_noise(sketch.size, 8).convert('L')
    noise = noise.point(lambda p: int(p * 0.08))
    textured = ImageChops.add(sketch, noise) if 'ImageChops' in globals() else sketch
    textured.save(outp, quality=92)
    print(f"Saved sketch to {outp}")

if __name__ == '__main__':
    try:
        from PIL import ImageChops  # lazy import
    except Exception:
        pass
    main()
