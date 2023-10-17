def main():
    food = Category("Food")
    food.deposit(1000, "initial deposit")
    food.withdraw(10.15, "groceries")
    food.withdraw(15.89, "restaurant and more food for dessert")
    print(food.get_balance())
    clothing = Category("Clothing")
    food.transfer(50, clothing)
    clothing.withdraw(25.55)
    clothing.withdraw(100)
    auto = Category("Auto")
    auto.deposit(1000, "initial deposit")
    auto.withdraw(15)

    print(food)
    print(clothing)
    
    print(create_spend_chart([food, clothing, auto]))

class Category:
    def __init__ (self, name):
        self.ledger = []
        self.name = name

    def __str__(self):
        name_width = 30
        description_width = 23
        amount_width = 7
        result = f"{self.name.center(name_width, '*')}\n"
        for item in self.ledger:
            result += (item["description"][:description_width].ljust(description_width) + "{:.2f}".format(item["amount"]).rjust(amount_width, ' ') + "\n")
        result += "Total: " + str(self.get_balance())
        return result

    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        return False

    def get_balance(self):
        balance = 0
        for item in self.ledger:
            balance += item["amount"]
        return balance

    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {category.name}")
            category.deposit(amount, f"Transfer from {self.name}")
            return True
        return False

    def check_funds(self, amount):
        if self.get_balance() >= amount:
            return True
        return False


def create_spend_chart(categories):
    spent_amounts = []

    for category in categories:
        spent = 0
        for item in category.ledger:
            if item["amount"] < 0:
                spent += abs(item["amount"])
        spent_amounts.append(round(spent, 2))

    total = round(sum(spent_amounts), 2)
    spent_percentage = list(map(lambda amount: int((((amount / total) * 10) // 1) * 10), spent_amounts))

    header = "Percentage spent by category\n"

    chart = ""
    for value in reversed(range(0, 101, 10)):
        chart += str(value).rjust(3) + '|'
        for percent in spent_percentage:
            if percent >= value:
                chart += " o "
            else:
                chart += "   "
        chart += " \n"
    
    chart += "    " + "-" * (len(categories) * 3 + 1) + "\n"
    chart += "     "
    for category in categories:
        chart += category.name[0].upper() + "  "
    chart += "\n"

    max_len = max(len(category.name) for category in categories)

    for i in range(1, max_len):
        chart += "     "
        for category in categories:
            if i < len(category.name):
                chart += category.name[i].lower() + "  "
        else:
            chart += "   "
        chart += "\n"

    return (header + chart).rstrip("\n")


if __name__ == "__main__":
    main()