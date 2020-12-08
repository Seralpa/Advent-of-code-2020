import copy as cp

def run(program):
    accumulator, pc=0, 0
    visited=set()
    fixable_visited=set()#nop and jmp instructions
    while pc not in visited:
        visited.add(pc)
        if pc==len(program):
            print(accumulator)
            break
        if program[pc][0]=='acc':
            accumulator+=int(program[pc][1])
            pc+=1
        elif program[pc][0]=='jmp':
            fixable_visited.add(pc)
            pc+=int(program[pc][1])
        else:
            fixable_visited.add(pc)
            pc+=1
    return fixable_visited

with open('day8/input.txt') as f:
    program=[l.split() for l in f.read().splitlines()]
fixable_visited=run(program)
for ins in fixable_visited:
    modProgram=cp.deepcopy(program)
    modProgram[ins][0]='jmp' if modProgram[ins][0]=='nop' else 'nop'
    run(modProgram)