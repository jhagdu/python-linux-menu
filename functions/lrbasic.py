from os import system

def showDate(preCmndStr):
    cmnd = "date"
    system("{} {}".format(preCmndStr, cmnd))

def showCal(preCmndStr):
    system("{} {}".format(preCmndStr, 'cal'))
    choice = str(input("\nWant to See Specific Month or Year (Y/N): ")).lower()
    if choice in ['y', 'yes']:
        month = str(input("\n    Enter Month: "))
        year = str(input("    Enter Year: "))
        print()
        cmnd = "cal {} {}".format(month, year)
        system("{} {}".format(preCmndStr, cmnd))

def showNICConf(preCmndStr):
    nic = str(input("\nEnter Interface Name [All]: "))
    print()
    cmnd = "ifconfig {}".format(nic)
    system("{} {}".format(preCmndStr, cmnd))

def listDir(preCmndStr):
    path = str(input("\nPath: "))
    cmnd = "ls {}".format(path)
    system("{} {}".format(preCmndStr, cmnd))
    choice = str(input("\nWant to Detailed List with Hidden Files (Y/N): ")).lower()
    if choice in ['y', 'yes']:
        print()
        cmnd = "ls -al {}".format(path)
        system("{} {}".format(preCmndStr, cmnd))

def makeNewDir(preCmndStr):
    path = str(input("\nEnter Dir Path: "))
    prnt = str(input("\nCreate Parent Directories if needed (Y/N): ")).lower()
    if prnt in ['y', 'yes']:
        cmnd = "mkdir -p {}".format(path)
    else:
        cmnd = "mkdir {}".format(path)
    print()
    system("{} {}".format(preCmndStr, cmnd))

def delFile(preCmndStr):
    while True:
        choice = str(input('\nWant to Remove Directory of File (D/F): ')).lower()
        if choice in ['f', 'file', 'remove file']:
            path = str(input('\nEnter File Path: '))
            sure = input("\033[91m\nThis can't be undo, Are you Sure? (Yes/[No]): ").lower()
            system("tput sgr0")
            if sure in ['y', 'yes']:
                print()
                cmnd = "rm -f {}".format(path)
                system("{} {}".format(preCmndStr, cmnd))
            break
        elif choice in ['d', 'dir', 'directory', 'directories']:
            path = str(input('\nEnter Directory Path: '))
            recrs = input('\nWant to br recursive if Directory not empty (Y/[N]): ').lower()
            sure = input("\033[91m\nThis can't be undo, Are you Sure? (Yes/[No]): ").lower()
            system("tput sgr0")
            if sure in ['y', 'yes']:
                if recrs in ['y', 'yes']:
                    cmnd = "rm -drf {}".format(path)
                else:
                    cmnd = "rm -df {}".format(path)
                print()
                system("{} {}".format(preCmndStr, cmnd))
            break
        else: 
            print('\033[91mEnter a Valid Choice!')
            system("tput sgr0")

def readFile(preCmndStr):
    path = str(input("\nEnter File Path: "))
    print()
    cmnd = "cat {}".format(path)
    system("{} {}".format(preCmndStr, cmnd))
    print("\n\n")

def createFile(preCmndStr):
    while True:
        choice = str(input('\nCreate a New File or Edit a File (C/E): ')).lower()
        if choice in ['e', 'edit', 'edit file', 'edit a file']:
            path = str(input('\nEnter file Path: '))
            cmnd = "vim {}".format(path)
            system("{} {}".format(preCmndStr, cmnd))
            break
        elif choice in ['c', 'create', 'new', 'create new', 'new file', 'create new file']:
            while True:
                choice = str(input('\nWant to create a Empty file or with Data (E/D): ')).lower()
                if choice in ['e', 'empty', 'empty file']:
                    path = str(input('\nEnter file Path: '))
                    cmnd = "touch {}".format(path)
                    break
                elif choice in ['d', 'data file', 'file with data', 'data', 'with data']:
                    path = str(input('\nEnter file Path: '))
                    editor = str(input('\nWhich Editor you want to use (cat/vim): ')).lower()
                    if editor in ['cat', 'c']:
                        print("\nStart writing the file and Press LeftCtrl+D to stop writing...\n\n")
                    cmnd = "cat > {}".format(path) if editor in ['cat', 'c'] else "vim {}".format(path)
                    break
                else:
                    print('\033[91mEnter a Valid Choice!')
                    system("tput sgr0")
            system("{} {}".format(preCmndStr, cmnd))
            break
        else: 
            print('\033[91mEnter a Valid Choice!')
            system("tput sgr0")
