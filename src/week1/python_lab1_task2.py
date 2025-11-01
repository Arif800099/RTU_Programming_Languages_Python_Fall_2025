def greet_user(name):
    return f"Hello, {name.strip().capitalize()}! Welcome to Python!"

if __name__ == "__main__":
    name = input("Enter your name: ")
    print(greet_user(name))
