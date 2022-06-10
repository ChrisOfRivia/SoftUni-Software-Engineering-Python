def abs_value(nums):
    result = [abs(num) for num in nums]
    return result


numbers = list(map(float, input().split(" ")))
print(abs_value(numbers))
