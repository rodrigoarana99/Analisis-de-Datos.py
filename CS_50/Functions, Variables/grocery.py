def main():
    grocery()
def grocery():
    #Odds are you’ll want to store your grocery list as a dict.
    grocery_list = {}

    while True:
        item = input(" ").strip().title().upper()
        if item == '':
            break
        grocery_list[item] = grocery_list.get(item, 0) +1 
    #quiero que imprima asi : 1 bananan 2 manzanas 3 peras
    for item, quantity in grocery_list.items():
        print(f"{quantity} {item}")

main()

        