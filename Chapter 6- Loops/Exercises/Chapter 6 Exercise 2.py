while True:
    age = int(input("Enter your age (or type 'quit' to stop): "))

    if age == 'quit':
        break
    elif age < 3:
        print("Your ticket is free!")
    elif 3 <= age <= 12:
        print("The cost of your movie ticket is $10.")
    else:
        print("The cost of your movie ticket is $15.")