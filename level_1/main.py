#!/usr/bin/env python3
import pandas as pd
import csv

def main():
    input = []
    with open("level1_2_large.in", "r") as f:
        first_line = f.readline().strip()
        for line in f:
            input.append(line.split(" "))
    output = []
    for line in input:
        summe = 0
        for num in line:
            summe += int(num)
        output.append(summe)
    return output

if __name__ == '__main__':
    out = main()
    with open("output_2.out", "w") as f:
        for items in out:
            f.write('%s\n' % items)




































    main()
