import urllib.parse
import urllib.request
import json

service_url = 'https://maps.googleapis.com/maps/api/geocode/json?key=******'

while True:
    address = input('Enter location: ')
    if len(address) < 1:
        break

    url = service_url + urllib.parse.urlencode({'sensor': 'false',
                                               'address': address})
    print('Retrieving', url)
    uh = urllib.request.urlopen(url)
    data = uh.read()
    print('Retrieved', len(data), 'characters')
    try:
        js = json.loads(data)
    except:
        js = None
    if 'status' not in js or js['status'] != 'OK':
        print('==== Failure To Retrieve ====')
        print(data)
        continue

    print(json.dumps(js, indent=4))

    lat = js["results"][0]["geometry"]["location"]["lat"]
    lng = js["results"][0]["geometry"]["location"]["lng"]
    print('lat', lat, 'lng', lng)
    location = js['results'][0]['formatted_address']
    print(location)