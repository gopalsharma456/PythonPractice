def list_fn(a):
    count = 0
    for i in a:
        if type(i) == list:
            count +=1
    return count

n = [1,2,3, [1,2], [3,4]]
print(list_fn(n))
