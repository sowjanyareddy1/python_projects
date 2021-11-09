
 # print the following
print("""Starting to make a coffee
Grinding coffee beans
Boiling water
Mixing boiled water with crushed coffee beans
Pouring coffee into the cup
Pouring some milk into the cup
Coffee is ready!""")

min_water = 200 # in ml
min_milk = 50 # in ml
min_beans = 15 # in gm

water = int(input("Write how many ml of water the coffee machine has:\n"))
milk = int(input("Write how many ml of milk the coffee machine has:\n"))
beans = int(input("Write how many g of beans the coffee machine has:\n"))
cups = int(input("Write how many cups of coffee you will need:\n"))
max_water = int(water/min_water)
max_milk = int(milk/min_milk)
max_beans = int(beans/min_beans)

avail_cups = [max_water, max_milk, max_beans]
n = min(avail_cups) - cups
if min(avail_cups) == cups:
    print("Yes, I can make that amount of coffee")
elif min(avail_cups) > cups:
    print(f"Yes, I can make that amount of coffee (and even {n} more than that")
elif min(avail_cups) < cups:
    print(f"No, I can make only {min(avail_cups)} amount of coffee")


