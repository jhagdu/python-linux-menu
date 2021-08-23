from os import system

def login():
    choice = str(input("Select action (Login/Logout/[Noting]): ").lower() or "nothing")
    while True:
        if choice == "login":
            server = str(input("\nEnter Server [Default is defined by the daemon]: "))
            system("docker login {}".format(server))
            break
        elif choice in ["logout"]:
            server = str(input("\nEnter Server [Default is defined by the daemon]: "))
            system("docker logout {}".format(server))
            break
        elif choice in ["nothing", "back", "exit", "quit", "q", "not", "no"]:
            break
        else:
            choice = str(input("\033[91mSelect Valid Action: ").lower() or "nothing")
            system("tput sgr0")

def daemon():
    print("Actions for Docker Daemon :-\
        \n    1. Status\
        \n    2. Start\
        \n    3. Restart\
        \n    4. Stop\
    \n")
    choice = str(input("Select Action: ").lower() or "1")
    while True:
        if choice in ["1", "status"]:
            system("systemctl status docker")
            break
        elif choice in ["2", "start"]:
            system("systemctl start docker")
            break
        elif choice in ["3", "restart"]:
            system("systemctl restart docker")
            break
        elif choice in ["4", "stop"]:
            system("systemctl stop docker")
            break
        else:
            choice = str(input("\033[91mSelect Valid Action: ").lower() or "1")
            system("tput sgr0")

def build():
    path = str(input("Enter Path/URL of Dockerfile: ") or "")
    filename = str(input("Enter Name of Dockerfile (default is PATH/Dockerfile): ") or "")
    if filename != "": filename = "-f {}".format(filename)
    imgtag = str(input("Enter Image Tag: ") or "")
    extraopts = str(input("Specify Extra Options if needed (Type --help for help): ") or "")
    if extraopts in ["-h", "--help"]: 
        system("docker builder build --help | grep '\--add-host\|--build-arg\|--cache-from\|--cgroup-parent\|--compress\|--cpu\|--disable-content-trust\|--force-rm\|--iidfile\|--isolation\|--label\|--memory\|--network\|--no-cache\|--pull\|--quiet\|--rm\|--security-opt\|--shm-size\|--target\|--ulimit'")
        print() 
        extraopts = str(input("Specify Extra Options if needed: ") or "")
    print()
    system("docker builder build {} -t {} {} {}".format(extraopts, imgtag, filename, path))
