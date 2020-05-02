from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.error import HTTPError, URLError

html = urlopen("https://www.udemy.com/")
print(f"Html 1 : {html}")

# Tratando o HTTP error - Erro do servidor
try:
    # Terá erro, pois está fora do ar ou não existe mais a html
    html = urlopen("https://www.udemy.com/erro")
    print(f"Html 2 : {html}")
except HTTPError as erro:
    print(erro)

# URLError, quando a página existe - Erra da página
try:
    # Essa url não existe
    html = urlopen("http://www.1223332121312.com/")
except URLError as erro:
    print(f"Erro URL: {erro}")


# E se a página for recuperada com sucesso mas o conteúdo não for
# o que esperamos?
# Ao acessar um tag em um objeto BeautifulSoup, temos que verificar
# se a mesma existe, caso contrário., o BS retorna None (ou null).
# Ao tentar acessar uma tag em um obj None ocorrerá o AttributeError.

# Tratando o erro de atributo
# para evitar que o programa quebre por uma tag inexistente
html = urlopen("https://www.udemy.com/")
obj = BeautifulSoup(html.read(), "html.parser")

try:
    # Atributo inexistente
    response = obj.html.tag_nao_existente.tag_vai_dar_erro
    print(response)
except AttributeError as erro:
    print(f"Erro: {erro}")


# Testando se um tag NÃO é nula
if obj.html.tag_nao_existente is not None:
    print(obj.html.tag_nao_existente.outra_tag)
else:
    print("objobj.html.tag_nao_existente é None")

# Testando se o html não é None
if obj.html is not None:
    response = obj.html.body
    print("obj.html.body ok")
else:
    print("Obj é None")

# Testando que uma tag dentro do html
if obj.html is not None:
    response = obj.html.bodyTeste
    print(f"Resultado: {responde}") # html ok, bodyTeste é None
else:
    print("obj.html é None")