# Netflix MONTHLY & ANNUAL FEE GENERATOR +TAX
# 9/26/2021
# CTI-110 P1HW2 - Basic Math
# Anthony English
#

charge = 17.99
tax = charge * .06
monthly = charge + tax
annual = monthly * 12
name = ('Netflix')

print('Enter name of Expense:', end=' ')
name = input()
print('Enter monthly charge:', end=' ')
monthly = input()
print()

print('Bill: Netflix', end=' ')
print('---------', end=' ')
print('Before Tax: $17.99 ')
print('Monthly Tax:            $1.08 ')
print('Monthly Charge:         $19.07 ')
print('Annual Netflix Charge:  $228.84 ')
print()
