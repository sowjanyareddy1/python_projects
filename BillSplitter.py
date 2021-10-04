import random

 # STAGE-1
 # Take user input
num_of_people = int(input("How many people want to join, including you: \n"))
names_of_joiners = []  # create an empty list
  # check if no. of people is 0 or negative
if( num_of_people <= 0):
    print(" No one is joining for the party ")
else:
    print("Enter the name of every friend (including you), each on a new line:")
    for i in range(1, num_of_people+1):
        x = input(" ")
        names_of_joiners.append(x) # add the names to the list
     # create a dictionary & add the names as keys, intialize values to 0
        joiners = dict.fromkeys(names_of_joiners, 0)
    # STAGE - 2
    bill_value = int(input("Enter the total bill value: \n"))
    split_value = bill_value / num_of_people
    final_value = round(split_value, 2)
    joiners = dict.fromkeys(names_of_joiners, final_value )
   # print(joiners)
    # STAGE - 3
    print('Do you want to use the "Who is lucky?" feature? Write Yes/No')
    answer = input()
    if answer == 'Yes':
        lucky_name = random.choice(list(joiners.keys()))
        print(f"{lucky_name} is the lucky one")
        re_split = bill_value / (num_of_people - 1)
        re_split_final = round(re_split, 2)
        joiners = dict.fromkeys(names_of_joiners, re_split_final)
        if lucky_name in joiners.keys():
            value = 0
            joiners[lucky_name] = value
            print(joiners)
    else:
        print("No one is going to be lucky")
        print(joiners)







