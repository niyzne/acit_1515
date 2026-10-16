# csv_text = """lunch,bento box b - sashimi,box combo,$9.59
# dinner,vegetable sushi,6 rolls,$3.50
# dinner,tuna roll,3 rolls,$4.50
# dinner,roe,2 rolls,$3.95
# lunch,bento box a - chicken teriyaki,box combo,$8.59"""

csv_text = """lunch,bento box b - sashimi,box combo,$9.59
dinner,vegetable sushi,6 rolls,$3.50
dinner,tuna roll,3 rolls,$4.50
dinner,roe,2 rolls,$3.95
lunch,bento box a - chicken teriyaki,box combo,$8.59
dessert,cheesecake,1 slice,$8.00"""

def getDict(longString):
    listOfThings = longString.split('\n')
    newList = []
    for row in listOfThings:
        bitsOfRow = row.split(",")
        newList.append({"when":bitsOfRow[0],"foodName":bitsOfRow[1],"amount":bitsOfRow[2],"price":bitsOfRow[3]})
    return newList

def organize(meals):
    result = {}
    for item in meals:
        if str(item["when"]) not in result:
            result[str(item["when"])] = []
        result[str(item["when"])].append(item)
    return result

def makeUniqueMeals(newMenuDict):
    newUniqueMeals = []
    for type in newMenuDict:
        newUniqueMeals.append(type)
    return newUniqueMeals
