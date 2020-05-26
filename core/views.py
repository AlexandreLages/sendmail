from django.shortcuts import render

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

import smtplib
from email.mime.text import MIMEText


@api_view(['POST'])
def send_email(request):
    if request.method == 'POST':
        emails = request.data['emails']

        for email in emails:
            message = MIMEText(email['mensagem'], 'html')
            message['subject'] = 'Intimação de Protesto'
            message['from'] = email['remetente']
            message['to'] = email['destinatario']

            server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
            server.login(email['remetente'], email['senha'])
            server.sendmail(email['remetente'], email['destinatario'], message.as_string())
            server.quit()

        return Response({"message": "Emails enviados com sucesso!"}, status = status.HTTP_200_OK)
