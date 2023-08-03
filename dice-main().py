# Creating the dice_roll() function.
def dice_roll():
    dice_roll = random.randint(1,6)
    return dice_roll

# Creating main() function
def main():
    # Create required variables
    player1 = 0
    player1_score = 0
    player2 = 0
    player2_score = 0
    rounds = 1
    # Create a while loop which runs till rounds != 11
    while rounds != 11:
        # print current round number using print() function as print("Round: ", rounds)
        print("\nRound:", rounds)
        # Call dice_roll() function for Player 1 and Player 2 and store the return value in player1 and player2 respectively.
        dice_roll()
        player1 = dice_roll()
        dice_roll()
        player2 = dice_roll()
        # print the outcomes of Player 1 & 2
        print("Player 1 roll:", player1)
        print("Player 2 roll:", player2)
        # Check if, player1 value equals that of player2. If it does, print Draw!.
        if player1 == player2:
          print("Draw!")
        # check if player1 is greater than player2. If yes, increase player1_score by 1 and print Player 1 wins!
        elif player1 > player2:
          print("Player 1 wins!")
          player1_score = player1_score + 1
        # else increase player2_score by 1 and print Player 2 wins!.
        else:
          print("Player 2 wins!")
          player2_score = player2_score + 1
        # Increase rounds by 1.
        rounds = rounds + 1
    # Outside while loop check if, player1_score value equals that of player2_score, print Draw!
    if player1_score == player2_score:
      print("\nDraw!")
    # check whether player1_score is greater than player2_score.
    # If yes, print("Final Winner: Player 1- Rounds Won: ", player1_score)
    elif player1_score > player2_score:
      print("\nFinal winner is Player 1! Rounds won:", player1_score)
    # Otherwise print("Final Winner: Player 2 - Rounds Won: ", player2_score)
    else:
      print("\nFinal winner is Player 2! Rounds won:", player2_score)


# Call the 'main()' function
main()