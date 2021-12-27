def prettyPrintModInfo(ModID,ModName,LatestUpdate,NeedsUpdated = True):
	idlength = len(str(ModID))
	namelength = len(str(ModName))
	lastupdatetime = len(str(LatestUpdate))
	needsupdatelength = len(str(NeedsUpdated))
	maxlength = max(idlength,namelength, lastupdatetime,needsupdatelength)
	totalstring = "╔"
##Mod Title
	for x in range (0,maxlength+13):
		totalstring += "═"
	totalstring += "╗\n"
	totalstring += "║Title:       " + ModName
	if namelength < maxlength:
		for x in range (namelength,maxlength):
			totalstring += " "
	totalstring += "║\n╠"
##Mod ModID
	for x in range (0,maxlength+13):
		totalstring += "═"
	totalstring += "╣\n"
	totalstring += "║ID:          " + ModID
	if idlength < maxlength:
		for x in range (idlength,maxlength):
			totalstring += " "
	totalstring += "║\n╠"
##Mod Last Update
	for x in range (0,maxlength+13):
		totalstring += "═"
	totalstring += "╣\n"
	totalstring += "║Last Update: " + str(LatestUpdate)
	if lastupdatetime < maxlength:
		for x in range (lastupdatetime,maxlength):
			totalstring += " "
	totalstring += "║\n╠"
##Mod Needs Update
	for x in range (0,maxlength+13):
		totalstring += "═"
	totalstring += "╣\n"
	totalstring += "║Needs Update:" + str(NeedsUpdated)
	if needsupdatelength < maxlength:
		for x in range (needsupdatelength,maxlength):
			totalstring += " "
	totalstring += "║\n╚"
##endline
	for x in range (0,maxlength+13):
			totalstring += "═"
	totalstring +="╝"
	print(totalstring)