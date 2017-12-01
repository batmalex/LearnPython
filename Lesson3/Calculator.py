def words_to_numbers(expression):
    dictionary_interpreter = {"один": '1',
                             "два": '2',
                             "три": '3',
                             "четыре": '4',
                             "пять": '5',
                             "шесть": '6',
                             "семь": '7',
                             "восемь": '8',
                             "девять": '9',
                             "десять": '10',
                             "ноль": '0',
                             "и": '.',
                             "плюс": '+',
                             "минус": '-',
                             "умножить": '*',
                             "поделить": '/',
                             "равно": "="}
    num_expression = ''
    expression = expression.replace('умножить на', 'умножить')
    expression = expression.replace('поделить на', 'поделить')
    expression = expression.split()
    # print(expression)
    for word in expression:
        num_expression += dictionary_interpreter.get(word, '')
    # print(num_expression)
    return num_expression


def calculate(expression):
    arithmetic_operators_list = '*/+-='
    expression = expression.replace(' ', '')
    operator_symbol = None

    if expression[0] in '+-':
        expression = '0' + expression

    try:
        for position, symbol in enumerate(expression):
            if symbol in arithmetic_operators_list:
                if not operator_symbol:
                    operator_symbol = symbol
                    operator_position = position
                    result = float(expression[:operator_position])
                else:
                    second_part_expression = float(expression[operator_position + 1: position])
                    if operator_symbol == '+':
                        result += second_part_expression
                    elif operator_symbol == '-':
                        result -= second_part_expression
                    elif operator_symbol == '*':
                        result *= second_part_expression
                    elif operator_symbol == '/':
                        result /= second_part_expression
                    operator_position = position
                    operator_symbol = symbol
        print(result)
    except ZeroDivisionError:
        print("деление на 0!")


expr = "минус три плюс два и два минус   четыре поделить на ноль и пять равно "
words_to_numbers(expr)

# expr = '+ 6.7 + 7 + 4 * 2 / 500 = '
calculate(words_to_numbers(expr))