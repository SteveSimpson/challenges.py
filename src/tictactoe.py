import math

class TicTacToe:
    def __init__(self, size: int):
        self.empty_value = -1

        if size < 3:
            raise ValueError("Must have board size of 3x3 or bigger")
        
        # is the size odd or even?
        if size/2 == math.floor(size/2):
            raise ValueError("Board size must be odd")

        self.last_player = -1 # init to a non-player number value, don't really care who starts or if index is 0 or 1 based
        self.size = size

        # use with [column][row] so we can just call [x][y]
        self.state = [[self.empty_value for _ in range(size)] for _ in range(size)] 

    def testWin(self, x: int, y: int, player: int):
        winCol = 1
        winRow = 1
        winDia1 = 1
        winDia2 = 1

        for i in range(self.size):
            # test column
            if self.state[x][i] != player:
                winCol = 0
            
            # test row
            if self.state[i][y] != player:
                winRow = 0

            # test Diag 1
            if self.state[i][i] != player:
                winDia1 = 0

            if self.state[self.size - i -1][i] != player:
                winDia2 = 0

        if (winCol  + winRow + winDia1 + winDia2) > 0:
            return True
            
        return False


    def move(self, x, y, player):
        if self.state[x][y] != self.empty_value:
            # could just be a double click... not worth raising an error
            print("Warning: that space was already taken")
            return False

        if player == self.last_player:
            raise ValueError("Not your turn")
        
        self.last_player = player

        self.state[x][y] = player

        return self.testWin(x,y,player)


game = TicTacToe(3)

print(game.move(0, 0, 1)) # false
print(game.move(0, 1, 2)) # false
print(game.move(1, 1, 1)) # false
print(game.move(0, 2, 2)) # false
print(game.move(2, 2, 1)) # true (player 1 wins)

try:
    game = TicTacToe(2)
except ValueError as e:
    print (f"PASS: {e}") # too small

try:
    game = TicTacToe(4)
except ValueError as e:
    print (f"PASS: {e}") # must be odd

game = TicTacToe(5)
print(game.move(0, 0, 1)) # false
try:
    print(game.move(0, 0, 1)) # duplicate move should generate a warning and just return false
    print(game.move(1,1,1)) # cheater - game should raise a typeerror
except ValueError as e:
    print (f"PASS: {e}") # 2 moves from the same player


