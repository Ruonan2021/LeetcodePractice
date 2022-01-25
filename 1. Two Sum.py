# This is my solution
# def twoSum(nums, target):
#     for i in range(0, len(nums)):
#         sub = target - nums[i]
#         print(i)
#         if sub in nums:
#             index2 = nums.index(sub)
#             if index2 != i:
#                 return [i, index2]

# This is the recommend sample
# Use a dictionary to store seen records
# New knowledge need to bear in mind is enumerate
def twoSum(nums, target):
    seen = {}
    for count, value in enumerate(nums):
        m = target - value
        if m in seen:
            print(seen)
            return [seen[m], count]
        else:
            seen[value] = count


if __name__ == '__main__':
    print(twoSum([3, 2, 4], 6))
