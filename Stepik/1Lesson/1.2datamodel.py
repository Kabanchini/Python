a = [1,2]
b = a
c = [1,2]
print(a is b)
print(a is c)
print(c is b)

objects = [a, b, c, 2, 3]

ans = 0
distinct = []
for obj in objects: # доступная переменная objects
    new = True
    for temp in distinct:
        if temp is obj:
            new = False
            break
    if new:
        distinct.append(obj)
print(len(distinct))
