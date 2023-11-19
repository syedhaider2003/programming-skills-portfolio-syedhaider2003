def make_shirt(size="large", message="I love Python"):
    print(f"This shirt is a {size} with the message '{message}'.")

make_shirt() # Make a large shirt with the default message
make_shirt(size="medium") # Make a medium shirt with the default message
make_shirt(size="small", message="Python is amazing!") # Make a shirt of any size with a different message