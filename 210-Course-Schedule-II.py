
from collections import deque


def findOrder(numCourses: int, prerequisites: list[list[int]]) -> list[int]:

    # build the adjacency list from the prerequisites list
    adj_list = {}
    for course, prereq in prerequisites:
        if prereq not in adj_list:
            adj_list[prereq] = []
        adj_list[prereq].append(course)

    # use Kahn's algorithm to perform topological sorting
    def topoSort(adj, numCourses):
        n = numCourses
        indegree = [0] * n
        res = []
        queue = deque()

        # Compute indegrees
        for i in range(n):
            for next_node in adj.get(i, []):
                indegree[next_node] += 1
                
        # Add all nodes with indegree 0 into the queue
        for i in range(n):
            if indegree[i] == 0:
                queue.append(i)

        # Kahn’s Algorithm
        while queue:
            top = queue.popleft()
            res.append(top)

            for next_node in adj.get(top, []):
                indegree[next_node] -= 1
                if indegree[next_node] == 0:
                    queue.append(next_node)

        return res

    # Check if the topological sort result has the same number of courses as numCourses
    if len(topoSort(adj_list, numCourses)) != numCourses:
       return []
    
    res = topoSort(adj_list, numCourses)
    return res


if __name__ == "__main__":

    # test case 1
    numCourses = 2
    prerequisites = [[1,0]]
    print(findOrder(numCourses, prerequisites))     # [0,1]

    # test case 2
    numCourses = 4
    prerequisites = [[1,0],[2,0],[3,1],[3,2]]
    print(findOrder(numCourses, prerequisites))     # Output: [0,2,1,3] or [0,1,2,3]

    # test case 3
    numCourses = 1
    prerequisites = []
    print(findOrder(numCourses, prerequisites))     # Output: [0]