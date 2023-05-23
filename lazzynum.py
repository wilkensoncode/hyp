memory = 0


class Messages:
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
        return Messages.msg_1


def is_oper(operator):
    oper = ['+', '-', '*', '/']
    if operator in oper:
        return True
    else:
        print(Messages.msg_2)


while True:
    try:
        print(Messages.msg_0)
        x, oper, y = input().split()
        if x.isalpha():
            x = memory
        if y.isalpha():
            y = memory
        if is_oper(oper) and not_number(x, y):
            result = calc(float(x), oper, float(y))
            print(result)
        is_yes = input(Messages.msg_4).lower()
        if is_yes == 'y':
            memory = result
        else:
            pass
        is_continue = input(Messages.msg_5).lower()
        if is_continue == 'y':
            pass
        else:
            break
    except ZeroDivisionError:
        print(Messages.msg_3)
    except ValueError:
        print(Messages.msg_1)
