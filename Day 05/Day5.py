import os
import re

def load_input(file):
    with open(file, 'r') as lines:
        return [line for line in lines]

def get_stacks(lines):
    stacks = {}
    bottom = 0
    for line in lines:
        if(line=='\n'):
            break
        else:
            bottom+=1
        
    keys = [int(num) for num in lines[bottom-1].strip().split('  ')]
    for key in keys:
        stack = []
        for line in lines[bottom-2::-1]: #read stack no. [key]
            temp = line[1+(key-1)*4]
            if(temp!=' '):
                stack.append(temp)
            else:
                break
        stacks[key]=stack

    return stacks

def get_procedure(lines):
    start = 0
    for line in lines:
        start+=1
        if(line=='\n'):
            break

    temp = [re.findall(r'\d+', line) for line in lines[start:]]
    return [[int(num) for num in line] for line in temp]

def move(stacks, instruction):
    a,b,c=instruction
    for i in range(a):
        stacks[c].append(stacks[b].pop())

def move_multiple(stacks, instruction):
    a,b,c=instruction
    temp = []
    for i in range(a):
        temp.insert(0, stacks[b].pop())
    for i in temp:
        stacks[c].append(i)

def main():
    file_name = os.path.join(os.path.dirname(__file__), "input.txt")
    lines = load_input(file_name)
    procedure = get_procedure(lines)

    #Part 1
    stacks = get_stacks(lines) 
    for instruction in procedure:
        move(stacks, instruction)
    top = []
    for key, value in stacks.items():
        if(len(value)>0):
            top.append(value[-1])
    print("Part 1: " + ''.join(top))
        
    #Part 2
    stacks = get_stacks(lines)
    for instruction in procedure:
        move_multiple(stacks, instruction)
    top = []
    for key, value in stacks.items():
        if(len(value)>0):
            top.append(value[-1])
    print("Part 2: " + ''.join(top))

if __name__ == '__main__':
    main()