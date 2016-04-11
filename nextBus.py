import requests
import json
import time

class NextBus(object):

	def getAllBusStops(self):
		url ="https://nextbus.comfortdelgro.com.sg/eventservice.svc/BusStops"
		r=requests.get(url)
		return r.json()

	def save_as_json(self):
		response = self.getAllBusStops()
		response['last_updated'] = time.strftime("%d %b %Y %H:%M:%S" , time.localtime())
		with open('busStops.json', 'w') as outfile:
			json.dump(response, outfile)
			print('Success')

	def getBusTiming(self,name):
		url ="https://nextbus.comfortdelgro.com.sg/eventservice.svc/Shuttleservice?busstopname="+name
		r=requests.get(url)
		return r.json()

	def getAllBusTimings(self):
		with open('busStops.json') as data_file:
			data = json.load(data_file)

		data_result = {'time':time.strftime("%d %b %Y %H:%M:%S" , time.localtime())}
		
		names = [r['name'] for r in data['BusStopsResult']['busstops']]

		results = []

		for name in names:
			result = self.getBusTiming(name)['ShuttleServiceResult']
			results.append(result)
		data_result['results'] = results

		return data_result
