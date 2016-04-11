from pymongo import MongoClient
import nextBus

if __name__ == '__main__':
	client = MongoClient("mongodb://terencelimzw:terencelimzw@ds019950.mlab.com:19950/nus-next-bus")
	db = client.get_default_database()
	db = db["results"]
	results = nextBus.NextBus().getAllBusTimings()
	result = db.insert_one(results)
	print(result)