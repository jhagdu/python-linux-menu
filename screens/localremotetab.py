from os import system
from uidesign.lookdesign import *
from functions import lrmain
from localremotemenus import basicCommands, services, lvm, crontab, webserver
from screens import switchscrn
from subprocess import getstatusoutput

def connSettings(terSpec, authMethod):
	spclnth = int((terSpec['width']-52)/4)
	switchAuth = 'Switch To Pass (SP)' if authMethod == 'key' else 'Switch To Key (SK)'
	system('tput setaf 3')
	print()
	print(" "*spclnth + "Change Host (CH) " + " "*spclnth + switchAuth + " "*spclnth + "Close Conn (CC)  " + " "*spclnth)
	print()
	print(terSpec['width'] * "~")

def chkRemote(terSpec, chktype, host='127.0.0.1', user='root', authMethod='password', keyfile='passwd'):
	if chktype == "conn":
		chk = getstatusoutput("ping -c 1 " + host)
		isHostup = True if chk[0] is 0 else False
		return isHostup
	elif chktype == "auth":
		chkcmnd = "ssh -l {0} {1} whoami".format(user, host) if authMethod == 'password' else "ssh -l {0} {1} -o PasswordAuthentication=no -i {2} whoami".format(user, host, keyfile)
		chk = getstatusoutput(chkcmnd)
		isValid = True if chk[0] is 0 else False
		return isValid

def remoteConn(terSpec):
	headbar('REMOTE TUI', terSpec['width'])
	connectionWindow(terSpec['width'])
	i = 1
	while True:
		if i == 4:
			input("\n\nMax Tries Reached, Press any key for Main Menu!")
			clearScr()
			switchscrn.switchtabs(0)
			break
		i+=1
		host = str(input("\nEnter Remote Host IP: "))
		isUP = chkRemote(terSpec, "conn", str(host))
		if isUP == True:
			break
		else:
			print("\033[91m{0} is Unreachable, Try with another!".format(host))
			system("tput sgr0")
	user = str(input("\nEnter Remote User: "))
	authMethod = str(input("\nSpecify Authentication Method (Password/Key): ")).lower()
	i = 1
	while True:
		if i == 4:
			input("\n\nMax Tries Reached, Press any key for Main Menu!")
			clearScr()
			switchscrn.switchtabs(0)
			break
		i+=1
		if authMethod in ['k', 'key', 'keys']:
			authMethod = 'key'
			break
		elif authMethod in ['p', 'pass', 'passwd', 'password']:
			authMethod = 'password'
			break
		else:
			authMethod = str(input("\033[91mEnter Password or Key: "))
			system('tput sgr0')
	keyfile = str(input("\nEnter Key File Path: ")) if authMethod == 'key' else 'passwd'
	isValid = chkRemote(terSpec, "auth", str(host), str(user), str(authMethod), str(keyfile))
	if isValid == False:
		choice = input("\033[91m\n\nUnsuccessfull Authentication!, Back to Main Menu (B) or Retry: ").lower()
		if choice in ['b', 'back']:
			clearScr()
			switchscrn.switchtabs(0)
		else:
			switchscrn.switchtabs(2)
	switchscrn.remotehost.remoteDetails = {'host': host, 'user': user, 'authMethod': authMethod, 'keyfile': keyfile}
	switchscrn.remotehost.isRemoteSet = True
	return switchscrn.remotehost.remoteDetails

def showOption(terSpec, connType, authMethod):
	spclnth = int((terSpec['width']-51)/4)
	headstr = 'LOCAL TUI' if connType == 'Local' else "REMOTE [{}@{}] TUI".format(switchscrn.remotehost.remoteDetails['user'], switchscrn.remotehost.remoteDetails['host'])
	headbar(headstr, terSpec['width'])
	activeTab = 1 if connType == 'Local' else 2
	menubar(activeTab, terSpec['width'])
	connSettings(terSpec, authMethod) if connType == 'Remote' else print()
	system('tput setaf 6')
	print()
	print(" "*spclnth + " 1: Basic Command" + " "*spclnth + " 2: Mange Service" + " "*spclnth + " 3: LVM          " + " "*spclnth)
	print(" "*spclnth + " 4: Fdisk Utility" + " "*spclnth + " 5: Webserver    " + " "*spclnth + " 6: Crontab      " + " "*spclnth)  
	print(" "*spclnth + " 7: Run Command  " + " "*spclnth + " 8: Get Shell    " + " "*spclnth + " 9: Back         " + " "*spclnth)
	print()
	print(terSpec['width'] * "_")
	system('tput setaf 7')
	print("\n")

def selectOption(connType):
	terSpec = tersize()
	clearScr()
	if switchscrn.remotehost.isRemoteSet == False and connType == 'Remote':
		switchscrn.remotehost.remoteDetails = remoteConn(terSpec)
	preCmndStr = ''
	if connType == 'Local':
		preCmndStr = ''
	elif connType == 'Remote' and switchscrn.remotehost.remoteDetails['authMethod'] == 'password':
		preCmndStr = "ssh {0}@{1} ".format(switchscrn.remotehost.remoteDetails['user'], switchscrn.remotehost.remoteDetails['host'])
	elif connType == 'Remote' and switchscrn.remotehost.remoteDetails['authMethod'] == 'key':
		preCmndStr = "ssh -i {2} {0}@{1} ".format(switchscrn.remotehost.remoteDetails['user'], switchscrn.remotehost.remoteDetails['host'], switchscrn.remotehost.remoteDetails['keyfile'])
	while True:
		terSpec = tersize()
		clearScr()
		showOption(terSpec, connType, switchscrn.remotehost.remoteDetails['authMethod'])
		choice = str(input("Enter Choice: ")).lower()
		print()
		if choice in ['l', 'local']:
			print("Already On Local Menu!") if connType == 'Local' else switchscrn.switchtabs(1)
		elif choice in ['r', 'remote']:
			print("Already On Remote Menu!\n{}".format(switchscrn.remoteConnDetails())) if connType == 'Remote' else switchscrn.switchtabs(2)
		elif choice in ['d', 'docker']:
			switchscrn.switchtabs(3)
		elif choice in ['ch', 'change host'] and connType == 'Remote':
			switchscrn.remotehost.isRemoteSet = False
			switchscrn.switchtabs(2)
		elif choice in ['sk', 'switch to key', 'switch 2 key', 'switch key'] and connType == 'Remote' and switchscrn.remotehost.remoteDetails['authMethod'] == 'password':
			switchscrn.remotehost.isRemoteSet = False
			switchscrn.switchtabs(2)
		elif choice in ['sp', 'switch to pass', 'switch 2 pass', 'switch pass', 'switch to password', 'switch to password', 'switch to passwd', 'switch to passwd', 'switch 2 passwd', 'switch 2 passwd'] and connType == 'Remote' and switchscrn.remotehost.remoteDetails['authMethod'] == 'key':
			switchscrn.remotehost.isRemoteSet = False
			switchscrn.switchtabs(2)
		elif choice in ['cc', 'close conn', 'close connection', 'close connect'] and connType == 'Remote':
			switchscrn.remotehost.isRemoteSet = False
			switchscrn.remotehost.remoteDetails = {'host': 'LocalHost', 'user': 'LocalUser', 'authMethod': 'LocalAuth', 'keyfile': 'LocalKey'}
			switchscrn.switchtabs(2)
		elif choice=='1':
			basicCommands.selectOption(terSpec, connType, preCmndStr)
		elif choice=='2':
			services.selectOption(terSpec, connType, preCmndStr)
		elif choice=='3':
			lvm.selectOption(terSpec, connType, preCmndStr)
		elif choice=='4':
			lrmain.fdiskUtility(preCmndStr)
		elif choice=='5':
			webserver.selectOption(terSpec, connType, preCmndStr)
		elif choice=='6':
			crontab.selectOption(terSpec, connType, preCmndStr)
		elif choice=='7':
			lrmain.runCommand(preCmndStr)
		elif choice=='8':
			lrmain.getShell(preCmndStr, connType)
		elif choice in ['9','b','back']:
			clearScr()
			switchscrn.switchtabs(0)
		else :
			print("PLEASE ENTER A VALID INPUT")

		print()
		input("Press Enter... ")
		system('clear')
