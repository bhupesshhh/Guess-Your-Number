import random

# Game Initiation
print("GUESS YOUR NUMBER!!!\n")
print("Computer will try to guess your number.\n")
print("Number should lie between (1-100)\n")
limit = input("Have you picked your number? (yes/no)")

if limit.lower() == "yes":
  # Start the game with Yes only
  gameplay = True
  gameon = True
  print("\nLet's start the game!")
else:
  gameplay = False
  gameon = False

# Gameon Condition
while gameon:

  # Setting The Range
  counts = 0
  start = 0
  end = 100

  # Gameplay Condition
  while gameplay:

    # Guess Count
    counts += 1

    # Computer Guess
    guess = random.randint(start,end)
    print(f"\nComputer Guess: {guess}")

    # Condition for start and equal is same
    if start == end-2 or end == start+2:
      print(f"\n{guess} is the correct answer\n")
      gameplay = False
      break

    # Condition to choose from the desired
    while True:
      answer = input("Computer guess is ____ (high/low/correct) ")
      if answer.lower() in ["high","low","correct"]:
          break
      else:
        print("Incorrect Input")

    # Check for correct guess
    if answer == "correct":
      print(f"\n{guess} is the correct answer\n")
      gameplay = False
      break

    # Condition to adjust range as per the user input
    if answer == "low":
      start = guess
    if answer == "high":
      end = guess


  # Result and Score
  print(f"You took {counts} guesses to get the right answer\n")

  # Replay Game
  replay = input("Do you wanna play the game again? (yes/no)")
  if replay.lower() == "yes":
    gameon = True
    gameplay = True
    print("\n")
  else:
    gameon = False
    break

# Endnote
print("\nThanks for playing the game")
print("We hope to see you soon!\n")