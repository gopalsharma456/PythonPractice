# print hello world 10 times

# i = 1
# while i <=10 :
#     print(f"hello world {i}") # i is the loop number
#     i += 1

# sum of numbers

# total = 0
# i = 1 
# while i <= 10 :
#     total += i
#     i += 1
# print(total)

# exe 3

# number = int(input("enter natural number : "))
# total = 0
# i = 1
# while i <= number :
#     total += i
#     i += 1
# print(total) 

#exe 4

# n = input("enter any number : ")
# sum = 0
# i = 0
# while i < (len(n)) :
#     sum += int(n[i])
#     i += 1
# print(sum)

# exe 5

name = input("enter your name : ")
temp = ""
i = 0
while i < len(name) :
    if name[i] not in temp :
        temp += name[i]
        print(f"{name[i]} : {name.count(name[i])} ")
    i += 1




















