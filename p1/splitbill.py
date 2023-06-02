import random


def main():
    bill_split = BillSplit()

    members = int(input("Enter the number of friends joining (including you):\n"))

    if members < 1:
        print("No one is joining for the party")
    else:
        #  init dict with friends name and value 0

        print("Enter the name of every friend (including you), each on a new line:\n")
        bill_split.party_members(members, 0)  # all friends joining the party

        #  get the bill and split among friends

        bill = int(input("Enter the total bill value:\n"))
        friend_bill = bill_split.bill_split(bill, members)

        # who is lucky? feature

        lucky = input('Do you want to use the "Who is lucky?" feature? Write Yes/No:\n')

        if lucky == "Yes":
            name, friend_d = bill_split.lucky_one(bill, members)
            print(f"{name} is the lucky one!")
            friend_bill = friend_d
        else:
            print("No one is going to be lucky")

        print(friend_bill)


class BillSplit:
    def __init__(self):
        self.friends = {}
        self.num_friends = 0
        self.bill = 0  # amount after
        self.name = ""

    def party_members(self, members: int, amount):  # nuber of people joining the party including the host
        self.num_friends = members
        while members > 0:
            self.name = input()
            self.friends[self.name] = amount
            members -= 1
        return self.friends  # initial friends dict

    def bill_split(self, bill_value: int, num_friends):
        bill = bill_value / num_friends
        decimal = bill - int(bill)
        self.bill = int(bill) if decimal == 0 else round(bill, 2)
        for name in self.friends.keys():
            self.friends[name] = self.bill
        return self.friends  # updated friend dict

    def lucky_one(self, bill, num_friend):  # choose one friends to have their bill pay by other friends

        self.name = random.choice(list(self.friends.keys()))
        f_num = num_friend - 1  # lucky friend does not pay nay bill
        self.bill_split(bill, f_num)
        self.friends.update({self.name: 0})
        return self.name, self.friends


main()
