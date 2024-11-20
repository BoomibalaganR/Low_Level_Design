from mongoengine import connect, connection

# Establish the MongoEngine connection
client = connect(
    host="mongodb://admin:superuserofcyberitus@172.26.11.196/dochub?ssl=true&ssl_cert_reqs=CERT_NONE&replicaSet=rs0"
)


# Access the database (this gives you a pymongo database object)
db = connection.get_db()

# List all collections
collections = db.list_collection_names()
print(collections)
