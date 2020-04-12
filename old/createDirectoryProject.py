def mkdir(HowManyColDeep, fileSystem, name, input):
    
    #make mkdir only take path
    var = input.split("/") 
    
    if not var[0]:   
        
        
        result = parsePath(var, name, HowManyColDeep)
    else:
        
        var = currentPath(HowManyColDeep)[::-1] + var
        
        result = parsePath(var, name, HowManyColDeep)
        
        
    if  result is not None:
        folder = "folder:" + str(name) + "[]"
        index = findLocation(HowManyColDeep)
        fileSystem2 = fileSystem[:result] + folder + fileSystem[result:]
        
        return (0, fileSystem2) 
    else:  
        return (1, "Can't do dat")

def parsePath(var, name, HowManyColDeep):
    loc = HowManyColDeep
    for i in range(len(var)-2): 
        loc+=1
        if not (var[i+1] in parseContents(reverseLookup(var[i]))) and var[0] is not None:
            return None
        
        tempvar = parseContents(loc)
    
        if name in tempvar:
            return None
    return findLocation(reverseLookup(var[(len(var)-2)])) + len(var[(len(var)-2)]) + 2
