import math

"""loan = int(input("Enter the loan principal: \n > "))
monthly_payment = int(input("Enter the monthly payment: \n >"))
print()
print(f"It will take {int(loan / monthly_payment)} months to repay the loan.")

calc = input('What do you want to calculate?\n'
             'type "m" - for number of monthly payments,\n'
            'type "p" - for the monthly payment: \n > ')

if calc == "m":
    monthly_payment = int(input("Enter the monthly payment: \n > "))
    if monthly_payment == 1000:
        print(f"It will take {math.ceil(loan / monthly_payment)} month to repay the loan.")
    else:
        print(f"It will take {math.ceil(loan / monthly_payment)} months to repay the loan.")
else:
    number_of_months = int(input("Enter the number of months: \n > "))
    if loan % number_of_months == 0:
        print(f"Your monthly payment = {int(loan / number_of_months)}")
    else:
        monthly_payment = math.ceil(loan - (number_of_months - 1) * (loan / number_of_months))
        print(f"Your monthly payment = {monthly_payment} and the last payment = {loan - (monthly_payment * (number_of_months - 1))}.")
              #and the last payment = {loan - (number_of_months - 1) * (monthly_payment)}")
        #print(f"Your monthly payment = {math.ceil(loan - (number_of_months - 1) * (loan / number_of_months))} and the last payment = {loan - ((number_of_months - 1) * math.ceil(loan - (number_of_months - 1) * (loan / number_of_months)))}.")
"""

"""import argparse
import math

parser = argparse.ArgumentParser(description = "Annuity payment")
parser.add_argument("--principal", type = int)
parser.add_argument("--payment", type = float)
parser.add_argument("--periods", type = int)
parser.add_argument("--interest", type = float)

args = parser.parse_args()

i = (args.interest / 100) / 12

if args.principal and args.payment and args.interest and not args.periods:
    n = math.log(args.payment / (args.payment - i * args.principal), 1+ i)
    n = math.ceil(n)

    years = n // 12
    months = n % 12

    if years > 0 and months > 0:
        print(f"It will take {years} years and {months} months to repay this loan.")
    elif years > 0 and months == 0:
        print(f"It will take {years} years to repay this loan.")
    else:
        print(f"It will take {months} months to repay this loan.")

elif args.principal and args.periods and args.interest and not args.payment:
    a = args.principal * (i * (1 + i) ** args.periods) / ((1 + i) ** args.periods -1)
    print(f"Your monthly payment = {math.ceil(a)}!")

elif args.payment and args.periods and args.interest and not args.principal:
    A = float(args.payment)
    n = int(args.periods)
    i = args.interest / 1200
    P = A / ((i * (1 + i) ** n) / ((1 + i) ** n - 1))
    print(f"Your loan principal = {P}!")"""

import argparse
import math

parser = argparse.ArgumentParser(description = "Annuity payment")
parser.add_argument("--principal", type = int)
parser.add_argument("--payment", type = float)
parser.add_argument("--periods", type = int)
parser.add_argument("--interest", type = float)
parser.add_argument("--type", type = str)

args = parser.parse_args()

nums = [args.principal, args.payment, args.periods, args.interest]

if args.type not in ["diff", "annuity"]:
    print("Incorrect parameters")
    exit()

if args.type == "diff" and args.payment is not None:
    print("Incorrect parameters")
    exit()

if args.interest is None:
    print("Incorrect parameters")
    exit()

if sum (arg is not None for arg in nums) != 3:
    print("Incorrect parameters")
    exit()

for a in nums:
    if a is not None and a < 0:
        print("Incorrect parameters")
        exit()

if args.type == "diff":
    i = (args.interest / 100) / 12

    month = args.periods

    total = 0

    for month in range (1, args.periods + 1):
        monthly_payment = math.ceil((args.principal / args.periods) + i * (args.principal - (args.principal * (month - 1) / args.periods)))
        print(f"Month {month}: payment is {monthly_payment}")
        total += monthly_payment
    print(f"Overpayment = {round(total, 0) - args.principal}")

if args.type == "annuity":
    i = (args.interest / 100) / 12

    month = args.periods

    if args.principal and args.periods and args.interest:
        a = args.principal * (i * (1 + i) ** args.periods) / ((1 + i) ** args.periods -1)
        monthly = math.ceil(a)
        print(f"Your annuity payment = {monthly}!")
        overpayment = monthly * args.periods - args.principal
        print(f"Overpayment = {overpayment}")


    elif args.principal and args.payment and args.interest:
        n = math.log(args.payment / (args.payment - i * args.principal), 1 + i)
        n = round(n)

        years = n // 12
        months = n % 12

        if years > 0 and months > 0:
            print(f"It will take {years} years and {months} months to repay this loan.")
        elif years > 0 and months == 0:
            print(f"It will take {years} years to repay this loan.")
        else:
            print(f"It will take {months} months to repay this loan.")

        overpayment = round((years * 12 * args.payment) - args.principal)
        print(f"Overpayment = {overpayment}")

    elif args.payment and args.periods and args.interest:
        A = float(args.payment)
        n = int(args.periods)
        i = args.interest / 1200
        P = A / ((i * (1 + i) ** n) / ((1 + i) ** n - 1))
        principal = math.floor(P)
        print(f"Your loan principal = {principal}!")
        overpayment = round((args.periods * args.payment) - principal)
        print(f"Overpayment = {overpayment}")