from Player.Player import HumanPlayer
from Player.Player import MinimaxComputerPlayer

class Board():
	def __init__(self, board_data):
		self.board_data = board_data
		self.next_turn = 'X'


class TerminalBoard(Board):
	def __init__(self, board_data):
		super().__init__(board_data)
		self.init_game()

	def init_game(self):
		print("Please choose X or O:", end = ' ')
		self.h_letter = input()

		if self.h_letter == 'X' or self.h_letter == 'x':
			self.c_letter = 'O'
		else:
			self.c_letter = 'X'

		self.draw_board()
		self.hp = HumanPlayer(self)
		self.mcp = MinimaxComputerPlayer(self)

	def draw_board(self):
		"""
		Prints out the current board state.
		"""
		print('\n')
		for i in [0, 3, 6]:
			print("\t\t\t %s | %s | %s \n" %(self.board_data[i], self.board_data[i + 1], self.board_data[i + 2]))

	def available_moves(self):
		"""
		Returns an array of all available moves in the current board state.
		"""
		return [i for i, space in enumerate(self.board_data) if space == '-']

	def is_winner(self, letter):
		"""
		Checks if letter (either 'X' or 'O') has won the game.
		"""
		# Check for three in a row.
		for i in [0, 3, 6]:
			if self.board_data[i] == letter and self.board_data[i + 1] == letter and self.board_data[i + 2] == letter:
				return True
		
		# Check for three in a column.
		for i in range(3):
			if self.board_data[i] == letter and self.board_data[i + 3] == letter and self.board_data[i + 6] == letter:
				return True

		# Check for three in a diagonal.
		if self.board_data[0] == letter and self.board_data[4] == letter and self.board_data[8] == letter:
			return True

		if self.board_data[2] == letter and self.board_data[4] == letter and self.board_data[6] == letter:
			return True

		# Return False if no three in a row, column, or diagonal are the same.
		return False

	def play(self):
		while len(self.available_moves()) != 0: 
			if self.next_turn == 'X':
				if self.h_letter == 'X':
					self.hp.next_move()	
					self.draw_board()
					if self.is_winner('X'):
						print("X is the winner.")
						exit()
					self.next_turn = 'O'
				else:
					self.mcp.next_move()
					self.draw_board()	
					if self.is_winner('X'):
						print("X is the winner.")
						exit()
					self.next_turn = 'O'
			else:
				if self.h_letter == 'O':
					self.hp.next_move()	
					self.draw_board()
					if self.is_winner('O'):
						print("O is the winner.")
						exit()
					self.next_turn = 'X'
				else:
					self.mcp.next_move()	
					self.draw_board()
					if self.is_winner('O'):
						print("O is the winner.")
						exit()
					self.next_turn = 'X'
		print("X and O tie.")
