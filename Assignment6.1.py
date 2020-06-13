import json
import urllib.request,urllib.parse,urllib.error
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input("Enter Url: ")
da=urllib.request.urlopen(url)
data=da.read().decode()

sum=0
info=json.loads(data)
for i in info["comments"]:
    sum=sum+i["count"]


print(sum)