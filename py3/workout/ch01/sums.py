# coding=utf-8


def sum2(*numbers):
    result = 0

    # if len(numbers) == 1 and isinstance(numbers[0], (list, tuple)):
    #     numbers = numbers[0]

    for num in numbers:
        result += num
    return result


if __name__ == '__main__':
    print(sum2())
    print(sum2(1))
    print(sum2(1, 2))
    print(sum2(*[1, 2, 3]))
