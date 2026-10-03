import random
import os
while(True):
    os.system('cls')
    user_choice=int(input("Enter user choice\n0:Rock\n1:Paper\n2:Scissor\n")) 
    game_image=['🪨','📝','✂️']  
    if user_choice>=3 or user_choice<0:
        print("Invalid choice")
        break
    else:
        print(f"User Choosen:{game_image[user_choice]}")
        computer_choice=random.randint(0,2)
        print(f"Computer Choosen:{game_image[computer_choice]}")
        if user_choice==computer_choice:
            print("Drawn")
        elif user_choice==0 and computer_choice==1:
            print("Computer Win")
        elif user_choice==0 and computer_choice==2:
            print("User win")
        elif user_choice==1 and computer_choice==0:
            print("User Win")
        elif user_choice==1 and computer_choice==2:
            print("Computer Win")
        elif user_choice==2 and computer_choice==0:
            print("Computer wins")
        elif user_choice==2 and computer_choice==1:
            print("User Wins")
    confirm= input("Want to play again? (yes/no): ").lower()
    
    if confirm=='yes':
        continue
    else:
        break
print("Thank you for using rock paper scissor ?")