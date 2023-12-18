# https://adventofcode.com/2023/day/9
import os
import datetime as dt


def solve(lines):
    
    def predict(data,next=True):
        diffs = [[d for d in data]]
        while sum(diffs[-1])!=0:
            diffs.append([b-a for a,b in zip(diffs[-1][:-1], diffs[-1][1:])])

        predicted=0
        if next:
            for d in diffs[::-1]:
                predicted += d[-1]
        else:
            for d in diffs[::-1]:
                predicted = d[0] - predicted
        return predicted
    
    reports = [list(map(int,row.split())) for row in lines]
    return sum([predict(report,next=False) for report in reports])
        
def main(test):
    # READ INPUT FILE
    script_path = os.path.dirname(os.path.realpath(__file__))
    with open(
        os.path.join(script_path, "test.txt" if test else "input.txt"), encoding="utf-8"
    ) as input:
        lines = input.readlines()
    lines = list(map(str.strip, lines))

    result = solve(lines)
    print(f"The result is {result}.")
    # 

start_t = dt.datetime.now()
main(test=True)

start_t = dt.datetime.now()
main(test=False)
end_t = dt.datetime.now()
print(f"Runtime: {(end_t-start_t).total_seconds()}")