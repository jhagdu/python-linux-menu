from os import system
from uidesign.lookdesign import *
from dockermenus import container, dkrsystem, images, network, volume
from functions import dkrmain
from screens import switchscrn

def showOption(terSpec):
	spclnth = int((terSpec['width']-51)/4)
	headbar('DOCKER TUI', terSpec['width'])
	menubar(3, terSpec['width'])
	system('tput setaf 6')
	print()
	print(" "*spclnth + " 1: Container    " + " "*spclnth + " 2: Volume       " + " "*spclnth + " 3: Network      " + " "*spclnth)
	print(" "*spclnth + " 4: Images       " + " "*spclnth + " 5: Builder      " + " "*spclnth + " 6: System       " + " "*spclnth)  
	print(" "*spclnth + " 7: Login/Logout " + " "*spclnth + " 8: Daemon       " + " "*spclnth + " 9: Back         " + " "*spclnth)
	print()
	print(terSpec['width'] * "_")
	system('tput setaf 7')
	print("\n")

def selectOption():
	while True:
		terSpec = tersize()
		clearScr()
		showOption(terSpec)
		choice = str(input("Enter Choice: "))
		print()
		if choice in ['L', 'l', 'Local', 'local']:
			switchscrn.switchtabs(1)
		elif choice in ['R', 'r', 'Remote', 'remote']:
			switchscrn.switchtabs(2)
		elif choice in ['D', 'd', 'Docker', 'docker']:
			print("Already On Docker Menu!")
		elif choice=='1':
			container.selectOption(terSpec)
		elif choice=='2':
			volume.selectOption(terSpec)
		elif choice=='3':
			network.selectOption(terSpec)
		elif choice=='4':
			images.selectOption(terSpec)
		elif choice=='5':
			dkrmain.build()
		elif choice=='6':
			dkrsystem.selectOption(terSpec)
		elif choice=='7':
			dkrmain.login()
		elif choice=='8':
			dkrmain.daemon()
		elif choice in ['9','b','back', 'B', 'Back']:
			clearScr()
			switchscrn.switchtabs(0)
		else :
			print("PLEASE ENTER A VALID INPUT")

		print()
		input("Press Enter... ")
		system('clear')
