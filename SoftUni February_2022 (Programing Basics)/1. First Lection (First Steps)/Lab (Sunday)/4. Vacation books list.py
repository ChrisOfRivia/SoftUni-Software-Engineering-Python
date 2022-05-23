pages = int(input())
pages_for_hour = int(input())
days = int(input())

time_to_read = pages / pages_for_hour
needed_days = time_to_read // days

print(needed_days)
