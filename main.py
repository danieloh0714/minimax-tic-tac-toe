from Board.Board import TerminalBoard
from Player.Player import HumanPlayer
from Player.Player import MinimaxComputerPlayer

board_data = ['-', '-', '-', '-', '-', '-', '-', '-', '-']
board = TerminalBoard(board_data)

board.play()
