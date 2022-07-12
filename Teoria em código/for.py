# Print each fruit in a fruit list:
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)

# Loop through the letters in the word "banana":
for x in "banana":
    print(x)


# Exit the loop when x is "banana":
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)
    if x == "banana":
        break

# Exit the loop when x is "banana", but this time the break comes before the print:
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        break
    print(x)


    fruits = [1,2,3,4,5,6,7,8,9]
for x in fruits:
    if x >3  & x< 7:
        continue
    else:
        print("SL")



for x in range(6):
    print(x)
else:
    print("Finally finished!")

for x in range(6):
    if x == 3:
        break
    print(x)
else:
    print("Finally finished!")


# Print each adjective for every fruit:
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
    for y in fruits:
        print(x, y)

# function receive 2 itens and print the 2 received arguments


def my_function(fname, lname):
    print(fname + " " + lname)


my_function("Cris", "Marcelo")

# If the number of arguments is unknown, add a * before the parameter name:


def my_function(*kids):
    print("The youngest child is " + kids[2])


my_function("Emil", "Tobias", "Linus")


# more arguments and stuff
def my_function(child3, child2, child1):
    print("The youngest child is " + child2)


my_function(child1="Emil", child2="Tobias", child3="Linus")

# returning argumetns


def my_function(x):
    return 5 * x


print(my_function(3))
print(my_function(5))
print(my_function(9))
