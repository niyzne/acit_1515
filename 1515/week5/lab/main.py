import menu_data
from menu_data import csv_text

def main(text):
    newDict = menu_data.getDict(text)
    organizeDict = menu_data.organize(newDict)
    print(organizeDict)

main(csv_text)
