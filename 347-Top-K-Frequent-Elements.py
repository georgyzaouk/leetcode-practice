
import heapq

def topKFrequent_dict(nums: list[int], k: int) -> list[int]:

    freq = {}
    res = []

    for i in range(len(nums)):

        if nums[i] in freq:
            freq[nums[i]] = freq[nums[i]] + 1
        else:
            freq[nums[i]] = 1

    while k > 0:

        max_key = max(freq, key=freq.get)
        res.append(max_key)
        freq[max_key] = 0
        k -= 1

    return res


def topKFrequent_heap(nums: list[int], k: int) -> list[int]:

    freq = {}
    heap = []    # define res as a heap with element with max frequency at the top
    res = []

    # find each element's frequency and store it in a dictionary
    for i in range(len(nums)):

        if nums[i] in freq:
            freq[nums[i]] = freq[nums[i]] + 1
        else:
            freq[nums[i]] = 1

    # go over the frequency dictionary and push each element into the heap
    for key, value in freq.items():
        heapq.heappush(heap, (-value, key))

        # keep the heap size to k
        if len(heap) == k:
            break

    # pop the top k elements from the heap and append them to the result list
    while k > 0:
        res.append(heapq.heappop(heap)[1])
        k -= 1
        
    return res


def topKFrequent(nums: list[int], k: int) -> list[int]:
    # using bucket sort to find the top k frequent elements
    freq = {}
    buckets = [[] for _ in range(len(nums) + 1)] # bucket list can have at most len(nums) + 1 buckets, since the maximum frequency of any element can be len(nums)

    # compute the frequency of each element in the input list
    for i in range(len(nums)):
        if nums[i] in freq:
            freq[nums[i]] = freq[nums[i]] + 1
        else:
            freq[nums[i]] = 1

    # scatter / distribute the elements into buckets based on their frequency
    for key, value in freq.items():
        # index of the bucket is the frequency of the element, 
        # and the value is the list of elements with that frequency
        buckets[value].append(key)

    # collect the top k frequent elements from the buckets 
    # going in descending order of frequency (higheset to lowest)
    res = []
    for i in range(len(buckets) - 1, 0, -1):
        for num in buckets[i]:
            res.append(num)
            if len(res) == k:
                return res

    

if __name__ == "__main__":

    # test case 1
    nums = [1,1,1,2,2,3]
    k = 2
    print(topKFrequent(nums, k))

    # test case 2
    nums = [1]
    k = 1
    print(topKFrequent(nums, k))

    # test case 3
    nums = [1,2,1,2,1,2,3,1,3,2]
    k = 2
    print(topKFrequent(nums, k))
