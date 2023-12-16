# https://adventofcode.com/2023/day/16
import os
import datetime as dt
from collections import namedtuple

def solve(lines):
    # (x,y)
    RIGHT=(1,0)
    LEFT=(-1,0)
    UP=(0,-1)
    DOWN=(0,1)
    NEWDIR= {(".",RIGHT): (RIGHT,),
             (".",LEFT): (LEFT,),
             (".",UP): (UP,),
             (".",DOWN): (DOWN,),
             ("-",RIGHT): (RIGHT,),
             ("-",LEFT): (LEFT,),
             ("-",UP): (LEFT, RIGHT,),
             ("-",DOWN): (LEFT, RIGHT,),
             ("|",RIGHT): (UP, DOWN,),
             ("|",LEFT): (UP, DOWN,),
             ("|",UP): (UP,),
             ("|",DOWN): (DOWN,),
             ("\\",RIGHT): (DOWN,),
             ("\\",LEFT): (UP,),
             ("\\",UP): (LEFT,),
             ("\\",DOWN): (RIGHT,),
             ("/",RIGHT): (UP,),
             ("/",LEFT): (DOWN,),
             ("/",UP): (RIGHT,),
             ("/",DOWN): (LEFT,),
            }
    MAXX=len(lines[0])-1
    MAXY=len(lines)-1
    # read the maze
    class Square:
        def __init__(self, type: str):
            self.type = type
            self.dirs = {UP: False,
                        DOWN: False,
                        LEFT: False,
                        RIGHT: False,}
        
        def set_beam_was_here(self, dir):
            self.dirs[dir] = True

        def beam_was_here(self, dir):
            return self.dirs[dir]

    Beam = namedtuple("Beam","x y dir")

    maze_energy = [[" " for col in row] for row in lines]
    maze = [[Square(col) for col in row] for row in lines]
    beams = [Beam(x=0,y=0,dir=RIGHT)]
    while len(beams):
        nextbeams=[]
        for beam in beams:
            if not maze[beam.y][beam.x].beam_was_here(beam.dir):
                maze[beam.y][beam.x].set_beam_was_here(beam.dir)
                maze_energy[beam.y][beam.x]="#"
                newdirs=NEWDIR[(maze[beam.y][beam.x].type,beam.dir)]
                for newdir in newdirs:
                    inside = 0<=(beam.x + newdir[0])<=MAXX and 0<=(beam.y + newdir[1])<=MAXY
                    if inside:
                        nextbeam=Beam(x=beam.x+newdir[0],y=beam.y+newdir[1],dir=newdir)
                        if nextbeam not in nextbeams:
                            nextbeams.append(nextbeam)
        beams = nextbeams
        #energy = sum([row.count("#") for row in maze_energy])
        #print(energy)
    
    # count the energy
    energy= sum([row.count("#") for row in maze_energy])
    return energy


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
    # 7477

start_t = dt.datetime.now()

#main(test=True)
main(test=False)

end_t = dt.datetime.now()
print(f"Runtime: {(end_t-start_t).total_seconds()}")
