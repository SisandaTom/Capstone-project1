import math
#dispalying the instructions to the user 
#Displaying instructions for User to choose investment or bond 
print("Choose either 'investment' or 'bond' from the menu below to proceed: ")
print('''\ninvestment - to calculate the amount of interest you'll earn on your
      investment''')
print("bond - to calculate the the amount you'll have to pay on a home loan ")

#Asking the user for selection and storing in variable choice if they choose investment or bond
choice = input("Choose either 'investment' or 'bond': ")
final_choice = choice.lower()

#conditional statement to calculate the total amounyt if user chose investement
if final_choice == "investment":
    amount = float(input("\nPlease enter the amount of money you are depositing: "))
    interest_rate = float(input('''Please enter the interest rate,note that only
    the number should be entered, ignore the % ''')
    years = float(input("Enter the number of years you are investing for "))#variable years to store the number of years they are investing for
    interest = input("Enter the type of interest, between 'compound' and 'simple'interest: ") 

    #conditional statement for the user to choosesimple or compound
    if interest.lower() == "simple":
        Total_amount = amount*(1+(interest_rate / 100*years))
        print(f"The total amount is: {Total_amount} ")
            
    elif interest.lower() == "compound":
        Total_amount =  amount* math.pow(1+(interest_rate / 100)),years)
        print(f"The total amount is: {Total_amount} ")
        
#conditional statemt to calculate total amount if the user chose bond
elif final_choice == "bond":
    value = float(input("Enter the present value of the house: "))
    interest_rate2 = float(input("Enter the interest rate: "))
    i = interest_rate2/12
    period = float(input("The number of months to repay the bond: "))
    repayment = (i*value)/(1 - (1+i)**(-period))
    print(f"The monthly bond payment will be: {repayment} ")
    
#displaying a message if the user made an icorrect selection
else:
    print("invalid choice")

    

