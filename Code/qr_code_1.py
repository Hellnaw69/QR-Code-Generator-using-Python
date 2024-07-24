'''
6, 7, 8 lines of code is important
to generate a basic qr code
'''

import qrcode as qr
img = qr.make("https://www.instagram.com/p/C1U_RtuyM0XEftvbD0NOpy3sAqY1uhtWMRilck0/")
img.save("1.png")