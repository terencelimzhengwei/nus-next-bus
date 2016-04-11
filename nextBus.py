import requests
import json

class NextBus(object):

	def getAllBusStops(self):
		url ="https://nextbus.comfortdelgro.com.sg/eventservice.svc/BusStops"
		r=requests.get(url)
		return r.json()

	def save_as_json(self):
		response = self.getAllBusStops()
		with open('busStops.json', 'w') as outfile:
			json.dump(response, outfile)
			print('Success')

	def getBusTiming(self,name):
		url ="https://nextbus.comfortdelgro.com.sg/eventservice.svc/Shuttleservice?busstopname="+name
		r=requests.get(url)
		return r.json()