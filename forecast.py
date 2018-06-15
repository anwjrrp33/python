import urllib.request
import urllib.parse

API = "http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp"

values = {'stnId': '108'}

stringUrl = 'stnId=108'

params = urllib.parse.urlencode(values)

print("values = " , values)

print("params = " + params)

url = API + "?" + params

print("url = " + url)

data = urllib.request.urlopen(url).read()

text = data.decode("utf-8")

print(text)




