# Crawler para Olx.pt
O script foi desenvolvido para buscar os anuncios atuais (hoje) postados no site Olx.pt e os envia por e-mail.
Para que o script funcione corretamente será necessário instalar as bibliotecas selenium, psycopg2 (caso seu BD seja postgres), smtplib e BeautifulSoup.
OBS: A integração com o banco é únicamente para salvar os ID's dos anuncios já enviados.
