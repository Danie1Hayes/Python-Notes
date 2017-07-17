#思路1的生成器
def pascal_triangle1(n):
    list = [1]
    while n > 0:
       yield list
       list = [1] + [list[x] + list[x + 1] for x in range(len(list) - 1)] + [1]
       n -= 1
    return
for x in pascal_triangle1(5):
    print(x)


#思路2的生成器
def pascal_triangle2(n):
    list = [1]
    while n > 0:
       yield list
       list = [1] + [x + y for x, y in zip(list[:], list[1:])] + [1]
       n -= 1
    return
for y in pascal_triangle2(10):
    print(y)