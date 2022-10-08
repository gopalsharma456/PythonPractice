##if passed two arguments print reverse with first capital
## else just capitalise first letter 
# def fun(r, **kwargs):  # **KWARG used because 2 arguments can be or can't be defined
#     if kwargs.get('rev_str') == True: #2nd argument passed or not
#         return [i[::-1].title() for i in r]  #for reversal
#     else:
#         return [i.title() for i in r]  #if only 1 argument passed

# n = ['abc', 'xyz']
# print(fun(n, rev_str = True))




###  v.152   take two arguments as string and find that string in list 
### ---> return index of string if  not found return -1

# def found(s, t):
#     for pos, i in enumerate(s):
#         if i == t:
#             return pos
#     return -1

# n = ('abc', 'pot', 'kjh')
# print(found(n, 'pot'))

n = (1,2,3,4)
def sqr(a):
    return a**2
a = list(map(sqr, n))
print(a)

b = list(map(lambda a : a**2 , n))
print(b)

c = [i**2 for i in n]
print(c)



