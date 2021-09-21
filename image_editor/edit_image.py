from PIL import Image

im = Image.open(r"image_editor/2.png")

width, height = im.size

left = 4

top = height/5

right = 154

bottom = 3*height/5

# im1 = im.crop((left, top, right, bottom))
newsize = (300, 300)
im1 = im.resize(newsize)

im1.show()