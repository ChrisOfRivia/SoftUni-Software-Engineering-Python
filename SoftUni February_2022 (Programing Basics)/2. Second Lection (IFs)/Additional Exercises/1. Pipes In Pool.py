V = int(input())
P1 = int(input())
P2 = int(input())
H = float(input())

first_pipe = H * P1
second_pipe = H * P2

all_pipes = first_pipe + second_pipe

if all_pipes <= V:
    percentage_all = all_pipes / V * 100
    percentage_P1 = first_pipe / all_pipes * 100
    percentage_P2 = second_pipe / all_pipes * 100
    print(f"The pool is {percentage_all:.2f}% full. "
          f"Pipe 1: {percentage_P1:.2f}%. Pipe 2: {percentage_P2:.2f}%.")
else:
    diff = abs(all_pipes - V)
    print(f"For {H:.2f} hours the pool overflows with {diff:.2f} liters.")