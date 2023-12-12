# coding=utf-8
for i in range(3):
    print(i, end=' ')
else:
    print(' -> for done.')

# continue，也认为一次迭代是”执行了“的
for i in range(3):
    if i >= 2:
        continue
    print(i, end=' ')

else:
    print(' -> for done.')

for i in range(3):
    if i == 1:
        continue
    print(i, end=' ')

else:
    print(' -> for done.')

# break，即使并未跳过任何语句
for i in range(3):
    print(i, end=' ')
    if i >= 2:
        break
else:
    print(' -> for done.')
