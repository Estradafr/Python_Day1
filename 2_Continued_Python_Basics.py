""" Section 1 - sets and tuples: """
# * Pre-Question: Take a look at this JavaScript Array:
# * let javaScriptArray = [12, 55, 33, 40, 55, 33, 20, 12

# ? How would you remove duplicates from this JavaScript Array? Take a few minutes to consider what steps are necessary to iterate through this array in JavaScript and remove the duplicates values.
# * What advantages are available when we're working with Python? If this Array was instead a set, we wouldn't be able to store multiple values in it. Uncomment the identical set below and run the print statement. What did you notice in the console return?

my_set = {12, 55, 33, 40, 55, 33, 20, 12}
print(my_set)

# ? Question 1a: Create a set of your own with at least 3 different elements.
# * A set is an unordered collection of unique elements. This means that each element can only appear once in a set. They are separated by commas. No duplicates are allowed.

three_different_elements = {
    "apple",
    "banana",
    "orange"
}

# ? Question 1b: Add an item to the set that you just created.

three_different_elements.add("grape")

# ? Question 1c: Print the set with the new data that you added to it:

print(three_different_elements)

# ? Question 2a: Create a tuple with at least 3 elements inside of it.

three_element_tuple = ("apple", "banana", "orange")

# ? Question 2b: Print the tuple you just created.
# * A tuple is an ordered collection of elements, similar to a list. However, unlike a list, a tuple is immutable, which means that once it is created, its elements cannot be modified. Tuples are defined using parentheses and their elements are separated by commas.

print(three_element_tuple)

""" Section 2 - loops: """

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
# ? Question 3: Use a for loop to iterate through the 'days' list above and print the days of the week:

for d in days:
    print(d)

for i, x in enumerate(days):
    print(f"{i}\t {x}")
#   0 Monday
#   1 Tuesday
#   2 Wednesday
#   3 Thursday
#   4 Friday

# ? Question 4: Loop through add_list and add each value to x. Print the value of x at each increment:
x = 10
add_list = [10, 6, 12, 4, 5]

for value in add_list:
    x += value
    print(x)
    # * 20, 26, 38, 42, 47
    # * Shortcut: x += sum([10, 6, 12, 4, 5])

# ? Question 5: While Loops

# Declare an iterator variable (set to the number 1) and write a While loop that adds 5 to the value of the variable starting_value as long as the iterator is under 10:

starting_value = 5
iterator = starting_value
while iterator < 10:
    iterator += 1
    print(iterator)
    # * 6, 7, 8, 9, 10


""" Section 3 - conditionals: if, elif, else statements"""

favorite_movie = "Back to the Future II"
# ? Question 6a: Uncomment the favorite_movie variable above and change the value to the title of your favorite movie
# Below, write a conditional statement that prints the string "that's a great movie" if the favorite_movie variable equals your favorite movie.
# Otherwise (else), print the string "that's not my favorite movie".
# Mess around with the value of the favorite_movie variable and trigger both conditional responses:

if favorite_movie == "Back to the Future II":
    print("That's a great movie")
else:
    print("That's not my favorite movie")


# ? Question 6b: Uncomment the movie_list variable below and implement a for loop that iterates through each item in the list.
# If the item is a blueberry (or another fruit), print "item is a fruit and not movie";
# if the item is a car manufacturing company like Toyota, print "item is a car and not a movie";
# otherwise, just print the movie in the list:

movies = ["Inception", "blueberries", "Toyota", "Good Will Hunting"]

for movie in movies:
    if movie == "blueberries":
        print(f"This item is a fruit and not a movie!")
    elif movie == "Toyota":
        print("This item is a car..")
    else:
        print(f"{movie} is a great movie!")


# * BONUS - conditional and operators practice:

a = 5
b = 5
c = 12

# ? Question 7a: Use the correct operator to add variables a & c:

a + c

# ? Question 7b: Use the correct operator to subtract variables b & c:

b - c

# ? Question 7c: Use the correct comparison operator that shows if variables a & b equal each other:

a == b

# ? Question 7d: Use the correct operator to find the quotient of variables c & a

c / a

# ? Question 7e: Use the correct operator to find if variables c & b are not equal to each other:

c != b
