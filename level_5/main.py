#!/usr/bin/env python3
import pandas as pd
import csv
from helper import *

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

def get_step_instructions(x_pace, y_pace):
    time = max(get_time(x_pace), get_time(y_pace))
    step_instructions = []
    for _ in range(time):
        step_instructions.append([0,0])
    t_x = 0
    for i in x_pace:
        is_negative = i < 0
        i = abs(i)
        if i > 0:
            t_x += (i-1)
            step_instructions[t_x][0] = 1 if not is_negative else -1
        t_x += 1

    t_y = 0
    for i in y_pace:
        is_negative = i < 0
        i = abs(i)
        if i > 0:
            t_y += (i - 1)
            step_instructions[t_y][1] = 1 if not is_negative else -1
        t_y += 1
    return step_instructions

def is_colliding(step_instructions, ast_x, ast_y, verbose=False):
    pos_x = 0
    pos_y = 0
    for i, step in enumerate(step_instructions):
        pos_x += step[0]
        pos_y += step[1]
        if abs(pos_x - ast_x) <= 2 and abs((pos_y - ast_y)) <= 2:
            if verbose:
                print("Collision at step ", i, " with asteroid at (", ast_x, ",", ast_y, ")")
            return True
    return False

def pad_speed_to_equal_length(speed_x, speed_y):
    time_x = get_time(speed_x)
    time_y = get_time(speed_y)
    time = max(time_x, time_y)
    for _ in range(time - time_x):
        speed_x.append(0)
    for _ in range(time - time_y):
        speed_y.append(0)

def main():
    input = []

    out_x = []
    out_y = []
    with open("level5_2_large.in", "r") as f:
        first_line = f.readline().strip()
        for line in f:
            input.append(line.strip())

    out_x = []
    out_y = []
    ast_x = []
    ast_y = []

    for i in range(0, len(input), 2):
        dist, time = input[i].split(" ")
        time = int(time)
        dist_x, dist_y = map(int, dist.split(","))
        ast_x, ast_y = map(int, input[i+1].split(","))
        x = get_speed(dist_x)
        y = get_speed(dist_y)

        step_instructions = get_step_instructions(x, y)

        if is_colliding(step_instructions, ast_x, ast_y):
            waypoints = get_alt_waypoints(ast_x, ast_y, dist_x, dist_y) + [[dist_x, dist_y]]
            x = []
            y = []
            pos_x = 0
            pos_y = 0
            for point in waypoints:
                wp_x, wp_y = point
                dist_x = wp_x - pos_x
                dist_y = wp_y - pos_y
                x_wp = get_speed(dist_x)
                y_wp = get_speed(dist_y)
                pad_speed_to_equal_length(x_wp, y_wp)
                pos_x = wp_x
                pos_y = wp_y

                x += x_wp
                y += y_wp
            step_instructions = get_step_instructions(x, y)
            if is_colliding(step_instructions, ast_x, ast_y, verbose=True):
                print("Error: Still colliding after waypoints! in Line ", i+3)

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