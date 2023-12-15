# https://adventofcode.com/2023/day/13
import os
import datetime as dt


def solve(lines):
    
    def find_reflections_vertical(pattern):
        new_pattern=["".join(list(col)) for col in zip(*pattern)]
        return find_reflections_horizontal(new_pattern)

    def find_reflections_horizontal(pattern):
        # find all side by side rows, which are equal 
        middles = [y for y, line in enumerate(pattern[:-1]) if line == pattern[y+1] ]
        
        m=-1
        for middle in middles:
            # check, if the middle is really a perfect mirror
            mirror_width = min(middle,len(pattern)-(middle+1)-1)
            perfect=[ pattern[middle-r]==pattern[middle+1+r] for r in range(1,mirror_width+1) ]
            if all(perfect):
                m=middle
                break

        return m+1 if m>=0 and (all(perfect) or len(perfect)==0) else 0
    
    # separate the patterns
    patterns=[[]]
    for line in lines:
        if line=="":
            patterns.append([])
        else:
            patterns[-1].append(line)
    
    res=0
    for pattern in patterns:
        h = find_reflections_horizontal(pattern)
        v = find_reflections_vertical(pattern)
        res+=h*100+v

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
    # 37381

start_t = dt.datetime.now()

#main(test=True)
main(test=False)

end_t = dt.datetime.now()
print(f"Runtime: {(end_t-start_t).total_seconds()}")
