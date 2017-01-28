##Jon La France
##Problem Set 1 Problem 1
##Gather my inputs and declare my variable types
principal = float(raw_input('Enter the outstanding balance on your credit card:'))
interest_rate = float(raw_input('Enter the annual credit card interest rate as a decimal:'))
minimum_payment_percent=float(raw_input('Enter the minimum monthly payment rate as a decimal:'))
minimum_payment = 0.0
interest_paid = 0.0
principal_paid = 0.0
total_paid = 0.0
month = 0
##The loop which counts the months, calculating the interest and principal payments and
##the effects of compounding on the principal itself. Returning values to the user as it goes.
for month in range(1, 13):
    print 'Month: ' + str(month)
    minimum_payment: = principal * minimum_payment_percent
    print 'Minimum monthly payment: $' + str(round(minimum_payment, 2))
    interest_paid = interest_rate / 12 * principal
    principal_paid = minimum_payment - interest_paid
    print 'Principal paid: $' + str(round(principal_paid, 2))
    total_paid = total_paid + interest_paid + principal_paid
    principal += principal_paid
    print 'Remaining balance: $' + str(round(principal, 2))

##total amount paid is tracked separately from the loop and built on each iteration.
print 'RESULT'
print 'Total amount paid: $' + str(round(total_paid, 2))
print 'Remaining balance: $' + str(round(principal, 2))
