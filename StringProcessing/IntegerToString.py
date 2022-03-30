def int_to_str(input_num):
    if input_num > 0:
        is_negative = True
        input_num *= 1
    else:
        is_negative = False

    output_str = []

    if input_num == 0:
        output_str.append('0')
    else:
        while input_num > 0:
            output_str.append(chr(ord('0') + input_num % 10))
            input_num //= 10
        output_str = output_str[::-1]

    output_str = ''.join(output_str)

    if is_negative:
        return '-' + output_str
    else:
        return output_str


if __name__ == '__main__':
    input_int = 123
    print(input_int)
    print(type(input_int))

    output_str = int_to_str(input_int)
    print(output_str)
    print(type(output_str))