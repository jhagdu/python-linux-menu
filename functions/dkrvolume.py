from os import system

def listvolumes():
    filters = str(input("Specify Volume Filters (Press Enter for No Filter): ") or "")
    if filters != "": filters = "--filter {}".format(filters)
    print()
    system("docker volume ls {}".format(filters))

def create():
    name = str(input("Enter Volume Name to Create: "))
    driver = str(input("Volume Driver (Press Enter for default): ") or "")
    if driver != "": driver = "--driver {}".format(driver)
    label = str(input("Volume Label List (Press Enter for no label): ") or "")
    if label != "": label = "--label {}".format(label)
    options = str(input("Volume Options Map (Press Enter for no options): ") or "")
    if options != "": options = "--opt {}".format(options)
    print()
    system("docker volume create {} {} {} {}".format(driver, label, options, name))
    
def remove():
    names = str(input("Enter Volume Name(s) to Remove: "))
    force = str(input("Remove Forcefully (Y/[N]): ").lower())
    force = "--force" if force in ["y", "yes"] else ""
    print()
    system("docker volume rm {} {}".format(force, names))

def inspect():
    names = str(input("Enter Volume Name(s) (Space Seperated): "))
    print()
    system("docker volume inspect {}".format(names))
    
def prune():
    filters = str(input("Specify Volume Filters (Press Enter for No Filter): ") or "")
    if filters != "": filters = "--filter {}".format(filters)
    print()
    system("docker volume prune {}".format(filters))
