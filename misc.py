# # name = input("enter name : ")
# # tmp = ""
# # i = 0
# # while i < len(name):
# #     if name[i] not in tmp:
# #         tmp += name[i]
# #         print(f"{name[i]}:{name.count(name[i])}")
# #     i += 1


# import random
# winning_number = random.randint(1,100)
# guess = 1
# n = int(input("enter number : "))
# game_over = False
# while not game
# if n == winning_number:
#     print(f"you win, guessed in {i}")




# 95 exe 1 return square of list

# def square_list(l):
#     square = []
#     for i in l:
#         square.append(i**2)
#     return square

# numbers = list(range(1,11))
# print(square_list(numbers))


# 97 print reverse of list using pop and append methods


# def reversed_list(l):
#     reversed = []
#     for i in range(len(l)):
#         popped_item = l.pop()
#         reversed.append(popped_item)
#     return reversed
 
# alphabets = list(range(1,11))
# print(reversed_list(alphabets))


#  99 reverse each element in list


# def reversed_list(l):
#     r_list = []
#     for i in l:
#         r_list.append(i[::-1])
#     return r_list

# n = ['avd', 'pre', 'tde' ]
# print(reversed_list(n))

# def odd_even(l):
#     odd = []
#     even = []
#     for i in l:
#         if i % 2 == 0:
#             even.append(i)
#         else:
#             odd.append(i)
#     out = [odd, even]
#     return  out
# n = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
# print(odd_even(n))


# 103 common finder


# def common_finder(l, a):
#     common = []
#     for i in l:
#         if i in a:
#             common.append(i)
#     return common
# n = [1,2,3,4]
# s = [1,2,5,6]
# print(common_finder(n, s))

def linl(s):
    count = 0
    for i in s:
        if type(i) == list :
            count += 1
    return count
n = [1,3, [1,2,3], [1,4,5], [1,2,3]]

print(linl(n))






















