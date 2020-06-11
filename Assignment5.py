import xml.etree.ElementTree as ET
from urllib.request import urlopen
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input("Enter Url: ")
data =urlopen(url, context=ctx).read()
tree=ET.fromstring(data)
lst=tree.findall("comments/comment")
count=0
for item in lst:
    x=int(item.find('count').text)
    count=count+x


print("count:",count)