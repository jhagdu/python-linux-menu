from os import system, popen
from pyfiglet import figlet_format
from time import sleep
from random import choice

def tersize():
	try:
		rows, columns = popen('stty size', 'r').read().split()
	except:
		rows = 37
		columns = 100
	finally:
		terSpec = {'height': int(rows), 'width': int(columns)}
	return terSpec

def bannerPrint(terSpec, value, color):
    i = 0
    print()
    while i < len(value):
        print("\033[{}m".format(choice(color)) + " "*int((terSpec['width'] - int(len(value)/8))/2) + value[int(i):int(i+(len(value)/8)-1)])
        i = int(i + len(value)/8)
    print()

def thanks():
    while True:
        system("tput reset")
        terSpec = tersize()
        bannerPrint(terSpec, figlet_format("T H A N K S", font = "banner3-D" ), color = [91, 92, 93, 94, 95, 96, 97])
        bannerPrint(terSpec, figlet_format(" V I M A L ", font = "banner3-D" ), color = [91, 92])
        bannerPrint(terSpec, figlet_format(" D A G A ", font = "banner3-D" ), color = [94, 96])
        bannerPrint(terSpec, figlet_format(" S I R ", font = "banner3-D" ), color = [31, 32, 33, 34, 35, 36, 37])
        sleep(1)
        system("tput reset")

thanks()