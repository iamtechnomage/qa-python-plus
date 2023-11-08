def calc(operation, first_int, second_int):
    if operation == "sum":
        return first_int + second_int
    elif operation == "subt":
        return first_int - second_int
    elif operation == "mult":
        return first_int * second_int
    elif operation == "div":
        return first_int / second_int
    else:
        raise Exception("Wrong operation")
