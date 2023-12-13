# https://adventofcode.com/2023/day/13
import os
import datetime as dt


def solve(lines):
    
    def find_reflections_vertical(pattern):
        new_pattern=["".join(list(reversed(col))) for col in zip(*pattern)]
        return find_reflections_horizontal(new_pattern)

    def find_reflections_horizontal(pattern):
        middles=[]
        for y, line in enumerate(pattern[:-1]):
            if line == pattern[y+1]:
                middles.append(y)
        for middle in middles:
            # check, if perfect
            mirror_width = min(middle,len(pattern)-(middle+1)-1)
            perfect=[]
            for r in range(1,mirror_width+1):
                perfect.append(pattern[middle-r]==pattern[middle+1+r])
            if all(perfect):
                break

        return middle+1 if middle>0 and (all(perfect) or len(perfect)==0) else 0
    

    patterns=[[]]
    for line in lines:
        if line=="":
            patterns.append([])
        else:
            patterns[-1].append(line)
    
    hor=vert=0
    for p, pattern in enumerate(patterns):
        h = find_reflections_horizontal(pattern)
        hor += h
        v = find_reflections_vertical(pattern)
        vert += v
        print(p, v,h)

    return hor*100+vert


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
