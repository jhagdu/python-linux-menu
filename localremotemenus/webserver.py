from os import system
from uidesign.lookdesign import *
from functions.lrwebserver import *
from screens import switchscrn

def showOption(terSpec, connType):
	spclnth = int((terSpec['width']-51)/4)
	headstr = 'LOCAL APACHE WEBSERVER TUI' if connType == 'Local' else 'REMOTE [{}@{}] APACHE WEBSERVER TUI'.format(switchscrn.remotehost.remoteDetails['user'], switchscrn.remotehost.remoteDetails['host'])
	headbar(headstr, terSpec['width'])
	activeTab = 1 if connType == 'Local' else 2
	menubar(activeTab, terSpec['width'])
	system('tput setaf 6')
	print()
	print(" "*spclnth + " 1: Check HTTPD  " + " "*spclnth + " 2: Install HTTPD" + " "*spclnth + " 3: Server Status" + " "*spclnth)
	print(" "*spclnth + " 4: Start Server " + " "*spclnth + " 5: RestartServer" + " "*spclnth + " 6: Stop Server  " + " "*spclnth)  
	print(" "*spclnth + " 7: Show Compile " + " "*spclnth + " 8: Change Port  " + " "*spclnth + " 9: Back         " + " "*spclnth)
	print()
	print(terSpec['width'] * "_")
	system('tput setaf 7')
	print("\n")

def selectOption(terSpec, connType, preCmndStr):
	clearScr()
	while True:
		clearScr()
		showOption(terSpec, connType)
		choice = str(input("Enter Choice: ")).lower()
		print()
		if choice in ['l', 'local']:
			print("Already On Local Menu!") if connType == 'Local' else switchscrn.switchtabs(1)
		elif choice in ['r', 'remote']:
			print("Already On Remote Menu!\n{}".format(switchscrn.remoteConnDetails())) if connType == 'Remote' else switchscrn.switchtabs(2)
		elif choice in ['d', 'docker']:
			switchscrn.switchtabs(3)
		elif choice=='1':
			check(preCmndStr)
		elif choice=='2':
			install(preCmndStr)
		elif choice=='3':
			svcStatus(preCmndStr)
		elif choice=='4':
			svcStart(preCmndStr)
		elif choice=='5':
			svcRestart(preCmndStr)
		elif choice=='6':
			svcStop(preCmndStr)
		elif choice=='7':
			compileSetting(preCmndStr)
		elif choice=='8':
			changePort(preCmndStr)
		elif choice in ['9','b','back']:
			clearScr()
			switchscrn.switchtabs(1) if connType == 'Local' else switchscrn.switchtabs(2)
		else :
			print("PLEASE ENTER A VALID INPUT")

		print()
		input("Press Enter... ")
		system('clear')
