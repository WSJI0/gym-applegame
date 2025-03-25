import numpy as np
import random

class Board:
    def __init__(self):
        self.width = 17
        self.height = 10
        self.board = np.zeros((17, 10))
        
        self.init_board()


    def init_board(self):
        '''
        Fills the game board with random numbers from 1 to 9.

        Args:
            None

        Returns:
            None
        '''

        for y in self.height:
            for x in self.width:
                self.board[y][x] = random.randint(1, 9)


    def check(self, y1, x1, y2, x2):
        '''
        Sum of numbers within a given space

        Args:
            y1 (int): start pos y
            x1 (int): start pos x
            y2 (int): end pos y
            x2 (int): end pos x

        Returns:
            int: Sum of given space

        '''

        if y1 < 0 or x1 < 0 or y1 >= self.height or x1 >= self.width:
            return 0
        if y2 < 0 or x2 < 0 or y2 >= self.height or x2 >= self.width:
            return 0

        res = 0
        for y in range(y1, y2 + 1):
            for x in range(x1, x2 + 1):
                res += self.board[y][x]

        return res


    def remove(self, y1, x1, y2, x2):
        '''
        Removes the selected space if the sum of the given space is 10.

        Args:
            y1 (int): start pos y
            x1 (int): start pos x
            y2 (int): end pos y
            x2 (int): end pos x

        Returns:
            int: Number of apples removed
        '''
        
        apples = 0
        if self.check(y1, x1, y2, x2) == 10:
            for y in range(y1, y2 + 1):
                for x in range(x1, x2 + 1):
                    if self.board[y][x] != 0:
                        apples += 1
                        self.board[y][x] = 0
            return apples
        
        return 0
