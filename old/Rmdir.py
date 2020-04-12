def Rmdr(index, foldername):
    print "spencer"
    openB = 0
    closedB = 0
    deletethis = changeDirectory(findLocation(index),foldername)
    if fileSystem[foldername.length + findLocation(myLoc) + 1, foldername.length + findLocation(myLoc) + 2] == "[]" :
        fileSystem = fileSystem[0, findLocation(index) - 6] + fileSystem[foldername.length + findLocation(myLoc) + 3, fileSystem.length]
    else:
        print "cannot delete. Something is in that folder"