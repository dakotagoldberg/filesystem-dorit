global fileSystem
fileSystem = "[folder:dorit[folder:winter[folder:december[]][folder:january[]][file:sleet][file:ice]]]"



def findLocation(index):
    count = 0
    for i in range(len(fileSystem)):
        if fileSystem[i] == ":":
            if (count == index):
                return i
            count+=1

myLoc = 0

def totalItems():
    return fileSystem.count(":")



def currentFolderContents(index):
    openB = 0
    closedB = 0
    for i in range(findLocation(index) + len(currentFolderName(index))+1, len(fileSystem)):
        if fileSystem[i] == "[":
            openB+=1
        if fileSystem[i] == "]":
            closedB +=1
        if openB == closedB - 1:
            return fileSystem[findLocation(index) + len(currentFolderName(index))+1:i]


def currentFolderName(index):
    i = findLocation(index)
    while (fileSystem[i] != "[" and fileSystem[i] != "]"):
        i+=1
    return fileSystem[findLocation(index)+1:i]

def currentPath(index):
    path = []
    path.append(currentFolderName(index))
    openB = 0
    closedB = 0
    count = index
    i = findLocation(index)
    while (i > 0):
        if fileSystem[i] == ":":
            if (openB > closedB):
                path.append(str(currentFolderName(count)))
            count-=1
        if fileSystem[i] == "[":
            openB+=1
        if fileSystem[i] == "]":
            closedB +=1
        i-=1
    return path



def showHelp():
    print("%5s %30s" % ("ls", "lists all items in folder")) 
    print("%5s %30s" % ("cd", "changes directory")) 
    print("%5s %30s" % ("mkdir", "creates a new directory")) 
    print("%5s %30s" % ("touch", "creates a new file")) 
    print("%5s %30s" % ("edit", "edits the contents of a file")) 
    print("%5s %30s" % ("rm", "removes a file")) 
    print("%5s %30s" % ("rmdir", "removes a folder"))  



while (True):

    command = raw_input(currentFolderName(myLoc) + ": ")
    # The big IF: based on command entered, run specific action.

    if (command == "help"):
        showHelp()

    break

# print(findLocation(1))
# print(currentFolderContents(3))
# print(currentFolderName(1))
# print(findLocation(3))
# print(currentFolderName(1))
# print(totalItems())
# print(currentFolderContents(0))
# print("")
# print(currentPath(1))
