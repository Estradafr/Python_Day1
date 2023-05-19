# A function named hello() that prints a greeting to the user. This function should accept no arguments and returns nothing.

def greet_user():
    print("Hello, user!")

# A function named pack() that accepts three arguments, and returns a single list with the three arguments inside as list elements.


def pack(arg1, arg2, arg3):
    return [arg1, arg2, arg3]

# A function called eat_lunch(). This function should accept a list of any length, and print out a series of strings that say "First I eat __"
# (the first element of the list), and "Next I eat ___" (for the following elements in the list). If the list is empty, print "My lunchbox is empty!".
# The function should not return anything.


def eat_lunch(lunch_items):
    if not lunch_items:
        print("My lunchbox is empty!")
    else:
        for idx, item in enumerate(lunch_items):
            if idx == 0:
                print(f"First I'll eat my {item}")
            elif idx == len(lunch_items) - 1:
                print(f"For desert I'll eat my {item}")
            else:
                print(f"Then I'll eat my {item}")


greet_user()
print(pack("a", "b", "c"))
print(pack(1, 2, 3))
eat_lunch([])
eat_lunch(["sandwich"])
eat_lunch(["apple", "banana", "sandwich", "cookie"])
