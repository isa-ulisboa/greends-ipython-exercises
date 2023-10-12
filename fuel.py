""" 
def main():
    # f=get_fuel_fraction
    # compute and print out percentage, E or F

def get_fuel_fraction()
    while True:
        # fuel=get input from user (string)
        try:
            # parse input
            # if conditions are fulfilled, return percentage and breaks from while loop
        except ValueError:
            # print smth
        except ZeroDivisionError:
            # print smth
 """

def main():
    f=get_fuel_fraction()
    if f<0.01:
        print("E")
    elif f>0.99:
        print("F")
    else:
        print(f"{round(100*f)}%")

def get_fuel_fraction():
    while True:
        fuel = input("Fraction: ")
        try:
            string_X, string_Y= fuel.split("/")
            X,Y=int(string_X),int(string_Y)
            if 0<=X<=Y:
                return X/Y
            else:
                pass # could print error message
        except ValueError:
            pass # could print error message
        except ZeroDivisionError:
            pass # could print error message
    
main()


