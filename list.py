# n = ['abc', 'abfd', 'abc', 'por']
# n.append('por')
# print(n)

# append , insert, extend   ----> used for adding elements
# pop, del, remove ----> used for deleting elements

# in ----> used for checking element's presence

# if 'abc' in n :
#     print("present")
# else :
#     print("not present")


# count 
# print(n.count('abc')) ------> it will print count of 'abc'

# sort 
# print(n.sort()) ----> will sort in ascending order


# sorted

#print(sorted(n)) -----> sort only thid time will not change anything

#    reverse
# n.reverse()
# print(n)   -------> print in reverse order 

#     clear 
# n.clear() ----> will clear all element

#    copy 
# new_n = n.copy()
# print(new_n) -------> will copy all element in new list


# equals (==)

# n1 = ['abc', 'por', 'xyz' ]
# n2 = ['avd', 'frt', 'ftr']
# n3 = ['abc', 'por', 'xyz']
# print(n1 == n3)  -----------> True because chacks only valuse


# is

# print(n1 is n3)  -------> False checks valuse and position(location)

# for i in n :
#     print(i)
# n = 12
# print(type(n))

# pass function to a list

# n = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# def neg_no(a):
#     negative = []
#     for i in a :
#         negative.append(-i)
#     return(negative)
# print(neg_no(n))

# print square of defined list
# def square_list(a):
#     square = []
#     for i in a :
#         square.append(i**2)
#     return(square)

# numbers = list(range(1, 11))
# print(square_list(numbers))

# reverse list using pop and append

# def character(a):
#     rev_char = []
#     for i in range(len(a)) :
#         popped_item = a.pop()
#         rev_char.append(popped_item)
#     return(rev_char)

# n = list(range(1, 11))
# print(character(n))

# reverse each element of string in reverse order


# def l_word (a):
#     r_word = []
#     for i in a:
#         r_word.append(i[::-1])
#     return r_word
# n = ['abc', 'def', 'ghi']
# print(l_word(n))


# print even odd nos. in diff. sublists

# def odd_even(a):
#     odd = []
#     even = []
#     for i in a:
#         if i%2 == 0:
#             even.append(i)
#         else:
#             odd.append(i)
#     filter_ls = [odd, even]
#     return filter_ls
# n = list(range(1,21))
# print(odd_even(n))


# take 2 lists and print common element 

# def com_num(l1, l2):
#     com_list = []
#     for i in l1:
#         if i in l2:
#             com_list.append(i)
#     return com_list

# a1 = [1,2,3,4,5]
# a2 = [1,2,4,6,7]
# print(com_num(a1, a2))

# find how many lists are in list

# def ls_no(a):
#     list1 = 0
#     for i in a:
#         if  type(i) == list:
#             list1 +=1
#     return list1
# n = [1,2,3, [1,2,3,4,5], [1,4,6,7], [2,4,5]]
# print(ls_no(n))



























