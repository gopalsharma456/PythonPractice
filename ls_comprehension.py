##### return list item in reversed order
# normal method
# def r_str(l):
#     rev_l = []
#     for i in l:
#         rev_l.append(i[::-1])
#     return rev_l
# a = ['tuv','xyz','abc']
# print(r_str(a))

# list comprehension method 

# def r_str(l):
#     return [i[::-1] for i in l]
# a = ['tuv','xyz','abc']
# print(r_str(a))

#### v.132 num to str 
# normal method
# def nts(a):
#     string = []
#     for i in a:
#         if (type(i) == int or type(i) == float):
#             string.append(str(i))
#     return string
# n = [1,2,3,4]
# print(nts(n))

# comprehension method

# def nts(a):
#     return [str(i) for i in a if (type(i) == int or type(i) == float)]
# n = [1,2,3,4]
# print(nts(n)) 

## 143 exer. take nums and tuple or list and return list with power of tuple

def cube(n, *args):
    if args:
        return[i**n for i in args]
    else:
        return "you didn 't pass any argument"
a = [1,2,3,4]    
print(cube(3, *a))















