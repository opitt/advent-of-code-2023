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
        
        def set_beam_was_here(self, beam):
            self.dirs[beam.dir] = True

        def beam_was_here(self, beam):
            return self.dirs[beam.dir]

    class Maze:
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
        def __init__(self, lines: list):
            self.maze_energy = [[" " for _ in row] for row in lines]
            self.maze = [[Square(col) for col in row] for row in lines]
        
        def beam_was_here(self, beam):
            return self.maze[beam.y][beam.x].beam_was_here(beam)
        
        def set_beam_was_here(self, beam):
            self.maze[beam.y][beam.x].set_beam_was_here(beam)
            self.maze_energy[beam.y][beam.x]="#"
            return self.NEWDIR[(self.maze[beam.y][beam.x].type,beam.dir)]
        
        def get_energy(self):
            return sum([row.count("#") for row in self.maze_energy])
            

    Beam = namedtuple("Beam","x y dir")

    beam_configurations=[]
    beam_configurations.extend([[Beam(x=x,y=0,dir=DOWN),] for x in range(MAXX+1)])
    beam_configurations.extend([[Beam(x=x,y=MAXY,dir=UP),] for x in range(MAXX+1)])
    beam_configurations.extend([[Beam(x=0,y=y,dir=RIGHT),] for y in range(MAXY+1)])
    beam_configurations.extend([[Beam(x=MAXX,y=y,dir=LEFT),] for y in range(MAXY+1)])

    configuration_energy=[]
    for beams in beam_configurations:
        # initialise
        maze = Maze(lines)
        while len(beams):
            nextbeams=[]
            for beam in beams:
                if not maze.beam_was_here(beam):
                    newdirs=maze.set_beam_was_here(beam)
                    for newdir in newdirs:
                        inside = 0<=(beam.x + newdir[0])<=MAXX and 0<=(beam.y + newdir[1])<=MAXY
                        if inside:
                            nextbeam=Beam(x=beam.x+newdir[0],y=beam.y+newdir[1],dir=newdir)
                            if nextbeam not in nextbeams:
                                nextbeams.append(nextbeam)
            beams = nextbeams
        
        # count the energy
        energy= maze.get_energy()
        configuration_energy.append(energy)
 
    return max(configuration_energy)


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
    # 7853

start_t = dt.datetime.now()

#main(test=True)
main(test=False)

end_t = dt.datetime.now()
print(f"Runtime: {(end_t-start_t).total_seconds()}")
