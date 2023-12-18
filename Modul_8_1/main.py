from pymongo.mongo_client import MongoClient

uri = "mongodb+srv://userweb17:<password>@cluster0.r7yz0bl.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
client = MongoClient(uri)
db = client.web17
# Send a ping to confirm a successful connection
try:
    db.cats.insert_many([
        {
            "name": 'Boris',
            "age": 12,
            "features": ['ходить в лоток', 'не дає себе гладити', 'сірий'],
        },
        {
            "name": 'Murzik',
            "age": 1,
            "features": ['ходить в лоток', 'дає себе гладити', 'чорний'],
        },
    ])
except Exception as e:
    print(e)



