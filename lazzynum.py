MSG_0 = "Enter an equation"
MSG_1 = "Do you even know what numbers are? Stay focused!"
MSG_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
MSG_3 = "Yeah... division by zero. Smart move..."
MSG_4 = "Do you want to store the result? (y / n):\n"
MSG_5 = "Do you want to continue calculations? (y / n):\n"
MSG_6 = " ... lazy"
MSG_7 = " ... very lazy"
MSG_8 = " ... very, very lazy"
MSG_9 = "You are"
MSG_10 = "Are you sure? It is only one digit! (y / n) 10\n"
MSG_11 = "Don't be silly! It's just one number! Add to the memory? (y / n) 11\n"
MSG_12 = "Last chance! Do you really want to embarrass yourself? (y / n) 12\n"


def is_one_digit(v):
    if -10 < v < 10 and v == int(v):
        return True
    else:
        return False


def check(v1, v2, v3):
    msg = ""
    if is_one_digit(v1) and is_one_digit(v2):
        msg += MSG_6
    if v1 == 1 or v2 == 1:
        msg += MSG_7
    if (v1 == 0 or v2 == 0) and v3 != "/":
        msg += MSG_8
    if msg != '':
        msg = MSG_9 + msg
        print(msg)


operations = {
    "+": (lambda x_num, y_num: x_num + y),
    "-": (lambda x_num, y_num: x_num - y),
    "*": (lambda x_num, y_num: x_num * y),
    "/": (lambda xx_num, y_num: xx_num / y),
}

memory = 0.0

while True:
    print(MSG_0)
    x, oper, y = input().split()
    try:
        x = memory if x == "M" else float(x)
        y = memory if y == "M" else float(y)
        check(x, y, oper)
        result = operations[oper](x, y)
        print(result)
        if input(MSG_4) == "y":  # yes store result
            if memory < result:
                memory = result

            if is_one_digit(result):
                msg_index = 10
                if input(MSG_10) == 'y':
                    # memory = result
                    # print(memory)
                    if input(MSG_11) == 'y':
                        if msg_index < 12:
                            msg_index = msg_index + 1
                        else:
                            memory = result
                        if input(MSG_12) == 'y':
                            memory = result

                            # else:
            #  memory = result

        if input(MSG_5) == "n":
            break

    except ValueError:
        print(MSG_1)
    except KeyError:
        print(MSG_2)
    except ZeroDivisionError:
        print(MSG_3)
