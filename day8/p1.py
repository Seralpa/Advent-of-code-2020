def run(program):
    visited=set()
    accumulator, pc=0, 0
    while pc not in visited:
        visited.add(pc)
        if program[pc][0]=='acc':
            accumulator+=int(program[pc][1])
            pc+=1
        elif program[pc][0]=='jmp':
            pc+=int(program[pc][1])
        else:   #nop
            pc+=1
    print(accumulator)

with open('day8/input.txt') as f:
    run([l.split() for l in f.read().splitlines()])