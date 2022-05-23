length = int(input())
width = int(input())
height = int(input())
percent = int(input()) / 100

volume_aquarium = length * width * height
volume_liters = volume_aquarium * 0.001
gotten_space = percent
needed_liters = volume_liters * (1-gotten_space)

print(needed_liters)