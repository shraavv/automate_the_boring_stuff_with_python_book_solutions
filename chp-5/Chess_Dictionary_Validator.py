def isValidChessBoard(key_values):
    alph = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    for i in key_values.keys():
        if int(i[0]) > 8 or i[1] not in alph:
            return 0

    piece = ['pawn', 'knight', 'bishop', 'rook', 'queen', 'king']
    for j in key_values.values():
        color, piece_type = j[0], j[1:]
        if color not in ['b', 'w'] or piece_type not in piece:
            return 0

    return 1

key_values = {'1h': 'bking', '6c': 'wqueen', '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking'}
x = isValidChessBoard(key_values)

if x == 0:
    print("Chess board is invalid")
elif x == 1:
    print("Chess board is valid")
