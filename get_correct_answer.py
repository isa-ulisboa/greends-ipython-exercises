def get_correct_answer(message,N,max_tries):
        tries=0
        while tries<max_tries:
            tries+=1
            try:
                answer=int(input(message))
            except ValueError:
                pass
            else:
                 if answer==N:
                     return True,tries
        return False,tries

print(get_correct_answer("number: ",4,3))