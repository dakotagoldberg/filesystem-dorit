global fileSystem
global myLoc
fileSystem = "[folder:dorit[folder:winter[folder:december[folder:christmas[]][folder:kwanzaa[]]][folder:january[]][file:sleet is cool][file:ice]]]"
myLoc = 1


def findLocation(index):
    count = 0
    for i in range(len(fileSystem)):
        if fileSystem[i] == ":":
            if (count == index):
                return i
            count+=1

def reverseLookup(name):
    count = 0
    for i in range(len(fileSystem)):
        if fileSystem[i] == ":":
            if (currentFolderName(count) == name):
                return count
            count+=1


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

def numberOfFilesInFolder(index):
    count = 0
    for i in parseContents(index):
        if itemType(reverseLookup(i)) == "file":
            count+=1
    return count


def currentFolderName(index):
    i = findLocation(index)
    while (fileSystem[i] != "[" and fileSystem[i] != "]"):
        i+=1
    return fileSystem[findLocation(index)+1:i]

def itemType(index):
    i = findLocation(index)
    while (fileSystem[i] != "[" and fileSystem[i] != "]"):
        i-=1
    return fileSystem[i + 1:findLocation(index)]

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


def parseContents(index):
    raw = currentFolderContents(index)
    items = []
    openB = 0
    closedB = 0
    count = index + 1
    start = findLocation(index) + len(currentFolderName(index)) + 1
    i = start
    while (i < len(raw) + start):
        if fileSystem[i] == "[":
            openB+=1
        elif fileSystem[i] == "]":
            closedB +=1
        elif fileSystem[i] == ":":
            if (openB - closedB == 1):
                items.append(str(currentFolderName(count)))
            count+=1
        i+=1
    return items


def showHelp():
    print("%5s %40s" % ("ls", "lists all items in folder")) 
    print("%5s %40s" % ("cd", "changes directory")) 
    print("%5s %40s" % ("mkdir", "creates a new directory")) 
    print("%5s %40s" % ("touch", "creates a new file")) 
    print("%5s %40s" % ("edit", "edits the contents of a file")) 
    print("%5s %40s" % ("rm", "removes a file")) 
    print("%5s %40s" % ("rmdir", "removes a folder"))  
    print("%5s %40s" % ("path", "displays path of current location"))  


def listContents(index):
    numFiles = 0
    for i in parseContents(index):
        if itemType(reverseLookup(i)) == "file":
            print(i + " --> " + itemType(reverseLookup(i)) + " ["+ str(numFiles) +"]")
            numFiles+=1
        else:
            print(i + " --> " + itemType(reverseLookup(i)))

def changeDirectory(currentIndex, newLoc):
    if newLoc == ".." and currentIndex != 0:
        x = currentPath(currentIndex)
        return reverseLookup(x[1])
    else:
        x = parseContents(currentIndex)
        if newLoc in x and itemType(reverseLookup(newLoc)) == "folder":
            return reverseLookup(newLoc)
    return currentIndex


def rm(fileIndex):
    fileName =""
    numFiles = 0
    for i in parseContents(myLoc):
        if itemType(reverseLookup(i)) == "file":
            #print(i + " --> " + itemType(reverseLookup(i)) + " ["+ str(numFiles) +"]")
            numFiles+=1
            if(numFiles == fileIndex):
                fileName = i
    print(fileSystem)
    print(fileName)
    if fileName in parseContents(myLoc):
        print("run Code")
        tbd = findLocation(findFileGivenIn(myLoc,fileIndex))
        scabbard = fileSystem[0:tbd-5]
        print(scabbard)
        print()
        sword = fileSystem[tbd+len(fileName)+2:len(fileSystem)]
        print(sword)
        print()
        print(scabbard+sword)

def findFileGivenIn(index,fileIndex):
    raw = currentFolderContents(index)
    openB = 0
    closedB = 0
    count2 =0
    count = index + 1
    start = findLocation(index) + len(currentFolderName(index)) + 1
    i = start
    while (i < len(raw) + start):
        if fileSystem[i] == "[":
            openB+=1
        elif fileSystem[i] == "]":
            closedB +=1
        elif fileSystem[i] == ":":
            if (openB - closedB == 1):
                if(fileSystem[findLocation(count)-4:findLocation(count)]== "file"):
                    if(count2 == fileIndex):
                        print(fileSystem[findLocation(count)+1:findLocation(count)+4])
                        return(count)
                    count2+=1
                        
            count+=1
        i+=1
    return 0
#print(findFileGivenIn(myLoc,0))
print(findLocation(findFileGivenIn(myLoc,0)))
