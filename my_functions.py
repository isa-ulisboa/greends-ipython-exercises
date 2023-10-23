def print_reversed(names: list):
    # using the global variable instead of the parameter by accident
    print(__name__)
    i = len(names) - 1
    while i>=0:
        print(names[i])
        i -= 1

if __name__ == "__main__":
    # here the global variable is assigned
    name_list = ["Steve", "Jean", "Katherine", "Paul"]
    print_reversed(name_list)
    print()
    print_reversed(["Huey", "Dewey", "Louie"])