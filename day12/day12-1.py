# https://adventofcode.com/2023/day/12
import os
import datetime as dt
import re
import itertools

def solve(lines):

    res=0
    for line in lines:
        pattern,parts=line.split()
        parts=list(map(int,parts.split(",")))
        #pattern = "?###????????"
        #parts = [3,2,1]
        # total length: 12
        # filler_pos = 12 - 6 (6 is the length of known parts)
        # (0-?) 3 (1-?) 2 (1-?)  1 (0-?)
        #  0-4     1-5     1-5      0-4
        # result: 10
        regex = pattern.replace(".","[.]").replace("?",".")
        filler_pos=len(pattern)-sum(parts)
        separators = len(parts)-1
        ranges = [range(0,filler_pos-separators+1), *[range(1,filler_pos-separators+2)]*separators, range(0,filler_pos-separators+1)]
        # Generate all combinations
        combinations = list(itertools.product(*ranges))
        possible_combinations = [combination for combination in combinations if sum(combination)==filler_pos]

        for combo in possible_combinations:
            check=""
            for p,part in enumerate(parts):
                check+=combo[p]*"." + part*"#"
            check += combo[-1]*"."
            if re.fullmatch(regex,check):
                res+=1
                #print(check)
        
    return res

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
    # 6958

start_t = dt.datetime.now()
main(test=True)

start_t = dt.datetime.now()
main(test=False)
end_t = dt.datetime.now()
print(f"Runtime: {(end_t-start_t).total_seconds()}")