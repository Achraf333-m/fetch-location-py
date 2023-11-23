import urllib.request as req, urllib.parse as parse, urllib.error as err
import xml.etree.ElementTree as ET
import ssl

api_key = False

if api_key is False:
    api_key = 42
    serviceCurl = 'http://py4e-data.dr-chuck.net/xml?'
else:
    serviceCurl = 'https://maps.googleapis.com/maps/api/geocode/xml?'

# here I am ignoring the SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    address = input('Enter location: ')
    if len(address) < 1: break

    parms = dict()
    parms['address'] = address
    if api_key is not False: parms['key'] = api_key
    url = serviceCurl + parse.urlencode(parms)
    print('Retrieving ', url)
    uh = req.urlopen(url, context=ctx)

    data = uh.read()
    print('Retrieved ', len(data), ' characters')
    print(data.decode())
    tree = ET.fromstring(data)

    results = tree.findall('result')
    lat = results[0].find('geometry').find('location').find('lat').text
    lng = results[0].find('geometry').find('location').find('lng').text
    location = results[0].find('formatted_address').text

    print('lat ', lat, ' lng ', lng)
    print(location)