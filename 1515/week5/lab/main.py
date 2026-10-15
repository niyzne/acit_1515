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
        # if (smth)
            # smth
        # smth append

    return newDict

print(makeDict(csv_text))

def main(string):
    listWithGroups = group(string)
    print(listWithGroups)

# main(csv_text)
