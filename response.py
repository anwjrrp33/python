import urllib.request

name = "C:\\img\\test.jpg"

url = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRLZWgy6Jsc5JO3YBotFUCXGbIPzxX7UDf9EhIXb4IifKAupW4MAg"

data = urllib.request.urlopen(url).read();

with open(name, mode = "wb") as f:
    f.write(data)
    print("저장")
   

