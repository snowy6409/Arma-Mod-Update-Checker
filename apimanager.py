import datetime
import requests
import json
class SteamAPIManager:
	__instance = None
	@staticmethod
	def getInstance():
		if SteamAPIManager.__instance == None:
			SteamAPIManager()
		return SteamAPIManager.__instance
	@staticmethod
	def getWorkshopMod(itemID):
		Workshop_Item_URL = "https://api.steampowered.com/ISteamRemoteStorage/GetPublishedFileDetails/v1"
		Data = {"itemcount":1,"publishedfileids[0]":itemID}
		API_Result = requests.post(Workshop_Item_URL,data = Data)
		return json.loads(API_Result.text)
	def __init__(self):
		if SteamAPIManager.__instance != None:
			raise Exception("This class is a singleton")
		else:
			SteamAPIManager.__instance = self