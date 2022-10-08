# def function and return avg 
# (1+4+7)/3, (2,5,8), (3+6+9)/3

# def avg_find(*args):
#     avg =[]
#     for i in zip(*args):
#         avg.append(sum(i)/len(i))
#     return avg

### using lambda expression

avg_find = lambda *args : [sum(i)/len(i) for i in zip(*args)]


print(avg_find([1,2,3],[4,5,6],[7,8,9]))