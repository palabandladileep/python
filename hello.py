#question 1 ,2
num1 = int(input("Enter the first number"))
num2 = int(input("enter the second number"))
num3 = int(input("enter the third number"))
def find_largest():
    if(num1 > num2):
        if(num1 > num3):
            largest = num1
        else:
            largest = num3
    elif(num2 > num3):
            largest = num2
    else:
            largest = num3
    print("The largest number is",largest)

find_largest()

#question3 using function
name = input("Enter your name:")
age = int(input("Enter the age:"))
def age():
    y = 100-age
    x = 2021+y
    print("Person will turn 100 years in the year", x)
    return
print(age())

#question 6
p1= input("player 1, Enter rock/paper/scissors:")
p2= input("player 2, enter rock/paper/scissors:")
def rock_paper_scissors(player1,player2):
    while player1 == player2:
        print("Match is tied. play again")
        player1 = input("player1, Enter rock/paper/scissors:")
        player2 = input("player2, Enter rock/paper/scissors:")
    if player1 == "rock" and player2 == "paper":
        print("player 2 wins")
    elif player1 == "paper" and player2 == "rock":
        print("player 1 wins")
    elif player1 == "rock" and player2 == "scissors":
        print("player 1 wins")
    elif player1 == "scissors" and player2 == "rock":
        print("player 2 wins")
    elif player1 == "paper" and player2 == "scissors":
        print("player 2 wins")
    elif player1 == "scissors" and player2 == "paper":
        print("player 1 wins")
rock_paper_scissors(p1,p2)
