def create_move_string(square_index, move_instruction):
    square_name = index_to_square_converter(square_index)

    letter = square_name[0]
    number = int(square_name[1])

    second_direction = None

    direction = move_instruction[1]
    if not move_instruction[0] == 'knight':
        amount = int(move_instruction[0])
    else:
        amount = [2, 1]
        second_direction = move_instruction[2]

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
        if direction == 'N' and second_direction == 'E':
            number += amount[0]
            letter = chr(ord(letter) + amount[1])

        elif direction == 'N' and second_direction == 'W':
            number += amount[0]
            letter = chr(ord(letter) - amount[1])

        elif direction == 'E' and second_direction == 'N':
            number += amount[1]
            letter = chr(ord(letter) + amount[0])

        elif direction == 'E' and second_direction == 'S':
            number -= amount[1]
            letter = chr(ord(letter) + amount[0])

        elif direction == 'S' and second_direction == 'E':
            number -= amount[0]
            letter = chr(ord(letter) + amount[1])

        elif direction == 'S' and second_direction == 'W':
            number -= amount[0]
            letter = chr(ord(letter) - amount[1])

        elif direction == 'W' and second_direction == 'N':
            number += amount[1]
            letter = chr(ord(letter) - amount[0])

        elif direction == 'W' and second_direction == 'S':
            number -= amount[1]
            letter = chr(ord(letter) - amount[0])


    destination_square = letter + str(number)
    move = square_name + destination_square

    return move


def index_to_square_converter(index):
    file = index % 8
    rank = (index // 8)+1
    file_letter = chr(file + ord('a'))
    return file_letter + str(rank)
