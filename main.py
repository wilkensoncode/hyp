import math
from argparse import ArgumentParser, Namespace

parser = ArgumentParser(description="loan payments calculator")


def main():
    parser.add_argument("--type", help="type can be annuity or diff for differential")
    parser.add_argument("--principal", type=float)
    parser.add_argument("--periods", type=int)
    parser.add_argument("--interest", type=float, help="can be integer or decimal")
    parser.add_argument("--payment", type=float)

    args: Namespace = parser.parse_args()
    # and args.principal and args.periods and args.interest

    if args.type == "diff" and args.principal is not None and \
            args.interest is not None and args.periods is not None:
        diff_calculate(args.principal, args.periods, args.interest)
    elif args.principal is not None and args.periods is not None \
            and args.interest is not None and args.type == "annuity":
        annuity_payment, overpay = annuity_calculate(args.principal, args.periods, args.interest)
        print(f"Your annuity payment = {annuity_payment}!")
        print(f"Overpayment = {overpay}")
    elif args.payment is not None and args.interest is not None \
            and args.periods is not None and args.type == "annuity":
        principal, overpay = principal_calculate(args.payment, args.interest, args.periods)
        print(f"Your loan principal = {principal}!")
        print(f"Overpayment = {overpay}")
    elif args.principal is not None and args.payment is not None \
            and args.interest is not None:
        length = payment_length_calculate(args.principal, args.payment, args.interest)
        print(length)

    else:
        print("Incorrect parameters")


# ans = option()
# if ans == 'a':
#     res = calculate(ans)
#     print(res)
# if ans == 'p':
#     res = calculate(ans)
#     print(res)
# if ans == 'n':
#     res = calculate(ans)
#     print(res)


def option():
    choice = 'What do you want to calculate?' \
             '\ntype "n" - for number of monthly payments,' \
             '\ntype "a" for annuity monthly payment amount,' \
             '\ntype "p" for loan principal:'
    print(choice)
    return input()


def diff_calculate(principal, period, interest):
    differentiate = Payment()
    total = 0
    for month_current in range(1, int(period) + 1):
        diff_payments = differentiate.differentiate_payments(principal, period, interest,
                                                             month_current)
        print(f"Month {month_current}: payment is {diff_payments}")
        total += diff_payments
    overpay = abs(int(principal) - total)
    if overpay != 0:
        print(f"\nOverpayment = {overpay}")


def annuity_calculate(principal, period, interest):
    payment = Payment()
    args: Namespace = parser.parse_args()
    if args.type == "annuity":
        annuity_pay = payment.annuity_payments(int(principal), int(period), int(interest))
        pay = math.ceil(annuity_pay)  # annuity payment
        overpay = int(period) * pay - int(principal)
        return pay, overpay


def principal_calculate(annuity, interest, month):
    payment = Payment()
    principal, overpay = payment.principle_loan(annuity, interest, month)
    return principal, overpay


def payment_length_calculate(principal, payment, interest):
    length = Payment()
    month = length.payment_length(principal, payment, interest)
    m = math.ceil(month)
    overpay = math.ceil(overpay_calculate(m, payment, principal))
    if m % 12 == 0:
        return f"It will take {m // 12} years to repay this loan!" \
               f"\nOverpayment = {overpay}"
    else:
        return f'It will take {m // 12} years and {m % 12} months to repay this loan!' \
               f"\nOverpayment = {overpay}"


def overpay_calculate(m, payment, principal):
    overpay = int(m) * payment - principal
    return overpay


def calculate(chose):
    annuity = Annuity()

    if chose == "p":
        annuity_pays = float(input("Enter the annuity payment:"))
        num_periods = periods()
        interest = interest_rate()
        principal = annuity.calculate_principal(annuity_pays, interest, num_periods)
        return f"Your loan principal = {math.floor(principal)}!"

    if chose == "a":
        principal = principal_amt()
        months = periods()
        interest = interest_rate()
        monthly_payment = annuity.annuity_payment(interest, months, principal)
        return f"Your monthly payment = {math.ceil(monthly_payment)}"

    if chose == "n":
        principal = principal_amt()
        payment = int(input("Enter the monthly payment:"))
        interest = interest_rate()
        monthly_payment = annuity.num_payments(principal, payment, interest)
        month = math.ceil(monthly_payment)
        if month % 12 == 0:
            return f'It will take {month // 12} years months to repay this loan!'
        else:
            return f'It will take {month // 12} years and {month % 12} months to repay this loan!'


# helper methods
def periods():
    months = int(input("Enter the number of periods:"))
    return months


def interest_rate():
    interest = float(input("Enter the loan interest:"))
    return interest


def principal_amt():
    principal = float(input("Enter the loan principal:"))
    return principal


class Annuity:
    def __init__(self):
        self.interest = 0.0

    def annuity_payment(self, interest, month, principal):
        self.interest_calc(interest)
        annuity = principal * (
                (self.interest * ((1 + self.interest) ** month)) / ((1 + self.interest) ** month - 1))
        return annuity  # monthly payment

    def interest_calc(self, interest):  # helper method
        self.interest = (float(interest) / 100) / (12 * (100 / 100))
        return self.interest

    def calculate_principal(self, annuity, interest, month):
        self.interest_calc(interest)
        principal = annuity / (
                (self.interest * (1 + self.interest) ** month) / (
                (1 + self.interest) ** month - 1))
        return principal

    def num_payments(self, principal, annuity, interest):
        self.interest_calc(interest)
        num_payment = annuity / (annuity - (self.interest * principal))
        num_month = math.log(num_payment, 1 + self.interest)
        return num_month


class Payment(Annuity):
    def __init__(self):
        self.interest = 0
        super().__init__()

    def differentiate_payments(self, principal, month, interest, current_month=0):  # monthly payments each month
        principal = int(principal)
        month = int(month)
        self.interest = self.interest_calc(interest)
        dm = (principal / month) + (self.interest * (principal - (principal * (current_month - 1) / month)))
        return math.ceil(dm)  # mth differentiated payment

    def annuity_payments(self, principal, period, interest, total=0):  # monthly payment
        annuity_pay = self.annuity_payment(interest, period, principal)
        return annuity_pay

    def principle_loan(self, payment, interest, month):
        principal = self.calculate_principal(payment, interest, month)
        p = math.floor(principal)
        return p, month * payment - p  # principal and overpay amount

    def payment_length(self, principal, payment, interest):
        num_pay = self.num_payments(principal, payment, interest)  # number od months or payments
        return num_pay


if __name__ == '__main__':
    main()
