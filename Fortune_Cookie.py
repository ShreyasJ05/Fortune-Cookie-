print("Welcome to Fortune Cookie - Know your future from AI")
print("Disclamier : This program is just for fun - and a learning process of my python journey \n")

value = input("Press 1 to continue \n")

if value == 1:
    print("Helo")



import random

lucky_number = random.randint(1, 100)

fortune_number = random.randint(1, 3)

fortune_text = ""
if fortune_number == 1:
        fortune_text = "Hope your day goes well"
if fortune_number == 2:
        fortune_text = "you are going to have a bad day"
if fortune_number == 3:
        fortune_text = "You gonna get what you needed"

print(f"{fortune_text} and your lucky number is {lucky_number}")

print("Thank You Hope you got your fortune ")
end=input("Press any number to end")









