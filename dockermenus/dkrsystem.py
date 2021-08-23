from os import system
from uidesign.lookdesign import *
from functions.dkrsystem import *
from screens import switchscrn

def showOption(terSpec):
	spclnth = int((terSpec['width']-51)/4)
	headstr = 'DOCKER SYSTEM MANAGEMENT TUI'
	headbar(headstr, terSpec['width'])
	activeTab = 3
	menubar(activeTab, terSpec['width'])
	system('tput setaf 6')
	print()
	print(" "*spclnth + " 1: Info         " + " "*spclnth + " 2: Disk Usage   " + " "*spclnth + " 3: Prune        " + " "*spclnth)
	print(" "*spclnth + " 4: Events       " + " "*spclnth + " 5: Back         " + " "*spclnth)  
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
			info()
		elif choice=='2':
			disk()
		elif choice=='3':
			prune()
		elif choice=='4':
			events()
		elif choice in ['5','b','back']:
			clearScr()
			switchscrn.switchtabs(3)
		else :
			print("PLEASE ENTER A VALID INPUT")

		print()
		input("Press Enter... ")
		system('clear')
