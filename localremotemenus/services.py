from os import system
from uidesign.lookdesign import *
from functions.lrservices import *
from screens import switchscrn

def showOption(terSpec, connType):
	spclnth = int((terSpec['width']-51)/4)
	headstr = 'LOCAL SERVICES TUI' if connType == 'Local' else 'REMOTE [{}@{}] SERVICES TUI'.format(switchscrn.remotehost.remoteDetails['user'], switchscrn.remotehost.remoteDetails['host'])
	headbar(headstr, terSpec['width'])
	activeTab = 1 if connType == 'Local' else 2
	menubar(activeTab, terSpec['width'])
	system('tput setaf 6')
	print()
	print(" "*spclnth + " 1: Services     " + " "*spclnth + " 2: Check Status " + " "*spclnth + " 3: Restart Svc  " + " "*spclnth)
	print(" "*spclnth + " 4: Start Service" + " "*spclnth + " 5: EnableService" + " "*spclnth + " 6: Force Reload " + " "*spclnth)  
	print(" "*spclnth + " 7: Stop Service " + " "*spclnth + " 8: Disable Svc  " + " "*spclnth + " 9: Back         " + " "*spclnth)
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
			services(preCmndStr)
		elif choice=='2':
			chkStatus(preCmndStr)
		elif choice=='3':
			svcRestart(preCmndStr)
		elif choice=='4':
			svcStart(preCmndStr)
		elif choice=='5':
			svcEnable(preCmndStr)
		elif choice=='6':
			svcFrcReload(preCmndStr)
		elif choice=='7':
			svcStop(preCmndStr)
		elif choice=='8':
			svcDisable(preCmndStr)
		elif choice in ['9','b','back']:
			clearScr()
			switchscrn.switchtabs(1) if connType == 'Local' else switchscrn.switchtabs(2)
		else :
			print("PLEASE ENTER A VALID INPUT")

		print()
		input("Press Enter... ")
		system('clear')
