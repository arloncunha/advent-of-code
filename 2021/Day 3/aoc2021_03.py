# --- Day 3: Binary Diagnostic ---
# https://adventofcode.com/2021/day/3

def raw_report(report_list):
    raw_report = [0]*len(report_list[0])
    for line in report_list:
        for i, bit in enumerate(line):
            raw_report[i] = raw_report[i] + -1 if bit == '0' else raw_report[i] + 1
    return raw_report

def gamma_rate(report):
    rep = list(report)
    for i in range(len(report)):
        rep[i] = '0' if rep[i] <= 0 else '1'
    return int("".join(rep), 2) # class int(x, base=10)

def epsilon_rate(report):
    rep = list(report)
    for i in range(len(rep)):
        rep[i] = '1' if rep[i] <= 0 else '0'
    return int("".join(rep), 2) # class int(x, base=10)


def oxygen_rate(report, input):
    input2 = [elem for elem in input]

    for i in range(len(input2[0])):
        report2_list = []
        for j in range(len(input2)):
            if input2[j][i] == '1' and report[i] >= 0:
                 report2_list.append(input2[j])
            elif input2[j][i] == '0' and report[i] < 0:
                 report2_list.append(input2[j])
        input2 = report2_list
        report = raw_report(input2)
    return int("".join(report2_list), 2) # class int(x, base=10)

def co2_rate(report, input):
    input2 = [elem for elem in input]

    for i in range(len(input2[0])):
        report2_list = []
        for j in range(len(input2)):
            if input2[j][i] == '1' and report[i] < 0:
                 report2_list.append(input2[j])
            elif input2[j][i] == '0' and report[i] >= 0:
                 report2_list.append(input2[j])
        if len(report2_list) == 1: # hack if list with only one before looping all
            return int("".join(report2_list), 2)
        input2 = report2_list
        report = raw_report(input2)
    return int("".join(report2_list), 2) # class int(x, base=10)

with open('input.txt', 'r') as reader:
    input = [i.rstrip("\n") for i in reader.readlines()]

report = raw_report(input)
print gamma_rate(report) * epsilon_rate(report)
print oxygen_rate(report, input) * co2_rate(report, input)
