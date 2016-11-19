#coding:utf8

# Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.
#
# How many such routes are there through a 20×20 grid?

def getNextPos(x,y):
    positions = []
    nextX = x + 1
    nextY = y + 1
    if nextX <= MAX_X:
        positions.append((nextX,y))
    if nextY <= MAX_Y:
        positions.append((x,nextY))
    return positions

MAX_X = 20
MAX_Y = 20

matrix = [[0 for col in range(MAX_X+1)] for row in range(MAX_Y+1)]
x = MAX_X
y = MAX_Y
for x in range(MAX_X,-1,-1):
    for y in range(MAX_Y, -1, -1):
        paths = 0
        positions = getNextPos(x,y)
        if len(positions) == 0:
            paths = 1
        else:
            for pos in positions:
                paths += matrix[pos[0]][pos[1]]
        matrix[x][y] = paths

print matrix[0][0]

# for x in range(MAX_Y+1):
#     for y in range(MAX_X+1):
#         print matrix[x][y],
#     print "\n"

