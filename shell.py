global fileSystem
fileSystem = "[folder:dorit[folder:winter[folder:december[folder:christmas[]][folder:kwanzaa[]]][folder:january[]][file:sleet is cool][file:ice]][folder:spring[file:flowers]]]"

# currentLoc is the current macrolocation starting at 0 (folder:dorit is 0).
# getType(currentLoc) should always return "folder"
global currentLoc
currentLoc = 0

# Returns the character index of a given macrolocation. 
def getIndex(loc):
    count = 0
    for i in range(len(fileSystem)):
        if fileSystem[i] == ":":
            if count == loc:
                return i
            count+=1

# Returns whether there is a folder or file at a given macrolocation.
def getType(loc):
    count = 0
    for i in range(len(fileSystem)):
        if fileSystem[i] == ":":
            if count == loc:
                if fileSystem[i-1] == "e":
                    return "file"
                else:
                    return "folder"
            count+=1

# Returns the name of the folder at a given macrolocation.
def getFolderName(loc):
    start = getIndex(loc) + 1
    stop = 0
    for i in range(start, len(fileSystem)):
        if fileSystem[i] == "[":
            stop = i
            break
    return fileSystem[start:stop]

# Returns the contents of the file at a given macrolocation.
def getFileContents(loc):
    start = getIndex(loc) + 1
    stop = 0
    for i in range(start, len(fileSystem)):
        if fileSystem[i] == "]":
            stop = i
            break
    return fileSystem[start:stop]

# Gets the name of a folder or the contents of a file at the given macrolocation.
def getName(loc):
    if getType(loc) == "folder":
        return getFolderName(loc)
    else:
        return getFileContents(loc)

# Returns a string of a folder and everything inside the brackets of that folder at a given macrolocation.
def rawFolder(loc):
    start = getIndex(loc) - len(getType(loc)) - 1
    stop = 0
    openB = 0
    closedB = 0
    for i in range(start, len(fileSystem)):
        if fileSystem[i] == "[":
            openB+=1
        elif fileSystem[i] == "]":
            closedB+=1
        if openB == closedB:
            stop = i + 1
            break
    return fileSystem[start:stop]

# Returns a string containing everything inside the brackets of that folder at a given macrolocation.
def rawFolderContents(loc):
    folder = rawFolder(loc)
    margin = len(getType(loc)) + len(getFolderName(loc)) + 3
    start = getIndex(loc) + len(getFolderName(loc)) + 1
    stop = start + len(folder) - margin 
    return fileSystem[start:stop]

# Returns the macrolocation of the folder that the folder or file at the given macrolocation is in.
    # Returns -1 for dorit (which has no parent).
def getParent(loc):
    if loc == 0:
        return -1
    index = getIndex(loc)
    openB = 0
    closedB = 0
    count = 0
    for i in range(index, 0, -1):
        if fileSystem[i] == "[":
            openB+=1
        elif fileSystem[i] == "]":
            closedB+=1
        elif fileSystem[i] == ":":
            if openB > closedB:
                return loc - count
            count+=1

# Returns the number of files in a folder.
def numberOfFiles(loc):
    items = listFolderContents(loc)
    count = 0
    for i in items:
        if i[2] == "file":
            count+=1
    return count

# Returns a 2D-array.
    # 0: name of folder/file
    # 1: macrolocation of folder/file
    # 2: type of folder/file   
    # 3: [if type="file"] relative index of file in the folder
def listFolderContents(loc):
    items = []
    tempLoc = loc
    start = getIndex(loc) + len(getFolderName(loc)) + 1
    stop = start + len(rawFolderContents(loc))
    openB = 0
    closedB = 0
    fileCount = 0
    for i in range(start, stop):
        if fileSystem[i] == "[":
                openB+=1
        elif fileSystem[i] == "]":
            closedB+=1
        elif fileSystem[i] == ":":
            tempLoc += 1
            if openB - closedB == 1:
                itemInfo = []
                itemInfo.append(getName(tempLoc))
                itemInfo.append(tempLoc)
                itemInfo.append(getType(tempLoc))
                if getType(tempLoc) == "file":
                    fileCount+=1
                    itemInfo.append(fileCount)
                items.append(itemInfo)
    return items

# Lists the contents of a folder (includes file indexes).
def ls(loc):
    items = listFolderContents(loc)
    for i in items:
        if i[2] == "file":
            print(i[0] + " --> [" + str(i[3]) + "]")
        else:
            print(i[0])

# Changes directory.
def cd(loc, newDirectory):
    items = listFolderContents(loc)
    if newDirectory == "..":
        return getParent(loc)
    elif newDirectory == "":
        return -1
    for i in items:
        if i[0] == newDirectory and i[2] == "folder":
            return i[1]
    return -1

# Creates a new folder with a unique name in the beginning of a given directory.
def mkdir(loc, newFolderName):
    items = listFolderContents(loc)
    firstItem = True

    # Ensure the name is unique.
    for i in items:
        if i[0] == newFolderName and i[2] == "folder":
            print("Sorry, a folder with that name already exists.")
            return fileSystem

    if len(items) != 0:
        newFolder = "[folder:" + newFolderName + "[]" + "]"
        newLocation = getIndex(loc) + len(getFolderName(loc)) + 1
        return fileSystem[:newLocation] + newFolder + fileSystem[newLocation:]
    else:
        newFolder = "folder:" + newFolderName + "[]" + "]"
        newLocation = getIndex(loc) + len(getFolderName(loc)) + 2
        return fileSystem[:newLocation] + newFolder + fileSystem[newLocation + 1:]

# Removes a folder from a given directory.
def rmdir(loc, folderName):
    items = listFolderContents(loc)
    folderExists = False
    folder = 0
    for i in items:
        if i[0] == folderName and i[2] == "folder":
            folder = i[1]
            folderExists = True

    # Make sure the folder exists and is empty.
    if not folderExists:
        return fileSystem
    if len(listFolderContents(folder)) > 0:
        print("You can only delete empty folders.")
        return fileSystem
    # Realistically, this will never be a problem... but you never know!
    if folder == 0:
        print("You can't delete the filesystem! Long live dorit!!")
        return fileSystem

    # Check if the folder to delete is the only item in the current folder. Remove accordingly.
    if len(items) != 1:
        start = getIndex(folder) - len(getType(folder)) - 1
        end = getIndex(folder) + len(getFolderName(folder)) + 4
        return fileSystem[:start] + fileSystem[end:]
    else:
        start = getIndex(folder) - len(getType(folder))
        end = getIndex(folder) + len(getFolderName(folder)) + 3
        return fileSystem[:start] + fileSystem[end:]

# Creates a new, empty file (value="null") in a given folder.
def touch(loc):
    items = listFolderContents(loc)
    if len(items) != 0:
        file = "[file:null]"
        newLocation = getIndex(loc) + len(getFolderName(loc)) + 1
        return fileSystem[:newLocation] + file + fileSystem[newLocation:]
    else:
        file = "file:null]"
        newLocation = getIndex(loc) + len(getFolderName(loc)) + 2
        return fileSystem[:newLocation] + file + fileSystem[newLocation + 1:]

# Edits the contents of a file at a given index in a folder.
def edit(loc, fileIndex):
    if not fileIndex.isdigit():
        return fileSystem
    fileIndex = int(fileIndex)
    items = listFolderContents(loc)
    numFiles = numberOfFiles(loc)
    fileLoc = 0
    newValue = ""

    # See if the given index is valid.
    if fileIndex > numFiles:
        print("Sorry, there is no file at that index!")
        return fileSystem

    # Get the absolute location of the file.
    for i in items:
        if i[2] == "file" and i[3] == fileIndex:
            fileLoc = i[1]

    # Collect a new value for the file.
    entering = True
    while entering:
        newValue = raw_input("Enter new file value: ")
        if not all(x.isalpha() or x.isspace() for x in newValue):
            print("No punctuation allowed in files.")
        else:
            entering = False

    # Replace the file value.
    start = getIndex(fileLoc) + 1
    end = getIndex(fileLoc) + len(getFileContents(fileLoc)) + 1
    return fileSystem[:start] + newValue + fileSystem[end:]

def rm(loc, fileIndex):
    if not fileIndex.isdigit():
        return fileSystem
    fileIndex = int(fileIndex)
    items = listFolderContents(loc)
    numFiles = numberOfFiles(loc)
    fileLoc = 0

    # See if the given index is valid.
    if fileIndex > numFiles:
        print("Sorry, there is no file at that index!")
        return fileSystem

    # Get the absolute location of the file.
    for i in items:
        if i[2] == "file" and i[3] == fileIndex:
            fileLoc = i[1]
        else:
            print("You can't use this command to delete folders.")

    # Check if the file to delete is the only item in the current folder. Remove accordingly.
    if len(items) != 1:
        start = getIndex(fileLoc) - len(getType(fileLoc)) - 1
        end = getIndex(fileLoc) + len(getFileContents(fileLoc)) + 2
        return fileSystem[:start] + fileSystem[end:]
    else:
        start = getIndex(fileLoc) - len(getType(fileLoc)) - 0
        end = getIndex(fileLoc) + len(getFileContents(fileLoc)) + 1
        return fileSystem[:start] + fileSystem[end:]
    
def showHelp():
    print("%19s %40s" % ("ls", "lists all items in folder")) 
    print("%19s %40s" % ("cd [folder name]", "changes directory")) 
    print("%19s %40s" % ("mkdir [folder name]", "creates a new directory")) 
    print("%19s %40s" % ("touch", "creates a new file")) 
    print("%19s %40s" % ("edit [file index]", "edits the contents of a file")) 
    print("%19s %40s" % ("rm [file index]", "removes a file")) 
    print("%19s %40s" % ("rmdir [folder name]", "removes a folder"))  

while (True):
    # print(fileSystem)
    command = raw_input(getFolderName(currentLoc) + ": ")
    # The big IF: based on command entered, run specific action.
    inputs = command.split(" ")
    if (inputs[0] == "ls"):
        ls(currentLoc)
    elif (inputs[0] == "cd" and len(inputs) > 1):
        if cd(currentLoc, inputs[1]) != -1:
            currentLoc = cd(currentLoc, inputs[1])
    elif (inputs[0] == "mkdir" and len(inputs) > 1):
        fileSystem = mkdir(currentLoc, inputs[1])
    elif (inputs[0] == "rmdir" and len(inputs) > 1):
        fileSystem = rmdir(currentLoc, inputs[1])
    elif (inputs[0] == "touch"):
        fileSystem = touch(currentLoc)
    elif (inputs[0] == "edit" and len(inputs) > 1):
        fileSystem = edit(currentLoc, inputs[1])
    elif (inputs[0] == "rm" and len(inputs) > 1):
        fileSystem = rm(currentLoc, inputs[1])
    if (inputs[0] == "help"):
        showHelp()
