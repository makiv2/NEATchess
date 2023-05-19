def create_move_string(initial_square_index, increments):
    square_name = index_to_square_converter(initial_square_index)

    letter = square_name[0]
    number = int(square_name[1])

    direction = increments[1]
    amount = int(increments[0])

    if isinstance(amount, int):
        if direction == 'N':
            number += amount

        elif direction == 'NE':
            number += amount
            letter = chr(ord(letter) + amount)

        elif direction == 'E':
            letter = chr(ord(letter) + amount)

        elif direction == 'SE':
            number -= amount
            letter = chr(ord(letter) + amount)

        elif direction == 'S':
            number -= amount

        elif direction == 'SW':
            number -= amount
            letter = chr(ord(letter) - amount)

        elif direction == 'W':
            letter = chr(ord(letter) - amount)

        elif direction == 'NW':
            number += amount
            letter = chr(ord(letter) - amount)

        else:
            print('Move a knight')

    destination_square = letter + str(number)
    move = square_name + destination_square

    return move


def index_to_square_converter(index):
    file = index % 8
    rank = 8 - index // 8
    file_letter = chr(file + ord('a'))
    return file_letter + str(rank)
