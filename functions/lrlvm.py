from os import system
from subprocess import getoutput

def listDisks(preCmndStr):
    system("{} fdisk -l".format(preCmndStr))

def listBlk(preCmndStr):
    system("{} lsblk -a".format(preCmndStr))

def fdiskutil(preCmndStr):
    print("\nDISK LIST - \n")
    system("{} 'fdisk -l | grep /dev'".format(preCmndStr))
    print("\nFDISK UTILITY - \n")
    diskname = input("Enter Disk Name: ")
    print()
    system("{} fdisk {}".format(preCmndStr,diskname))

def formatDisk(preCmndStr):
    ft = input("Full or Resized Format (Enter F or R): ")
    if ft.lower() == 'f':
        print("\nDISK LIST - \n")
        system("{} lsblk -a".format(preCmndStr))
        print("\nFORMAT FULL DISK - \n")
        diskname = input("Enter Disk Name: ")
        frmtType = input("Fromat Type: ")
        print()
        system("{} mkfs -t {} {}".format(preCmndStr,frmtType, diskname))
    elif ft.lower() == 'r':
        print("\nDISK LIST - \n")
        system("{} lsblk -a".format(preCmndStr))
        print("\nFORMAT RESIZED DISK - \n")
        diskname = input("Enter Disk Name: ")
        print()
        system("{} resize2fs {}".format(preCmndStr ,diskname))
    else:
        print("Enter F or R")
        formatDisk()

def mountUmountDisk(preCmndStr):
    ft = input("Mount or Unmount Disk (Enter M or U): ")
    if ft.lower() == 'm':
        print("DISK LIST - \n")
        system("{} lsblk -a".format(preCmndStr))
        print("\nMOUNT DISK - \n")
        diskname = input("Enter Disk Name: ")
        mntPath = input("Enter Mount Path: ")
        print()
        system("{} mount {} {}".format(preCmndStr, diskname, mntPath))
    elif ft.lower() == 'u':
        print("DISK LIST - \n")
        system("{} lsblk -a".format(preCmndStr))
        print("\nUNMOUNT DISK - \n")
        path = input("Enter Disk or Path to unmount: ")
        print()
        system("{} umount {}".format(preCmndStr ,path))
    else:
        print("Enter M or U")
        mountUmountDisk()

def listPVs(preCmndStr):
    system("{} pvdisplay".format(preCmndStr))

def listVGs(preCmndStr):
    system("{} vgdisplay".format(preCmndStr))

def listLVs(preCmndStr):
    system("{} lvdisplay".format(preCmndStr))
    
def createPV(preCmndStr):
    print("DISK LIST - \n")
    system("{} 'fdisk -l | grep {}'".format(preCmndStr, "Disk /"))
    print("\nCREATE PV - \n")
    disknames = input("Enter Disk Names (Seperate by Space if multiple): ")
    print()
    system("{} pvcreate {}".format(preCmndStr, disknames))
    
def createVG(preCmndStr):
    print("PV LIST - \n")
    system("{} pvdisplay -C".format(preCmndStr))
    print("\nCREATE VG - \n")
    vgname = input("Enter VG Name: ")
    pvnames = input("Enter PV Names (Seperate by Space if multiple): ")
    print()
    system("{} vgcreate {} {}".format(preCmndStr, vgname, pvnames))

def createLV(preCmndStr):
    print("VG LIST - \n")
    system("{} vgdisplay -C".format(preCmndStr))
    print("\nCREATE LV - \n")
    lvname = input("Enter LV Name: ")
    vgnames = input("Enter VG Name (Seperate by Space if multiple): ")
    lvsize = input("Enter LV Size: ")
    print()
    system("{} lvcreate --size {} --name {} {}".format(preCmndStr, lvsize, lvname, vgnames))

def extendVG(preCmndStr):
    print("VG LIST - \n")
    system("{} vgdisplay -C".format(preCmndStr))
    print("PV LIST - \n")
    system("{} pvdisplay -C".format(preCmndStr))
    print("\nREDUCE VG - \n")
    vgname = input("Name of VG to Extend: ")
    pvname = input("Enter PV Name to Add: ")
    print()
    system("{} vgextend {} {}".format(preCmndStr, vgname, pvname))

def reduceVG(preCmndStr):
    print("VG LIST - \n")
    system("{} vgdisplay -C".format(preCmndStr))
    print("PV LIST - \n")
    system("{} pvdisplay -C".format(preCmndStr))
    print("\nREDUCE VG - \n")
    vgname = input("Name of VG to Reduce: ")
    pvname = input("Enter PV Name to Remove: ")
    print()
    system("{} vgreduce {} {}".format(preCmndStr, vgname, pvname))
    
def extendLV(preCmndStr):
    print("LV LIST - \n")
    system("{} lvdisplay -C".format(preCmndStr))
    print("\nEXTEND LV - \n")
    lvname = input("Enter LV Name: ")
    size = input("Enter Size to Extend (nM = nMB): ")
    print()
    system("{} lvextend -L+{} {}".format(preCmndStr,size,lvname))

def reduceLV(preCmndStr):
    print("LV LIST - \n")
    system("{} lvdisplay -C".format(preCmndStr))
    print("\nEXTEND LV - \n")
    lvname = input("Enter LV Name: ")
    size = input("Enter Size to Reduce (nM = nMB): ")
    print()
    system("{} lvreduce -L-{} {}".format(preCmndStr, size, lvname))

def movePV(preCmndStr):
    print("PV LIST - \n")
    system("{} pvdisplay -C".format(preCmndStr))
    print("\nMOVE PV - \n")
    oldpv = input("Enter Old PV Name: ")
    newpv = input("Enter New PV Name: ")
    print()
    system("{} pvmove {} {}".format(preCmndStr,oldpv,newpv))
    
def removePV(preCmndStr):
    print("PV LIST - \n")
    system("{} pvdisplay -C".format(preCmndStr))
    print("\nREMOVE PV - \n")
    pvname = input("Enter PV Name: ")
    print()
    system("{} pvremove {}".format(preCmndStr,pvname))

def removeVG(preCmndStr):
    print("VG LIST - \n")
    system("{} vgdisplay -C".format(preCmndStr))
    print("\nREMOVE VG - \n")
    vgname = input("Enter VG Name: ")
    print()
    system("{} vgremove {}".format(preCmndStr, vgname))

def removeLV(preCmndStr):
    print("LV LIST - \n")
    system("{} lvdisplay -C".format(preCmndStr))
    print("\nREMOVE LV - \n")
    lvname = input("Enter LV Name: ")
    print()
    system("{} lvremove {}".format(preCmndStr, lvname))
