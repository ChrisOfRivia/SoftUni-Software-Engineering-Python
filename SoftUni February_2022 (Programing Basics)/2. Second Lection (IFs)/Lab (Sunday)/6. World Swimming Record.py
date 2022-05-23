from math import floor

record_in_seconds = float(input())
length_in_meters = float(input())
time_swimming_for_1_meter = float(input())

swimming_meters_in_seconds = length_in_meters * time_swimming_for_1_meter

each_15_meters = (floor(length_in_meters / 15)) * 12.5


whole_time = swimming_meters_in_seconds + each_15_meters

time_needed_to_beat_record = abs(whole_time - record_in_seconds)

if whole_time >= record_in_seconds:
    print(f"No, he failed! He was {time_needed_to_beat_record:.2f} seconds slower.")
else:
    print(f"Yes, he succeeded! The new world record is {whole_time:.2f} seconds.")