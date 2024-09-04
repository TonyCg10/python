class Pawn:
    W_DIRECTION = -1
    B_DIRECTION = 1

    def __init__(self, is_white, color):
        self.first_move = True
        self.is_white = is_white
        self.color = color

    def validate_move(self, start_row, start_col, target_row, target_col, piece):
        direction = self.direction()

        if self.first_move and target_row == start_row + 2 * direction and target_col == start_col and not piece:
            self.first_move = False
            return True
        if target_row == start_row + direction and target_col == start_col and not piece:
            self.first_move = False
            return True
        if target_row == start_row + direction and abs(target_col - start_col) == 1 and piece:
            if self.color == 'w' and self.is_white or self.color == 'b' and not self.is_white:
                return False
            self.first_move = False
            return True
        return False

    def direction(self):
        return self.W_DIRECTION if self.is_white else self.B_DIRECTION
