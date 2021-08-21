# Global Variables

# основная доска
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]

game_still_going = True

winner = None

current_player = "X"

# функции
def board_display():
    print(board[0], "|", board[1], "|", board[2])
    print(board[3], "|", board[4], "|", board[5])
    print(board[6], "|", board[7], "|", board[8])


# основная логика игры
def main_game():

    board_display()

    while game_still_going:

        handle_turns(current_player)

        check_game_over()

        flip_player()


# игра окончена
    if winner == "X" or winner == "O":
            print(winner + " победил!")

    elif winner is None:
            print("Ничья")


def handle_turns(player):
    print("Очередь " + player)
    position = input("Выберете цифру между 1 и 9: ")

    valid = False
    while not valid:

        while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            position = input("Выберете любую цифру в промежутке между 1 и 9: ")

        position = int(position) - 1

        if board[position] == "-":
            valid = True
        else:
            print("Ой! Эта клетка занята. Поробуйте другую.")

    board[position] = player
    board_display()


def check_game_over():
    check_if_win()
    check_if_tie()


def check_if_win():
    global winner
    row_winner = check_row()
    column_winner = check_column()
    diag_winner = check_diag()
    if row_winner:
        winner = row_winner
    elif column_winner:
        winner = column_winner
    elif diag_winner:
        winner = diag_winner
    else:
        winner = None
    return


def check_row():
    global game_still_going
    row_1 = board[0] == board[1] == board[2] != "-"
    row_2 = board[3] == board[4] == board[5] != "-"
    row_3 = board[6] == board[7] == board[8] != "-"
    if row_1 or row_2 or row_3:
        game_still_going = False

    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]
    return


def check_column():
    global game_still_going
    column_1 = board[0] == board[3] == board[6] != "-"
    column_2 = board[1] == board[4] == board[7] != "-"
    column_3 = board[2] == board[5] == board[8] != "-"
    if column_1 or column_2 or column_3:
        game_still_going = False

    if column_1:
        return board[0]
    elif column_2:
        return board[1]
    elif column_3:
        return board[2]
    return


def check_diag():
    global game_still_going
    diag_1 = board[0] == board[4] == board[8] != "-"
    diag_2 = board[2] == board[4] == board[6] != "-"

    if diag_1 or diag_2:
        game_still_going = False

    if diag_1:
        return board[0]
    elif diag_2:
        return board[2]

    return


def check_if_tie():
    global game_still_going
    if "-" not in board:
        game_still_going = False
    return


def flip_player():
    global current_player
    if current_player == "X":
        current_player = "O"
    elif current_player == "O":
        current_player = "X"
    return

main_game()
