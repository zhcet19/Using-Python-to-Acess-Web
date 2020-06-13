import json
import urllib.request,urllib.parse,urllib.error


serviceurl='http://maps.googleapis.com/maps/api/geocode/json?'

while True:
    address=input("Enter the location to get geocoding: ")
    if len(address)<1 : break


    url=serviceurl + urllib.parse.urlencode({'address':address})

    print('Retrieving',url)
    da=urllib.request.urlopen(url)
    data=da.read().decode()
    print('Retrievred', len(data), 'characters')

    try:
        js=json.loads(data)
    except:
        js=None


    if not js or 'status' not in js or js['status']!='OK':
       print("====FAILED TO RETRIEVE DATA=====")
       print(data)
       continue

    print(json.dumps(js, indent=4))

    lat = js["results"][0]["geometry"]["location"]["lat"]
    lng= js["results"][0]["geometry"]["location"]["lng"]
    print("latitude",lat,"longitude",lng)
    location=js['results'][0]['formatted_adress']

    print("location is:=",location)