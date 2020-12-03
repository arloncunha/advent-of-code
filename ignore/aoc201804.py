# https://adventofcode.com/2018/day/3
import re
import datetime

def prints(v):
    print(str(v))

def do_action(min, action):
    global guard_id
    global last_min
    if   action == "falls asleep": guards(guard_id) = min - last_min
    elif action == "wakes up": last_min = min
    else #Guard #XX begins shift



def get_minutes(year, month, day, hour, min):
    d1 = datetime.datetime(year, 1, 1)
    d2 = datetime.datetime(year, month, day, hour=hour, minute=min)
    return (d2 - d1).total_seconds() / 60

guard_id = 0
last_min = 0
guards = {} #guards sleeping time

with open('/Users/i813686/Documents/Coding/AoC-Python/input2018_04_test.txt', 'r') as reader:
    input = [i.strip() for i in reader.readlines()]
for line in sorted(input):
    m = re.search(r"\[(\d+)-(\d+)-(\d)+ (\d+):(\d+)\] (.*)", line)
    print(line),
    print(get_minutes(int(m.group(1)), int(m.group(2)), int(m.group(3)), int(m.group(4)), int(m.group(5))))
