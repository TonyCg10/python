from PyQt5.QtGui import QPixmap
from movi_piezas.torre import Rook
from movimientos import Move
from movi_piezas.peon import Pawn


class Piece_Logic:
    @staticmethod
    def crear_pieza(piece_name, piece_row, piece_col):
        square_size = 80
        pixmap = QPixmap(f'ajedrez/assets/pieces-svg/{piece_name}')

        if 'pawn' in piece_name:
            piece_logic = Pawn('pawn-w' in piece_name, piece_name[-1])
        elif 'rook' in piece_name:
            piece_logic = Rook()
        else:
            piece_logic = None

        piece = Move(
            pixmap, piece_col * square_size, piece_row * square_size, piece_name, piece_logic)
        piece.setScale(square_size / pixmap.width())
        piece.setPos(piece_col * square_size + (square_size - pixmap.width() * piece.scale()) / 2,
                     piece_row * square_size + (square_size - pixmap.height() * piece.scale()) / 2)
        piece.setData(0, {"chess_piece": piece_name})

        return piece


class Pieces:
    def __init__(self):
        super().__init__()

    def add_pieces(self, scene):
        pieces = [
            ("rook-b", 0, 0), ("knight-b", 0,
                               1), ("bishop-b", 0, 2), ("queen-b", 0, 3),
            ("king-b", 0, 4), ("bishop-b", 0,
                               5), ("knight-b", 0, 6), ("rook-b", 0, 7),
            ("pawn-b", 1, 0), ("pawn-b", 1, 1), ("pawn-b", 1, 2), ("pawn-b", 1, 3),
            ("pawn-b", 1, 4), ("pawn-b", 1, 5), ("pawn-b", 1, 6), ("pawn-b", 1, 7),
            ("rook-w", 7, 0), ("knight-w", 7,
                               1), ("bishop-w", 7, 2), ("queen-w", 7, 3),
            ("king-w", 7, 4), ("bishop-w", 7,
                               5), ("knight-w", 7, 6), ("rook-w", 7, 7),
            ("pawn-w", 6, 0), ("pawn-w", 6, 1), ("pawn-w", 6, 2), ("pawn-w", 6, 3),
            ("pawn-w", 6, 4), ("pawn-w", 6, 5), ("pawn-w", 6, 6), ("pawn-w", 6, 7),
        ]

        for piece_name, piece_row, piece_col in pieces:
            piece = Piece_Logic.crear_pieza(piece_name, piece_row, piece_col)
            if piece:
                scene.addItem(piece)
