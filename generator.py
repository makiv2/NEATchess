def generate_codes():
    codes, i = {}, 0

    # Add all possible moves for each piece. (except knights)
    for nSquares in range(1, 8):
        for direction in ["N", "NE", "E", "SE", "S", "SW", "W", "NW"]:
            codes[(nSquares, direction)] = i
            i += 1

    # Add knight possible moves.
    for two in ["N", "S"]:
        for one in ["E", "W"]:
            codes[("knight", two, one)], i = i, i + 1
    for two in ["E", "W"]:
        for one in ["N", "S"]:
            codes[("knight", two, one)], i = i, i + 1

    # https://ai.stackexchange.com/questions/27336/how-does-the-alpha-zeros-move-encoding-work
    # for move in ["N", "NW", "NE"]:
    #     for promote_to in ["Rook", "Knight", "Bishop"]:
    #         codes[("underpromotion", move, promote_to)], i = i, i + 1

    return codes
