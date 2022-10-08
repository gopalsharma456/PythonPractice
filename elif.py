age = input("enter your age ")
age = int(age)
if age==0 or age <0 :
    print("can't watch show")
elif 0<age<=5:
    print("ticket price = free")
elif 5<age<10:
    print("ticket price = 100")
elif 10<age<60:
    print("ticket price = 250")
elif 60<age:
    print("ticket price = 200")