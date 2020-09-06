class Player():
    def __init__(self, board):
        self.board = board


class HumanPlayer(Player):
    def __init__(self, board):
        super().__init__(board)

    def next_move(self):
        print("Please enter your move:", end = ' ')
        move = int(input())
        self.board.board_data[move - 1] = self.board.h_letter


class MinimaxComputerPlayer(Player):
    def __init__(self, board):
        super().__init__(board)

    def next_move(self):
        bestScore = -99999
        bestMove = 0
        for move in self.board.available_moves():
            self.board.board_data[move] = self.board.c_letter
            score = self.minimax(self.board, False)
            self.board.board_data[move] = '-'
            if score > bestScore:
                bestScore = score
                bestMove = move
        self.board.board_data[bestMove] = self.board.c_letter

    def minimax(self, board, maximizing_player):
        available_moves = board.available_moves()
        num_empty_squares = len(available_moves)

        if board.is_winner(board.c_letter):
            return (num_empty_squares + 1)
        elif board.is_winner(board.h_letter):
            return -(num_empty_squares + 1)
        elif num_empty_squares == 0:
            return 0

        if maximizing_player:
            maxEval = -99999
            for move in available_moves:
                board.board_data[move] = board.c_letter
                eval = self.minimax(board, False)
                board.board_data[move] = '-'
                maxEval = max(eval, maxEval)
            return maxEval
        else:
            minEval = 99999
            for move in available_moves:
                board.board_data[move] = board.h_letter
                eval = self.minimax(board, True)
                board.board_data[move] = '-'
                minEval = min(eval, minEval)
            return minEval
