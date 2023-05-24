memory = 0


def check(v1, v2, v3):
    msg_6 = " ... lazy"

    msg_7 = " ... very lazy"

    msg_8 = " ... very, very lazy"

    msg_9 = "You are"

    msg = ""
    if is_one_digit(v1) and is_one_digit(v2):
        msg = msg + msg_6
    if v1 == 1 or v2 == 1 and v3 == '*':
        msg = msg + msg_7
    if v1 == 0 or v2 == 0 and v3 == "-":
        msg = msg + msg_8
    if msg != "":
        msg = msg_9 + msg
    print(msg)


def is_one_digit(n):
    output = False
    if -10 < n < 10 and n.is_digit():
        output = True
    return output


class Calc:
    msg_0 = "Enter an equation"
    msg_1 = "Do you even know what numbers are? Stay focused!"
    msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
    msg_3 = "Yeah... division by zero. Smart move..."
    msg_4 = "Do you want to store the result? (y / n): \n"
    msg_5 = "Do you want to continue calculations? (y / n): \n"

    def calc(x, oper, y):
        if oper == '+':
            return x + y
        elif oper == '-':
            return x - y
        elif oper == '*':
            return x * y
        elif oper == '/':
            return x / y

    def not_number(x, y):
        if x.isalpha() and y.isalpha():
            return True
        else:
            return Calc.msg_1

    def is_oper(self, operator):
        oper = ['+', '-', '*', '/']
        if operator in oper:
            self.check(x, y, oper)
        else:
            print(Calc.msg_2)


while True:

    try:
        result = 0
        print(Calc.msg_0)
        x, oper, y = input().split()
        if x.isalpha():
            x = memory
        if y.isalpha():
            y = memory
        if Calc.is_oper(oper) and Calc.not_number(x, y):
            result = Calc.calc(float(x), oper, float(y))
            # check(x,y,oper)
        is_yes = input(Calc.msg_4).lower()
        if is_yes == 'y':
            memory = result
        else:
            pass
        is_continue = input(Calc.msg_5).lower()
        if is_continue == 'y':
            pass
        else:
            break
    except ZeroDivisionError:
        print(Calc.msg_3)
    except ValueError:
        print(Calc.msg_1)

check()
