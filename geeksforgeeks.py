import qrcode as qr
img = qr.make("https://www.geeksforgeeks.org/user/hackerrafiq/")
img.save("geekforgeeks.png")