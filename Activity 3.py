valid = False
while not valid:
    x = int(input("Enter a number: "))
    try:
        while x % 2 == 0:
            print("bye")
        valid = True
    except ValueError:
        print("Enter a digit.")


