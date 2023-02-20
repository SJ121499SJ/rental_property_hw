class Rental_property_calculator:
    def __init__(self, investment_name):
        self.investment_name = investment_name
        self.income = {}
        self.expenses = {}
        self.investment_cost = {}

        
    def income_function(self):
        while True:
            income_type = str(input("What type of income is it? "))
            income_amount = int(input("How much is the monthly income? (Type '00' if done) "))
            if income_amount == 00:
                print(self.income)
                break
            elif income_type not in self.income:
                self.income[income_type] = income_amount
            elif income_type in self.income:
                print(f"{income_type} already entered!")
    
    def expenses_function(self):
        while True:
            expense_type = str(input("What type of expense is it? "))
            expense_amount = int(input("How much is the expense? (Type '00' if done) "))
            if expense_amount == 00:
                print(self.expenses)
                break
            elif expense_type not in self.expenses:
                self.expenses[expense_type] = expense_amount
            elif expense_type in self.income:
                print(f"{expense_type} already entered!")
    
    def cash_flow_function(self):
        total_annual_cashflow = 12* ((sum(self.income.values()) - sum(self.expenses.values())))
        print ("Your total annual cashflow is " + str(total_annual_cashflow) + " dollars")
    
    def roi_function(self):
        while True:
            cost_type = str(input("What type of investment cost was it? "))
            cost_amount = int(input("How much is the cost? (Type '00' if done) "))
            if cost_amount == 00:
                print(self.investment_cost)
                break
            elif cost_type not in self.investment_cost:
                self.investment_cost[cost_type] = cost_amount
            elif cost_type in self.investment_cost:
                print(f"{cost_type} already entered!")
        total_investment_cost = sum(self.investment_cost.values())
        total_annual_cashflow = 12* ((sum(self.income.values()) - sum(self.expenses.values())))
        roi = (total_annual_cashflow / total_investment_cost) * 100
        print("Your total return on investment is " + str(roi) + " percent!" )

    def runner(self):
        while True:
            print("Choose an option below")
            user_choice = str(input("(a) Enter Income, (b) Enter Expenses, (c) See Cashflow, (d) Check ROI "))
            if user_choice.lower() == 'a':
                test.income_function()
            elif user_choice.lower() == 'b':
                test.expenses_function()
            elif user_choice.lower() == 'c':
                test.cash_flow_function()
            elif user_choice.lower() == 'd':
                test.roi_function()
                break
            else:
                print("Please choose from the given options")
            

    



test = Rental_property_calculator('house')
test.runner()

            
#OUTPUT SHOULD BE
#total income = 200
# total expense = 100
# total cashflow = 1200
# total investment = 12000
#roi = 10%
            






