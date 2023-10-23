def return_name():
    print(f'The __name__ from functions is "{__name__}"')

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


# input: string (prompt to user), float (minimum value for input), float (maximum value for input)
# output: integer (user's provided integer between minimum and maximum)
def get_decimal(prompt: str,Min: float, Max: float) -> float:
    while True:
        try:
            x=float(input(prompt+' '))
        except ValueError:
            pass
        else:
            if Min <= x <= Max:
                return x

def my_sqrt(x):
    if x<0: 
        return 'NaN'
    delta=0.0001
    Max=x+1
    Min=0
    sqrt=(Min+Max)/2
    while Max-Min>delta:
        if sqrt*sqrt > x:
            Max=sqrt
        else:
            Min=sqrt
    return sqrt




