from PIL import Image, ImageFilter

img = Image.open('./images/pikachu.jpg')

# Format , size, mode, 
# print(img.format)

# BLUR,SMOOTH, SHARPEN
filtered_img = img.filter(ImageFilter.BLUR)

# L : Gray
filtered_img = img.convert('L')
# crooked = filtered_img.rotate(90)

# resize = filtered_img.resize((300,300))
# thumbnail 
# crooked.save('./images/crooked.png', format='png')
# resize.save('./images/resize.png', format='png')


box = (100, 100, 400,400)
region= filtered_img.crop(box)
region.save('./images/cropped.png', format='png')