csv_text = """lunch,bento box b - sashimi,box combo,$9.59
dinner,vegetable sushi,6 rolls,$3.50
dinner,tuna roll,3 rolls,$4.50
dinner,roe,2 rolls,$3.95
lunch,bento box a - chicken teriyaki,box combo,$8.59"""

def getDict(longString):
    listOfThings = csv_text.split('\n')
    newList = []
    for row in listOfThings:
        bitsOfRow = row.split(",")
        newList.append({"when":bitsOfRow[0],"what":bitsOfRow[1],"amount":bitsOfRow[2],"price":bitsOfRow[3]})
    print(newList)

getDict(csv_text)
