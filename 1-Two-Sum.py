
def twoSum_Naive(nums, target):
    S = []
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                S.append(i)
                S.append(j)
                return S
    return -1

def twoSum(nums, target):
    num_map = {}
    for i in range(len(nums)):
        comp = target - nums[i]
        if comp in num_map:
            return [num_map[comp], i]
        num_map[nums[i]] = i


if __name__ == "__main__":

    # test case 1
    nums1 = [2,7,11,15]
    target1 = 9
    print(twoSum(nums1, target1))

    # test case 2
    nums2 = [3,2,4]
    target2 = 6
    print(twoSum(nums2, target2))

    # test case 3
    nums3 = [3,3]
    target3 = 6
    print(twoSum(nums3, target3))