# https://adventofcode.com/2023/day/15
import os
import datetime as dt

def solve(lines):

    def hash_it(s):
        # Determine the ASCII code for the current character of the string.
        # Increase the current value by the ASCII code you just determined.
        # Set the current value to itself multiplied by 17.
        # Set the current value to the remainder of dividing itself by 256.
        current_value=0
        for c in s:
            current_value+=ord(c)
            current_value*=17
            current_value=current_value%256
        return current_value

    #rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7
    sequences = lines[0].split(",")
    hashes = [hash_it(s) for s in sequences]
    return sum(hashes)
    


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
    # 503154

start_t = dt.datetime.now()

#main(test=True)
main(test=False)

end_t = dt.datetime.now()
print(f"Runtime: {(end_t-start_t).total_seconds()}")