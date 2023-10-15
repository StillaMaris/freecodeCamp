class Category:
    
    def __init__(self, description):
        self.description = description
        self.ledger = []
        self.balance = 0.0
     
    '''
    When the budget object is printed it should display:
    1) A title line of 30 characters where the name of the category is centered in a line of * characters.
    2) A list of the items in the ledger. Each line should show the description and amount. 
        The first 23 characters of the description should be displayed, then the amount. 
        The amount should be right aligned, contain two decimal places, and display a maximum of 
        7 characters.
    3) A line displaying the category total. 
    '''
    def __repr__(self):
        header = f"{self.description:*^30s}\n"
        ledger = ""
        for s in self.ledger:  #food.ledger = [{amount, description}]
            line_description = f"{s['description']:<23s}"
            line_amount = f"{s['amount']:>7.2f}"
            line = line_description[:23] + line_amount[:7]
            ledger += line + '\n'
        total = self.balance
        return header + ledger+f"Total: {total}"
            
            

    ''' 
    A deposit method that accepts an amount and description. If no description is given,
    it should default to an empty string. The method should append an object to the ledger 
    list in the form of {"amount": amount, "description": description}.
    '''    
    def deposit(self, amount, description = ""):
        self.balance += amount 
        self.ledger.append({"amount": amount, "description": description})
    
    '''
    A withdraw method that is similar to the deposit method, but the amount passed in should
    be stored in the ledger as a negative number. If there are not enough funds, nothing should 
    be added to the ledger. This method should return True if the withdrawal took place,
    and False otherwise.
    '''
    
    def withdraw(self, expenses, descr_expenses = ""):
        if self.check_funds(expenses):
            self.balance -= expenses
            self.ledger.append({"amount": - expenses, "description": descr_expenses})
            return True
        else:
            return False        
    '''
    A get_balance method that returns the current balance of the budget category based on the 
    deposits and withdrawals that have occurred.
    '''
    
    def get_balance(self):
        return round(self.balance, 2)
    
    '''
    A transfer method that accepts an amount and another budget category as arguments. 
    The method should add a withdrawal with the amount and the description "Transfer to 
    [Destination Budget Category]".
    The method should then add a deposit to the other budget category with the amount and the
    description "Transfer from [Source Budget Category]".
    If there are not enough funds, nothing should be added to either ledgers.
    This method should return True if the transfer took place, and False otherwise.
    '''
    def transfer(self, money_to_transfer, destination_budget):
        if self.check_funds(money_to_transfer):
           self.withdraw(money_to_transfer, "Transfer to " + str(destination_budget.description))
           destination_budget.deposit(money_to_transfer, "Transfer from {}".format(self.description))
           return True
        else:
           return False
       
    '''
    A check_funds method that accepts an amount as an argument. It returns False
    if the amount is greater than the balance of the budget category and returns True otherwise.
    This method should be used by both the withdraw method and transfer method.
    '''
       
    def check_funds(self, amount):
       if amount > self.balance:
           return False
       else:
           return True
           
           

def create_spend_chart(categories): #args è una lista di oggetti Category
    
    spent_amount = []
    # Let's calculate the total expense for each category
    for category in categories:
        spent = 0
        for item in category.ledger:
            if item['amount']< 0:
                spent += abs(item['amount'])
        spent_amount.append(round(spent,2))
        
    # Let's calculate the sum of the total_expenses
    total_spent = round(sum(spent_amount),2)
    
    # Let's calculate the percentage spent for each category
    # Total_spent : spent_amount[i] = 100 : percentage

    percentage_list = []
    for i in spent_amount:
        percentage = 100*i/total_spent 
        percentage_list.append(int(percentage//10 *10 ))  #arrotondo al decimo più vicino
    
    # Let's create the chart

    title = "Percentage spent by category\n"
    chart = ""
    
    for yticks in reversed(range(0, 101, 10)):  #creo la barra verticale dell'istogramma
        chart += f"{yticks:>3d}|"
        
        # devo aggiungere le colonne dell'istogramma
        for percentage in percentage_list:
            if percentage >= yticks:
                chart += " o "                
            else:
                chart += " "*3
        chart += " \n"
       
       
    # Preparo l'asse x 
    x_axes = " "*4 + "-"*(3 * len(categories) + 1)+"\n"
    
    # Preparo l'etichetta
    descriptions = [category.description for category in categories] #['Food', 'Clothing', 'Auto']
    max_len = max( len(ii) for ii in descriptions)
    
    # aggiungo tanti spazi quanti mancano affinchè le descrizioni abbiano la stessa lunghezza
    # e poi uso zip per creare una tuple in verticale 
    new_ticks = []
    for description in descriptions:
        if len(description) < max_len:
            description += ' '*(max_len-len(description))
            
        new_ticks.append(description)
    
    new_ticks = list(zip(*new_ticks)) 
    '''
    new_ticks sono della forma
    [
        (F, C, A),
        (o, l, u),
        (o, o, t),
        (d, t, o), 
        ( , h, ),
        ....
    ]
    '''
    
    x_ticks = ""
    for row in new_ticks:  # accedo ai dati dentro la tuple
        x_ticks += " "*4 
        for letter in row:  # accedo alle lettere dentro x 
            x_ticks += letter.center(3)
        x_ticks += ' \n'        

    # devo togliere l'ultimo '\n' a xticks:
    
    return (title+ chart + x_axes + x_ticks).rstrip('\n')
        