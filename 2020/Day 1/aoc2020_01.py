# --- Day 1: Report Repair ---
# https://adventofcode.com/2020/day/1
import re

result = 0
with open('input.txt', 'r') as reader:
    input = [int(i.strip()) for i in reader.readlines()]

for i in range(len(input)):
    for j in range(len(input)):
        if i != j and i < j:
            if input[i] + input[j] == 2020:
                print(input[i] * input[j])


for i in range(len(input)):
    for j in range(len(input)):
        for k in range(len(input)):
            if i != j != k and i < j and j < k:
                if input[i] + input[j] + input[k] == 2020:
                    print(input[i] * input[j] * input[k])
