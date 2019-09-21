from urllib.request import urlopen
from bs4 import BeautifulSoup

url = "https://www.mcdelivery.co.kr/kr/browse/menu.html?daypartId=1&catId=11"
html = urlopen(url)
source = html.read()
html.close()

soup = BeautifulSoup(source, "lxml")
table = soup.find(id="product-cards")
menus = table.find_all(class_="product-title")
prices = table.find_all(class_="starting-price")
kcal = table.find_all(class_="text-default")

for menu in menus:
				name = menu.get_text()
				print(name)

for price in prices:
				pri = price.get_text()
				print(pri)
				
for cal in kcal:
				c = cal.get_text()
				print(c)

