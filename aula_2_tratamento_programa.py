from urllib.request import urlopen
from urllib.error import HTTPError, URLError
from bs4 import BeautifulSoup

# Função que recebe como parâmetro a url que vai ser usada
def getTitulo(url):
    #Tratando os erros que podem ocorrer
    try:
        html  = urlopen(url)
    except HTTPError as erro:
        print("Erro HTTP: {erro}")
        return None
    except URLError as erro:
        print("Erro URL: {erro}")
        return None
    except: # caso tenha algum outro erro
        print("Erro na página")
        return None


    # Tratando os erros que podem ocorrer com BS
    try:
        # Retornando o parser da HTML para obj
        obj = BeautifulSoup(html.read(), "html.parser")

        # É aqui que você diz o que quer pegar
        titulo = obj.body.h1 # recebe o primeiro h1 da url
    except AttributeError as erro:
        print("Erro de atributo: {erro}")
        return None
    except:
        print("Erro ao acessar conteúdo da página")
        return None

    # Caso não dê erro nenhum
    return titulo # retorna o conteúdo da variável título


# Usando a função - URL solicitada ao usuário no input
titulo = getTitulo(input("Informa a URL completa:"))

if titulo is not None:
    print(titulo)
else:
    print("Não encontrado.")


# Como um sistema de web scrapping normalmente é executado durante horas
# ou até mesmo dias, é muito importante que sejam tratados todos os possíveis erros
# para que o sistema não aborte a execução e você não perca tempo entre o ajuste do erro
# e uma nova execução.