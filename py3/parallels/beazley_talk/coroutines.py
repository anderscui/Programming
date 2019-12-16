# coding=utf-8
def countdown(n):
    while n > 0:
        yield n
        n -= 1

c = countdown(5)
print(c)

# for i in c:
#     print(i)

from collections import deque
tasks = deque()
tasks.extend([countdown(10), countdown(5), countdown(20)])
print(tasks)


def run():
    while tasks:
        task = tasks.popleft()
        try:
            x = next(task)
            print(x)
            tasks.append(task)
        except StopIteration:
            print('Task done')


run()
