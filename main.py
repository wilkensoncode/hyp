import math


def main():
    ans = option()

    if ans == 'a':
        res = calculate(ans)
        print(res)
    if ans == 'p':
        res = calculate(ans)
        print(res)
    if ans == 'n':
        res = calculate(ans)
        print(res)

 

def option():
 
    choice = 'What do you want to calculate?' \
             '\ntype "n" - for number of monthly payments,' \
             '\ntype "a" for annuity monthly payment amount,' \
             '\ntype "p" for loan principal:'
    print(choice)
    return input()


def calculate(chose):
    annuity = Annuity()

    if chose == "p":
        annuity_pays = float(input("Enter the annuity payment:"))
        num_periods = periods()
        interest = interest_rate()
        principle = annuity.calculate_principle(annuity_pays, interest, num_periods)
        return f"Your loan principal = {math.floor(principle)}!"

    if chose == "a":
        principle = principle_amt()
        months = periods()
        interest = interest_rate()
        monthly_payment = annuity.annuity_payment(interest, months, principle)
        return f"Your monthly payment = {math.ceil(monthly_payment)}"

    if chose == "n":
        principle = principle_amt()
        payment = int(input("Enter the monthly payment:"))
        interest = interest_rate()
        monthly_payment = annuity.num_payments(principle, payment, interest)
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


def principle_amt():
    principle = float(input("Enter the loan principal:"))
    return principle


class Annuity:
    def __init__(self):
        self.interest = 0

    def annuity_payment(self, interest, month, principle):
        self.interest_calc(interest)
        annuity = principle * (
                (self.interest * ((1 + self.interest) ** month)) / ((1 + self.interest) ** month - 1))
        return annuity  # monthly payment

    def interest_calc(self, interest):  # helper method
        self.interest = (interest / 100) / (12 * (100 / 100))

    def calculate_principle(self, annuity, interest, month):
        self.interest_calc(interest)
        principle = annuity / (
                (self.interest * (1 + self.interest) ** month) / (
                (1 + self.interest) ** month - 1))
        return principle

    def num_payments(self, principle, annuity, interest):
        self.interest_calc(interest)
        num_payment = annuity / (annuity - (self.interest * principle))
        num_month = math.log(num_payment, 1 + self.interest)
        return num_month


if __name__ == '__main__':
    main()
