# # A program to practice try and except.

# try:
#     # Code that may raise an error or exception
#     result = 3 / 9
#     print(result)
# except:
#     # Incase the code above raise an error then do this below.
#     print("An exception occured in the code above.")


# function that demonstrates the try and except concept.


def divide(x, y):
    try:
        result = x // y
        print(f"Yes! the answer of dividing x by y is: {result}")
    except ZeroDivisionError:
        print(
            f"You encountered the zero division error one of your numbers either {x} or {y} is a zero, choose another number. "
        )


divide(4, 2)
# divide(4, 0)

# Trying to catch the exact error.


# def add(x, y):
#     try:
#         result = x + y
#         print(f"Answer of {x} + {y} is: {result}")
#     except Exception as error:
#         # Catching the exact error
#         print(f"The error is: {error}")


# add(2, 3)
# add(2, "boy")

# Trying the try-except concept that has an else clause.


def divide1(x, y):
    try:
        result = x // y
        print(f"Answer is: {result}")
    except ZeroDivisionError:
        print("Error!, number cannot be divisible by zero.")
    else:

        add = lambda x, y: x + y
        print(f"Addition of {x} and {y} is: {add(4, 5)}")


divide1(8, 4)
