
def monthly_payments(loan_amount, deposit, interest_rate, loan_lenght):

    # Validate loan lenght
    if loan_lenght <= 0:
        raise ValueError("Please enter a positive number.")
    
    # Validate deposit amount
    if deposit > loan_amount:
        raise ValueError("Deposit cannot be greater than the loan amount.")
        
    # Calculate loan amount based on deposit 
    loan_amount -= deposit

    # Calculate monthly interest rate
    monthly_interest_rate = (interest_rate/12)/100 

    # Calculate total number of payments 
    total_payments = loan_lenght *12

    # Calculate monthly mortgage payments 
    monthly_payment = loan_amount * (monthly_interest_rate *(1+monthly_interest_rate)**total_payments) / ((1 + monthly_interest_rate)**total_payments -1)
    return monthly_payment 

def monthly_savings(deposit_amount, months_saving):
    # Divide deposit amount by number of months
    saving_amount = deposit_amount / months_saving
    return saving_amount

def get_numeric(prompt, number_type=float):
    # Ensure numeric input from user
    while True:
        try:
            user_input = number_type(input(prompt))
            return user_input
        except ValueError:
            print("Please enter a valid number")

# Menu options
print("Welcome! Thinking about buying your first house? We're here to assist you!\n")

while True: 
    menu_choice = input("Please choose from the following options:\n 1 - Mortgage calculator\n 2 - Saving for a deposit\n 3 - Exit\n")

    if menu_choice == "1":
        # Asking for user input 
        loan_amount = get_numeric(" To calculate your monthly mortgage payments, please enter the total value of the property: ")
        deposit = get_numeric("Enter the deposit: ")
        interest_rate = get_numeric("Enter the interest rate: ")
        loan_length = get_numeric("Enter the lenght of the mortgage in years: ")

        # Calculate and print monthly mortgage payments 
        monthly_payment = monthly_payments(loan_amount, deposit, interest_rate, loan_length)
        print(f"Your monthly mortgage payments would be: £{monthly_payment:.2f}")
        print("\nBack to the main menu. \n")
    elif menu_choice == "2":
        # Asking for user input
        deposit_amount = get_numeric("To calculate how much you need to save every month, please enter the total deposit: ")
        months_saving = get_numeric("Enter how many months you wish to save for your deposit: ")

        #Calculate monthly saving based on deposit amount
        saving_amount = monthly_savings (deposit_amount, months_saving)
        print(f"You will need to save £{saving_amount} every month to reach your goal.")
        print("\nBack to the main menu. \n")

    elif menu_choice == "3":
        print("Goodbye!")
        break 
    else: 
        print("Please enter a valid option.\n") 


