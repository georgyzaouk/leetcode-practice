
def orangesRotting(grid: list[list[int]]) -> int:

    # build a binary undirected (unweighted) graph
    # return the depth of it (most efficient using BFS)

    rows = len(grid)
    cols = len(grid[0])

    directions = [
        (-1, 0),  # up
        (1, 0),   # down
        (0, -1),  # left
        (0, 1),   # right
    ]

    def is_valid(row: int, col: int) -> bool:
        """Check whether a cell can be visited by BFS."""

        # The coordinates must be inside the grid
        if row < 0 or row >= rows or col < 0 or col >= cols:
            return False

        # The cell must not have been explored already
        if visited[row][col]:
            return False

        # BFS should only move through fresh oranges
        if grid[row][col] != 1:
            return False

        return True

    # bfs needs to start from every rotten orange in the queue simultaneously
    # multi-source BFS is the most efficient way to do this

    # This array stores the distances of the vertices
    # from the nearest source
    dist = [[0] * cols for _ in range(rows)]

    # This boolean array is true if the current vertex
    # is visited otherwise it is false
    visited = [[False] * cols for _ in range(rows)]
    
    # Multisource BFS Function
    def Multisource_BFS(q):
        while q:
            row, col = q.pop(0)

            for dr, dc in directions:
                new_row = row + dr
                new_col = col + dc

                if is_valid(new_row, new_col):
                    # Pushing the adjacent unvisited vertices
                    # with distance from current source 
                    # = this vertex's distance + 1
                    q.append((new_row, new_col))
                    visited[new_row][new_col] = True
                    dist[new_row][new_col] = dist[row][col] + 1

    # the propagation should start simultaneously from every rotten orange in the grid
    # scan the grid and put all initial rotten oranges into the queue
    sources = []
    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == 2:
                sources.append((row, col))
                visited[row][col] = True

    # we then need to calculate the distance of each
    # vertex from nearest source and returns the maximum distance
    
    # Create a queue for BFS
    q = []

    # Mark all the source vertices as visited and enqueue it
    for i in range(len(sources)):
        q.append(sources[i])
        visited[sources[i][0]][sources[i][1]] = True

    Multisource_BFS(q)

    # if there is a fresh orange that is not rotten, return -1
    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == 1 and not visited[row][col]:
                return -1

    # if all oranges are rotten, return the maximum distance
    # = number of minutes taken to rot all oranges
    max_dist = 0
    for row in dist:
        for distance in row:
            if distance > max_dist:
                max_dist = distance
    return max_dist


if __name__ == "__main__":
    
    # test case 1
    grid = [
        [2,1,1],
        [1,1,0],
        [0,1,1]
    ]
    print(orangesRotting(grid))  # Output: 4

    # test case 2
    grid = [
        [2,1,1],
        [0,1,1],
        [1,0,1]
    ]
    print(orangesRotting(grid))  # Output: -1

    # test case 3
    grid = [
        [0,2]
    ]
    print(orangesRotting(grid))  # Output: 0
   
    


