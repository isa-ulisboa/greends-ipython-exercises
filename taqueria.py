# menu
menu = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

""" 
# Sugestion of pseudo-code
def main():
    # while order is not finished
        # option=get_option_from_user()
        # print total cost

def get_option_from_user():
    # input option
 """

def main():
    total=0
    # request options
    while True:
        x = get_option_from_user()
        if x>=0:
            total += x
            print(f"Total: ${total:.2f}")
        else:
            break

# returns -1 if EOFError is raised, otherwise returns option's price
def get_option_from_user():
    while True:
        try:
            option = input("Item: ")
            return(menu[option.title()])
        except KeyError:
            pass # could print warning instead
        except EOFError:
            #print("crtl-Z")
            return(-1)


main()




""" 
# solution that works:
total = 0
while True: 
    try:
        item = input("Item: ").lower()
        for i in menu:
            if item == i.lower():
                total += menu[i]
                print(f"Total: ${total:.2f}")
            else:
                pass
    except EOFError:
        print()
    break """




    
