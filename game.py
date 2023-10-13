import random

def main():
    level=get_integer("Level: ")
    # number to guess
    number=random.randint(1,level)
    while True:
        n=get_integer("Guess: ")
        if n==number:
            print("Just right!")
            break
        elif n<number:
            print("Too small!")
        else:
            print("Too large!")

def get_integer(message):
    while True:
        try:
            return(int(input(message)))
        except ValueError:
            pass

main()

