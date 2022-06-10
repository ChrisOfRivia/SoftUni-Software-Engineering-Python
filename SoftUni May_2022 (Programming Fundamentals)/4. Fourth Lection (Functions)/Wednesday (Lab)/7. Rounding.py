def rounding(nums):
    result = [round(num) for num in nums]
    return result


numbers = list(map(float, input().split(" ")))
print(rounding(numbers))