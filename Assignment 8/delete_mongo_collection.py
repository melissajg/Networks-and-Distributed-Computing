from pymongo import MongoClient, database

DBName = "test" #Use this to change which Database we're accessing
connectionURL = "mongodb+srv://melissajg:327-hw5-pw@cluster0.ac0ucdm.mongodb.net/?retryWrites=true&w=majority"
#Put your database URL here
sensorTable = 'traffic data' #Change this to the name of your sensor data table

client = MongoClient(connectionURL)

cluster = connectionURL
client = MongoClient(cluster)
db = client[DBName]
sensorTable = db[sensorTable]

query = {"topic": {"$regex": "Melissa"}}
d = sensorTable.delete_many(query)
 
print(d.deleted_count, " documents deleted !!")
