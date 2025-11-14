#!/usr/bin/env python3
import pandas as pd
import csv

def get_speed(dist):
    half = dist // 2

    speed = [0]
    current_pace = 5
    for i in range(half):
        speed.append(current_pace)
        if current_pace > 1:
            current_pace -= 1

    reversed = speed.copy()
    reversed.reverse()
    if dist % 2 == 1:
        speed.append(current_pace)
    return (speed + reversed)

def get_time(speed):
    sum_time = 0
    for num in speed:
        if num == 0:
            sum_time += 1
        else:
            sum_time += abs(num)
    return sum_time


def main():
    input = []
    with open("level3_2_large.in", "r") as f:
        first_line = f.readline().strip()
        for line in f:
            input.append(line.split(" "))

    out = []
    for line in input:
        dist = int(line[0])
        time = int(line[1])
        x = get_speed(abs(dist))
        if dist < 0:
            x = [i*-1 for i in x]
        if get_time(x) > time:
            print("Warning: Generated time exceeds limit!")
        out.append(x)
    return out

if __name__ == '__main__':
    out = main()
    with open("output_2.out", "w") as f:
        for i in range(len(out)):
            outstr = ' '.join(map(str, out[i]))
            f.write(f'{outstr}\n')




































    main()
