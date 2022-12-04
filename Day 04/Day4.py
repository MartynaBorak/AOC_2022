import os
import re

def load_input(file):
    with open(file, 'r') as lines:
        return [line.strip() for line in lines]

def get_pairs(lines):
    lines_div = [re.split('[- ,]', line) for line in lines]
    return [[int(num) for num in nums] for nums in lines_div]

def check_containing(pair):
    a, b, c, d = pair
    #[a,b] jest w [c,d]
    if(c<=a and b<=d):
        return True
    #[c,d] jest w [a,b]
    elif(a<=c and d<=b):
        return True
    else:
        return False

def check_overlap(pair):
    a, b, c, d = pair
    #dowolny koniec [a,b] jest w [c,d]
    if(c<=a<=d or c<=b<=d):
        return True
    #dowolny koniec [c,d] jest w [a,b]
    elif(a<=c<=b or a<=d<=b):
        return True
    else:
        return False

def main():
    file_name = os.path.join(os.path.dirname(__file__), "input.txt")
    lines = load_input(file_name)
    pairs = get_pairs(lines)

    #Part 1
    print("Part 1: " + str(sum(check_containing(pair) for pair in pairs)))
        
    #Part 2
    print("Part 2: " + str(sum(check_overlap(pair) for pair in pairs)))

if __name__ == '__main__':
    main()