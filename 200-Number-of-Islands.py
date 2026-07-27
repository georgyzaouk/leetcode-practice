
def numIslands(grid: list[list[str]]) -> int:
    if not grid:
        return 0

    rows = len(grid)
    cols = len(grid[0])

    visited = [[False] * cols for _ in range(rows)]

    directions = [
        (-1, 0),  # up
        (1, 0),   # down
        (0, -1),  # left
        (0, 1),   # right
    ]

    def is_valid(row: int, col: int) -> bool:
        """Check whether a cell can be visited by DFS."""

        # The coordinates must be inside the grid
        if row < 0 or row >= rows or col < 0 or col >= cols:
            return False

        # The cell must not have been explored already
        if visited[row][col]:
            return False

        # DFS should only move through land cells
        if grid[row][col] != "1":
            return False

        return True
    
    def dfs(start_row: int, start_col: int) -> None:
        """Visit all land cells connected to the starting cell."""

        # The stack stores cells that still need to be explored
        stack = [(start_row, start_col)]

        # Mark cells when they enter the stack so they are not added twice
        visited[start_row][start_col] = True

        while stack:
            row, col = stack.pop()

            # Check the four neighbouring cells
            for dr, dc in directions:
                new_row = row + dr
                new_col = col + dc

                if is_valid(new_row, new_col):
                    visited[new_row][new_col] = True
                    stack.append((new_row, new_col))

    number_of_islands = 0

    # Search the entire grid for unvisited land cells
    for row in range(rows):
        for col in range(cols):
            if is_valid(row, col):
                # An unvisited land cell starts a new island
                number_of_islands += 1

                # Mark every cell belonging to this island
                dfs(row, col)

    return number_of_islands


if __name__ == "__main__":

    # test case 1
    grid = [
        ["1","1","1","1","0"],
        ["1","1","0","1","0"],
        ["1","1","0","0","0"],
        ["0","0","0","0","0"]
    ]
    print(numIslands(grid))  # Output: 1

    # test case 2
    grid = [
        ["1","1","0","0","0"],
        ["1","1","0","0","0"],
        ["0","0","1","0","0"],
        ["0","0","0","1","1"]
    ]
    print(numIslands(grid))  # Output: 3