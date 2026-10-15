from menu_data import csv_text

# call your helper functions from in here
def makeList(msg):
  newList = []
  for row in msg.splitlines():
    for part in row.split(","):
      newList.append(part)
  
  return newList

def main(string):
    newList = makeList(string)
    print(newList)

main(csv_text)
