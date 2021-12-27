import tkinter as tk
import json
from tkinter import filedialog
import os
from apimanager import SteamAPIManager
import datetime
class FileManager:
	__instance = None
	@staticmethod
	def getInstance():
		if FileManager.__instance == None:
			FileManager()
		return FileManager.__instance
	##This method reads from the local update file if it exists and if it dose not it will create it
	@staticmethod
	def readJsonFile():
		try:
			with open('localupdates.json', 'r') as openfile:
				json_object = json.load(openfile)
			return json_object
		except FileNotFoundError:
			print("Not Found Creating Base File")
			FileManager.createJsonFile()
	##This method is used to create the new update file and populate it. The directory it is looking for is the workshop
	##folder with the id for Arma 3 (107410)
	@staticmethod
	def createJsonFile():
		root = tk.Tk()
		root.withdraw()
		folder_path = filedialog.askdirectory(title = "Path to steam workshop content for arma '107410' ")
		if '107410' not in folder_path:
			Exception("ERROR FILE DIRECTORY MUST BE 107410 usually located in steamapps\workshop\content")
			exit()
		root = folder_path
		dirlist = [ item for item in os.listdir(root) if os.path.isdir(os.path.join(root, item)) ]
		modlist = []
		for item in dirlist:
			modlist.append({"id":item,"dt":FileManager.getUpdate(itemid=item)})
		basejson = {
			"dirpath":root,
			"mods":modlist
		}
		with open('localupdates.json','w') as outfile:
			json.dump(basejson,outfile)	
	##This method is used to update all mods once they have been updated by the user
	@staticmethod
	def updateJsonFile():
		item = SteamAPIManager.getWorkshopMod(itemid)
		try:
			try:
				lastupdate = item["response"]["publishedfiledetails"][0]["time_updated"];
				dt = datetime.datetime.fromtimestamp(lastupdate)
				return str(dt)
			except KeyError:
				print("This mod has no published update time")
				return "NA"
		except KeyError:
			print("Mod: " + itemid + " is most likely hidden or not public")
			return "NA"
	def getUpdate(itemid):
		item = SteamAPIManager.getWorkshopMod(itemid)
		try:
			try:
				lastupdate = item["response"]["publishedfiledetails"][0]["time_updated"];
				dt = datetime.datetime.fromtimestamp(lastupdate)
				return str(dt)
			except KeyError:
				print("This mod has no published update time")
				return "NA"
		except KeyError:
			print("Mod: " + itemid + " is most likely hidden or not public")
			return "NA"
	def __init__(self):
		if FileManager.__instance != None:
			raise Exception("This class is a singleton")
		else:
			FileManager.__instance = self