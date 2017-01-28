##Problem Set 1 Problem 2 Rev 3
##Gathering inputs and declaring initial variables
init_balance = float(raw_input('Enter the outstanding balance on your credit card: '))
balance = init_balance
interest_rate = float(raw_input('Enter the annual credit card interest rate as a decimal: '))
monthly_rate = interest_rate / 12.0
lower = init_balance / 12.0
upper = (balance * (1 + monthly_rate) ** 12.0) / 12.0
month = 1
payment = (lower + upper) / 2
margin = 0.01
last_balance = 0.00
##
while (abs(round(lower, 3) - round(upper, 3)) - margin) > 0 :
    for month in range(1, 13):
        balance = balance * (1 + interest_rate / 12.0)
        balance = balance - payment
    if balance - margin > 0:
        lower = payment
    else:
        upper = payment
    payment = (lower + upper) / 2
    last_balance = balance
    balance = init_balance    
##Displays values
print 'RESULT'
print 'Monthly payment to pay off debt in 1 year: ' + str(round(payment, 2))
print 'Number of months needed: ' + str(int(month))
print 'Balance: ' + (str(round(last_balance , 2)))
