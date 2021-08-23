from os import system

def services(preCmndStr):
    cmnd = "systemctl -a"
    system("{} {}".format(preCmndStr, cmnd))

def chkStatus(preCmndStr):
    name = str(input("\nEnter Service Name: "))
    print()
    cmnd = "systemctl status {}".format(name)
    system("{} {}".format(preCmndStr, cmnd))

def svcRestart(preCmndStr):
    name = str(input("\nEnter Service Name: "))
    print()
    cmnd = "systemctl restart {}".format(name)
    system("{} {}".format(preCmndStr, cmnd))

def svcStart(preCmndStr):
    name = str(input("\nEnter Service Name: "))
    print()
    cmnd = "systemctl start {}".format(name)
    system("{} {}".format(preCmndStr, cmnd))

def svcEnable(preCmndStr):
    name = str(input("\nEnter Service Name: "))
    print()
    cmnd = "systemctl enable {}".format(name)
    system("{} {}".format(preCmndStr, cmnd))

def svcFrcReload(preCmndStr):
    name = str(input("\nEnter Service Name: "))
    print()
    cmnd = "systemctl reload -f {}".format(name)
    system("{} {}".format(preCmndStr, cmnd))

def svcStop(preCmndStr):
    name = str(input("\nEnter Service Name: "))
    print()
    cmnd = "systemctl stop {}".format(name)
    system("{} {}".format(preCmndStr, cmnd))

def svcDisable(preCmndStr):
    name = str(input("\nEnter Service Name: "))
    print()
    cmnd = "systemctl disable {}".format(name)
    system("{} {}".format(preCmndStr, cmnd))
