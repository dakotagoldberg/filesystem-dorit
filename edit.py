def edit(charNum, fileVal, newVal, fileNum):

 firstString = fileSystem[:charNum]
 secondString = fileSystem[charNum:]
 found = 0
 temp = 0
 if found != -1:
  print "-1"
 else:
  for i = 0 to fileNum:
   found = secondString.find(fileVal, (0+temp))
   temp = secondString.find(fileVal, (0+temp))
   temp+1
  tempSub1 = secondString[:found]
  tempSub2 = secondString[found:]
  tempSub2.replace(fileVal, newVal)
  fileSystem = firstString + tempSub1 + tempSub2