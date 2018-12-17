class SnakeGame(object):

    def __init__(self, width, height, food):
        """
        Initialize your data structure here.
        @param width - screen width
        @param height - screen height
        @param food - A list of food positions
        E.g food = [[1,1], [1,0]] means the first food is positioned at [1,1], the second is at [1,0].
        :type width: int
        :type height: int
        :type food: List[List[int]]
        """
        self.border = (height, width)
        self.body = [(0, 0)]
        self.food = food
        self.dirs = {'U': (-1, 0), 'D': (1, 0), 'L': (0, -1), 'R': (0, 1)}
        self.score = 0

    class GameOverException(Exception):
        def __init__(self, msg):
            self.msg = msg

    def move(self, direction):
        """
        Moves the snake.
        @param direction - 'U' = Up, 'L' = Left, 'R' = Right, 'D' = Down
        @return The game's score after the move. Return -1 if game over.
        Game over when snake crosses the screen boundary or bites its body.
        :type direction: str
        :rtype: int
        """
        try:
            self.addHead(direction)
            self.getReward()
            self.removeTail()
        except SnakeGame.GameOverException:
            return -1
        else:
            return self.score

    def addHead(self, direction):
        ny, nx = self.getNextHeadPos(direction)
        dy, dx = self.dirs[direction]
        ny, nx = self.body[-1][0] + dy, self.body[-1][1] + dx
        self.checkValid(ny, nx)
        self.body.append((ny, nx))

    def removeTail(self):
        if not self.gotFood:
            self.body.pop(0)

    def checkValid(self, y, x):
        if 0 <= y < self.border[0] and 0 <= x < self.border[1] and (y, x) not in self.body[1:]:
            pass
        else:
            raise SnakeGame.GameOverException("GameOver")

    def getReward(self):
        # print
        y, x = self.body[-1]
        self.gotFood = False
        if self.food and [y, x] == self.food[0]:
            self.score += 1
            self.food.pop(0)
            self.gotFood = True

    def getNextHeadPos(self, direction):
        ny = self.body[-1][0] + self.dirs[direction][0]
        nx = self.body[-1][1] + self.dirs[direction][1]
        return ny, nx
# Your SnakeGame object will be instantiated and called as such:
# obj = SnakeGame(width, height, food)
# param_1 = obj.move(direction)