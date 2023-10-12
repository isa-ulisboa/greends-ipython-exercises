def main():
    name=input("Input: ")
    output='Output: '
    for c in name:
        if not is_vowel(c):
            output += c
    print(output)

def is_vowel(c):
    return c.lower() in ['a','e','i','o','u']

main()
