from venv import create
import psycopg2
import smtplib
from email.message import EmailMessage

def conexao():
    con = psycopg2.connect(host="localhost", user="user", password="senha", database="db")
    
    #CRIAR A TABELA NO POSTGRES
    #cursor = con.cursor()

    #sql="create table anuncios (id varchar(30))"
    #cursor.execute(sql)
    #con.commit()
    return con

def email(email,titulo, mensagem):
    email_address = ""
    email_passowrd = ""

    msg = EmailMessage()
    msg['Subject'] = titulo
    msg['From'] = email_address
    msg['To'] = email#emails destinatários
    msg.set_content(mensagem)#corpo do email

    #conexao para gmail
    with smtplib.SMTP('smtp.gmail.com: 587') as smtp:
        smtp.starttls()
        smtp.login(email_address, email_passowrd)
        smtp.send_message(msg)
    print("E-mail enviado!")
    
def enderecos_email():
    enderecos = [""]
    return enderecos

def gerar_arquivo(texto):
    try:
        with open('Id.txt', 'a') as file:
            if texto != " ":
                file.write(texto+"|")
        file.close()
    except:
        with create('Id.txt', 'w+') as file:     
            if texto != " ":   
                file.write(texto)
        file.close()