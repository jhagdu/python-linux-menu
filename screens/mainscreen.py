from os import system
from screens import switchscrn 
from uidesign.lookdesign import welcomeBanner, clearScr, tersize

def mainscreen():
    while True:
        terSpec = tersize()
        welcomeBanner(terSpec)
        system("tput cup {} {}".format(int(terSpec['height']/2+4), int((terSpec['width']-17)/2)))
        print("Enter Your Choice")
        system("tput cup {} {}".format(int(terSpec['height']- 4), int((terSpec['width']-23)/2)))
        system("tput setaf 1")
        print("Enter q or quit to exit")
        system("tput setaf 7")
        system("tput cup {} {}".format(int(terSpec['height']/2+6), int((terSpec['width']-1)/2)))
        choice = str(input())
        if choice in ['L', 'l', 'Local', 'local']:
            switchscrn.switchtabs(1)
        elif choice in ['R', 'r', 'Remote', 'remote']:
            switchscrn.switchtabs(2)
        elif choice in ['D', 'd', 'Docker', 'docker']:
            switchscrn.switchtabs(3)
        elif choice in ['q', 'Q', 'quit', 'Quit', 'exit', 'Exit']:
            clearScr()
            exit()
        else:
            clearScr()
            system("tput cup {} {}".format(int(terSpec['height'] - 7), int((terSpec['width']-21)/2)))
            system("tput setaf 1")
            print("Enter a Valid Choice!")
            system("tput cup 0 0")
