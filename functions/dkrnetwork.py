from os import system

def netlist():
    filters = str(input("Specify Network Filters (Press Enter for No Filter): ") or "")
    if filters != "": filters = "--filter {}".format(filters)
    print()
    system("docker network ls {}".format(filters))

def inspect():
    names = str(input("Enter Network Name(s) (Space Sperated): "))
    print()
    system("docker network inspect {}".format(names))

def connect():
    netname = str(input("Enter Network Name to connect: "))
    contname = str(input("Enter Container Name to connect with: "))
    link = str(input("Add link to another container: ") or "")
    if link != "": link = "--link {}".format(link)
    alias = str(input("Add network-scoped alias for the container: ") or "")
    if alias != "": alias = "--alias {}".format(alias)
    dopts = str(input("Driver options for the network: ") or "")
    if dopts != "": dopts = "--dopts {}".format(dopts)
    extraopts = str(input("Specify Extra Options if needed (Type --help for help): ") or "")
    if extraopts in ["-h", "--help"]: 
        system("docker network connect --help | grep ip")
        print()
        extraopts = str(input("Specify Extra Options if needed: ") or "")
    print()
    system("docker network connect {} {} {} {} {} {}".format(link, alias, dopts, extraopts, netname, contname))

def disconnect():
    netname = str(input("Enter Network Name to disconnect: "))
    contname = str(input("Enter Container Name from which to disconnect: "))
    force = str(input("Disconnect Forcefully (Y/[N]): ").lower())
    force = "--force" if force in ["y", "yes"] else ""
    print()
    system("docker network disconnect {} {} {}".format(force, netname, contname))

def create():
    netname = str(input("Enter Network Name: "))
    driver = str(input("Driver for the network [default bridge]: ") or "")
    if driver != "": driver = "--driver {}".format(driver)
    internal = str(input("Restrict external access to the network (Y/[N]): ").lower())
    internal = "--internal" if internal in ["y", "yes"] else ""
    attachable = str(input("Enable manual container attachment ([Y]/N): ").lower())
    attachable = "" if attachable in ["n", "no", "not"] else "--attachable"
    extraopts = str(input("Specify Extra Options if needed (Type --help for help): ") or "")
    if extraopts in ["-h", "--help"]: 
        system("docker network create --help | grep '\--aux-address\|--config\|--ingress\|--ip\|--label\|--scope\|--subnet'")
        print() 
        extraopts = str(input("Specify Extra Options if needed: ") or "")
    print()
    system("docker network create {} {} {} {} {}".format(driver, internal, attachable, extraopts, netname))

def remove():
    names = str(input("Enter Network Name(s) to Remove: "))
    print()
    system("docker network rm {}".format(names))

def prune():
    filters = str(input("Specify Network Filters (Press Enter for No Filter): ") or "")
    if filters != "": filters = "--filter {}".format(filters)
    print()
    system("docker network prune {}".format(filters))
