csv_text = """lunch,bento box b - sashimi,box combo,$9.59
dinner,vegetable sushi,6 rolls,$3.50
dinner,tuna roll,3 rolls,$4.50
dinner,roe,2 rolls,$3.95
lunch,bento box a - chicken teriyaki,box combo,$8.59
dessert,cheesecake,1 slice,$8.00"""

def main():
    manu = {}
    for line in csv_text.split("\n"):
        category, item = parse_items(line)
        if category in menu:
            menu[category].append(item)
        else:
            menu[category] = [item]

    # TODO: format groupings into a pretty menu str
    # TODO: print the pretty menu

main()
