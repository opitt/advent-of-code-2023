# https://adventofcode.com/2023/day/6
import os
import re
import datetime as dt
from functools import reduce

def solve(lines):
    
    def race(t, d):
        dists = [1 for press in range(1,t) if press*(t-press)>d]
        return sum(dists)
          
    races=[r for r in zip(map(int,re.findall("\d+",lines[0])),map(int,re.findall("\d+",lines[1])))]
    wins = [race(t,d) for t, d in races]
    return reduce(lambda x,y: x*y,wins,1)


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
#main(test=False)

end_t = dt.datetime.now()
print(f"Runtime: {(end_t-start_t).total_seconds()}")
