from PIL import Image, ImageEnhance, ImageFilter

img = Image.open('p.png')
img = img.convert('L')
img = ImageEnhance.Contrast(img).enhance(0.6)

# blur to kill the grain first
img = img.filter(ImageFilter.GaussianBlur(radius=0))

# now threshold
img = img.point(lambda p: 255 if p > 128 else 0)

img.save('pe.png')