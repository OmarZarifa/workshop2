def name():
    name = input("Enter your name: ")
    return name
    
def age():
    age = int(input("Enter your age: "))
    return age

def get_info(name, age):
    print(f"Your name is: {name} and your age is {age}")

def main():
    n = name()
    a = age()
    get_info(n, a)


if __name__ == '__main__':
    main()
