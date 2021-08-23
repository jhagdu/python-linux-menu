from os import system, popen
from pyfiglet import figlet_format

def tersize():
	# Specify Terminal Height and Terminal Width
	try:
		rows, columns = popen('stty size', 'r').read().split()
	except:
		rows = 37
		columns = 100
	finally:
		terSpec = {'height': int(rows), 'width': int(columns)}
	return terSpec

def headbar(string, terWdt):
	system('tput setaf 3')
	system('tput bold')
	headLen = len(string) + 8
	print(("-" * int((terWdt - headLen)/2)) + "{0} CONSOLE".format(string) + "-" * int((terWdt - headLen)/2))
	print("=" * terWdt)
	system('tput sgr0')
	system('tput setaf 7')

def menubar(activeStatus, terWdt):
	system('tput setaf 1')
	print("\n")
	system('tput cup 3 $(expr {0} - 4 )'.format(int(terWdt/6)))
	if activeStatus == 1:	
		system('tput bold')
		system('tput setaf 2')
	print("Local(L)" + " " * int((terWdt)/6 - 4) + "|")
	system('tput sgr0')
	system('tput setaf 1')
	print("|")
	system('tput cup 3 $(expr {0} - 4 )'.format(int(terWdt/2)))
	if activeStatus == 2:
		system('tput bold')
		system('tput setaf 2')
	print("Remote(R)" + " " * int(terWdt/6 - 5) + "|")
	system('tput sgr0')
	system('tput setaf 1')
	print("|")
	system('tput cup 3 $(expr {0} - 5 )'.format(int((terWdt*5)/6)))
	if activeStatus == 3:
		system('tput bold')
		system('tput setaf 2')
	print("Docker(D)" + " " * int(terWdt/6 - 6) + "|")
	system('tput setaf 3')
	print("_" * terWdt)
	system('tput sgr0')
	system('tput setaf 7')

def welcomeBanner(terSpec):
	headbar('TUI', terSpec['width'])
	menubar(0, terSpec['width'])
	centerSpec = int((terSpec['width'] - 75)/2)
	wlcm = (figlet_format("WELCOME", font = "banner3-D" ))
	print("\n\n")
	print("\033[91m" + " "*centerSpec + wlcm[0:74])
	print("\033[91m" + " "*centerSpec + wlcm[75:149])
	print("\033[91m" + " "*centerSpec + wlcm[150:224])
	print("\033[97m" + " "*centerSpec + wlcm[225:299])
	print("\033[97m" + " "*centerSpec + wlcm[300:374])
	print("\033[92m" + " "*centerSpec + wlcm[375:449])
	print("\033[92m" + " "*centerSpec + wlcm[450:524])
	print("\033[92m" + " "*centerSpec + wlcm[525:600])
	system("tput setaf 7")
	print("\n\n")
	sideoutline(terSpec)

def sideoutline(terSpec):
    for i in range(5, terSpec['height']-1):
        system('tput cup {} {}'.format(i, 0))
        system("tput setaf 6")
        print("#")
        system("tput setaf 6")
        system('tput cup {} {}'.format(i, terSpec['width']))
        print("#")

    system("tput setaf 6")
    system('tput cup {} 1'.format(terSpec['height']-2))
    print("\\"*(terSpec['width']-2))
    system("tput setaf 7")

def connectionWindow(terWdt):
	system('tput cup 3 $(expr {0} - 14 )'.format(int(terWdt/2)))
	system('tput setaf 2')
	print("Establish Remote Connection")
	system('tput setaf 3')
	print("_"*terWdt)
	system('tput setaf 7')
	print()


def clearScr():
	try:
		try:
			system('clear')
		except:
			system('cls')
	except:
		pass
	