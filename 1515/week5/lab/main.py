import menu_data
from menu_data import csv_text

def main(text):
    newDict = menu_data.getDict(text)
    organizeDict = menu_data.organize(newDict)
    uniqueMeals = menu_data.makeUniqueMeals(organizeDict)
    uniqueMeals.sort()
    for mealType in uniqueMeals:
        print()
        print(f"* {mealType.capitalize()} Items *")
        for i in range(len(organizeDict[mealType])):
            price = float(organizeDict[mealType][i]['price'].replace('$', ''))
            price = price * 1.8
            print(f"${price:.2f} {organizeDict[mealType][i]['foodName']} {organizeDict[mealType][i]['amount']}")

main(csv_text)
