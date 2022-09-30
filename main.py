import chrome
import olx_funcoes
navegador = chrome.chrome()

navegador.navegar("https://www.olx.pt/d/imoveis/quartos-para-aluguer/porto/?search%5Border%5D=created_at:desc")
anuncioshoje = navegador.crawler()

#CONEXÃO BD
con = olx_funcoes.conexao()
cursor = con.cursor()

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

    string_sql = (f"select id from anuncios where id='{id}'")

    condicao_insert_bd = True

    cursor.execute(string_sql)
    for i in cursor.fetchall():
        if int(id) == int(i[0]):
            condicao_insert_bd  = False
    if condicao_insert_bd :
        string_sql = (f"insert into anuncios(id)  values ({id[1].strip()})")
        cursor.execute(string_sql)
        con.commit()
        olx_funcoes.email(olx_funcoes.enderecos_email(),(f"Corre!!! OLX! - {titulo + ' - ' + valor}"), (f"{corpo_email}"))
navegador.sair()
con.close()
