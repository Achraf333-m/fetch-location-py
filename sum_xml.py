import urllib.request as req
import xml.etree.ElementTree as ET
import ssl


ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

def get_sum_xml():
    while True:
        url = input('Enter URL: ')
        if len(url) < 1:  break

        print('retrieving: ', url)
        open_url = req.urlopen(url, context=ctx)
        data = open_url.read()
        print('Retrieved ', len(data), ' characters')
        tree = ET.fromstring(data)
        results = tree.findall('.//count')
        sum = 0
        for i in range(len(results)):
            count = results[i].text
            sum += int(count)
        return sum

sum = get_sum_xml()

print(sum)