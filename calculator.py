# built-in function- it's comes installed with python, so you can use it without creating the function.

# variable: a small container that stores small pieces of data (integers, strings, booleans, etc.)
operator = input("Choose either +, -, *, or /:")
while operator != "+" and operator != "-" and operator != "*" and operator != "/":
    operator = input("Please choose again! ")



# data casting- turning one data type into another temporarily


alphabet = "!@#$%^&*()_+=-qwertyuiopasdfghjklzxcvbnm,./;'[]"
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

