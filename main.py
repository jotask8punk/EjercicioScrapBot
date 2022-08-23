from flask import Flask
from scraper import scraper
from TelegramConnect import EnvioTelegram
from CapaBD import capabd
from config import appID_telegram, appAPIHash_telegram, num_telefono_bot, TOKEN_TELEGRAM

app = Flask(__name__)

try:
    claseScraper = scraper()
    cantDisp = claseScraper.EscrapearObjetivo()
    capadats = capabd()
    ultimoDisp = capadats.LeerUltimo()
    if ultimoDisp == "" or ultimoDisp != cantDisp:
        capadats.insertarHistorico(cantDisp)
        mensajeador = EnvioTelegram()
        listaDest = mensajeador.ListaDestinatarios(TOKEN_TELEGRAM)
        for UsuId in listaDest:
            mensajeador.EnviarMensaje(num_telefono_bot, UsuId, appID_telegram, appAPIHash_telegram,
                                      'El artículo Impresora Multifuncional Epson Ecotank L3110 ha actualizado su disponible: ' + cantDisp)
    else:
        capadats.insertarHistorico(cantDisp)

    print("Finalizado con éxito")
except (KeyError, TypeError) as e:
    print(str(e))
except Exception as e:
    print(str(e))


''' Aquí le indicamos para que ejecute la aplicación principal de nuestra solución.'''
if __name__ == '__main__':
    app.run()
