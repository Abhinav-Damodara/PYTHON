import pyqrcode
import png
from pyqrcode import QRCode
s = "www.geeksforgeeks.org"
url=pyqrcode.create(s)
url.svg("myqrcode.svg",scale=8)
url.png('myqrcode.png', scale = 6)