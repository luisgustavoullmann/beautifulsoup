from urllib.request import urlopen
from bs4 import BeautifulSoup

# Link do website de economia do g1
html = urlopen("https://g1.globo.com/economia/")
obj = BeautifulSoup(html.read(), "html.parser") # parse de um html

# Loop
# find_all("a") - busca todos as tags a
# .get - retornar todos os links dentro dos hrefs
for link in obj.find_all("a"):
    print(link.get("href"))