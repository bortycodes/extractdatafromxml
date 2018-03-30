import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

#http://py4e-data.dr-chuck.net/comments_85471.xml
#http://py4e-data.dr-chuck.net/comments_42.xml

while True:
    url = input('Enter location: ')
    if len(url) < 1: break

    print('Retrieving', url)
    uh = urllib.request.urlopen(url)
    data = uh.read()
    print('Retrieved', len(data), 'characters')

    tree = ET.fromstring(data)

    sum = 0
    comments = tree.findall('.//comment')
    for item in comments:
        sum = sum + int(item.find('count').text)

    print('Count: ', len(comments))
    print('Sum: ', sum)