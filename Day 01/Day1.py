import os

def load_input(file):
    with open(file, 'r') as lines:
        return [line for line in lines]

def sum_calories(calorie_list):
    calories = []
    total = 0
    for line in calorie_list:
        try:
            total = total + int(line)
        except:
            calories.append(total)
            total=0
    return calories

def main():
    file_name = os.path.join(os.path.dirname(__file__), "input.txt")
    calorie_list = load_input(file_name)
    
    calories = sum_calories(calorie_list)
    calories.sort(reverse=True)
    print("Part 1: " + str(calories[0]))
        
    top3 = calories[0] + calories[1] + calories[2]
    print("Part 2: " + str(top3))

if __name__ == '__main__':
    main()