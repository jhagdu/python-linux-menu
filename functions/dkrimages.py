from os import system

def imglist():
    system("docker image ls")
    print()
    more = str(input("\nShow More Options (Y/[N]): ").lower())
    if more in ["y", "yes"]:
        filters = str(input("Specify Image Filters (Press Enter for No Filter): ") or "")
        if filters != "": filters = "--filter {}".format(filters)
        showall = str(input("\nShow All Images (Y/[N]): ").lower())
        showall = "--all" if showall in ["y", "yes"] else ""
        digest = str(input("\nShow Digests (Y/[N]): ").lower())
        digest = "--digests" if digest in ["y", "yes"] else ""
        print()
        system("docker image ls {} {} {}".format(filters, showall, digest))

def inspect():
    names = str(input("Enter Image Name(s) (Space Sperated): "))
    print()
    system("docker image inspect {}".format(names))

def history():
    name = str(input("Enter Image Name: "))
    print()
    system("docker image history -H {}".format(name))

def pullpush():
    choice = str(input("Want to Pull or Push: ").lower())
    while True:
        if choice == "pull":
            name = str(input("Enter Image name with tag [default tag latest]: "))
            system("docker image pull {}".format(name))
            break
        elif choice == "push":
            name = str(input("Enter Image name with tag [default tag latest]: "))
            system("docker image push {}".format(name))
            break
        elif choice == "":
            break
        else:
            choice = str(input("Enter valid choice (Pull/Push): ").lower())
            print()

def loadsave():
    choice = str(input("Want to Load or Save: ").lower())
    while True:
        if choice == "load":
            src = str(input("Enter input file path: "))
            system("docker image load --input {}".format(src))
            break
        elif choice == "save":
            names = str(input("Enter Image Name(s) to Save: "))
            output = str(input("Enter output file: ") or "")
            if output != "": output = "--output ".format(output)
            system("docker image save {} {}".format(output, names))
            break
        elif choice == "":
            break
        else:
            choice = str(input("Enter valid choice (Load/Save): ").lower())
            print()

def tagimg():
    src = str(input("Enter Source Image name with tag: "))
    target = str(input("Enter Target Image name with tag: "))
    system("docker image tag {} {}".format(src, target))

def importimg():
    image = str(input("Enter Image name with tag: "))
    src = str(input("Enter File/URL: "))
    extraopts = str(input("Specify Extra Options if needed (Type --help for help): ") or "")
    if extraopts in ["-h", "--help"]:
        system("docker image import --help | grep '\--change\|--message\|--platform'")
        print()
        extraopts = str(input("Specify Extra Options if needed: ") or "")
    print()
    system("docker image import {} {} {}".format(extraopts, src, image))

def remove():
    names = str(input("Enter Image Name(s) to Remove: "))
    print()
    system("docker image rm {}".format(names))
