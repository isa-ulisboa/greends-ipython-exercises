import random

# global variables:
N=2 # number of problems
T=3 # maximum number of tries

def main():
    level=get_level()
    count_correct=0
    for i in range(N):
        # result can be True (success) or False (failure)
        prompt,correct_answer=generate_prompt(level)
        solved=False
        for t in range(T):
            print(prompt,end="")
            answer=get_integer("")  # <-- needs to count the number of tries here too
            if answer==correct_answer:
                solved=True
                count_correct +=1
                break
            else:
                print("EEE")
        if not solved:
            print(prompt,correct_answer)
        
def get_level():
    while True:
        level=get_integer("Input integer between 1 and 3: ")
        if 1<=level<=3:
            return(level)

def generate_prompt(level):
    X=generate_integer(level)
    Y=generate_integer(level)
    prompt=f"{X} + {Y} = "
    correct_answer=X+Y
    return prompt, correct_answer

def generate_integer(level):
    return(random.randint(0,10**level-1))

def get_integer(message):
    while True:
        try:
            return(int(input(message)))
        except ValueError:
            print("EEE")

if __name__ == "__main__":
    main()


