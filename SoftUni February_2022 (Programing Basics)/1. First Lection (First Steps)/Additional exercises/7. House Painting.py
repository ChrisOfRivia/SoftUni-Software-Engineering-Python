x_height_of_house = float(input())
y_width_of_house = float(input())
h_height_of_roof = float(input())

house_side = x_height_of_house * y_width_of_house
window = 1.5*1.5
both_sides = house_side * 2 - window * 2
house_back = x_height_of_house * x_height_of_house
door = 1.2*2
front_and_back = 2 * house_back - door
whole_area_base = both_sides + front_and_back

green_paint = whole_area_base / 3.4

rectangle_side_of_roof = 2*(x_height_of_house*y_width_of_house)
triangle_side_of_roof = 2*(x_height_of_house*h_height_of_roof/2)

whole_area_roof = rectangle_side_of_roof + triangle_side_of_roof

red_paint = whole_area_roof / 4.3

print(format(green_paint, ".2f"))
print(format(red_paint, ".2f"))
