# https://adventofcode.com/2023/day/14
import os
import datetime as dt
import re
from copy import deepcopy

def solve(lines):

    def shift_rocks(row,left=True):
        
        def repl(s):
            rocks_to_shift = s.group(0)
            O="O"*rocks_to_shift.count("O")
            D="."*rocks_to_shift.count(".")
            if left:
                return f"{O}{D}"
            else:
                return f"{D}{O}"
        
        if left:
            # starts with a . followed by . or O and ending with O
            regex = r"(?=[.])[.O]+O"
        else:
            # starts O followed by . or O and ending with .
            regex = r"O[.O]+(?<=[.])"
        while True:
            # find and move all moveable rocks
            row, n = re.subn(regex, repl, row)
            if n==0:break
        return row
    
    def tilt_4(rows):
        for dir in range(4):
            #north=0, west=1, south=2, east=3
            if dir==0:
                #rotate
                cols = ["".join(el) for el in zip(*rows)]
                #tilt left
                cols = [shift_rocks(col,left=True) for col in cols]
                #rotate back
                rows = ["".join(el) for el in zip(*cols)]
            elif dir==1:
                rows = [shift_rocks(row,left=True) for row in rows]
            elif dir==2:
                #rotate
                cols = ["".join(el) for el in zip(*rows)]
                #tilt left
                cols = [shift_rocks(col,left=False) for col in cols]
                #rotate back
                rows = ["".join(el) for el in zip(*cols)]
            elif dir==3:
                rows = [shift_rocks(row,left=False) for row in rows]
        return rows
    
    def hash_rows(dish):
        return ";".join(row for row in dish) 

    def rows_value(rows):
        return sum([val*row.count("O") for val, row in enumerate(rows[::-1],start=1)])

    rows = deepcopy(lines)
    seen = {}
    cycles=1_000_000_000
    for cycle in range(1,cycles+1):
        rows_hash = hash_rows(rows)
        if rows_hash in seen:
            rows_to,cycle_loop_start,value = seen[rows_hash]
            break
        else:
            rows = tilt_4(rows)
            rows_to = hash_rows(rows)
            seen[rows_hash] = (rows_to, cycle, rows_value(rows))

    loop_len=cycle-cycle_loop_start
    cycles_remaining = cycles - cycle
    shortcut = cycles_remaining % loop_len
    find_cycle = cycle_loop_start + shortcut
    _,_,value = min([v for v in seen.values() if v[1]==find_cycle])
    return value

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
    # 101292

start_t = dt.datetime.now()
main(test=True)

start_t = dt.datetime.now()
main(test=False)
end_t = dt.datetime.now()
print(f"Runtime: {(end_t-start_t).total_seconds()}")