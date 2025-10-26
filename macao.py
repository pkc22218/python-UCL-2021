#Description: a Player class so that you can make a multiplayer version of the dice game. 
#Attributes:
#given_name: Must be greater than 2 characters and must only contain alphabetic characters. 
#A ValueError exception with a suitable error message must be generated if the given_name is invalid.

#surname: Must be greater than 2 characters and must only contain alphabetic characters. A ValueError 
#exception with a suitable error message must be generated if the surname is invalid.

#games_played: Must be equal to or greater than 0. A ValueError exception with a suitable error message
#must be generated if games_played is invalid.

#games_won:Must be equal to or greater than 0. A ValueError exception with a suitable error message must 
#be generated if games_won is invalid.

#games_bust: Must be equal to or greater than 0. A ValueError exception with a suitable error message must
#be generated if the games_bust is invalid.
    
#num_throws: Must be equal to or greater than 0. A ValueError exception with a suitable error message must 
#be generated if the num_throws is invalid.

import random
from player import Player

MAXIMUM_SCORE = 9


def intro():
    """Print the introduction to the game.
    """    
    print("\n=================")
    print("Welcome to Macao!")
    print("=================")
    print(f'\nRoll the die, see if you can reach the magic number {MAXIMUM_SCORE}.')


def get_players(player_list):
    """Collect player information, create player object and store in list.

    Args:
        player_list (list): List of Player objects.
    """    
    num_players = int(input("How many players: "))
    for num in range(num_players):
        player_list.append(create_player(num + 1))


def create_player(current_player):
    """Create and return Player object

    Args:
        current_player (Player): Player object

    Returns:
        Player: Player object.
    """    
    valid = False

    while not valid:
        print(f'Player {current_player}.')
        given_name = input("\t\tGiven name: ")
        surname = input("\t\tSurname: ")
        try:
            player_obj = Player(given_name, surname)
            valid = True
        except ValueError as error_message:
            print(error_message)  

    return player_obj


def do_turn(player, total_this_turn):
    """Logic for player taking a turn.

    Args:
        player (Player): Player object
        total_this_turn (int): Total of dice throws this turn.

    Returns:
        tuple: (continue_turn, total_this_turn), flag indicating whether to 
                continue this turn and the total dice throw this turn.
    """    
    continue_turn = True
    dice_throw = random.randint(1,6)
    player.num_throws += 1

    total_this_turn += dice_throw
    print(f'Dice throw: {dice_throw}, total: {total_this_turn}.')

    if total_this_turn == MAXIMUM_SCORE:
        print('You won!!!!') 
        continue_turn = False
        player.games_won += 1
    elif total_this_turn > MAXIMUM_SCORE:
        print('You lost.')
        player.games_bust +=1
        continue_turn = False   

    return continue_turn, total_this_turn


def play(player_list):
    """Play the game

    Args:
        player_list (list): the list of Player objects.
    """        

    for player in player_list:
        print(f"\n{player.given_name}'s turn: ")

        player.games_played += 1

        play_again = True
        total_this_turn = 0

        while play_again: 
            play_again, total_this_turn = do_turn(player, total_this_turn)
            if play_again:
                answer = input('Take another turn (y/n)? ')
                if answer != 'y' and answer != 'Y':
                    play_again = False


def print_results(player_list):
    """Print the results for all players.

    Args:
        player_list (list): List of Player objects.
    """    
    print('\nResults:')
    print('========')
    for player in player_list:
        print(player)


def main():

    player_list = []

    intro()
    get_players(player_list)

    playing = True

    while playing:
        print("\nPLAYING!!!")

        play(player_list)

        answer = input('\nPlay again (y/n)? ')
        if answer != 'y' and answer != 'Y':
            playing = False

    print_results(player_list)


if __name__ == "__main__":
    main()

