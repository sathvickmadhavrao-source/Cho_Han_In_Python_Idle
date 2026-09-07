import random
import time
print("Welcome to Cho-Han(Japanese Dice Game)")
die_numbers=[1,2,3,4,5,6]
game_continue=True
score=0
comp_score=0
while game_continue==True:
    user_input=input("Do you want to roll your share of die in the invisible cup? Type 'y' for yes and 'n' for no:").lower()
    if user_input=='y':
        user_dice_one=random.choice(die_numbers)
        user_dice_two=random.choice(die_numbers)
        user_die_count=user_dice_one+user_dice_two
        user_choice=input("Do you want to choose even(cho) or odd(han):").lower()
        time.sleep(1)
        print(f"The combined sum of the two dice is {user_die_count}")
        if user_choice=="even" or user_choice=="cho" or user_choice=="even(cho)" or user_choice=="cho(even)":
            if user_die_count%2==0:
                score+=1
                print(f"You chose {user_choice} and won a point, your score is {score}")
                time.sleep(1)
            else:
                score-=1
                print(f"You chose {user_choice} and lost a point, your score is {score}")
                time.sleep(1)
        elif user_choice=="odd" or user_choice=="han" or user_choice=="odd(han)" or user_choice=="han(odd)":
            if user_die_count%2!=0:
                score+=1
                print(f"You chose {user_choice} and won a point, your score is {score}")
                time.sleep(1)
            else:
                score-=1
                print(f"You chose {user_choice} and lost a point, your score is {score}")
                time.sleep(1)
        choice_of_comp=random.randint(1,2)
        if choice_of_comp==1:
            if user_die_count%2!=0:
                comp_score+=1
                print(f"Computer chose odd(han) and won a point, computer's score is {comp_score}")
                time.sleep(1)
            else:
                comp_score-=1
                print(f"Computer chose odd(han) and lost a point, computer's score is {comp_score}")
                time.sleep(1)
        elif choice_of_comp==2:
            if user_die_count%2==0:
                comp_score+=1
                print(f"Computer chose even(cho) and won a point, computer's score is {comp_score}")
                time.sleep(1)
            else:
                comp_score-=1
                print(f"Computer chose even(cho) and lost a point, computer's score is {comp_score}")
    elif user_input=='n':
        if score==comp_score:
            print(f"You and the computer have a draw. Both of your scores are the same {score}")
        elif score>comp_score:
            score_difference=score-comp_score
            print(f"You won by {score_difference} points. The computer's score was {comp_score} and your score was {score}")
        elif score<comp_score:
            score_difference=comp_score-score
            print(f"You lost by {score_difference} points. The computer's score was {comp_score} and your score was {score}")
        time.sleep(2)
        game_continue=False
    else:
        print("Please choose 'y' or 'n' only")
