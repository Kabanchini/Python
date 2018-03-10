def nearest_square(max):
    cur = 1
    while(cur * cur < max):
        cur += 1
    cur -= 1
    return cur*cur

test1 = nearest_square(40)
print("expected result: 36, actual result: {}".format(test1))
