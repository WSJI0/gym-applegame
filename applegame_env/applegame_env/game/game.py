import board

class Game:
    def __init__(self):
        self.board = board.Board()

    
    def drag(self, y1, x1, y2, x2):
        '''
        Drag the given space

        Args:
            y1 (int): start pos y
            x1 (int): start pos x
            y2 (int): end pos y
            x2 (int): end pos x

        Returns:
            int: Number of removed apples
        '''
        
        if y1 > y2:
            y1, y2 = y2, y1
        if x1 > x2:
            x1, x2 = x2, x1

        return self.board.remove(y1, x1, y2, x2)
