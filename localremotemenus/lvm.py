from os import system
from functions.lrlvm import *
from uidesign.lookdesign import *
from screens import switchscrn

def showOption(terSpec, connType):
	spclnth = int((terSpec['width']-68)/5)
	headstr = 'LOCAL LVM TUI' if connType == 'Local' else 'REMOTE [{}@{}] LVM TUI'.format(switchscrn.remotehost.remoteDetails['user'], switchscrn.remotehost.remoteDetails['host'])
	headbar(headstr, terSpec['width'])
	activeTab = 1 if connType == 'Local' else 2
	menubar(activeTab, terSpec['width'])
	system('tput setaf 6')
	print()
	print(" "*spclnth + " 1: List Disks   " + " "*spclnth + " 2: List PVs     " + " "*spclnth + " 3: List VGs     " + " "*spclnth + " 4: List LVs     " + " "*spclnth)
	print(" "*spclnth + " 5: List Blocks  " + " "*spclnth + " 6: Create PV    " + " "*spclnth + " 7: Create VG    " + " "*spclnth + " 8: Create LV    " + " "*spclnth)  
	print(" "*spclnth + " 9: Format Disk  " + " "*spclnth + "10: Move PV      " + " "*spclnth + "11: Extend VG    " + " "*spclnth + "12: Extend LV    " + " "*spclnth)
	print(" "*spclnth + "13: Mount/Unmount" + " "*spclnth + "14: Remove PV    " + " "*spclnth + "15: Reduce VG    " + " "*spclnth + "16: Reduce LV    " + " "*spclnth)
	print(" "*spclnth + "17: fdisk Utility" + " "*spclnth + "18: Back         " + " "*spclnth + "19: Remove VG    " + " "*spclnth + "20: Remove LV    " + " "*spclnth)
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
		elif choice == '1':
			listDisks(preCmndStr)
		elif choice=='2':
			listPVs(preCmndStr)
		elif choice=='3':
			listVGs(preCmndStr)
		elif choice=='4':
			listLVs(preCmndStr)
		elif choice=='5':
			listBlk(preCmndStr)
		elif choice=='6':
			createPV(preCmndStr)
		elif choice=='7':
			createVG(preCmndStr)
		elif choice=='8':
			createLV(preCmndStr)
		elif choice=='9':
			formatDisk(preCmndStr)
		elif choice=='10':
			movePV(preCmndStr)
		elif choice=='11':
			extendVG(preCmndStr)
		elif choice=='12':
			extendLV(preCmndStr)
		elif choice=='13':
			mountUmountDisk(preCmndStr)
		elif choice=='14':
			removePV(preCmndStr)
		elif choice=='15':
			reduceVG(preCmndStr)
		elif choice=='16':
			reduceLV(preCmndStr)
		elif choice=='17':
			fdiskutil(preCmndStr)
		elif choice=='19':
			removeVG(preCmndStr)
		elif choice=='20':
			removeLV(preCmndStr)
		elif choice in ['18','b', 'back']:
			clearScr()
			switchscrn.switchtabs(1) if connType == 'Local' else switchscrn.switchtabs(2)
		else :
			print("PLEASE ENTER A VALID INPUT")

		print()
		input("Press Enter... ")
		system('clear')
