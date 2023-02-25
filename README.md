# Capstone-project1
Create a new Python file in this folder called finance_calculators.py.
At the top of the file include the line import math
Write the code that will do the following:
The user should be allowed to choose which calculation they want
to do. The first output that the user sees when the program runs
should look like this : Choose either investment or bond
investment- To calculate the amount of interest you'll earn on interest
bond- To calculate the amount you'll have to pay on a home loan
If the user selects ‘investment’, do the following:
Ask the user to input:
The amount of money that they are depositing.
The interest rate (as a percentage). Only the number
of the interest rate should be entered — don’t worry
about having to deal with the added ‘%’, e.g. The user
should enter 8 and not 8%.
The number of years they plan on investing for.
Then ask the user to input whether they want “simple”
or “compound” interest, and store this in a variable
called interest. Depending on whether they typed
“simple” or “compound”, output the appropriate
amount that they will get after the given period at the
interest rate. Look below in “Interest formulae” for the
formulae to be used.
Print out the answer!
Try enter 20 years and 8 (%) and see what the difference is
depending on the type of interest rate!
If the user selects ‘bond’, do the following:
Ask the user to input:
The present value of the house. E.g. 100000
The interest rate. E.g. 7
The number of months they plan to take to repay the
bond. E.g. 120
Bond repayment formula:
The amount that a person will have to be repaid on a home loan each
month is calculated as follows: repayment = x = (i.P)/(1 - (1+i)^(-n))
In the formulae above:
‘P’ is the present value of the house.
‘i’ is the monthly interest rate, calculated 
