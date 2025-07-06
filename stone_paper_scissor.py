from random import choice
print("WELCOME TO ROCK PAPER SCISSORS")
print("\n\nHere are some general rules\nthere will be 5 a point  play\nif there exist a tie then a tie break will begin for 3 more points\nRock beats Scissors\nScissor beats paper\nPaper beats Rock\n\n")
print("LET THE GAME BEGIN")
options=["Rock","Scissors","Paper"]
user_points=0
computer_points=0
turn=0

while turn<5:
    choice_computer=choice(options)
    print("computer has successfully make its choice")
    try:
        choice_user=options[int(input("Enter:\n0 for Rocks\n1 for Scissors\n2 for Paper\t"))]
    except IndexError:
        print("you have entered a wrong choice")
        choice_user=options[int(input("Enter:\n0 for Rocks\n1 for Scissors\n2 for Paper\t"))]
    
    if choice_computer == choice_user:
        computer_points+=1
        user_points+=1
    elif (choice_computer=="Rock" and choice_user=="Paper" ) or (choice_computer=="Paper" and choice_user=="Scissors" ) or (choice_computer=="Scissors" and choice_user=="Rock" ):
        user_points+=1
    else:
        computer_points+=1
    # print(computer_points+user_points)
    turn+=1
if computer_points==user_points:
    while (user_points+computer_points)!=8:
        choice_computer=choice(options)
        print("computer has successfully make its choice")
        try:
            choice_user=options[int(input("Enter:\n0 for Rocks\n1 for Scissors\n2 for Paper\t"))]
        except IndexError:
            print("you have entered a wrong choice")
            choice_user=options[int(input("Enter:\n0 for Rocks\n1 for Scissors\n2 for Paper\t"))]
    
        if choice_computer==choice_computer:
            computer_points+=1
            user_points+=1
        elif (choice_computer=="Rock" and choice_user=="Paper" ) or (choice_computer=="Paper" and choice_user=="Scissors" ) or (choice_computer=="Scissors" and choice_user=="Rock" ):
            user_points+=1
        else:
            computer_points+=1

print("\n\n\nAre you exiced for the results :)\n\n\n")
if computer_points>user_points:
    print("oops you lose 🥲")
else:
    print("yeah you won 😊😊")
    