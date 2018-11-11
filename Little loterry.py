import random


for i in range(3):
    answer = input("Choose your number ")
    print("Try", i +1)
    print("You give number ",answer)

number = random.randint(1, 10)
print ("Random number" ,number)

if number == answer:
    print("You've right")

else:
    print("Wrong!!")