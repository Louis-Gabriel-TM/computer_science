"""
Puzzle Wording
==============
Write a function that assigns the correct number in a field of Minesweeper (VF: jeu du démineur), which is represented as a list of lists (2 dimensional array).

Inputs:
------
'bombs': a list with the bomb locations.
'nb_rows': the number of rows in the field.
'nb_cols': the number of columns in the field.

Example:
-------
Input:  bombs = [[0, 0], [0, 1]], nb_rows = 3, nb_cols = 4
Ouput:  [[-1, -1, 1, 0],
         [2, 2, 1, 0],
         [0, 0, 0, 0]]
"""


def extract_neighbourhood(row, col, nb_rows, nb_cols):
    rows = [row + delta for delta in (-1, 0, 1) if 0 <= row + delta < nb_rows]
    cols = [col + delta for delta in (-1, 0, 1) if 0 <= col + delta < nb_cols]

    neighbourhood = [(row, col) for row in rows for col in cols]

    return neighbourhood


def init_field(nb_rows, nb_cols):
    field = []

    for _ in range(nb_rows):
        field.append([0] * nb_cols)

    return field


def minesweeper_placing_bombs_one_by_one(bombs, nb_rows, nb_cols):
    field = init_field(nb_rows, nb_cols)

    for bomb in bombs:
        field[bomb[0]][bomb[1]] = -1

        neighbourhood = extract_neighbourhood(
            bomb[0], bomb[1], nb_rows, nb_cols
        )
        for location in neighbourhood:
            if field[location[0]][location[1]] != -1:
                field[location[0]][location[1]] += 1

    return field


def place_bombs(bombs, nb_rows, nb_cols):
    field = init_field(nb_rows, nb_cols)

    for bomb in bombs:
        field[bomb[0]][bomb[1]] = 1

    return field


def minesweeper_placing_all_bombs_at_the_beginning(bombs, nb_rows, nb_cols):
    field = init_field(nb_rows, nb_cols)

    bomb_field = place_bombs(bombs, nb_rows, nb_cols)

    for row in range(nb_rows):
        for col in range(nb_cols):
            if bomb_field[row][col] == 1:
                field[row][col] = -1
            else:
                neighbourhood = extract_neighbourhood(
                    row, col, nb_rows, nb_cols
                )

                count_bombs = 0
                for location in neighbourhood:
                    count_bombs += bomb_field[location[0]][location[1]]

                field[row][col] = count_bombs

    return field


if __name__ == "__main__":
    pass
