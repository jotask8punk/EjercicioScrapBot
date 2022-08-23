''' Se colocan las librerías que usaremos'''
from asyncio.windows_events import NULL
from logging import NullHandler
from telethon.sync import TelegramClient
from telethon.tl.types import InputPeerUser, InputPeerChannel
from telethon import TelegramClient
from telethon.errors import SessionPasswordNeededError
import requests


class EnvioTelegram:
    def EnviarMensaje(self, num_telefono, idChatUsuarios, idApp, HashApi, mensaje):
        ''' App_ID, Api_Hash obtenidos desde web de Telegram de autorización de aplicación'''
        appID = idApp
        appAPIHash = HashApi
        ''' Mensaje que se enviará al chat del Bot de Telegram'''
        mensaje1 = mensaje
        '''mensaje1 = "Envío de mensaje desde aplicación Python a chat de bot de Telegram por ProyectoA, usando el ID de Chat 👍"'''
        ''' Número de telefóno móvil (incluyendo código de país)'''
        numeroTelefono = num_telefono
        ''' O bien, si no queremos usar el nombre de usuario, el ID del chat al que se enviará el mensaje'''
        idChat = idChatUsuarios

        print("Conectando con Telegram...")
        ''' Creamos sesión de Telegram'''
        clienteTelegram = TelegramClient('sesión', appID, appAPIHash)

        print("Iniciando sesión en Telegram...")
        ''' Iniciamos una sesión de Telegram'''
        clienteTelegram.connect()

        ''' Si se ejecuta por primera vez, Telegram generará un código de inicio de sesión'''
        ''' en el chat de Telegram "Telegram", si es así, la aplicación'''
        ''' pedirá este código de inicio de sesión'''
        print("Comprobando autorización...")
        if not clienteTelegram.is_user_authorized():
            clienteTelegram.send_code_request(numeroTelefono)
            ''' Pedimos el código de inicio de sesión que haya enviado Telegram al usuario'''
            try:
                clienteTelegram.sign_in(numeroTelefono, input('Introduzca el Código de inicio de sesión: '))
            except SessionPasswordNeededError:
                clienteTelegram.sign_in(numeroTelefono, input('Introduzca la contraseña: '))

        ''' *** Enviar mensaje usando el ID de chat de Telegram ***'''
        try:
            print("Creando un receptor de Telegram a partir del ID de chat de Tetlegram...")
            receptorChat = clienteTelegram.get_input_entity(idChat)

            async def main():
                ''' Enviamos el mensaje al chat de Telegram'''
                ''' Se enviará al chat de Telegram del Bot con ID indicado en el receptor'''
                print("Enviando mensaje a chat de Bot del receptor de Telegram (ID Chat)...")
                await clienteTelegram.send_message(receptorChat, mensaje1)
                ''' Solo a modo informativo, obtenemos el nombre del Bot de Telegram al que enviamos el mensaje'''
                print("Enviado mensaje a chat de Bot [{}] de Telegram".format(idChat))

            ''' Para que se ejecute la tarea anterior del método asíncrono'''
            clienteTelegram.loop.run_until_complete(main())

        except Exception as e:
            print("Se ha producido un error en el envío por ID de Chat: {}".format(e))


        ''' Desconectamos la sesión de Telegram abierta'''
        print("Desconectando sesión de Telegram...")
        clienteTelegram.disconnect()
        print("Desconectado y fin del programa")

    def ListaDestinatarios(self, token):
        url = 'https://api.telegram.org/bot'+token+'/getUpdates'
        response = requests.get(url)
        datos = response.json()
        listaUserNames = []
        for i in datos['result']:
            for j in i['message']['chat']:
                if (j == 'username'):
                    '''print(i['message']['chat']['username'])'''
                    if listaUserNames.count(i['message']['chat']['username']) == 0:
                        listaUserNames.append(i['message']['chat']['username'])
        '''print(listaUserNames)'''
        return listaUserNames