from urllib.request import urlopen
from bs4 import BeautifulSoup
import re # Lib Expressões Regulares

# Variáveis
paginas = set()
paginas_invalidas = set()
novas_paginas = set()

def abrir_pagina(url_da_pagina):
   
    # Definindo variável paginas como global
    global paginas
    global paginas_invalidas

    try:
        if url_da_pagina not in paginas_invalidas:
            html = urlopen(url_da_pagina)
            obj = BeautifulSoup(html, "html.parser")

            # Experrsão regular que vai procurar as palavras
            # Ponto '.' indica que pode estar no meio de qualquer outra palavra e "|" = ou
            serie = (".corinthians.|.flamengo")

            # Busca em todos os "a", a expressão regular
            # re.compile() - função de re
            for link in obj.find_all("a", href=re.compile(serie)):
                if "href" in link.attrs: # se um dos atributos do link é href

                    # Se o link o atributo href não estiver em paginas ou invalidas, atribui a uma nova página
                    if link.attrs["href"] not in paginas and link.attrs["href"] not in paginas_invalidas:
                        novas_paginas = link.attrs["href"]
                        print(novas_paginas)
                        # Add nova em paginas
                        paginas.add(novas_paginas)

                        # Novamente a função recursivamente, caso não ache o atributo nesta página
                        # precisa procurar em outras.
                        abrir_pagina(novas_paginas)
    except:
        # Em caso de erro, add nova página
        paginas_invalidas.add(novas_paginas)


# iniciando a aplicação - buscando no Globo Esporte
abrir_pagina("https://globoesporte.globo.com/")