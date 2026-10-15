from menu_data import csv_text

# call your helper functions from in here
def makeList(msg):
  newList = []
  for row in msg.splitlines():
    for part in row.split(","):
      newList.append(part)
  
  return newList

def group(string):
    newList = makeList(string)
    groups = []
    i = 0
    while i < len(newList):
        groups.append(newList[i:i+4])
        i += 4
    return groups

def makeDict(string):
    listWithGroups = group(string)
    newDict = {}
    for category in listWithGroups:
        if category[0] not in newDict:
            newDict[category[0]] = []
        newDict[category[0]].append(category)

    updatedDict = {}
    for category in newDict:
        newDict[category.pop(0)]

    # return newDict
    return updatedDict

print(makeDict(csv_text))

# def removeFirstIndex(newDictionary):
#     newDict = makeDict(newDictionary)
#     updatedDict = {}
#     for category in newDict:
#         print(newDict[category])
#
#
#     # return
#
# # print(makeDict(csv_text))
# print(removeFirstIndex(csv_text))

def main(string):
    listWithGroups = group(string)
    print(listWithGroups)

# main(csv_text)
