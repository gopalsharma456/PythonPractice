# number = input("enter number : ")
# winning_number = 55
# number = int(number)
# if number > 55 :
#     print("too high ")
# else :
#     if number < 55 :
#         print("too low ")
#     if number == 55 :
#         print("You WON!!!!!")

# import random
# winning_number = random.randint(1,100) # this is used for random number guessing
 
winning_number = 45
guess = 1
n = int(input("enter number : "))
game_over = False       #this will define at the start no game over
while not game_over :   #or use while True
    if n == winning_number :
        print(f"you won you guessed correctly after {guess} times  ")
        game_over = True  #break
    else :
        if n < winning_number :
            print("too low")
        else :
            print("too high")
            
        guess +=1
        n = int(input("enter number again : "))