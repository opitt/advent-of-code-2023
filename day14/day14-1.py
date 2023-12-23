# https://adventofcode.com/2023/day/14
import os
import datetime as dt
import re

def solve(lines):
    
    def tilt(col):
        regex = r"[.]O"
        subst = "O."
        while True:
            col, n = re.subn(regex, subst, col)
            if n==0:break
        value = sum([v if c=="O" else 0 for v,c in enumerate(reversed(col),1)])
        return value
    
    columns = ["".join(el) for el in zip(*lines)]
    res=0
    for col in columns:
        res += tilt(col)
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