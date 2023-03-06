# printing
print("Hello world")

# creating variable
a = 5

# conditions
if a > 3:
    print("is greater")


# while loop
while a < 10:
    print(a)
    a += 1

while a > 10:
    print(a)
    a += 1
else:
    print("isn't greater than 10")


# array
fruits = ["apple", "orange", "mango", "pineapple"]

# for loop
for fruit in fruits:
    print(fruit)

print()

# break keyword
for fruit in fruits:
    print(fruit)
    if fruit == "orange":
        break

# functions


def sayMyName():
    name = "Bobzero"
    print("Hello, " + name)


sayMyName()
