def main():
    name=input('camelCase: ')
    print_one('snake_case: ')
    for c in name:
        if is_upper(c): 
            print_one('_')
            print_one(c.lower())
        else:
            print_one(c)

# function that checks if one letter is uppercase
# input: a string of length one that contains one letter
# output: True or False
def is_upper(c):
    return c.upper()==c

# function that doesn't move the prompt after printing one string
def print_one(s):
    print(s,end='')

main()
