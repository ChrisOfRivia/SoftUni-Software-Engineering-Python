def stronger_group_of_neg_and_pos(list_of_numbers):
    positive_group = 0
    negative_group = 0

    for each_num in list_of_numbers:
        if each_num > 0:
            positive_group += each_num
        else:
            negative_group += each_num

    print(negative_group)
    print(positive_group)
    if abs(negative_group) > positive_group:
        print(f"The negatives are stronger than the positives")
    else:
        print(f"The positives are stronger than the negatives")


stronger_group_of_neg_and_pos(map(int, input().split()))
