def main():
    make_coffe = CoffeMachine()
    """
    # print ingredient needed for x cup of coffe

    num_cup_coffe = int(input("Write how many cups of coffee you will need:\n "))
    print(f"for {num_cup_coffe} cups of coffee you will need:")

    amount_water, amount_milk, amount_beans = make_coffe.ingredient(num_cup_coffe)

    print(f"{amount_water} ml of water")
    print(f"{amount_milk} ml of milk")
    print(f"{amount_beans} g of coffee beans")

    #  Inventory determine if machine can make needed coffe

    water = int(input("Write how many ml of water the coffee machine has:\n"))
    milk = int(input("Write how many ml of milk the coffee machine has:\n"))
    beans = int(input("Write how many grams of coffee beans the coffee machine has:\n"))
    cups = int(input("Write how many cups of coffee you will need:\n"))
    answer = make_coffe.inventory(water, milk, beans, cups)
    print(answer)
    
    """

    # buy fill take tasks to perform

    action = input("Write action (buy, fill, take, remaining, exit):\n")
    while action != "exit":
        if action == "buy":
            choice = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:\n")
            if choice.isdigit():
                print(make_coffe.perform_action(int(choice)))
        elif action == "fill":
            amt_water = int(input("Write how many ml of water you want to add:\n"))
            amt_milk = int(input("Write how many ml of milk you want to add:\n"))
            amt_beans = int(input("Write how many grams of coffee beans you want to add:\n"))
            amt_cups = int(input("Write how many disposable cups you want to add:\n"))
            make_coffe.fill(water=amt_water, cups=amt_cups, beans=amt_beans, milk=amt_milk)
        elif action == "remaining":
            print(make_coffe.machine_state())
        elif action == "take":
            withdraw = make_coffe.take()
            print(f"I gave you ${withdraw}")
        action = input("Write action (buy, fill, take,  remaining, exit):\n")


class CoffeMachine(object):
    def __init__(self):
        self.water = 200
        self.milk = 50
        self.beans = 15

        #  coffe current ingredient
        self.money_c = 550
        self.water_c = 400
        self.milk_c = 540
        self.beans_c = 120
        self.cups = 9

        self.msg = "I have enough resources, making you a coffee!"

    def machine_state(self):
        state = f"The coffee machine has:\n" \
                f"{self.water_c} ml of water\n" \
                f"{self.milk_c} ml of milk\n" \
                f"{self.beans_c} g of coffee beans\n" \
                f"{self.cups} disposable cups\n" \
                f"${self.money_c} of money"

        return state

    def ingredient(self, num_cups):  # ingredient needed to make 25 cups coffee
        water = self.water * num_cups
        milk = self.milk * num_cups
        beans = self.beans * num_cups
        return water, milk, beans

    def inventory(self, water, milk, beans, cup):  # can coffe be made

        w = water // self.water
        m = milk // self.milk
        b = beans // self.beans
        max_c = min(w, m, b)
        ms = f"No, I can make only {max_c} cups of coffee"
        if cup == max_c:
            ms = "Yes, I can make that amount of coffee"
        elif cup < max_c:
            ms = f"Yes, I can make that amount of coffee (and even {max_c - cup} more than that)"

        return ms

    # sell coffee
    def perform_action(self, action: int):
        if action == 1:
            return self.expresso()
        elif action == 2:
            return self.latte()
        elif action == 3:
            return self.cappuccino()

    def expresso(self, water=250, beans=16, cost=4):  # helper perform_action
        if self.water_c >= water and self.beans_c >= beans:
            self.update_ingredient(beans, cost, water)
            return self.msg
        return self.feedback(beans=beans, milk=None, water=water)

    def update_ingredient(self, beans, cost, water):  # helper
        if self.cups < 1:
            return "Sorry not enough cups"
        self.water_c -= water
        self.beans_c -= beans
        self.cups -= 1
        self.money_c += cost

    def latte(self, water=350, milk=75, beans=20, cost=7):  # helper perform_action
        if self.water_c >= water and self.milk_c >= milk and self.beans_c >= beans:
            self.milk_c -= milk
            self.update_ingredient(beans, cost, water)
            return self.msg
        return self.feedback(beans, milk, water)

    def feedback(self, beans, milk, water):  # helper
        if self.water_c < water:
            return "Sorry, not enough water!"
        elif self.milk < milk:
            return "Sorry, not enough milk"
        elif self.beans < beans:
            return "Sorry, not enough beans"

    def cappuccino(self, water=200, milk=100, beans=12, cost=6):  # helper perform_action
        if self.water_c >= water and self.milk_c >= milk and self.beans_c >= beans:
            self.milk_c -= milk
            self.update_ingredient(beans, cost, water)
            return self.msg
        return self.feedback(beans, milk, water)

    def fill(self, water, beans, milk, cups):
        self.milk_c += milk
        self.water_c += water
        self.beans_c += beans
        self.cups += cups

    def take(self):
        self.money_c -= self.money_c
        return self.money_c


main()
