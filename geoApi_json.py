import json
import ssl
import urllib
from urllib import request as req, parse as prs, error as err

# create ssl context
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

API_KEY = "********************************"
service_url = "https://maps.googleapis.com/maps/api/geocode/json?"

while True:
    address = input("Enter address: ")

    param = dict()
    param["address"] = address
    param["key"] = API_KEY

    url = service_url + prs.urlencode(param)

    open_url = req.urlopen(url, context=ctx)
    print("Retrivieving url...")

    read_url = open_url.read().decode()
    print("Reading url...")

    try:
        data = json.loads(read_url)
    except:
        data = None

    print("looking for your city :) ...")
    # makig sure theuser does not see a traceback error
    if not data or data["status"] != "OK" or 'status' not in data:
        print("Address not found, please try again :(")
        continue
    lat = round(data["results"][0]["geometry"]["location"]["lat"], 3)
    lng = round(data["results"][0]["geometry"]["location"]["lng"], 3)

    result = "latitude: " + str(lat) + ", longitude: " + str(lng)
    print(result)
