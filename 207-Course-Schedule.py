
from collections import deque


def canFinish(numCourses: int, prerequisites: list[list[int]]) -> bool:

    # prerequisites is a list of pairs [a, b] where b is a prerequisite for a
    # we can represent the courses and their prerequisites as a directed graph
    # use the prerequisites list as an edges list 
    # and create an adjacency list from it
    
    adj_list = {}
    for course, prereq in prerequisites:
        if course not in adj_list:
            adj_list[course] = []
        adj_list[course].append(prereq)

    # traverse the graph using DFS
    # check for cycles in the graph, if a cycle is detected, return False 

    def dfs(course, visited, rec_stack):
        if course in rec_stack:
            return False  # cycle detected
        if course in visited:
            return True  # already visited

        visited.add(course)
        rec_stack.add(course)

        for prereq in adj_list.get(course, []):
            if not dfs(prereq, visited, rec_stack):
                return False

        rec_stack.remove(course)
        return True

    # Start DFS from every course because the graph
    # may contain disconnected components.
    visited = set()
    for course in range(numCourses):
        if course not in visited:
            if not dfs(course, visited, set()):
                return False
    
    return True


def canFinishKahns(numCourses: int, prerequisites: list[list[int]]) -> bool:
    '''
    Another approach is to use Kahn's algorithm for topological sorting using BFS.

    '''

    # build the adjacency list from the prerequisites list
    adj_list = {}
    for course, prereq in prerequisites:
        if course not in adj_list:
            adj_list[course] = []
        adj_list[course].append(prereq)

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
        return False
    
    return True


if __name__ == "__main__":

    # test case 1
    numCourses = 2
    prerequisites = [[1, 0]]
    print(f"canFinish: {canFinish(numCourses, prerequisites)}")  # Output: True
    print(f"canFinishKahns: {canFinishKahns(numCourses, prerequisites)}\n")  # Output: True

    # test case 2
    numCourses = 2
    prerequisites = [[1, 0], [0, 1]]
    print(f"canFinish: {canFinish(numCourses, prerequisites)}")  # Output: False
    print(f"canFinishKahns: {canFinishKahns(numCourses, prerequisites)}\n")  # Output: False

    # test case 3
    numCourses = 4
    prerequisites = [[1, 0], [2, 1], [3, 2]]
    print(f"canFinish: {canFinish(numCourses, prerequisites)}")  # Output: True
    print(f"canFinishKahns: {canFinishKahns(numCourses, prerequisites)}\n")  # Output: True





        