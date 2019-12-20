def edit(fileNum):


 while True:

  #print("while1")

  newVal = raw_input("Enter new value: ")


  if newVal.isalnum():

   #print("alpha")

   break


  else:


   print ("Invalid value")

 #print(parseContents(myLoc))

 clown = numberOfFilesInFolder(myLoc)

 print(clown)

 place = findLocation(myLoc)


 if fileNum > clown:


  return "-1"


 else:


  firstString = fileSystem[:place]


  secondString = fileSystem[place:]


  temp = 0

  num  = 0

  while fileNum !=0:

   #print("while2")

   num=secondString.find("file:",temp+1)


   if num:

    temp = num

    print(num)

    fileNum-=1

  print(num)

  subFind = secondString.find(']', temp)

  print(subFind)

  tempSub1 = secondString[:(temp+5)]


  tempSub2 = secondString[(subFind):]


  return(firstString +tempSub1 + newVal + tempSub2)
