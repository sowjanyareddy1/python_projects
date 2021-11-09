class CoffeeMachine:
    def __init__(self, water, milk, coffee, cup, cash):
        self.water = water
        self.milk = milk
        self.coffee = coffee
        self.cup = cup
        self.cash = cash

    def remaining(self):
        print('The coffee machine has:')
        print(f'{self.water} of water')
        print(f'{self.milk} of milk')
        print(f'{self.coffee} of coffee beans')
        print(f'{self.cup} of disposable cups')
        print(f'${self.cash} of money')

    def fill(self, water_add, milk_add, coffee_add, cup_add):
        self.water += water_add
        self.milk += milk_add
        self.coffee += coffee_add
        self.cup += cup_add

    def coffee_check(self, water_need, milk_need, coffee_need, cash_need):
        if water_need <= self.water and coffee_need <= self.coffee and milk_need <= self.milk:
            print('I have enough resources, making you a coffee!')
            self.water -= water_need
            self.milk -= milk_need
            self.coffee -= coffee_need
            self.cup -= 1
            self.cash += cash_need
        elif water_need > self.water:
            print('Sorry, not enough water!')
        elif coffee_need > self.coffee:
            print('Sorry, not enough coffee beans!')
        elif milk_need > self.milk:
            print('Sorry, not enough milk!')

    def take(self):
        self.cash -= self.cash
x = CoffeeMachine(400, 540, 120, 9, 550)
while True:
    act = input('Write action (buy, fill, take, remaining, exit):')
    if act == 'fill':
        water_add = int(input('Write how many ml of water you want to add:'))
        milk_add = int(input('Write how many ml of milk you want to add:'))
        coffee_add = int(input('Write how many grams of coffee beans you want to add:'))
        cup_add = int(input('Write how many disposable coffee cups you want to add:'))
        x.fill(water_add, milk_add, coffee_add, cup_add)
    elif act == 'buy':
        y = input('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:')
        if y == '1':
            x.coffee_check(250, 0, 16, 4)
        elif y == '2':
            x.coffee_check(350, 75, 20, 7)
        elif y == '3':
            x.coffee_check(200, 100, 12, 6)
        elif y == 'back':
            pass
    elif act == 'take':
        x.take()
    elif act == 'remaining':
        x.remaining()
    elif act == 'exit':
        break

