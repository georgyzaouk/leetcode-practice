
def merge(intervals: list[list[int]]) -> list[list[int]]:

    # Sort intervals based on start values
    intervals.sort()

    res = []
    res.append(intervals[0])

    for i in range(1, len(intervals)):
        last = res[-1]
        curr = intervals[i]

        # If current interval overlaps with the last merged interval, merge them 
        if curr[0] <= last[1]:
            last[1] = max(last[1], curr[1])
        else:
            res.append(curr)

    return res


if __name__ == "__main__":

    # test case 1
    intervals = [[1,3],[2,6],[8,10],[15,18]]
    print(merge(intervals))  # Output: [[1,6],[8,10],[15,18]]

    # test case 2
    intervals = [[1,4],[4,5]]
    print(merge(intervals))  # Output: [[1,5]]

    # test case 3
    intervals = [[4,7],[1,4]]
    print(merge(intervals))  # Output: [[1,7]]