from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
import re


# Erro 403, porque alguns sites tratam scraping
# html = urlopen("")

# Abrindo url
# Temos que usar o request
# User-Agent - Informa que quem está fazendo a requisição é um browser
response = Request("https://www.tudogostoso.com.br/", headers={"User-Agent":"Mozilla/5.0"})
html = urlopen(response).read()
# Parse do Html
soup = BeautifulSoup(html, "html.parser")

# Dentro da tag a, atributo href, pegar a re de categorias
# O site alterou, começa com número, ver aula de RE
links = soup.find_all("a", {"href":re.compile("/categorias/.*\.php")})

# Para cada imagens, print o src
for l in links:
    print(l["href"])