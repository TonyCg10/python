class Rook:

    def validate_move(self, start_row, start_col, target_row, target_col, piece):
        if target_row == start_row or target_col == start_col:
            if piece:
                return False

            return True

        return False
