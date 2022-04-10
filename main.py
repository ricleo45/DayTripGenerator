# source lists
import random
destinations = ['California', 'Utah', 'Colorado', 'Florida', 'New York' ]
restaurants = ['Popeyes', 'MC Donalds', 'Applebees', 'Texas Road House', 'Gas Station']
transportation = ['Space Ship', 'Plane', 'Train', 'Bike', 'Bus']
entertainment = ['Movies', 'TV shows', 'Magazines', 'Nap taking', '']
ran_value1 = random.randint(0, 4)
ran_value2 = random.randint(0, 4)
ran_value3 = random.randint(0, 4)
user_name = input('Please enter your Name Here: ')
message = "Alright " + user_name + " let's being."
print(message)
# random destination choices 
while True:
    dest = input(f'Do you want to got to {destinations[ran_value1]} ? Enter y/n ')
    if dest == 'y':
        dest = destinations[ran_value1]
        print('Great choice!')
        break
    elif dest == 'n':
        break
while dest == 'n':
        dest = input(f'how about {destinations[ran_value2]} ? Enter y/n ')
        if dest == 'y':
            dest = destinations[ran_value2]
            print('Perfect!')
            break
        elif dest == 'n':
            break
while dest == 'n':
        if dest == 'y':
            dest = input(f'or {destinations[ran_value3]} ? Enter y/n ')
            dest = destinations[ran_value3]
            print('Nice choise!')
            break
        elif dest == 'n':
            print(f'Looks like we are out of choices {user_name} please try again :(')
            break

# mode of transportation choices
while True:
    trans = input(f'Do you want to use {transportation[ran_value1]} ? Enter y/n ')
    if trans == 'y':
        trans = transportation[ran_value1]
        print('Great choice!')
        break
    elif trans == 'n':
        break
while trans == 'n':
        trans = input(f'how about a {transportation[ran_value2]} ? Enter y/n ')
        if trans == 'y':
            trans = transportation[ran_value2]
            print('Perfect!')
            break
        elif trans == 'n':
            break
while trans == 'n':
        if trans == 'y':
            trans = input(f'or a {destinations[ran_value3]} ? Enter y/n ')
            trans = transportation[ran_value3]
            print('Nice choise!')
            break
        elif trans == 'n':
            print(f'Looks like we are out of choices {user_name} please try again :(')
            break
# entertainment random choices

# ability to (re)select random destinations, restaurants, mode of transportation, and/or entertainment

# ability to confirm trip completion
'''
user_is_done = input('if this is your ideal trip Enter y to confirm and n to end session and retry. Enter y/n ')
if user_is_done == 'y':
'''
# sum all functions into one final conclusion (each function should do just one thing!)