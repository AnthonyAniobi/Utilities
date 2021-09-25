"""
A script to generate applicaiton icon for
android applications
"""
from PIL import Image
import os


img_name = "icon.png"
imgSourceDirectory = "image_editor/resources/"
img = Image.open(imgSourceDirectory+img_name)


icon_name = "ic_launcher.png"
output_directory = "image_editor/resources/app_output/"

folderAndSizes = {
    "mipmap-mdpi": 48,
    "mipmap-hdpi": 72,
    "mipmap-xhdpi": 96,
    "mipmap-xxhdpi": 144,
    "mipmap-xxxhdpi": 192}


for k,v in folderAndSizes.items():
    image = img.resize((v, v))
    imagePath = output_directory + k
    os.mkdir(imagePath)
    image = image.save(f"{imagePath}/{icon_name}")

