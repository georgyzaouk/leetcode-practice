
def floodFill(image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:

    rows = len(image)
    cols = len(image[0])
    original_color = image[sr][sc]

    visited = [[False] * cols for _ in range(rows)]

    directions = [
        (-1, 0),  # up
        (1, 0),   # down
        (0, -1),  # left
        (0, 1),   # right
    ]

    def is_valid(row: int, col: int) -> bool:
        """Check whether a pixel can be visited by DFS."""

        # The coordinates must be inside the grid
        if row < 0 or row >= rows or col < 0 or col >= cols:
            return False

        # The pixel must not have been explored already
        if visited[row][col]:
            return False

        # DFS should only move through pixels of the same color as the original
        if image[row][col] != original_color:
            return False

        return True
    
    def dfs(start_row: int, start_col: int) -> None:
        """Visit all pixels connected to the starting pixel with the same original color."""

        # The stack stores pixels that still need to be explored
        stack = [(start_row, start_col)]

        # Mark pixels when they enter the stack so they are not added twice
        visited[start_row][start_col] = True

        while stack:
            row, col = stack.pop()

            # Check the four neighbouring pixels
            for dr, dc in directions:
                new_row = row + dr
                new_col = col + dc

                if is_valid(new_row, new_col):
                    visited[new_row][new_col] = True
                    stack.append((new_row, new_col))


    # Go through the dfs graph starting from image[sr][sc] 
    # and change the colors of visited pixels to the new color
    dfs(sr, sc)

    modified_image = [[image[row][col] for col in range(cols)] for row in range(rows)]
    for row in range(rows):
        for col in range(cols):
            if visited[row][col]:
                modified_image[row][col] = color

    return modified_image


if __name__ == "__main__":
    # test case 1
    image = [[1,1,1],[1,1,0],[1,0,1]]
    sr = 1
    sc = 1
    color = 2
    result = floodFill(image, sr, sc, color)
    print(result)

    # test case 2
    image = [[0,0,0],[0,0,0]]
    sr = 0
    sc = 0
    color = 0
    result = floodFill(image, sr, sc, color)
    print(result)