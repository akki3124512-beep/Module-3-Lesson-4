while True:
    try:
        def age(a):
            if a%2==0:
                return ("\n Your age is even.")
            else:
                return ("\n Your age is odd.")
        
        x = int(input("Enter your age: "))
        print("Your age is: ", x, age(x))

    except ValueError:
        print("Please enter your number in digit form.")
