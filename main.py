# source lists
import random
destinations = ['California', 'Utah', 'Colorado', 'Florida', 'New York' ]
restaurants = ['Popeyes', 'MC Donalds', 'Applebees', 'Texas Road House', 'Gas station food']
transportation = ['Space Ship', 'Plane', 'Train', 'Bike', 'Bus']
entertainment = ['Movie', 'TV show', 'Magazine', 'Nap', 'Draw']
ran_value1 = random.randint(0, 4)
ran_value2 = random.randint(0, 4)
ran_value3 = random.randint(0, 4)
user_name = input('Please enter your Name Here: ')
message = "Alright " + user_name + " let's being."
print(message)

# random destination choices 
while True:
    dest = input(f'Do you want to go to {destinations[ran_value1]}? Enter y/n ')
    if dest == 'y':
        dest = destinations[ran_value1]
        print('Great choice!')
        break
    elif dest == 'n':
        break
while dest == 'n':
        dest = input(f'how about {destinations[ran_value2]}? Enter y/n ')
        if dest == 'y':
            dest = destinations[ran_value2]
            print('Perfect!')
            break
        elif dest == 'n':
            break
while dest == 'n':
        if dest == 'y':
            dest = input(f'or {destinations[ran_value3]}? Enter y/n ')
            dest = destinations[ran_value3]
            print('Nice choise!')
            break
        elif dest == 'n':
            dest = ('nothing chosen')
            print(f'Looks like we are out of choices {user_name} please try again :(')
            break

# mode of transportation choices
while True:
    trans = input(f'For transportation do you want to use a {transportation[ran_value1]}? Enter y/n ')
    if trans == 'y':
        trans = transportation[ran_value1]
        print('Great choice!')
        break
    elif trans == 'n':
        break
while trans == 'n':
        trans = input(f'how about a {transportation[ran_value2]}? Enter y/n ')
        if trans == 'y':
            trans = transportation[ran_value2]
            print('Perfect!')
            break
        elif trans == 'n':
            break
while trans == 'n':
        if trans == 'y':
            trans = input(f'or a {transportation[ran_value3]}? Enter y/n ')
            trans = transportation[ran_value3]
            print('Nice choise!')
            break
        elif trans == 'n':
            trans = ('nothing chosen')
            print(f'Looks like we are out of choices {user_name} please try again :(')
            break

# entertainment random choices
while True:
    ent = input(f'For entertainment do you want to enjoy a {entertainment[ran_value1]}? Enter y/n ')
    if ent == 'y':
        ent =entertainment[ran_value1]
        print('Great choice!')
        break
    elif ent == 'n':
        break
while ent == 'n':
        ent = input(f'how about a {entertainment[ran_value2]}? Enter y/n ')
        if ent == 'y':
            ent =entertainment[ran_value2]
            print('Perfect!')
            break
        elif ent == 'n':
            break
while ent == 'n':
        if ent == 'y':
            ent = input(f'or a {entertainment[ran_value3]}? Enter y/n ')
            ent =entertainment[ran_value3]
            print('Nice choise!')
            break
        elif ent == 'n':
            ent = ('nothing chosen')
            print(f'Looks like we are out of choices {user_name} please try again :(')
            break

# ability to choose a restaurant
while True:
    rest = input(f'For places to eat, do you want to enjoy {restaurants[ran_value1]}? Enter y/n ')
    if rest == 'y':
        rest = restaurants[ran_value1]
        print('Great choice!')
        break
    elif rest == 'n':
        break
while rest == 'n':
        rest = input(f'how about {restaurants[ran_value2]}? Enter y/n ')
        if rest == 'y':
            rest = restaurants[ran_value2]
            print('Perfect!')
            break
        elif rest == 'n':
            break
while rest == 'n':
        if rest == 'y':
            rest = input(f'maybe {restaurants[ran_value3]}? Enter y/n ')
            rest = restaurants[ran_value3]
            print('Nice choise!')
            break
        elif rest == 'n':
            rest = ('nothing chosen')
            print(f'Looks like we are out of choices {user_name} please try again :(')
            break

# ability to confirm trip completion
user_is_done = input('if this is your ideal trip Enter y to confirm and n to end session and retry. Enter y/n ')
if user_is_done == 'y':
# sum all functions into one final conclusion (each function should do just one thing!)
    print(f'Alright {user_name} , the trip to {dest} will start by {trans} enjoying a {ent} and eating at {rest} when you get there.')
