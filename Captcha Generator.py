from captcha.image import ImageCaptcha
import random
image = ImageCaptcha(width=250, height=100)
a = ""
b = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
for i in range(5):
    a = a+b[random.randint(0,34)]
    res=image.generate(a)
    image.write(a,'ImageOut.png')
print("Image Captcha generated with Random Number.")
