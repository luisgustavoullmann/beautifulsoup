# Podemos utilizar expressões regulares com o BS para web scrapping
# A maioria das função que recebe uma string como argumento também pode receber uma expressão


# Exemplo com lista de produtos, capturar a imagem dos produtos
# Seguem um padrão por estarem na mesma página ../img/gifts/img1.jgp e outros
# Nesse exemplo, as imagens possuem no nome as letras "img" seguidas de um número

# Se nossa intenção é retornar todas as imagens de produtos e buscarmos por tags img (find_all),
# teremos um imagem que não é de um produto.
# Quuando estivermos realizando o scrapping, podemos nos deparar com um situação parecida,
# porque uma página podem existir diversas imagens além das que precisamos. Sejam imagens ocultas,
# imagens em branco utilizadas para espaçamento e alinhamento de elementos e etc.

# Este é o caminho da imagem <img src="../img.gifts.img1.jpg">
# Podemos utilizar a seguinte expressão regular para encontrar estas imagens:
# "\.{2}/img/gifts/img\d*\.jpg"

# Onde:
# \. = Representa o caractere "." litealmente
# {2} = Duas ocorrências de caractere anterior (ponto)
# /img/gifts/img = String literal
# \d = Dígito de zero a nove
# * = Zero ou mais ocorrências do caractere anterior
# \.jpg = ponto liteal e a string jpg

from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

# Abrindo url
html = urlopen("http://www.pythonscraping.com/pages/page3.html")
# Parse do Html
soup = BeautifulSoup(html, "html.parser")

# Encontrando, todos as tags img e pegando somente o atributo que interessa (src) e buscando re neles. 
imagens = soup.find_all("img", {"src":re.compile("\.{2}/img/gifts/img\d*\.jpg")})

# Para cada imagens, print o src
for img in imagens:
    print(img["src"])