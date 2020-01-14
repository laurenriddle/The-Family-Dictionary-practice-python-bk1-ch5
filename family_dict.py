# Define a dictionary that contains information about several members of your family.
my_family = {
    "sister": {
        "name": "Krista",
        "age": 42
    },
    "mother": {
        "name": "Cathie",
        "age": 70
    },
    "father": {
        "name": "James",
        "age": 75
    }
}

# Using a dictionary comprehension, produce output that looks like the following example: Krista is my sister and is 42 years old.

dict_2 = {f'{my_family[member]["name"]} is my {member} and is {my_family[member]["age"]} years old' for member in my_family}
print(dict_2)

# regular for loop
for member in my_family:
    print(f'{my_family[member]["name"]} is my {member} and is {my_family[member]["age"]} years old')