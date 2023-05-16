from generator import *

# Screen dimensions
WIDTH = 800
HEIGHT = 800

# Board dimensions
ROWS = 8
COLS = 8
SQSIZE = WIDTH // COLS

# Neat params
GENERATIONS = 300

# Stockfish params
DEPTH = 15

# CodeMaps
MOVEMAP = generate_codes()
