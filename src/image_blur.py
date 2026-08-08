from PIL import Image, ImageFilter

img = Image.open('map.png')
img = img.filter(ImageFilter.GaussianBlur(radius=3))
img.save('map_blurred.png')