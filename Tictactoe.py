#pogram to create a  two player TicTacToe Game

import random
import os


def display_board(board):
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')


def player_input():
    player1 = input("Enter the name for Player 1: ")
    marker1 = " "
    while marker1 != "X" and marker1 != "O":
        marker1 = input(f"{player1}, choose 'X' or 'O': ").upper()
        if marker1 != "X" and marker1 != "O":
            print("Invalid Input!")

    player2 = input("Enter the name for Player 2: ")
    marker2 = " "
    while marker2 != "X" and marker2 != "O":
        marker2 = input(f"{player2}, choose 'X' or 'O': ").upper()
        if marker2 != "X" and marker2 != "O":
            print("Invalid Input!")

    return player1, marker1, player2, marker2


def place_marker(board, marker, position):
    if 1 <= position <= 9:
        board[position] = marker
    else:
        print("Invalid position!")


def win_check(board, mark):
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or
            (board[4] == mark and board[5] == mark and board[6] == mark) or
            (board[1] == mark and board[2] == mark and board[3] == mark) or
            (board[7] == mark and board[4] == mark and board[1] == mark) or
            (board[8] == mark and board[5] == mark and board[2] == mark) or
            (board[9] == mark and board[6] == mark and board[3] == mark) or
            (board[7] == mark and board[5] == mark and board[3] == mark) or
            (board[9] == mark and board[5] == mark and board[1] == mark))


def choose_first():
    players = ['player1', 'player2']
    random_choice = random.randint(0, 1)
    return players[random_choice]


def space_check(board, position):
    return board[position] == " "


def full_board_check(board):
    for i in range(1, 10):
        if space_check(board, i):
            return False
    return True


def player_choice(board, player):
    player_next_choice = int(input(f"{player}, choose the next position (1-9): "))
    if space_check(board, player_next_choice):
        return player_next_choice
    else:
        print("The chosen position is not available. Please choose a different position.")
        return player_choice(board, player)


def replay():
    while True:
        player_choice = input("Do you want to play again? (yes/no): ").upper()
        if player_choice == 'YES':
            return True
        elif player_choice == 'NO':
            return False
        else:
            print("Invalid input. Please enter 'yes' or 'no.'")


print('Welcome to Tic Tac Toe!')

while True:
    the_board = [" "] * 10
    player1, player1_marker, player2, player2_marker = player_input()
    turn = choose_first()
    print(turn + " will go first")

    play_game = input("Are you ready to play? Enter (yes/no): ").lower()

    if play_game == "yes":
        game_on = True
    else:
        game_on = False
        print('Oops! See you again.')

    while game_on:
        print('\n' * 100)  # Clear the screen
        if turn == "player1":
            display_board(the_board)
            position = player_choice(the_board, player1)
            place_marker(the_board, player1_marker, position)

            if win_check(the_board, player1_marker):
                display_board(the_board)
                print(f"{player1} won the game!")
                game_on = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print("It's a Tie!")
                    game_on = False
                else:
                    turn = "player2"
        else:
            display_board(the_board)
            position = player_choice(the_board, player2)
            place_marker(the_board, player2_marker, position)

            if win_check(the_board, player2_marker):
                display_board(the_board)
                print(f"{player2} won the game!")
                game_on = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print("It's a Tie!")
                    game_on = False
                else:
                    turn = "player1"

    if not replay():
        break
