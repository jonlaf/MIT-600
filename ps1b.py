##Problem Set 1 Problem 2 Rev 3
##Gathering inputs and declaring initial variables
init_balance = float(raw_input('Enter the outstanding balance on your credit card: '))
balance = init_balance
interest_rate = float(raw_input('Enter the annual credit card interest rate as a decimal: '))
monthly_interest = interest_rate / 12.0
month = 0
payment = 10.0


while balance > 0:
    while balance > 0 & month <= 11:
        balance *= (1 + monthly_interest)
        balance -= payment
        if month >= 12:
            month = 1
            payment += 10.0
            balance = init_balance
        else:
            month += 1
            
##Displays values 
print 'RESULT'
print 'Monthly payment to pay off debt in 1 year: ' + str(payment)
print 'Number of months needed: ' + str(int(month))
print 'Balance: ' + (str(round(balance , 2)))

