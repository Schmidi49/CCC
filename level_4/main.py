#!/usr/bin/env python3
import pandas as pd
import csv

def get_speed(dist):
    is_negative = dist < 0
    dist = abs(dist)

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

    full = (speed + reversed)
    if is_negative:
        full = [i * -1 for i in full]
    return full

def get_time(speed):
    sum_time = 0
    for num in speed:
        if num == 0:
            sum_time += 1
        else:
            sum_time += abs(num)
    return sum_time


def main():
    out_x = []
    out_y = []

    with open("level4_2_large.in", "r") as f:
        first_line = f.readline().strip()
        for line in f:
            dist, time = line.split(" ")
            time = int(time)
            dist_x, dist_y = map(int, dist.split(","))

            x = get_speed(dist_x)
            y = get_speed(dist_y)

            if get_time(x) > time or get_time(y) > time:
                print("Warning: Generated time exceeds limit!")
            out_x.append(x)
            out_y.append(y)
    return out_x, out_y

if __name__ == '__main__':
    out_x, out_y = main()
    with open("output_2.out", "w") as f:
        for i in range(len(out_x)):
            x_str = ' '.join(map(str, out_x[i]))
            y_str = ' '.join(map(str, out_y[i]))

            f.write(f'{x_str}\n')
            f.write(f'{y_str}\n\n')





































    main()
