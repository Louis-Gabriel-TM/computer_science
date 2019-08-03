"""
Puzzle Wording
==============
Write a function where revealed cells are turned to -2 after clicking on a given cell.
If the clicked cell value is 0, reveal only all other 0's connected to it.
If the clicked cell has not the value 0, return the original field.

Inputs:
------
'field': a minesweeper field.
'nb_rows': the number of rows in the field.
'nb_cols': the number of columns in the field.
'clicked_row': the row where user has clicked.
'clicked_col': the column where user has clicked.

Example:
-------

Input:  field = [[-1, 1, 0, 0],
                 [1, 1, 0, 0],
                 [0, 0, 1, 1],
                 [0, 0, 1, -1]]
        nb_rows = 4, nb_cols = 4, clicked_row = 1, clicked_col = 3
Output: [[-1, 1, -2, -2],
         [1, 1, -2, -2],
         [-2, -2, 1, 1],
         [-2, -2, 1, -1]]
"""


def extract_neighbourhood(row, col, nb_rows, nb_cols):
    rows = [row + delta for delta in (-1, 0, 1) if 0 <= row + delta < nb_rows]
    cols = [col + delta for delta in (-1, 0, 1) if 0 <= col + delta < nb_cols]
    neighbourhood = [(row, col) for row in rows for col in cols]
    return neighbourhood


def reveal_zero_bomb_zone(
    field, nb_rows, nb_cols, clicked_row, clicked_col
):
    if field[clicked_row][clicked_col] != 0:
        return field
    else:
        expanded_zone = [(clicked_row, clicked_col)]
        field[clicked_row][clicked_col] = -2
        prev_size = 0
        new_size = 1

        while new_size > prev_size:
            prev_size = new_size

            for pos in expanded_zone:
                row, col = pos

                neighbourhood = extract_neighbourhood(
                    row, col, nb_rows, nb_cols
                )

                for location in neighbourhood:
                    loc_row, loc_col = location
                    #print("Location >>>", location)
                    not_in_zone = location not in expanded_zone
                    zero_location = field[loc_row][loc_col] == 0

                    if not_in_zone and zero_location:
                        expanded_zone.append(location)
                        new_size += 1
                        field[loc_row][loc_col] = -2

    return field


if __name__ == "__main__":
    field = [
        [0, 0, 1, 1, 1],
        [0, 0, 1, -1, 1],
        [1, 1, 2, 1, 1],
        [1, -1, 1, 0, 0]
    ]

    nb_rows, nb_cols = 4, 5
    clicked_row, clicked_col = 0, 1

    print("Init >>>", field)
    print("Clic >>>", reveal_zero_bomb_zone(
        field, nb_rows, nb_cols, clicked_row, clicked_col
    ))
