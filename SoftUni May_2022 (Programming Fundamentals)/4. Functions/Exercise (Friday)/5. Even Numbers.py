# def even(nums):
#     if nums % 2 == 0:
#         return True
#     else:
#         return False
#
#
# numbers = list(map(int, input().split(' ')))
#
# filtered = filter(even, numbers)
# list_of_evens = []
#
# for i in filtered:
#     list_of_evens.append(i)
#
# print(list_of_evens)
#

numbers = list(map(int, input().split(' ')))

filtered = list(filter(lambda x: x % 2 == 0, numbers))

print(filtered)



