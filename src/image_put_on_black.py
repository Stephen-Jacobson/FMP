from PIL import Image

img = Image.open('removed_me.png').convert('RGBA')

# create black background
background = Image.new('RGBA', img.size, (0, 0, 0, 255))
background.paste(img, mask=img.split()[3])  # use alpha as mask

result = background.convert('RGB')
result.save('removed_me.png')