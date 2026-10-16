import menu_data

def main(text):
    newDict = menu_data.getDict(text)
    organizeDict = menu_data.organize(newDict)
    uniqueMeals = menu_data.makeUniqueMeals(organizeDict)
    uniqueMeals.sort()
    for mealType in uniqueMeals:
        print(f"\n* {mealType.capitalize()} Items *")
        for i in range(len(organizeDict[mealType])):
            price = (float(organizeDict[mealType][i]['price'].replace('$', ''))) * 1.8
            food = organizeDict[mealType][i]['foodName']
            amount = organizeDict[mealType][i]['amount']
            print(f"${price:.2f} {food}, {amount}")

main(menu_data.csv_text)
