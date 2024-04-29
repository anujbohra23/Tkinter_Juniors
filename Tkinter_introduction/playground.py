# Functionality of args
def add(*numbers):
    total = 0
    for num in numbers:
        total += num
    print(f"Total : {total}")


add(1, 34, 5, 3, 2, 1, 5, 2131, 9)
add(1, 2, 3)
add(1, 2)


# Functionality of kwargs
def calculate(n, **operation):
    n += operation["add"]
    n *= operation["multiply"]
    print(f"Final answer: {n}")


calculate(5, add=5, multiply=2)
