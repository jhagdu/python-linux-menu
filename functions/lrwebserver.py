from os import system
from subprocess import getstatusoutput

def check(preCmndStr):
    chkpkg = getstatusoutput("rpm -q httpd")
    if chkpkg[0] == 0:
        print("Package httpd is Installed\nPackage Full Name - {}".format(chkpkg[1]))
        chkpkg = getstatusoutput("systemctl status httpd")
        if chkpkg[0] == 0:
            print("\n\033[92mWebserver Service is Running!".format(chkpkg[1]))
            system("tput sgr0")
            print("Listening on Address:Port - {}".format(getstatusoutput("netstat -tnlp | grep httpd | awk '{ print $4 }'")[1]))
        else:
            print("\n\033[91mWebserver Service Not Running!")
            system("tput sgr0")
    else:
        print("\033[91mPackage httpd is Not Installed")
        system("tput sgr0")

def install(preCmndStr):
    chkpkg = getstatusoutput("rpm -q httpd")
    if chkpkg[0] == 0:
        print("Package httpd is already installed, {}".format(chkpkg[1]))
    else:
        choice = str(input("\nInstall with Root Privilege i.e. sudo (Y/[N]): ").lower())
        if choice == "y":
            cmnd = "sudo yum install httpd -y >> /dev/null"
        else:
            cmnd = "yum install httpd -y >> /dev/null"
        system("{} {}".format(preCmndStr, cmnd))

def compileSetting(preCmndStr):
    chkpkg = getstatusoutput("rpm -q httpd")
    if chkpkg[0] == 0:
        system("httpd -V")
    else:
        print("\033[91mPackage httpd is Not Installed")
        system("tput sgr0")

def changePort(preCmndStr):
    configfile = str(input("\nServer Config File Path [/etc/httpd/conf/httpd.conf]: ") or "/etc/httpd/conf/httpd.conf")
    newport = int(input("Enter New Port Number [80]: ") or "80")
    cmnd = "sed -i s/'^Listen.*'/'Listen {}'/g {}".format(newport, configfile)
    system("{} {}".format(preCmndStr, cmnd))
    choice = str(input("Restart Webserver (Y/[N]): ").lower())
    if choice == "y":
        cmnd = "systemctl restart httpd"
        system("{} {}".format(preCmndStr, cmnd))

def svcRestart(preCmndStr):
    cmnd = "systemctl restart httpd"
    system("{} {}".format(preCmndStr, cmnd))

def svcStart(preCmndStr):
    cmnd = "systemctl start httpd"
    system("{} {}".format(preCmndStr, cmnd))

def svcStop(preCmndStr):
    cmnd = "systemctl stop httpd"
    system("{} {}".format(preCmndStr, cmnd))

def svcStatus(preCmndStr):
    cmnd = "systemctl status httpd"
    system("{} {}".format(preCmndStr, cmnd))
