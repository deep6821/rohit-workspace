"""
Flood fill Algorithm – how to implement fill() in paint?

In MS-Paint, when we take the brush to a pixel and click, the color of the region of that pixel is replaced with a new
selected color. Following is the problem statement to do this task.

Given a 2D screen, location of a pixel in the screen and a color, replace color of the given pixel and all adjacent same
colored pixels with the given color.

Input:
       screen[M][N] = {{1, 1, 1, 1, 1, 1, 1, 1},
                      {1, 1, 1, 1, 1, 1, 0, 0},
                      {1, 0, 0, 1, 1, 0, 1, 1},
                      {1, 2, 2, 2, 2, 0, 1, 0},
                      {1, 1, 1, 2, 2, 0, 1, 0},
                      {1, 1, 1, 2, 2, 2, 2, 0},
                      {1, 1, 1, 1, 1, 2, 1, 1},
                      {1, 1, 1, 1, 1, 2, 2, 1},
                      };
        x = 4, y = 4, newColor = 3

The values in the given 2D screen indicate colors of the pixels. x and y are coordinates of the brush,
newColor is the color that should replace the previous color on screen[x][y] and all surrounding pixels with same color.
"""

# Dimentions of paint screen
M = 8
N = 8


def flood_fill_util(screen, x, y, prevC, newC):
    # Base cases
    if x < 0 or x >= M or y < 0 or y >= N or screen[x][y] != prevC or screen[x][y] == newC:
        return

    # Replace the color at (x, y)
    screen[x][y] = newC

    # Recur for north, east, south and west
    flood_fill_util(screen, x + 1, y, prevC, newC)
    flood_fill_util(screen, x - 1, y, prevC, newC)
    flood_fill_util(screen, x, y + 1, prevC, newC)
    flood_fill_util(screen, x, y - 1, prevC, newC)


# It mainly finds the previous color on (x, y) and
# calls floodFillUtil()
def flood_fill(screen, x, y, new_color):
    prev_color = screen[x][y]
    print(prev_color)
    flood_fill_util(screen, x, y, prev_color, new_color)


# Driver Code
screen = [[1, 1, 1, 1, 1, 1, 1, 1],
          [1, 1, 1, 1, 1, 1, 0, 0],
          [1, 0, 0, 1, 1, 0, 1, 1],
          [1, 2, 2, 2, 2, 0, 1, 0],
          [1, 1, 1, 2, 2, 0, 1, 0],
          [1, 1, 1, 2, 2, 2, 2, 0],
          [1, 1, 1, 1, 1, 2, 1, 1],
          [1, 1, 1, 1, 1, 2, 2, 1]]

x = 4
y = 4
new_color = 3
flood_fill(screen, x, y, new_color)

print("Updated screen after call to floodFill:")
for i in range(M):
    for j in range(N):
        print(screen[i][j], end=' ')
    print()

