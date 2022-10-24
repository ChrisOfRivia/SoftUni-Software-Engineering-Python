def sorter(nums):
    result = sorted(nums)
    return result


numbers = list(map(int, input().split(" ")))
print(sorter(numbers))