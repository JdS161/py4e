import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

api_key = False

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
data = urllib.request.urlopen(url, context=ctx).read()
print('Retrieved', len(data), 'characters')

decdata = data.decode()
tree = ET.fromstring(decdata)
counts = tree.findall('.//count')
print('Count:', len(counts))

summ =0
for item in counts:
    it = int(item.text)
    summ += it
print('Sum: ', summ)
