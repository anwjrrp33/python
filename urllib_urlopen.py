import urllib.request

url = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRGmI-ssOiQCPsHpPOjV5RQtpGf4A4mySZH0rBgOdAAHiJlDBKX"

savename = "test2.jpg"

mem = urllib.request.urlopen(url).read()

with open(savename, mode = "wb") as f:
    f.write(mem)

print("저장")
