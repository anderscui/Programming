# coding=utf-8


def make_averager():
    items = []

    def averager(val):
        items.append(val)
        return sum(items) / len(items)

    return averager


def make_averager2():
    count = 0
    total = 0.0

    def averager(val):
        # order:
        # not global or nonlocal
        # not local (no assignment)
        # then go nonlocal -> global -> builtin scopes
        # NameError: name 'b' is not defined
        # print(b)
        nonlocal count, total
        count += 1
        total += val
        return total / count

    return averager


if __name__ == '__main__':
    print('--avg')
    avg = make_averager()
    print(avg(10), avg(11), avg(15))
    print(avg.__code__.co_varnames)
    print(avg.__code__.co_freevars)
    # __closure__ is a tuple, see co_freevars
    for free_var, var in zip(avg.__code__.co_freevars, avg.__closure__):
        print(free_var, var.cell_contents)

    print('\n--avg2')
    avg2 = make_averager2()
    print(avg2(10), avg2(11), avg2(15))
    print(avg2.__code__.co_varnames)
    print(avg2.__code__.co_freevars)
    for free_var, var in zip(avg2.__code__.co_freevars, avg2.__closure__):
        print(free_var, var.cell_contents)
