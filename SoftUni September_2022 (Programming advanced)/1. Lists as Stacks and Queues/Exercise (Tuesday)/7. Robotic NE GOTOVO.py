from collections import deque

robots = input().split(';')
starting_time = input()
hours = int(starting_time[0:1])
minutes = int(starting_time[2:4])
seconds = int(starting_time[5:7])

products = []
robots_dict = {}
occupied_robots = deque()

while True:
    product = input()
    if product == 'End':
        break
    products.append(product)

for each_robot in robots:
    robot_and_time = each_robot.split('-')
    robot_name = robot_and_time[0]
    robot_time = int(robot_and_time[1])
    robots_dict[robot_name] = robot_time

while products:
    


    seconds += 1
    if seconds == 60:
        seconds = 0
        minutes += 1
    if minutes == 60:
        minutes = 0
        hours += 1


print(products)

