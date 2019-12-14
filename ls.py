global fileSystem
fileSystem = "[folder:dorit[folder:winter[folder:december[]][file:sleet][file:ice]]]"

def ls(index):
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

print(ls(0))
