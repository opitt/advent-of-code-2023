# https://adventofcode.com/2023/day/3
import os
import re
from collections import namedtuple

def solve(input_lines):
    # extend the playing field to simplify indexing
    lines = ["."*len(input_lines)]
    lines.extend(input_lines)
    lines.append(lines[0])
    lines = [f".{line}." for line in lines ]

    # find the gears
    Gear = namedtuple("Gear", "y x")    
    gears=[]
    for y, line in enumerate(lines):
        matches=re.finditer("(\*)",line)
        if matches:gears.extend([Gear(y, m.start()) for m in matches])

    # find all numbers
    Partno = namedtuple("Partno", "value y x1 x2")    
    nums=[]
    for y, line in enumerate(lines):
        matches=re.finditer("(\d+)",line)
        nums.append([Partno(int(m.group()), y, m.start(), m.end()-1) for m in matches])

    # for each gear, find the adjecent 2 numbers
    result=0
    for gear in gears:
        parts=[]
        nums_found = [num.value for num in nums[gear.y-1] if num.x1-1<= gear.x <= num.x2+1]
        if nums_found:parts.extend(nums_found)
        nums_found = [num.value for num in nums[gear.y+1] if num.x1-1<= gear.x <= num.x2+1]
        if nums_found:parts.extend(nums_found)
        nums_found = [num.value for num in nums[gear.y] if num.x2+1== gear.x]
        if nums_found:parts.extend(nums_found)
        nums_found = [num.value for num in nums[gear.y] if num.x1-1== gear.x]
        if nums_found:parts.extend(nums_found)
        # when 2 adjecent numbers found ... add their multiplication to the result
        if len(parts)==2:
            result+=parts[0]*parts[1]

    return result

def main(test):
    # READ INPUT FILE
    script_path = os.path.dirname(os.path.realpath(__file__))
    with open(os.path.join(script_path, "test.txt" if test else "input.txt"), encoding="utf-8") as input:
        lines = input.readlines()
    lines = list(map(str.strip, lines))

    result = solve(lines)
    print(
        f"The result is {result}."
    )
    # 87605697


#main(test=True)
main(test=False)
