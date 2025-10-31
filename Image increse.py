from PIL import Image, ImageEnhance, ImageFilter

# Load image
img = Image.open("Samsung Recovery.jpg")

# Sharpen and enhance
enhanced = img.filter(ImageFilter.SHARPEN)
enhanced = ImageEnhance.Contrast(enhanced).enhance(1.2)

# Resize 2x
upscaled = enhanced.resize((img.width * 2, img.height * 2), Image.LANCZOS)

# Save high-DPI version
upscaled.save("Samsung's Recovery.png", dpi=(300, 300))

print("✅ Image enhanced & 2X upscaled (300 DPI)")