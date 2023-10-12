def main(x):
    print('Amount Due:',x)
    while x>0:
        y=int(input('Insert Coin: '))
        if accepted(y): 
            x=x-y
        if x>0:
            print('Amount Due:',x)
        else:
            print('Change Owed:', -x)

def accepted(y):
    return y==5 or y==10 or y==25

main(50)