import datetime
from db import MongoManager

class capabd:
    def insertarHistorico(self, disponibles):
        db_client = MongoManager()
        collection = db_client.db.get_collection("historico_disponibles")
        collection.insert_one({
                "fechaHora": datetime.datetime.now(),
                "fecha": datetime.datetime.today(),
                "disponibles": disponibles
            })

    def LeerUltimo(self):
        coll=""
        try:
            db_client = MongoManager()
            coll = db_client.db.get_collection("historico_disponibles").find().sort({'fechaHora': -1}).limit(1)
            return coll
        except Exception as e:
            print(str(e))
            return coll