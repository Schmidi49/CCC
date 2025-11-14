#!/usr/bin/env python3
import pandas as pd
import csv

def main():
    input = []
    with open("level2_2_large.in", "r") as f:
        first_line = f.readline().strip()
        for line in f:
            input.append(line.split(" "))
    time = []
    space = []
    for line in input:
        sum_space = 0
        sum_time = 0
        for num in line:
            num = int(num)
            if num > 0:
                sum_space += 1
            if num < 0:
                sum_space -= 1

            if num == 0:
                sum_time += 1
            else:
                sum_time += abs(num)

        time.append(sum_time)
        space.append(sum_space)
    return time, space

if __name__ == '__main__':
    space, time = main()
    with open("output_2.out", "w") as f:
        for i in range(len(space)):
            f.write(f'{time[i]} {space[i]}\n')




































    main()
