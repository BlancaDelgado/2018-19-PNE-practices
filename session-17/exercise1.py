# Testing a JSON object

import json
import termcolor

# -- Open the json file
f = open("people.json", 'r')

# Read the data from the file
# Now person is a dictionary with all the information
person = json.load(f)

# Print the number of people in the jason file
print()
num_people = len(person['Firstname'])
print("Total people in the database: {}".format(num_people))

for i in range(0,num_people):
    print()

    # Print the information of the object
    termcolor.cprint("Name: ", 'green', end="")
    print(person['Firstname'][i], person['Lastname'][i])

    termcolor.cprint("Age: ", 'green', end="")
    print(person['age'][i])

    # Get the phoneNumber list
    phoneNumbers = person['phoneNumber'][i]

    # Print the number of elements int the list
    termcolor.cprint("Phone numbers: ", 'green', end='')
    print(len(phoneNumbers))

    # Print all numbers
    for i, num in enumerate(phoneNumbers):
        termcolor.cprint("  Phone {}:".format(i), 'blue')

        # The element num contains 2 fields: number and type
        termcolor.cprint("    Type: ", 'red', end='')
        print(num['type'])
        termcolor.cprint("    Number: ", 'red', end='')
        print(num['number'])
