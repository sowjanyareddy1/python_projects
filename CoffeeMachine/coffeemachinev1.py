min_water = 400 # in ml
min_milk = 540 # in ml
min_beans = 120 # in gm
disposable_cups = 9
money = 550

print(f''' The coffee machine has:
{min_water} of water
{min_milk} of milk
{min_beans} of coffee beans
{disposable_cups} of disposable cups
{money} of money ''')
def coffee_machine():
    global min_beans, min_water, min_milk,disposable_cups,money
    while(True):
        print("Write action (buy, fill, take, remaining, exit): ")
        choice1 = input()
        if choice1 == "buy":
            print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, 4 - back:")
            choice2 = int(input())
            if min_water < 200:
                print("Sorry, not enough water!")
            elif min_milk < 100:
                print("Sorry, not enough milk!")
            elif min_beans < 12:
                print("Sorry, not enough beans!")
            else:
                print("I have enough resources, making you a coffee!")
                buy(choice2)

        elif choice1 == "fill":
            water = int(input("Write how many ml of water you want to add:\n"))
            milk = int(input("Write how many ml of milk you want to add:\n"))
            beans = int(input("Write how many g of beans you want to add:\n"))
            cups = int(input("Write how many disposable coffee cups you want to add:\n"))
            fill(water,milk,beans,cups)

        elif choice1 == "take":
            amount = money
            take(amount)

        elif choice1 == "remaining":
            values()
        elif choice1 == "exit":
            break

def values():
    print(f''' The coffee machine has:
    {min_water} of water
    {min_milk} of milk
    {min_beans} of coffee beans
    {disposable_cups} of disposable cups
    {money} of money \n''')

def buy(choice2):
    global min_beans,min_water,min_milk,disposable_cups,money
    if choice2 == 1:
        min_water = min_water - 250
        min_beans = min_beans - 16
        disposable_cups = disposable_cups - 1
        money += 4
    elif choice2 == 2:
        min_water = min_water - 350
        min_beans = min_beans - 20
        min_milk = min_milk - 75
        disposable_cups = disposable_cups - 1
        money += 7
    elif choice2 == 3:
        min_water = min_water - 200
        min_beans = min_beans - 12
        min_milk = min_milk - 100
        disposable_cups = disposable_cups - 1
        money += 6
    elif choice2 == 4:
        print("Write action (buy, fill, take, remaining, exit): ")

def fill(water, milk, beans, cups):
    global min_beans, min_water, min_milk, disposable_cups
    min_milk += milk
    min_water += water
    min_beans += beans
    disposable_cups += cups

def take(amount):
    print(f"I gave you $ {amount}")
    global money
    money = money - amount
coffee_machine()


