import random

#--------------------------------------Askii art---------------------------------------#

Rock ='''  
           _______
       ---'   ____)
            (_____)
            (_____)
            (____)
      ---.__(___) '''
Paper = '''   
           _______
       ---'   ____)____
                ______)
                _______)
               _______)
      ---.__________)
'''
Scissors = '''
          _______
      ---'   ____)____
                ______)
            __________)
            (____)
      ---.__(___)
''' 
print('''welcome to Rock paper scissors''')
Player = input('what is your name?:- ') 

# ------------------------------ players choice ---------------------------------------#
players_choice = (int(input('\nEnter your play (1 for rock , 2 for paper and 3 for scissor):- ')))
#______________________________________________________________________________________#
if players_choice == 1 :
      print('your choice is rock'+ '\n' + Rock)
elif players_choice == 2:
      print('your choice is paper'+ '\n' + Paper)
elif players_choice == 3:
      print('your choice is scissor'+ '\n' + Scissors)
else:
      print('Your choice is invalid ')
#-----------------------------Computers choice------------------------------------------#
Computers_options = ['1', '2', '3']
Computers_choice_possibility = random.randint(0,2)
computers_choice = int((Computers_options[Computers_choice_possibility]))

#________________________________________________________________________________________#
if computers_choice == 1 :
      print('computers choice is rock'+ '\n' + Rock)
elif computers_choice == 2:
      print('computers choice is paper'+ '\n' + Paper)
else:
      print('computers choice is scissor'+ '\n' + Scissors)
#______________________________In case of draw____________________________________________#

if computers_choice == 1 and players_choice == 1 or computers_choice == 2 and players_choice == 2 or computers_choice == 3 and players_choice == 3:
      print('It is a draw' )
elif computers_choice == 1 and players_choice == 3 or computers_choice == 2 and players_choice == 1 or computers_choice == 3 and players_choice == 2:
      print('computer wins')

elif computers_choice == 3 and players_choice == 1 or computers_choice == 1 and players_choice == 2 or computers_choice == 2 and players_choice == 3:
      print(Player + 'wins')
else:
      print('Error please try again')
      
      
