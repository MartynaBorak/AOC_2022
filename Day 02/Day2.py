import os

def load_input(file):
    with open(file, 'r') as lines:
        return [tuple(line.strip().split(' ')) for line in lines]

'''
A X rock 1
B Y paper 2
C Z scissors 3
win 6
draw 3
loss 0
'''
def get_score1(rounds):
    lookup = {
        ('A', 'X'):4,
        ('A', 'Y'):8,
        ('A', 'Z'):3,
        ('B', 'X'):1,
        ('B', 'Y'):5,
        ('B', 'Z'):9,
        ('C', 'X'):7,
        ('C', 'Y'):2,
        ('C', 'Z'):6
    }
    return sum([lookup[i] for i in rounds])

'''
A rock 1
B paper 2
C scissors 3
X loss 0
Y draw 3
Z win 6
'''
def get_score2(rounds):
    lookup = {
        ('A', 'X'):3,
        ('A', 'Y'):4,
        ('A', 'Z'):8,
        ('B', 'X'):1,
        ('B', 'Y'):5,
        ('B', 'Z'):9,
        ('C', 'X'):2,
        ('C', 'Y'):6,
        ('C', 'Z'):7
    }
    return sum([lookup[i] for i in rounds])

def main():
    file_name = os.path.join(os.path.dirname(__file__), "input.txt")
    rounds = load_input(file_name)
    
    print("Part 1: " + str(get_score1(rounds)))
        
    print("Part 2: " + str(get_score2(rounds)))

if __name__ == '__main__':
    main()