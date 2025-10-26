# Description: The player throws a die multiple times and attempts to get as
# close to a score of nine with the sum of his or her throws. If the player
# scores more than nine points the game ends. The player can choose to stop
# throwing the die on any turn. If the player scores exactly nine then this
# is counted as a win. 


# Draw the title
def box(width = 17, height = 3):
    print("=" * width)
    print("Welcome to Macao!")
    print("=" * width)

import random

MIN = 1
MAX = 6

def main():
    print()
    box()
    print("\nRoll the die, see if you can reach the magic number 9.")
    total_throw = 0
    total_number_of_game = 0
    total_games_won = 0
    total_games_bust = 0
    play = 'y'
    
    while play.lower() == 'y':
        play = input("\nDo you want to play the gamne (y/n)? ")
        if play.lower() == 'y': 
            # this is to distinguish both upper case and lower case y
            print("\nPLAYING!!!")
            total_number_of_game += 1
            another_turn = 'y'
            total = 0
            while another_turn.lower() == 'y':
                dice_throw = random.randrange(MIN,MAX)
                total += dice_throw 
                total_throw += 1
                print(f'Dice throw: {dice_throw}, total: {total}.')  
                
                if total < 9:
                    another_turn = input("Take another turn (y/n)? ")         
                
                elif total == 9:
                    print("You won!!!")
                    total_games_won += 1
                    break
                
                elif total > 9: 
                    print("You lost.")
                    total_games_bust += 1
                    break
        else:
            print(f'\nResults:\n========\nTotal number of games: \
                {total_number_of_game}.\nTotal throws: {total_throw}.\
                    \nTotal games won: {total_games_won}.\
                    \nTotal games bust: {total_games_bust}.')
            if total_number_of_game == 0:
                print(f'Average throws per game: 0.00')
            #to avoid the number divide zero, which is undefined
            else:
                ave_number_of_games = float(total_throw/total_number_of_game)
                print(f'Average throws per game: {ave_number_of_games:.2f}.')
            break        
            
# Start the program          
if __name__ == "__main__":
    main()
