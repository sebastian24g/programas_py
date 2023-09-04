import smtplib
import os
from dotenv import load_dotenv
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

load_dotenv() # carga de variaves desde .env

remitente = os.getenv('USER')
destinatario = 'melon24g@gmail.com'
asunto = 'Test'

msg = MIMEMultipart( )
msg['subject'] = asunto
msg['from'] = remitente
msg['to'] = destinatario

with open('email.html','r') as archivo:
    html = archivo.read()
    
# adjuntar contenido HTML
msg.attach(MIMEText(html, 'html'))
   
#conexion a un carreo electronico saliente
server = smtplib.SMTP('smtp.gmail.com',587)
#seguridad de connexion
server.starttls()
server.login(remitente, os.getenv('PASS'))

#envio de correo electronico 
server.sendmail(remitente, 
                destinatario, 
                msg.as_string())
server.quit()