def integer_square_root(k):
    n = int(k)
    i = result = 1
    while result <= n:
        i += 1
        result = i ** 2
    return i - 1


def countSquare(x):
    sqrt = x ** 0.5
    result = int(sqrt)
    return result


def integer_square_root_BS(k):
    low = 0
    high = k

    while low <= high:
        mid = (low + high) // 2
        mid_squared = mid * mid

        if mid_squared <= k:
            low = mid + 1
        else:
            high = mid - 1
    return low - 1


if __name__ == '__main__':
    val = integer_square_root(9)
    val2 = countSquare(239)
    print(val)
    print(val2)
