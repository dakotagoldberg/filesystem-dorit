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