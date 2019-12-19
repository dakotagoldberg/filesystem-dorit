#ls #pwd #the String #name of the folder

def mkdir(HowManyCharDeep, fileSystem, name):
    folder = "[folder:" + str(name) + "[]]"
    index = findPlace(pwd, fileSystem)
    if index is None: 
        return (1, "Can't do dat")
    else: 
        fileSystem = fileSystem[:index] + folder + fileSystem[index:]
        return (0, fileSystem)

def findPlace(HowManyCharDeep, fileSystem):


    return HowManyCharDeep #find place will also find duplicat folders
    return None #if there is a duplicate folder

    