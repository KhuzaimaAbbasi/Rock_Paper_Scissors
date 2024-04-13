import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''



arr=[rock,paper,scissors]

computer_index=random.randint(0,2)

player_index=int(input("What do you choose, Enter 0 for Rock, 1 for Paper or 2 for Scissors\n"))

print(f"You chose\n {arr[player_index]}\n")
print(f"Computer chose\n {arr[computer_index]}\n")

if player_index==computer_index:
  print("It was a draw")
elif player_index==0 and computer_index==2:
  print("You won")
elif player_index==2 and computer_index==0:
  print("You Lost")
elif player_index>computer_index:
  print("You won")
elif computer_index>player_index:
  print("You Lost")
elif player_index>3 or player_index<0:
  print("Please enter a valid index")