from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup

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
        laco = True
        all_anuncios = {}
        contador = 1
        soup = self.html_dados()
        for i in soup.find_all("a", class_="css-1bbgabe"):
            data = i.text
            if data.count("Hoje às") != 0:#Verifica se o anuncio foi postado hoje
                self.navegar("https://www.olx.pt/" + i.get('href'))
                try:
                    self.driver.execute_script('document.querySelector("#onetrust-accept-btn-handler").click()')
                except:
                    pass
                try:
                    id = self.driver.find_element("xpath", '//*[@id="root"]/div[1]/div[3]/div[3]/div[1]/div[2]/div[9]/div/span[1]').text
                except:
                    pass
                try:
                    titulo = self.driver.find_element("xpath", '//*[@id="root"]/div[1]/div[3]/div[3]/div[1]/div[2]/div[2]/h1').text
                except:
                    pass
                try:
                    valor = self.driver.find_element("xpath", '//*[@id="root"]/div[1]/div[3]/div[3]/div[1]/div[2]/div[3]/h3').text
                except:
                    pass
                try:
                    descricao = self.driver.find_element("xpath", '//*[@id="root"]/div[1]/div[3]/div[3]/div[1]/div[2]/div[8]/div').text
                except:
                    pass
                try:
                    dataPublicacao = self.driver.find_element("xpath", '//*[@id="root"]/div[1]/div[3]/div[3]/div[1]/div[2]/div[1]/span/span').text
                except:
                    pass
                try:
                    quantidadeCliques = self.driver.find_element("xpath", '//*[@id="root"]/div[1]/div[3]/div[3]/div[1]/div[2]/div[9]/div/span[2]').text
                except:
                    pass
                try:
                    anunciante = self.driver.find_element("xpath", '//*[@id="root"]/div[1]/div[3]/div[3]/div[2]/div[1]/div[2]/div/a/div/div[2]/h4').text
                except:
                    pass
                try:
                    localizacao = self.driver.find_element("xpath", '//*[@id="root"]/div[1]/div[3]/div[3]/div[2]/div[2]/div/section').text         
                except:
                    pass
                try:
                    self.driver.execute_script('document.querySelector("#root > div.css-50cyfj > div.css-1on7yx1 > div:nth-child(3) > div.css-1vnw4ly > div.css-1p8n2mw > div > div > div.css-1saqqt7 > div > button").click()')
                    telefone = self.driver.find_element("xpath", '//*[@id="root"]/div[1]/div[3]/div[3]/div[1]/section/div[2]/div/div[2]/div[2]/div/div/a').text
                except:
                    telefone = "Apenas mensagens pelo site."
                try:
                    if dataPublicacao.startswith("hoje"):
                        all_anuncios.update({"Anuncio " + str(contador): {"link: ": "https://www.olx.pt/" + i.get('href'), "Id: ": id, "Titulo: ": titulo, "Preço: ": valor, "Descricao: ": descricao, "Data Publicacao: ": dataPublicacao, "Quantidade Cliques: ": quantidadeCliques, "Anunciante: ": anunciante, "Fone: ": telefone, "localizacao: ": localizacao}} )
                except:
                    pass
                contador +=1
        self.sair()
        return all_anuncios
    
    def html_dados(self):
        pagina = self.driver.find_element("xpath",'//*[@id="root"]/div[1]/div[2]')
        htmcontent = pagina.get_attribute("outerHTML")
        soup = BeautifulSoup(htmcontent, "html.parser")
        return soup

