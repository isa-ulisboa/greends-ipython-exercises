import random

# global variables:
N=3 # number of problems
T=3 # maximum number of tries

def main():
    level=get_level()
    count_correct=0
    for i in range(N):
        # create problem
        prompt,correct_answer=generate_prompt(level)
        # prompt for answer: can be True (success) or False (failure)
        correct,tries=get_answer(prompt,correct_answer,T)
        # update number of correct answers or provide the correct answer
        if correct:
            count_correct += 1
        else:
            print(prompt,correct_answer)
    # print score
    print("Score:", count_correct)

# input: void
# output: integer (user provided integer between 1 and 3)
def get_level():
    return(get_integer("Level:",1,3))

# input: integer (level)
# output: string (prompt for the user, e.g. '3 + 8 = '), integer (correct answer, e.g. 11)
def generate_prompt(level):
    X=generate_integer(level)
    Y=generate_integer(level)
    prompt=f"{X} + {Y} ="
    correct_answer=X+Y
    return prompt, correct_answer

# input: integer (level)
# output: integer (non-negative random number between 0 and 9, or between 10 and 99 or between 100 and 999)
def generate_integer(level):
    if level==1:
        return random.randint(0,9)
    elif level==2:
        return random.randint(10,99)
    elif level==3:
        return random.randint(100,999)

# input: string (prompt for user), integer (correct answer), integer (T=maximum number of tries)
# output: L,n_iter, where L is boolean (True is the answer is correct within T tries, and False otherwise) 
def get_answer(prompt,n,T):
    tries=0
    while tries<T:
        tries+=1
        try:
            x=int(input(prompt+' '))
        except ValueError:
            pass
        else: 
            if x==n:
                return True
            else:
                print('EEE')
    return False

# input: string (prompt to user), integer (minimum value for input), integer (maximum value for input)
# output: integer (user's provided integer between minimum and maximum)
def get_integer(prompt,Min, Max):
    while True:
        try:
            x=int(input(prompt+' '))
        except ValueError:
            pass
        else:
            if Min <= x <= Max:
                return x



# main
if __name__ == "__main__":
    main()
