from os import system
from uidesign.lookdesign import *
from functions.lrbasic import *
from screens import switchscrn

def showOption(terSpec, connType):
	spclnth = int((terSpec['width']-51)/4)
	headstr = 'LOCAL BASIC TUI' if connType == 'Local' else 'REMOTE [{}@{}] BASIC TUI'.format(switchscrn.remotehost.remoteDetails['user'], switchscrn.remotehost.remoteDetails['host'])
	headbar(headstr, terSpec['width'])
	activeTab = 1 if connType == 'Local' else 2
	menubar(activeTab, terSpec['width'])
	system('tput setaf 6')
	print()
	print(" "*spclnth + " 1: Show Date    " + " "*spclnth + " 2: Show Cal     " + " "*spclnth + " 3: Show NIC Conf" + " "*spclnth)
	print(" "*spclnth + " 4: List Dir     " + " "*spclnth + " 5: Make New Dir " + " "*spclnth + " 6: Del File/Dir " + " "*spclnth)  
	print(" "*spclnth + " 7: Read File    " + " "*spclnth + " 8: New/Edit File" + " "*spclnth + " 9: Back         " + " "*spclnth)
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
			showDate(preCmndStr)
		elif choice=='2':
			showCal(preCmndStr)
		elif choice=='3':
			showNICConf(preCmndStr)
		elif choice=='4':
			listDir(preCmndStr)
		elif choice=='5':
			makeNewDir(preCmndStr)
		elif choice=='6':
			delFile(preCmndStr)
		elif choice=='7':
			readFile(preCmndStr)
		elif choice=='8':
			createFile(preCmndStr)
		elif choice in ['9','b','back']:
			clearScr()
			switchscrn.switchtabs(1) if connType == 'Local' else switchscrn.switchtabs(2)
		else :
			print("PLEASE ENTER A VALID INPUT")

		print()
		input("Press Enter... ")
		system('clear')
