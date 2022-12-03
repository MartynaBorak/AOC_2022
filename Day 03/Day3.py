import os

def load_input(file):
    with open(file, 'r') as lines:
        return [line.strip() for line in lines]

def get_halves(lines):
    return [[line[0:len(line)//2], line[len(line)//2:len(line)]] for line in lines]

def get_threes(lines):
    threes = []
    for i in range(0, len(lines), 3):
        threes.append([lines[i], lines[i+1], lines[i+2]])
    return threes

def find_badge(three):
    for i in three[0]:
        if(i in three[1] and i in three[2]):
            return get_priority(i)

def find_mistake(rucksack):
    for i in rucksack[0]:
        if(i in rucksack[1]):
            return get_priority(i)

def get_priority(letter):
    value = ord(letter)
    if(value>96):
        return value-96
    else:
        return value-38

def main():
    file_name = os.path.join(os.path.dirname(__file__), "input.txt")
    lines = load_input(file_name)

    #Part 1
    rucksucks = get_halves(lines)
    print("Part 1: " + str(sum(find_mistake(rucksack) for rucksack in rucksucks)))
        
    #Part 2
    threes = get_threes(lines)
    print("Part 2: " + str(sum(find_badge(three) for three in threes)))

if __name__ == '__main__':
    main()