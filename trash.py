# stuff we don't need at the moment

## Neat little way to list everything + type
# for i in range(totalItems()):
#     print(currentFolderName(i) + ": " + itemType(i))


# Old bracket-based methods

# def findLocation(index):
#     openB = 0
#     closedB = 0
#     for i in range(len(fileSystem)):
#         if fileSystem[i] == "[":
#             openB+=1
#         if fileSystem[i] == "]":
#             closedB +=1
#         if openB == index + 1:
#             return i



# def currentFolderContents(index):
#     index = index + 1
#     openB = 0
#     closedB = 0
#     for i in range(findLocation(index), len(fileSystem)):
#         if fileSystem[i] == "[":
#             openB+=1
#         if fileSystem[i] == "]":
#             closedB +=1
#         if openB == closedB - 1:
#             return fileSystem[findLocation(index):i]


# def currentFolderName(index):
#     index = index + 1
#     i = findLocation(index)
#     while (fileSystem[i] != ":"):
#         i-=1
#     return fileSystem[i+1:findLocation(index)]