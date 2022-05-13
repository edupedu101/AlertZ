import os
import requests
url = 'localhost:8000/api/addImagen'
files = {'media': open('../test.jpg', 'rb')}
requests.post(url, files=files)