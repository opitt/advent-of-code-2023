# https://adventofcode.com/2023/day/15
import os
import datetime as dt
import re

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

    boxes = [{} for _ in range(256)]
       
    #rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7
    instructions = [re.findall("\w+|[-=]|\d+", instr) for instr in lines[0].split(",")]
    for label, *ops in instructions:
        box=hash_it(label)
        if ops[0]=="-":
            # If the operation character is a dash (-), go to the relevant box and remove the lens with the given label if it is present in the box. Then, move any remaining lenses as far forward in the box as they can go without changing their order, filling any space made by removing the indicated lens. (If no lens in that box has the given label, nothing happens.)
            try:
                boxes[box].pop(label)
            except KeyError:
                pass
        elif ops[0]=="=":
            # If there is already a lens in the box with the same label, replace the old lens with the new lens: remove the old lens and put the new lens in its place, not moving any other lenses in the box.
            # If there is not already a lens in the box with the same label, add the lens to the box immediately behind any lenses already in the box. Don't move any of the other lenses when you do this. If there aren't any lenses in the box, the new lens goes all the way to the front of the box.
            boxes[box][label] = ops[1]
    
    # To confirm that all of the lenses are installed correctly, add up the focusing power of all of the lenses. The focusing power of a single lens is the result of multiplying together:
    #   One plus the box number of the lens in question.
    #   The slot number of the lens within the box: 1 for the first lens, 2 for the second lens, and so on.
    #   The focal length of the lens.
    power=0
    for box, content in enumerate(boxes,1):
        power+= sum([box*slot*int(content[lens_label]) for slot, lens_label in enumerate(content,1)])
    return power

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
    # 251353

main(test=True)

start_t = dt.datetime.now()
main(test=False)
end_t = dt.datetime.now()
print(f"Runtime: {(end_t-start_t).total_seconds()}")