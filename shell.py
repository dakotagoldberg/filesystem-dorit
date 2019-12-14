global fileSystem
fileSystem = "[folder:dorit[folder:winter[folder:december[]][file:sleet][file:ice]]]"

def findLocation(index):
    openB = 0
    closedB = 0
    for i in range(len(fileSystem)):
        if fileSystem[i] == "[":
            openB+=1
        if fileSystem[i] == "]":
            closedB +=1
        if openB == index + 1:
            return i

myLoc = 0

def currentFolderContents(index):
    index = index + 1
    openB = 0
    closedB = 0
    for i in range(findLocation(index), len(fileSystem)):
        if fileSystem[i] == "[":
            openB+=1
        if fileSystem[i] == "]":
            closedB +=1
        if openB == closedB - 1:
            return fileSystem[findLocation(index):i]

def currentFolderName(index):
    index = index + 1
    i = findLocation(index)
    while (fileSystem[i] != ":"):
        i-=1
    return fileSystem[i+1:findLocation(index)]

def showHelp():
    # print("ls"),
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
