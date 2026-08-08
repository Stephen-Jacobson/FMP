from rembg import remove
from PIL import Image

img = Image.open('me.jpeg')
result = remove(img)
result.save('removed_me.png')