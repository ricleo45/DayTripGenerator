# source lists
destinations = ['California', 'Utah', 'Colorado', 'Florida', 'New York' ]
restaurants = ['Popeyes', 'MC Donalds', 'Applebees', 'Texas Road House', 'Gas Station']
mode_of_transportation = ['Space Ship', 'Plane', 'Train', 'Bike', 'Bus']
entertainment = ['Movies', 'National Park', 'Theme Park', '']

# ask for user name
user_name = input('Please Enter Your Name Here: ')

# random destination choices
ask_destination = input('Hello ' + user_name + ' would you like to choose your destination today? y/n ')
if ask_destination == 'y':
    print(f'Great, would you like to go to {user_name} ?')
    for list in destinations:
            print(list)
elif ask_destination != 'y':
    print(f'My apologies for the inconveniece {user_name} check back soon! :)')
else:
    print('')



# random restaurants choises

# mode of transportaion choices

# entertainment random choices

# ability to (re)select random destinations, restaurants, mode of transportation, and/or entertainment

# ability to confirm trip completion

# sum all functions into one final conclusion (each function should do just one thing!)
