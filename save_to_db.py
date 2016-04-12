from pymongo import MongoClient
from credentials import credentials
import nextBus

if __name__ == '__main__':
	client = MongoClient("mongodb://"+credentials['username']+":"+credentials['password']+"@ds019950.mlab.com:19950/nus-next-bus")
	db = client.get_default_database()
	db = db["results"]
	results = nextBus.NextBus().getAllBusTimings()
	result = db.insert_one(results)
	print(result)