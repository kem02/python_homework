class TictactoeException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(message)


class Board:
    # Class-level list of all nine valid move names
    valid_moves = [
        "upper left",
        "upper center",
        "upper right",
        "middle left",
        "center",
        "middle right",
        "lower left",
        "lower center",
        "lower right",
    ]

    def __init__(self):
        # Initialize a 3×3 grid of blank spaces
        self.board_array = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
        # X always goes first
        self.turn = "X"
        # Track the last move if needed (not used below, but kept for compatibility)
        self.last_move = None

    def __str__(self):
        """
        Return a string representation of the board in this format:

         X |   | O
        -----------
           | X |
        -----------
         O |   | X

        (Each row, newline, then a separator, etc.)
        """
        lines = []
        lines.append(
            f" {self.board_array[0][0]} | {self.board_array[0][1]} | {self.board_array[0][2]} \n"
        )
        lines.append("-----------\n")
        lines.append(
            f" {self.board_array[1][0]} | {self.board_array[1][1]} | {self.board_array[1][2]} \n"
        )
        lines.append("-----------\n")
        lines.append(
            f" {self.board_array[2][0]} | {self.board_array[2][1]} | {self.board_array[2][2]} \n"
        )
        return "".join(lines)

    def move(self, move_string):
        """
        Place the current player's mark at the position named by move_string.
        - If move_string is not valid, raise TictactoeException("That's not a valid move.")
        - If the target cell is already occupied, raise TictactoeException("That spot is taken.")
        - Otherwise:
            * Update board_array[row][col] = self.turn
            * Flip self.turn to the other player ("X" → "O" or "O" → "X")
        """
        if move_string not in Board.valid_moves:
            raise TictactoeException("That's not a valid move.")

        # Determine row/column from the index in valid_moves
        move_index = Board.valid_moves.index(move_string)
        row = move_index // 3
        column = move_index % 3

        if self.board_array[row][column] != " ":
            raise TictactoeException("That spot is taken.")

        # Place the mark
        self.board_array[row][column] = self.turn

        # Flip turn
        if self.turn == "X":
            self.turn = "O"
        else:
            self.turn = "X"

    def whats_next(self):
        """
        Determine the current game status:
         - If all cells are filled and nobody has 3-in-a-row, return (True, "Cat's Game.")
         - If X or O has three in a row (row/column/diagonal), return (True, "<X or O> wins!")
         - Otherwise, return (False, "<current_player>'s turn.")
        """
        # 1) Check for a cat's game (full board, no spaces left)
        cat = True
        for i in range(3):
            for j in range(3):
                if self.board_array[i][j] == " ":
                    cat = False
                    break
            if not cat:
                break
        if cat:
            return True, "Cat's Game."

        # 2) Check rows for a win
        win = False
        for i in range(3):
            if self.board_array[i][0] != " ":
                if (
                    self.board_array[i][0] == self.board_array[i][1]
                    and self.board_array[i][1] == self.board_array[i][2]
                ):
                    win = True
                    break

        # 3) If no row win, check columns
        if not win:
            for i in range(3):
                if self.board_array[0][i] != " ":
                    if (
                        self.board_array[0][i] == self.board_array[1][i]
                        and self.board_array[1][i] == self.board_array[2][i]
                    ):
                        win = True
                        break

        # 4) If no row/column win, check diagonals
        if not win:
            if self.board_array[1][1] != " ":
                # Primary diagonal
                if (
                    self.board_array[0][0] == self.board_array[1][1]
                    and self.board_array[2][2] == self.board_array[1][1]
                ):
                    win = True
                # Secondary diagonal
                if (
                    self.board_array[0][2] == self.board_array[1][1]
                    and self.board_array[2][0] == self.board_array[1][1]
                ):
                    win = True

        # 5) If there's a win, announce who won
        if win:
            # Note: Since we flip `self.turn` immediately after placing,
            # the winner is the opposite of `self.turn` at this moment.
            if self.turn == "O":
                return True, "X wins!"
            else:
                return True, "O wins!"
        else:
            # 6) No win, no cat's game → next player's turn
            if self.turn == "X":
                return False, "X's turn."
            else:
                return False, "O's turn."


# 1) Create a new Board
board = Board()

# 2) Main game loop
while True:
    # Print the current board
    print(board)
    print()  # Blank line for readability

    # Check game status
    game_over, message = board.whats_next()
    if game_over:
        print(message)
        break

    # Prompt the current player for a move
    current_player = board.turn  # "X" or "O"
    prompt = f"{current_player}'s move (choose from {Board.valid_moves}): "
    user_input = input(prompt).strip().lower()

    try:
        board.move(user_input)
    except TictactoeException as e:
        print(e.message)
        print("--- Try again. ---\n")
        continue
