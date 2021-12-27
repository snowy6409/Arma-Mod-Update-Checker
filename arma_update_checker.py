import datetime
import requests
import json
import os
from apimanager import SteamAPIManager
from printutils import prettyPrintModInfo
from filemanager import FileManager
API = SteamAPIManager()
FM = FileManager()
def checkForUpdate(itemid,localupdate):
	item = API.getWorkshopMod(itemid)
	try:
		title = item["response"]["publishedfiledetails"][0]["title"];
		try:
			lastupdate = item["response"]["publishedfiledetails"][0]["time_updated"];
			dt = datetime.datetime.fromtimestamp(lastupdate)
			if str(dt) != localupdate:
				prettyPrintModInfo(itemid,title,dt,True)
		except KeyError:
			print("This mod has no published update time")
	except KeyError:
		print("Mod: " + itemid + " is most likely hidden or not public")
def Options():
	choice = "0"
	while choice != "-1":
		print("Please enter a number for the action you wish to do")
		print("1: First time setup")
		print("2: Check for updates")
		print("3: Mark all mods as updated")
		print("-1: Exit")
		choice = input()
		if choice == "1":
			print("ALL MODS MUST ME UPDATED BEFORE YOU RUN THIS")
			while (choice != "4" or choice != "5"):
				choice = input("Are all mods updated (Y/N):")
				if choice == 'Y' or choice == 'y' or choice == 'yes':
					print("Registering all mods")
					print("Please wait for this to finish, may take a while depending on mod count")
					FM.readJsonFile()
					choice = "4"
					break
				elif choice == 'N' or choice == 'n' or choice == 'no':
					print("Please update mods before running this")
					choice = "5"
					break
		if choice == "2":
			modlist = FM.readJsonFile()
			print("Please wait for this to finish, may take a while depending on mod count")
			for item in modlist['mods']:
				checkForUpdate(item['id'],item['dt'])
		if choice == "3":
			print("Please wait for this to finish, may take a while depending on mod count")
			FM.updateJsonFile()
			print("All mods updated successfully")
	print(choice)
Options()



