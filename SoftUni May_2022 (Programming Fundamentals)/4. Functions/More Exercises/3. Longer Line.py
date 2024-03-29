# better to just import the needed functions than a whole library
# import math
from math import sqrt, floor


def find_distance_between_two_points(num_x1, num_x2, num_y1, num_y2):
    # no need to use math pow when ** does the same thing faster
    # arg_a = math.pow(num_x2 - num_x1, 2)
    # arg_b = math.pow(num_y2 - num_y1, 2)
    arg_a = (num_x2 - num_x1)**2
    arg_b = (num_y2 - num_y1)**2
    return sqrt(arg_a + arg_b)


def print_closer_point_first(x1, x2, y1, y2):
    first_point_distance_to_center = find_distance_between_two_points(0, x1, 0, y1)
    second_point_distance_to_center = find_distance_between_two_points(0, x2, 0, y2)
    if first_point_distance_to_center <= second_point_distance_to_center:
        # can print tuples instead, maybe slightly simpler, but not going to change it
        print(
            f'({floor(x1)}, {floor(y1)})({floor(x2)}, {floor(y2)})')
    else:
        print(
            f'({floor(x2)}, {floor(y2)})({floor(x1)}, {floor(y1)})')


fl_x1 = float(input())
fl_y1 = float(input())
fl_x2 = float(input())
fl_y2 = float(input())
sl_x1 = float(input())
sl_y1 = float(input())
sl_x2 = float(input())
sl_y2 = float(input())

length_first_line = find_distance_between_two_points(fl_x1, fl_x2, fl_y1, fl_y2)
length_second_line = find_distance_between_two_points(sl_x1, sl_x2, sl_y1, sl_y2)


if length_first_line >= length_second_line:
    print_closer_point_first(fl_x1, fl_x2, fl_y1, fl_y2)
else:
    print_closer_point_first(sl_x1, sl_x2, sl_y1, sl_y2)