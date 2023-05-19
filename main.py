import math


def main():
    # set_loan()
    url = UrlFormat()
    # print(url.get_url(input(), input()))



def set_loan():
    principle = Calculator(int(input("Enter the principle: ")))

    choice = 'What do you want to calculate?' \
             '\ntype "m" - for number of monthly payments,' \
             '\n"p" - for the monthly payment:'
    print(choice)

    ans = input()
    if ans == "m":
        monthly_payment = int(input("Enter the monthly payment:"))
        num_month = principle.num_month_repay(monthly_payment)

        print(f"It will take {num_month} months to repay the loan") \
            if num_month > 1 else print(f"It will take {num_month} month to repay the loan")

    if ans == "p":
        num_of_month = int(input("Enter the number of months:"))
        payment, last_payment = principle.month_payment(num_of_month)

        print(f"Your monthly payment = {payment} and the last payment = {last_payment}") \
            if payment != last_payment else print(f"Your monthly payment = {payment}")


class Calculator:
    loan_stats = {}

    def __init__(self, principle):
        self.principle = principle
        self.monthly_payment = 0
        self.month_repay = 0

    def set_principle(self):
        self.loan_stats["Loan principal"] = self.principle

    def set_monthly_payment(self, month_number: str, payment: int):
        self.monthly_payment = payment
        self.loan_stats[month_number] = payment

    def num_month_repay(self, monthly_payment):
        self.month_repay = math.ceil(self.principle / monthly_payment)
        return self.month_repay

    def month_payment(self, month):
        monthly_pay = math.ceil(self.principle / month)
        last_pay = self.principle - (month - 1) * math.ceil(monthly_pay)
        return monthly_pay, last_pay

    def get_stats(self):
        set_loan()
        return self.loan_stats


class UrlFormat:
    def __init__(self):
        self.url = "http://example.com/{}/desirable/{}/profile"
        self.nickname = ""
        self.profession = ""

    def get_url(self, nickname: str, profession: str):
        self.nickname = nickname
        self.profession = profession
        return self.url.format(self.nickname, self.profession)




if __name__ == '__main__':
    main()
