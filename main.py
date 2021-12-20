from fastapi import FastAPI
from typing import Optional
import pymongo

PASSWORD = open('.mongopass').read()
client = pymongo.MongoClient(f"mongodb+srv://{PASSWORD}@cluster0.k244v.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = client.magoole
sites = db.sites
app = FastAPI(title="Magoole; Mes rechercher, Mes données, Mes droits", description="Un moteur de recherche où vos données sont respectées", version="0.0.0")

try:
    sites.drop_index([('title', 'text'), ('description', 'text'), ('word_list', 'text'), ('alt_list', 'text'), ('url', 'text')])
except:
    ...
finally:
    sites.create_index([('title', 'text'), ('description', 'text'), ('word_list', 'text'), ('alt_list', 'text'), ('url', 'text')])


def stringifyID(document):
    document['_id'] = str(document['_id'])
    return document


@app.get("/")
def root():
    return {"code": 200, "message": "Nothing here but welcome on our api !"}


@app.get("/search")
def search(q: str):
    query = q
    results = [stringifyID(site) for site in sites.find({'$text': {'$search': query}})]
    for i in results:
        print(i)
    return {"code": 200, "results": results}
