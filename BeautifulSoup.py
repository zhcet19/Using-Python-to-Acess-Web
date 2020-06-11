from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

     # Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input("Enter Url: ")
count = int(input("Enter count: "))
position = int(input("Enter position: "))

for i in range(count):
         html = urlopen(url, context=ctx).read()
         soup = BeautifulSoup(html, "html.parser")

         tags = soup('a')
         list1 = []

         for tag in tags:
             x = tag.get('href', None)
             list1.append(x)

         print(list1[position - 1])
         url=list1[position-1]
          
