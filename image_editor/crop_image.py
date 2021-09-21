from PIL import Image

im = Image.open(r"image_editor/resources/icon.png")

width = 200     # new width of the image
height = 200    # new height of the image

im = im.resize((width, height))