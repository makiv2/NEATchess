import chess.engine
import neat

from bitboard import board_to_3vector
from decoder import *
from helpers import *
from chessboard import display
from time import sleep


def train_ai(genome1, genome2, config):
    # Create the neural networks
    net1 = neat.nn.FeedForwardNetwork.create(genome1, config)
    net2 = neat.nn.FeedForwardNetwork.create(genome2, config)

    # Create the chess board
    print('creating board')
    board = chess.Board()

    board_display = display.start(board.fen())

    input('press enter to continue')

    # Play the game
    while not board.is_game_over():

        board_vector = board_to_3vector(board)

        if board.turn == chess.WHITE:

            # Get output for the white pieces
            output = net1.activate(board_vector)

            # Get moves
            moves = get_moves(output)

            # Find a valid move
            move = find_valid_move(board, moves)

            make_move(board, move)

            display.update(board.fen(), board_display)
            sleep(1)
            print('white MOVE MADE')
            print(board)
        else:
            # Get output for the white pieces
            output = net2.activate(board_vector)

            # Get moves
            moves = get_moves(output)

            # Find a valid move
            move = find_valid_move(board, moves)

            make_move(board, move)

            print('black MOVE MADE')
            print(board)
            display.update(board.fen(), board_display)
            sleep(1)

        # Get the legal moves for the current player
        legal_moves = list(board.legal_moves)

        # If there are no legal moves, the game is over
        if len(legal_moves) == 0:
            display.terminate()
            break

    # Return the winner
    # Update the fitness of the genomes


def evaluate_pick_up_square_probabilities(board, priorities, genome):
    for i in priorities:
        if board.piece_at(i) and board.piece_at(i).color == board.turn:
            return i
        else:
            genome.fitness -= 1


# def get_move_type(data):
#     moves_to_make = []
#     move_type_probabilities = get_move_type_probability(data)
#     indexes_to_which_move_in_move_map = sorted(range(len(move_type_probabilities)),
#                                                key=lambda i: move_type_probabilities[i], reverse=True)
#
#     print(MOVEMAP)  # map index to movemap
#
#     return indexes_to_which_move_in_move_map


def simple_fitness_eval(board, genome1, genome2):
    if board.is_checkmate:
        if board.turn == chess.BLACK:
            genome1.fitness *= 1.5
            genome2.fitness *= 0.8
        else:
            genome1.fitness *= 1.5
            genome2.fitness *= 0.8


def is_move_legal(board, move_obj):
    if move_obj in board.legal_moves:
        return True
    else:
        return False


def find_valid_move(board, moves):
    for square_index, move_instruction in moves:
        # LOG the failed moves to fitness
        move_string = create_move_string(square_index, move_instruction)

        # Check string validity
        if not check_string_validity(move_string):
            continue
        # Create move object
        move_obj = create_move_object(move_string)
        # Make legal move object

        if is_move_legal(board, move_obj):
            print('Move is legal and valid', move_obj)
            return move_obj

    print('No valid move found')


def create_move_object(move):
    return chess.Move.from_uci(move)


def make_move(board, move):
    board.push(move)


def check_string_validity(move_string):
    letter = move_string[2]
    number = move_string[3]

    if letter in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'] and number in ['1', '2', '3', '4', '5', '6', '7',
                                                                         '8'] and len(move_string) == 4:
        return True
    else:
        return False
