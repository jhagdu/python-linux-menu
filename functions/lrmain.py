from os import system

def fdiskUtility(preCmndStr):
    print("\nDISK LIST - \n")
    system(preCmndStr + "fdisk -l | grep /dev")
    print("\nFDISK UTILITY - \n")
    diskname = input("Enter Disk Name: ")
    print()
    cmnd = "fdisk {}".format(diskname)
    system("{} {}".format(preCmndStr, cmnd))    

def runCommand(preCmndStr):
    cmnd = str(input("Command to Run: "))
    print()
    system("{} {}".format(preCmndStr, cmnd))

def getShell(preCmndStr, connType):
    if connType == 'Remote':
        preCmndStr = preCmndStr + '-t'
    cmnd = "bash"
    system("{} {}".format(preCmndStr, cmnd))
