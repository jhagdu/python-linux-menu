from os import system

def listcont():
    system("docker container ls")
    showall = str(input("\nShow all Containers (Y/[N]): ").lower())
    print()
    if showall in ["y", "yes"]:
        system("docker container ls -a")

def run():
    image = str(input("Enter Image Name: ") or "")
    i = 1
    while image == "":
        i = i + 1
        image = str(input("Image Name Required: ") or "")
        if i > 3:
            print ("\nExited...No Image Name Passed!\n")
            return 1
    extraopts = str(input("Specify Options if needed (Type --help for help): ") or "")
    if extraopts in ["-h", "--help"]: 
        system("docker container run --help | sed -n '5,$p'")
        print() 
        extraopts = str(input("Specify Options if needed: ") or "")
    print()
    cmd = str(input("Command to run container with (leave empty for default): ") or "")
    system("docker container run {} {} {}".format(extraopts, image, cmd))

def restartop():
    choice = str(input("Want to Start/Restart/Stop container: ").lower())
    while True:
        if choice == "start":
            names = str(input("\nEnter Container Name(s) to Start: "))
            system("docker container start {}".format(names))
            break
        elif choice in ["stop"]:
            names = str(input("\nEnter Container Name(s) to Stop: "))
            system("docker container stop {}".format(names))
            break
        elif choice in ["restart"]:
            names = str(input("\nEnter Container Name(s) to Restart: "))
            system("docker container restart {}".format(names))
            break
        elif choice == "":
            break
        else:
            choice = str(input("Enter valid choice (start/restart/stop): ").lower())
            print()

def rename():
    oldname = str(input("Enter Container Current Name to Rename: "))
    newname = str(input("Enter Container New Name: "))
    print()
    system("docker container rename {} {}".format(oldname, newname))

def execcmnd():
    name = str(input("Enter Container Name: "))
    cmd = str(input("Enter Command with args: "))
    extraopts = str(input("Specify Extra Options if needed (Type --help for help): ") or "")
    if extraopts in ["-h", "--help"]: 
        system("docker container exec --help | grep '\--detach\|--env\|--interactive\|--privileged\|--tty\|--user\|--workdir'")
        print() 
        extraopts = str(input("Specify Extra Options if needed: ") or "")
    print()
    system("docker container exec {} {} {}".format(extraopts, name, cmd))

def attach():
    name = str(input("Enter Container Name to Attach: "))
    print()
    system("docker container attach {}".format(name))

def copyfiles():
    src = str(input("Enter Source: "))
    target = str(input("Enter Target: "))
    system("docker container cp {} {}".format(src, target))

def pause():
    names = str(input("Enter Container Name(s) to Pause: "))
    print()
    system("docker container pause {}".format(names))

def loginspect():
    choice = str(input("Want to see Logs or Inspect container: ").lower())
    while True:
        if choice in ["logs", "log", "l"]:
            name = str(input("Enter Container Name: "))
            extraopts = str(input("Specify Extra Options if needed (Type --help for help): ") or "")
            if extraopts in ["-h", "--help"]: 
                system("docker container logs --help | grep '\--details\|--follow\|--since\|--tail\|--timestamp\|until'")
                print() 
                extraopts = str(input("Specify Extra Options if needed: ") or "")
            print()
            system("docker container logs {} {}".format(extraopts, name))
            break
        elif choice in ["inspect", "inspec", "insp", "ins", "i"]:
            names = str(input("Enter Container Name(s): "))
            system("docker container inspect {}".format(names))
            break
        elif choice == "":
            break
        else:
            choice = str(input("Enter valid choice (Logs/Inspect): ").lower())
            print()

def topstat():
    choice = str(input("Want to see Stats or Top(Running Processes) of a container: ").lower())
    while True:
        if choice in ["top", "to", "t"]:
            names = str(input("Enter Container Name(s) (leave blank for all running): ") or "")
            showall = str(input("Want to see stats for all (Y/[N]): ").lower())
            showall = "--all" if showall in ["y", "yes"] else ""
            disablestream = str(input("Disable Stream, only pull first value (Y/[N]): ").lower())
            disablestream = "--no-stream" if disablestream in ["y", "yes"] else ""
            system("docker container top {} {} {}".format(showall, disablestream, names))
            break
        elif choice in ["stats", "stat", "sta", "st", "s"]:
            name = str(input("Enter Image name with tag [default tag latest]: "))
            system("docker container stats {}".format(name))
            break
        elif choice == "":
            break
        else:
            choice = str(input("Enter valid choice (Top/Stats): ").lower())
            print()

def commit():
    contname = str(input("Enter Container Name: "))
    targetimg = str(input("Enter Target Image Name: "))
    extraopts = str(input("Specify Extra Options if needed (Type --help for help): ") or "")
    if extraopts in ["-h", "--help"]: 
        system("docker container commit --help | grep '\--author\|--pause\|--message\|--change'")
        print() 
        extraopts = str(input("Specify Extra Options if needed: ") or "")
    print()
    system("docker container commit {} {} {}".format(extraopts, contname, targetimg))

def export():
    name = str(input("Enter Container Name to Export: "))
    output = str(input("Enter target file path/name: ") or "")
    if output != "": output = "--output {}".format(output)
    print()
    system("docker container kill {} {}".format(output, name))

def kill():
    names = str(input("Enter Container Name(s) to Kill: "))
    signal = str(input("Enter Signal to send [default KILL]: ") or "")
    if signal != "": signal = "--signal {}".format(signal)
    print()
    system("docker container kill {}".format(names))

def remove():
    names = str(input("Enter Container Name(s) to Remove: "))
    print()
    system("docker container rm {}".format(names))

def prune():
    filters = str(input("Specify Container Filters (Press Enter for No Filter): ") or "")
    if filters != "": filters = "--filter {}".format(filters)
    print()
    system("docker container prune {}".format(filters))
