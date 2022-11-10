from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
from lxml import etree

class chrome:

    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('mute-audio')
        self.driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), chrome_options=chrome_options)

    def navegar(self, link):
        self.driver.get(link)

    def sair(self):
        self.driver.quit()

    def crawler(self):
        all_anuncios = {}
        contador = 1
        soup = self.html_pagina()
        #print(soup)
        for i in soup.find_all('a'):
            data = i.text
            if data.count("Hoje às") != 0:#Verifica se o anuncio foi postado hoje
                if not i.get('href').startswith("http"):
                    self.navegar("https://www.olx.pt/" + i.get('href'))

                    #Variáveis Raspadas
                    dados_pagina = etree.HTML(str(self.html_pagina()))
                    print(dados_pagina)
                    id = self.xpath_valido(dados_pagina, '/html/body/div[1]/div[1]/div[3]/div[3]/div[1]/div[#valor1]/div[#valor2]/div/span[1]')
                    titulo = self.xpath_valido(dados_pagina,'/html/body/div[1]/div[1]/div[3]/div[3]/div[1]/div[#valor1]/div[#valor2]/h1')
                    valor = self.xpath_valido(dados_pagina,'/html/body/div[1]/div[1]/div[3]/div[3]/div[1]/div[#valor1]/div[#valor2]/h3')
                    descricao = self.xpath_valido(dados_pagina,'/html/body/div[1]/div[1]/div[3]/div[3]/div[1]/div[#valor1]/div[#valor2]/div')
                    dataPublicacao = self.xpath_valido(dados_pagina,'/html/body/div[1]/div[1]/div[3]/div[3]/div[1]/div[#valor1]/div[#valor2]/span/span')
                    quantidadeCliques = self.xpath_valido(dados_pagina,'/html/body/div[1]/div[1]/div[3]/div[3]/div[1]/div[#valor1]/div[#valor2]/div/span[2]')
                    anunciante = self.xpath_valido(dados_pagina,'/html/body/div[1]/div[1]/div[3]/div[3]/div[2]/div[1]/div[#valor1]/div/a/div/div[#valor2]/h4')
                    localizacao = self.xpath_valido(dados_pagina,'/html/body/div[1]/div[1]/div[3]/div[3]/div[2]/div[2]/div/section/div[#valor1]/div/p[#valor2]')
                    telefone = "Acessar o link no final deste e-mail." #O telefone é protegido e só é exibido ao logar, não implementei nada para buscar essa informação.
                    if dataPublicacao.lower().startswith("hoje"):
                        all_anuncios.update({"Anuncio " + str(contador): {"link: ": "https://www.olx.pt/" + i.get('href'), "Id: ": id, "Titulo: ": titulo, "Preço: ": valor, "Descricao: ": descricao, "Data Publicacao: ": dataPublicacao, "Quantidade Cliques: ": quantidadeCliques, "Anunciante: ": anunciante, "Fone: ": telefone, "localizacao: ": localizacao}} )
                    contador = contador + 1
                
        return all_anuncios
    
    def html_pagina(self):
        try:
            self.driver.execute_script('document.querySelector("#onetrust-accept-btn-handler").click()')
        except:
            pass
        pagina = self.driver.find_element("xpath",'/html/body')
        htmcontent = pagina.get_attribute("outerHTML")
        soup = BeautifulSoup(htmcontent, "html.parser")
        return soup

    def xpath_valido(self, dados, x_path):
        for t in range(1, 10):
            for j in range(1,10):
                xpath_p1 = str(x_path).split(f"#valor1")
                xpath_p2 = xpath_p1[1].split(f"#valor2")
                xpath_final = xpath_p1[0]+str(t)+xpath_p2[0]+str(j)+xpath_p2[1]
                try:
                    texto = dados.xpath(xpath_final)[0].text
                    if texto is not None:
                        return texto
                except:
                    pass