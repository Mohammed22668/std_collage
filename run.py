import os
import socket
import webbrowser
import datetime
# import qrcode
# import qrcode.image.svg

hostname=socket.gethostname()
IPAddr=socket.gethostbyname(hostname)
port = 8000
url = f'http://{IPAddr}:{port}/'
webbrowser.open(url)
# os.system('../venv/Scripts/activate')

##########################
# img = qrcode.make(url, image_factory=qrcode.image.svg.SvgImage)
# with open('../qr.svg', 'wb') as qr:
#     img.save(qr)
##################################    

# url = "http://127.0.0.1:8000/"
# webbrowser.open(url)
os.system(f'cmd /k "python manage.py runserver {IPAddr}:{port}"')