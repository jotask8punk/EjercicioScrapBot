from flask import Flask
from TelegramConnect import EnvioTelegram
from config import appID_telegram, appAPIHash_telegram, num_telefono_bot

app = Flask(__name__)

try:
    mensajeador = EnvioTelegram()
    mensajeador.EnviarMensaje(num_telefono_bot, 'JotaMendoza1987', appID_telegram, appAPIHash_telegram, 'mensaje prueba')

    print("Finalizado con éxito")
except (KeyError, TypeError) as e:
    print(str(e))
except Exception as e:
    print(str(e))

''' Aquí le indicamos para que ejecute la aplicación principal de nuestra solución.'''
if __name__ == '__main__':
    app.run()
