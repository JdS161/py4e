import json
import urllib.request, urllib.parse, urllib.error
import ssl



# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE



url = input('Enter - ')
data = urllib.request.urlopen(url, context=ctx).read()
print('Retrieved', len(data), 'characters')

count = 0
info = json.loads(data)
for item in info["comments"]:
	#print item["count"]
	number = int(item["count"])
	count = count + number
print (count)
