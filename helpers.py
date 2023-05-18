

def create_move(initial_square, increments):

    letter = initial_square[0]
    number = initial_square[1]

    direction = increments[1]
    amount = increments[0]
    final_square = ''


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
        print('Move a fucking knight')

    destination_square = letter+number
    move = initial_square+destination_square

    return move