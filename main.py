import chrome
import olx_funcoes
navegador = chrome.chrome()

navegador.navegar("https://www.olx.pt/d/imoveis/quartos-para-aluguer/porto/?search%5Border%5D=created_at:desc")
anuncioshoje = navegador.crawler()

#CONEXÃO BD
#con = olx_funcoes.conexao()
#cursor = con.cursor()

print("Em execução..")

for i in anuncioshoje:

    #VARIÁVEIS RASPADAS
    id = anuncioshoje[i]["Id: "]
    id = id.replace("ID:","").strip()
    titulo = anuncioshoje[i]["Titulo: "]
    descricao = anuncioshoje[i]["Descricao: "]
    link = anuncioshoje[i]["link: "]
    valor = anuncioshoje[i]["Preço: "]
    data = anuncioshoje[i]["Data Publicacao: "]
    qtdCliques = anuncioshoje[i]["Quantidade Cliques: "]
    anunciante = anuncioshoje[i]["Anunciante: "]
    fone = anuncioshoje[i]["Fone: "]
    local = anuncioshoje[i]["localizacao: "]

    corpo_email = (f"ID do Anúncio: {id}\nValor: {valor}\nLocal: {local}\nData: {data}\nAnunciante: {anunciante}\n{qtdCliques}\n{descricao}\nLink: {link}")
    
    condicao_insert_bd = True

    try:
        ids =  open('Id.txt', 'r')
        id_comparar = ids.read().split("|")
    except:
        id_comparar = ()

    for a in id_comparar:
        if id == a:
            condicao_insert_bd  = False
    if condicao_insert_bd :
        olx_funcoes.gerar_arquivo(str(id))
        olx_funcoes.email(olx_funcoes.enderecos_email(),(f"Corre!!! OLX! - {titulo + ' - ' + valor}"), (f"{corpo_email}"))
