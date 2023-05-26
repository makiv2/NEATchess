import chess.engine


class Stockfish:
    engine = None

    def __init__(self):
        self.engine = chess.engine.SimpleEngine.popen_uci("stockfish")

    def get_best_move(self, board):
        result = self.engine.play(board, chess.engine.Limit(time=0.1))
        return result.move

    def __del__(self):
        self.engine.quit()

