from bs4 import BeautifulSoup

html = """
<html><body>
  <h1 id='title'>스크레이핑이란?</h1>
  <p>웹 페이지를 분석하는것</p>
  <p id='body'>원하는 부분을 출력하는 것</p>
</body></html>
"""

soup = BeautifulSoup(html, 'html.parser')

title = soup.find(id="title")
body = soup.find(id="body")

print("#title = " + title.string)
print("#body = " + body.string)
