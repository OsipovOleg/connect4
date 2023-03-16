N_ROWS = 6
N_COLUMNS = 7
EMPTY_CELL = " "


class ConnectGame:

    def __init__(self, number_of_players: int = 2):
        if number_of_players != 2:
            raise ValueError("This game support only two players now")

        self.number_of_players = number_of_players
        self.board = [[EMPTY_CELL for _ in range(N_COLUMNS)] for _ in range(N_ROWS)]

        self.current_player = 0
        self.column_lengths = [0] * N_COLUMNS

        self.status_message = f"Current player {self.current_player}"

    def __str__(self):
        display = "Connect4 \n"
        display += str(self.column_lengths) + "\n"
        display += self.status_message
        for row in reversed(self.board):
            display += '\n' + str(row)
        return display

    def check_line(self, row_index: int, column_index: int) -> bool:
        """
        Check if the board contains a line going through a cell (row_index, column_index)
        :param row_index:
        :param column_index:
        :return:
        """
        return False

    def is_board_full(self) -> bool:
        for item in self.column_lengths:
            if item < N_ROWS - 1:
                return False
        return True

    def do_action(self, column_index: int) -> bool:
        """
        Do an action and return False if  the game is over
        :param column_index:
        :return:
        """
        column_len = self.column_lengths[column_index]

        self.status_message = ""

        if column_len < N_ROWS:
            self.board[self.column_lengths[column_index]][column_index] = self.current_player
            is_winner = self.check_line(self.column_lengths[column_index], column_index)

            self.column_lengths[column_index] += 1
            if is_winner:
                self.status_message = f"The player #{self.current_player} won"
                return False
            if self.is_board_full():
                self.status_message = "All board is full. Game is over."
                return False

            self.current_player = (self.current_player + 1) % self.number_of_players
            self.status_message = f"Current player {self.current_player}"

        else:
            self.status_message = f"This column is full, choose another. Current player {self.current_player}"

        return True
