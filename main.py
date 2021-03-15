import random
# Storing ACII Rock, Paper, Scissor art into variables
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
# Taking players choice and placing it into a variable.
choice = input("What do you Chose? Type 0 for Rack, 1 for Paper or 2 for Scissors.\n")

# Take players input - print the selection and place rock, paper, or scissor selection into variable
if choice == "0":
  print(f"You chose {rock}")
  player = rock
elif choice == "1":
  print(f"You chose {paper}")
  player = paper
elif choice == "2":
  print(f"You chose {scissors}")
  player = scissors
else:
  print("You lose.")

# Placing variables rock, paper, and scissors into a single variable for the computer.
ai_choice = rock, paper, scissors

# Getting the computer to choice at random from the list stored in ai_choice variable and place that selection into the computer_chose variable. Then print that selection.
computer_chose = random.choice(ai_choice)
print(f"Computer Chose:\n {computer_chose}")

# Getting what computer_chose selected and placed it into a variable.
pc_pick = computer_chose

# Creating several checks against the player to see who wins. If either wins, prints win or lose or draw.
if pc_pick == rock and player == paper:
  print("You win!")
elif pc_pick == paper and player == rock:
  print("You lose!")
elif pc_pick == rock and player == scissors:
  print("You lose!")
elif pc_pick == scissors and player == paper:
  print("You lose!")
elif pc_pick == paper and player == scissors:
  print("You win!")
elif pc_pick == scissors and player == rock:
  print("You win!")
elif pc_pick == player:
  print("Draw!!")
else:
  print("Not working")
