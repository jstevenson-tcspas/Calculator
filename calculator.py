# built-in function- it's comes installed with python, so you can use it without creating the function.

# variable: a small container that stores small pieces of data (integers, strings, booleans, etc.)

# parameters: variables that you use in a function
def add(bob, rob):
    print(bob + rob)
def sub(a, b):
    print(a - b)
def mult(c, d):
    print(c * d)
def div(e, f):
    print(e / f)
operator = input("Choose either +, -, *, or /:")
while operator != "+" and operator != "-" and operator != "*" and operator != "/":
    operator = input("Please choose again! ")



# data casting- turning one data type into another temporarily


alphabet = "!@#$%^&*()_+=-qwertyuiopasdfghjklzxcvbnm,./;'[] "
first_number = input("choose a number:  ")
running = True
while running:
    for letter in first_number:
        if letter in alphabet:
            first_number = input("please try again ")
            break
        else:
            running = False

second_number = input("chose another number to use:  ")
running = True
while running:
    for letter in second_number:
        if letter in alphabet:
            second_number = input("please try again ")
            break
        else:
            running = False

# arguments: data you put in parameters

if operator == "+":
    add(int(first_number), int(second_number))
elif operator == "-":
    sub(int(first_number), int(second_number))
elif operator == "*":
    mult(int(first_number), int(second_number))
elif operator == "/":
    div(int(first_number), int(second_number))
