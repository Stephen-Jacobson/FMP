from PIL import Image

img = Image.open('removed_me.png')

screen_w = 1920
screen_h = 1080

# scale to fit height, maintain aspect ratio
scale = screen_h / img.height
new_w = int(img.width * scale)
new_h = screen_h

img = img.resize((new_w, new_h))

# create black canvas and paste image centred
result = Image.new('L', (screen_w, screen_h), 0)
offset_x = (screen_w - new_w) // 2
result.paste(img, (offset_x, 0))

result.save('removed_me.png')
print(f"image width: {new_w}, offset: {offset_x}")