global fileSystem
fileSystem = "[folder:dorit[folder:winter[folder:december[][file:sleet][file:ice]]]]"

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

currentLocation = findLocation(0)

def currentFolderContents(index):
    index = index + 1
    openB = 0
    closedB = 0
    for i in range(findLocation(index), len(fileSystem)):
        if fileSystem[i] == "[":
            openB+=1
        if fileSystem[i] == "]":
            closedB +=1
        if openB == closedB:
            return fileSystem[findLocation(index):i+1]

def currentFolderName(index):
    index = index + 1
    i = findLocation(index)
    while (fileSystem[i] != ":"):
        i-=1
    return fileSystem[i+1:findLocation(index)]


# while (True):
#     # print(fileSystem[currentLocation] + " "),
#     input(fileSystem[currentLocation] + ": ")
#     break

print(findLocation(1))
print(currentFolderContents(1))
print(currentFolderName(0))
