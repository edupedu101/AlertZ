import os
import requests
url = 'http://localhost:8000/api/addImagen'
data = {'refcode':'2743847954'}
file = {'imagen' : open('../test.jpg', 'rb')}

x = requests.post(url, data, files=file,auth=('paco','EDUpedu1'))
print(x.content)