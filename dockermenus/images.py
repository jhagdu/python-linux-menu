from os import system
from uidesign.lookdesign import *
from functions.dkrimages import *
from screens import switchscrn

def showOption(terSpec):
	spclnth = int((terSpec['width']-51)/4)
	headstr = 'DOCKER IMAGE MANAGEMENT TUI'
	headbar(headstr, terSpec['width'])
	activeTab = 3
	menubar(activeTab, terSpec['width'])
	system('tput setaf 6')
	print()
	print(" "*spclnth + " 1: List         " + " "*spclnth + " 2: Inspect      " + " "*spclnth + " 3: History      " + " "*spclnth)
	print(" "*spclnth + " 4: Pull/Push    " + " "*spclnth + " 5: Load/Save    " + " "*spclnth + " 6: Tag          " + " "*spclnth)  
	print(" "*spclnth + " 7: Import       " + " "*spclnth + " 8: Remove       " + " "*spclnth + " 9: Back         " + " "*spclnth)
	print()
	print(terSpec['width'] * "_")
	system('tput setaf 7')
	print("\n")

def selectOption(terSpec):
	clearScr()
	while True:
		clearScr()
		showOption(terSpec)
		choice = str(input("Enter Choice: ")).lower()
		print()
		if choice in ['l', 'local']:
			switchscrn.switchtabs(1)
		elif choice in ['r', 'remote']:
			switchscrn.switchtabs(2)
		elif choice in ['d', 'docker']:
			print("Already On Docker Menu!")
		elif choice=='1':
			imglist()
		elif choice=='2':
			inspect()
		elif choice=='3':
			history()
		elif choice=='4':
			pullpush()
		elif choice=='5':
			loadsave()
		elif choice=='6':
			tagimg()
		elif choice=='7':
			importimg()
		elif choice=='8':
			remove()
		elif choice in ['9','b','back']:
			clearScr()
			switchscrn.switchtabs(3)
		else :
			print("PLEASE ENTER A VALID INPUT")

		print()
		input("Press Enter... ")
		system('clear')
