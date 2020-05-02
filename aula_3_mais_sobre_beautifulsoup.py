from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("") # url que você quer
obj = BeautifulSoup(html, "html.parser")

# "" = qualquer um class com atributo comments-link
teste = obj.find_all("", {"class":"comments-link"})

# Loop para imprimir todos
for a in teste:
    print(a)

# Loop que pega todos os textos Python e imprime
python = obj.find_all(text="Python")
for a in python:
    print(a)



# Explorando as tags HTML com BS

# .get_text() - Retorna todo o texto da página
print(obj.get_text())

# .tag - Retorna a primeira ocorrência da tag informada
print(obj.title) # primeira ocorrência da tag title

# .tag.name - Retorna o nome da primeira ocorrência da tag informada
print(obj.title.name) # nome da tag informada

# .tag.string - Retorna o texto da primeira ocorrência da tag informada
print(obj.title.string) # text da tah informada

# .tag.parent - Retorna a tag externa à tag atual (tag pai)
print(obj.title.parent)

# .tag.parent.name - Retorna o nome da tag externa à tag atual
print(obj.title.parent.name)

# .tag["atributo"] - Retorna todos os VALORES do atributo informado
print(obj.body["class"]) # todos os valores de class da tag body
print(obj.button["aria-controls"])

# .find(id="descricao") - Retorna a tag que possua o id informado
print(obj.find(id="menu-item"))
