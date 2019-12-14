global fileSystem
fileSystem = "[folder:dorit[folder:winter[folder:december[]][file:sleet][file:ice]]]"

def ls(index):
    print("working")
    index = index + 1
    openB = 0
    closedB = 0
    startRead = True
    temp = ""
    for i in range(findLocation(index), len(fileSystem)):
        if fileSystem[i] == "[":
            print ("open bracket")
            openB+=1
        if fileSystem[i] == "]":
            print ("close bracket")
            closedB +=1
            if startRead:
                temp += " "
        if openB == closedB +1:
            print ("read")
            startRead = True
        elif True :
            print ("close eyes")
            startRead = False
        if startRead and (fileSystem[i] != '[' and fileSystem[i] != ']'):
            print (fileSystem[i])
            temp += fileSystem[i]
        if openB < closedB:
            return temp

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

print(ls(1))
