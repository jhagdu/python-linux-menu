from os import system
from uidesign.lookdesign import *
from functions.dkrnetwork import *
from screens import switchscrn

def showOption(terSpec):
	spclnth = int((terSpec['width']-51)/4)
	headstr = 'DOCKER NETWORK MANAGEMENT TUI'
	headbar(headstr, terSpec['width'])
	activeTab = 3
	menubar(activeTab, terSpec['width'])
	system('tput setaf 6')
	print()
	print(" "*spclnth + " 1: List         " + " "*spclnth + " 2: Inspect      " + " "*spclnth + " 3: Connect      " + " "*spclnth)
	print(" "*spclnth + " 4: Disconnect   " + " "*spclnth + " 5: Create       " + " "*spclnth + " 6: Remove       " + " "*spclnth)  
	print(" "*spclnth + " 7: Prune        " + " "*spclnth + " 8: Back         " + " "*spclnth)
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
			netlist()
		elif choice=='2':
			inspect()
		elif choice=='3':
			connect()
		elif choice=='4':
			disconnect()
		elif choice=='5':
			create()
		elif choice=='6':
			remove()
		elif choice=='7':
			prune()
		elif choice in ['8','b','back']:
			clearScr()
			switchscrn.switchtabs(3)
		else :
			print("PLEASE ENTER A VALID INPUT")

		print()
		input("Press Enter... ")
		system('clear')
