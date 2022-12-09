# --- Day 7: Handy Haversacks ---
# https://adventofcode.com/2020/day/7
import re


def count_bags(b, bag_list):
    count = 1
    for bag in bag_list:
        if bag[1] in bags_tree:
            count = count + int(bag[0]) * count_bags(bag[1], bags_tree[bag[1]])
        else:
            count = count + int(bag[0])
    return count


def has_shiny_gold_bag(bag, bag_list, bags_tree):

    for bag in bag_list:
        if bag[1] == 'shiny gold':
            return True
        if bag[1] in bags_tree:
            if has_shiny_gold_bag(bag, bags_tree[bag[1]], bags_tree):
                return True
    return False


bags_tree = {}
part1 = 0
with open('input.txt', 'r') as reader:
    input = [i.strip() for i in reader.readlines()]
for line in input:
    m = re.match(r"(.+) bags? contain (.+)", line)
    n = re.findall(r"(\d+) (\S+ \S+) bags?. ?", m.group(2))
    if n:
        bags_tree[m.group(1)] = n

for bag in bags_tree:
    part1 = part1 + has_shiny_gold_bag(bag, bags_tree[bag], bags_tree)

print(part1)
print(count_bags('shiny gold', bags_tree['shiny gold']) - 1)
