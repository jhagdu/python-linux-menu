from screens import mainscreen, localremotetab, dockertab

class remotehost:
    isRemoteSet = False
    remoteDetails = {'host': 'LocalHost', 'user': 'LocalUser', 'authMethod': 'LocalAuth', 'keyfile': 'LocalKey'}

def remoteConnDetails():
    return "\nRemote Connection Details ->\
        \n>> Host :- {0}\
        \n>> User :- {1}\
        \n>> Auth Method :- {2}\
        \n".format(remotehost.remoteDetails['host'], remotehost.remoteDetails['user'], remotehost.remoteDetails['authMethod'])

def switchtabs(tab):
    if tab == 0:
        mainscreen.mainscreen()
    elif tab == 1:
        localremotetab.selectOption('Local')
    elif tab == 2:
        localremotetab.selectOption('Remote')
    elif tab == 3:
        dockertab.selectOption()
