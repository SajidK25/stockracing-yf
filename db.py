import pymongo
import ssl
def prepare_db():
    client = pymongo.MongoClient("mongodb+srv://dbUser:4URi64pnGMdeZT35@cluster0.7jeln.mongodb.net/myFirstDatabase?retryWrites=true&w=majority",ssl_cert_reqs=ssl.CERT_NONE)
    db = client.stockdata
    return (db,client)