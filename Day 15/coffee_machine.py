from beverage import Beverage

class Machine():
    def __init__(self, water, milk, coffee):
        self.water = water
        self.milk = milk
        self.coffee = coffee
        self.money = 0

    def report(self):
        print(f"Water: {self.water}ml\nMilk: {self.milk}ml\nCoffee: {self.coffee}g\nMoney: ${self.money}")
        return
    
    def check_resources(self, beverage) -> bool:
        stock = [self.water,self.milk,self.coffee]
        items = ['water','milk','coffee']
        for i in range(len(beverage.ingredients)):
            if beverage.ingredients[i] >= stock[i]:
                print(f"Sorry, there is not enough {items[i]}. Smodge")
                return False
        return True
    
    def make_coffee(self, beverage):
        self.water -= beverage.ingredients[0]
        self.milk -= beverage.ingredients[1]
        self.coffee -= beverage.ingredients[2]
        print(f"Here is your {beverage.name}. Enjoy!!")
        return True
    
    def process_coins(self,price) -> bool:
        quarters = float(input("Please enter quarters: "))
        dimes = float(input("Please enter dimes: "))
        nickles = float(input("Please enter nickles: "))
        pennies = float(input("Please enter pennies: "))
        total = (quarters*0.25) + (dimes*0.10) + (nickles*0.05) + (pennies*0.01)
        if total < price:
            print(f"Sorry that's not enough money. You're ${round(price-total,2)} short!")
            return False
        change = total - price
        if change != 0:
            print(f"Here is your change: ${round(change,2)}")
        self.money += price
        return True
    
    def order_up(self, beverage):
        if self.check_resources(beverage) == True:
            if self.process_coins(beverage.price):
                self.make_coffee(beverage)
                return True
        return False

    def start(self):
        cont = True
        while cont:
            choice = str(input("What would you like? (espresso/latte/cappuccino): ")).lower()
            # if drink is chosen, make drink
            if choice in ["espresso","latte","cappuccino"]:
                if choice == "espresso":
                    drink = Beverage("espresso",1.5,[50,0,10])
                elif choice == "latte":
                    drink = Beverage('latte',2.5,[200,150,24])
                elif choice == "cappuccino":
                    drink = Beverage("cappuccino",3.0,[250,100,24])
                self.order_up(drink)
            elif choice == "report":
                self.report()
            elif choice == "off":
                cont = False
            else:
                print("Sorry, type either esperesso, latte, or cappachungus")
    