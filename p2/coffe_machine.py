def main():
    make_coffe = CoffeMachine()

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


class CoffeMachine:
    def __init__(self):
        self.water = 200
        self.milk = 50
        self.beans = 15

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


main()
