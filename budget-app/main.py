class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []
    
    def deposit(self, amount, description = ''):
        self.ledger.append({'amount': amount, 'description': description})

    def withdraw(self, amount, description = ''):
        balance = sum(item['amount'] for item in self.ledger)
        if self.check_funds(amount) : 
            self.ledger.append({'amount': -amount, 'description': description})
            return True
        return False
    
    def get_balance(self):
        return sum(item['amount'] for item in self.ledger)
    
    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, f'Transfer to {category.name}')
            category.deposit(amount, f'Transfer from {self.name}')
            return True
        return False

    def check_funds(self, amount):
        return amount <= self.get_balance () 
        

    def __str__(self):
        title = self.name.center(30, '*')
        output = title + '\n'

        for item in self.ledger:
            output += f"{item['description'][:23]:<23}{item['amount']:>7.2f}\n"

        output += f"Total: {self.get_balance():.2f}"

        return output

food = Category('Food')
food.deposit(1000, 'initial deposit')
food.withdraw(10.15, 'groceries')
food.withdraw(15.89, 'restaurant and more food for dessert')
clothing = Category('Clothing')
food.transfer(50, clothing)

print(food)





def create_spend_chart(categories):
    total_spent = 0
    categories_spending = []
    output = "Percentage spent by category\n"

    # Calculate spending for each category
    for category in categories:
        spent = 0

        for item in category.ledger:
            if item['amount'] < 0:
                spent += abs(item['amount'])

        categories_spending.append(spent)
        total_spent += spent

    # Calculate percentages
    percentages = []

    for spent in categories_spending:
        if total_spent > 0:
            percentage = int((spent / total_spent * 100) // 10) * 10
        else:
            percentage = 0

        percentages.append(percentage)

    # Display percentage chart
    for level in range(100, -1, -10):
        output += f'{level:>3}| '

        for percentage in percentages:
            if percentage >= level:
                output += 'o  '
            else:
                output += '   '

        output += '\n'

    # Display horizontal line
    output += '    ' + '-' * (len(categories) * 3 + 1) + '\n'

    # Display category names vertically
    max_length = max(len(category.name) for category in categories)

    for i in range(max_length):
        output += '     '

        for category in categories:
            if i < len(category.name):
                output += category.name[i] + '  '
            else:
                output += '   '

        if i < max_length - 1:
            output += '\n'

    return output


print(create_spend_chart([food, clothing]))