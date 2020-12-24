import random
temp = random.randint(0,100)
No1=temp
print(temp)
i=0
temp=0

while(i<=9):

    print("Enetr the number between 0 to 100")
    No = int(input())

    if No1 == No :
        print("---------------------------------------")
        print("Correct Guess!")
        print("Number of guesses",i)
        print("---------------------------------------")
    else:
        print("Try again.")
    i=i+1


if i>9:
    print("---------------------------------------")
    print("             Number is",No1)
    print("             Game over!                ")
    print("---------------------------------------")