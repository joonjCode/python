from PIL import Image, ImageFilter

img = Image.open('./images/pikachu.jpg')

# Format , size, mode, 
# print(img.format)

# BLUR,SMOOTH, SHARPEN
filtered_img = img.filter(ImageFilter.BLUR)

# L : Gray
filtered_img = img.convert('L')
filtered_img.save('./images/gray.png', format='png')