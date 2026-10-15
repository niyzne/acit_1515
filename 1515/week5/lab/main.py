import menu_data
from menu_data import csv_text

def main(text):
    newDict = menu_data.getDict(text)
    organizeDict = menu_data.organize(newDict)
    uniqueMeals = menu_data.makeUniqueMeals(organizeDict)
    for mealType in uniqueMeals:
        print()
        print(f"* {mealType.capitalize()} Items *")
        for i in range(len(organizeDict[mealType])):
            print(f" {organizeDict[mealType][i]['price']} {organizeDict[mealType][i]['foodName']} {organizeDict[mealType][i]['amount']}")

main(csv_text)
