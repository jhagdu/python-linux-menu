from os import system
from uidesign.lookdesign import *
from functions.dkrcontainer import *
from screens import switchscrn

def showOption(terSpec):
	spclnth = int((terSpec['width']-68)/5)
	headstr = 'DOCKER CONTAINER MANAGEMENT TUI'
	headbar(headstr, terSpec['width'])
	activeTab = 3
	menubar(activeTab, terSpec['width'])
	system('tput setaf 6')
	print()
	print(" "*spclnth + " 1: List         " + " "*spclnth + " 2: Run          " + " "*spclnth + " 3: Re/Start/Stop" + " "*spclnth + " 4: Rename       " + " "*spclnth)
	print(" "*spclnth + " 5: Exec Command " + " "*spclnth + " 6: Attach       " + " "*spclnth + " 7: Copy Files   " + " "*spclnth + " 8: Pause/Unpause" + " "*spclnth)  
	print(" "*spclnth + " 9: Inspect/Logs " + " "*spclnth + "10: Stats/Top    " + " "*spclnth + "11: Commit       " + " "*spclnth + "12: Export       " + " "*spclnth)  
	print(" "*spclnth + "13: Kill         " + " "*spclnth + "14: Remove       " + " "*spclnth + "15: Prune        " + " "*spclnth + "16: Back         " + " "*spclnth)
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
			listcont()
		elif choice=='2':
			run()
		elif choice=='3':
			restartop()
		elif choice=='4':
			rename()
		elif choice=='5':
			execcmnd()
		elif choice=='6':
			attach()
		elif choice=='7':
			copyfiles()
		elif choice=='8':
			pause()
		elif choice=='9':
			loginspect()
		elif choice=='10':
			topstat()
		elif choice=='11':
			commit()
		elif choice=='12':
			export()
		elif choice=='13':
			kill()
		elif choice=='14':
			remove()
		elif choice=='15':
			prune()
		elif choice in ['16','b','back']:
			clearScr()
			switchscrn.switchtabs(3)
		else :
			print("PLEASE ENTER A VALID INPUT")

		print()
		input("Press Enter... ")
		system('clear')
