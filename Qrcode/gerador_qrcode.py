import qrcode

img = qrcode.make('https://docs.python.org/3.11/library/index.html')
type(img)
img.save("Py311.png")