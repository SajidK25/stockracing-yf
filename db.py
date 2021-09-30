import pymongo
import ssl
def prepare_db():
    client = pymongo.MongoClient("mongodb+srv://main:sPohhl8doYXHuah6@cluster0.92gdy.mongodb.net/myFirstDatabase?retryWrites=true&w=majority",ssl_cert_reqs=ssl.CERT_NONE)
    db = client.stockdata
    return (db,client)