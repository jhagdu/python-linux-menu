from os import system

def info():
    system("docker system info")

def disk():
    system("docker system df")
    choice = str(input("\n\nWant to see detailed information (Y/[N]): ").lower() or "n")
    if choice == "y":
        system("docker system df -v")

def events():
    filters = str(input("Specify Events Filters (Press Enter for No Filter): ") or "")
    if filters != "": filters = "--filter {}".format(filters)
    since = input("Show events created since (Specify Timestamp or Press Enter): ") or ""
    if since != "": since = "--since {}".format(since)
    until = input("Show events until (Specify Timestamp or Press Enter): ") or ""
    if until != "": until = "--until {}".format(until)
    print()
    system("docker system events {} {} {}".format(filters, since, until))

def prune():
    filters = str(input("Specify Prune Filters (Press Enter for No Filter): ") or "")
    if filters != "": filters = "--filter {}".format(filters)
    allprune = str(input("Remove all unused images (Y/[N]): ").lower())
    allprune = "--all" if allprune in ["y", "yes"] else ""
    volumes = str(input("Prune Volumes (Y/[N]): ").lower())
    volumes = "--volumes" if volumes in ["y", "yes"] else ""
    print()
    system("docker system prune {} {} {}".format(filters, allprune, volumes))
