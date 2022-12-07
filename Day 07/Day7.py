import os
import re

def load_input(file):
    with open(file, 'r') as lines:
        return [line for line in lines]

def get_structure(lines):
    cd = re.compile('[$]\scd\s(.+)')
    ls = re.compile('[$]\sls')
    dir = re.compile('dir\s(\w+)')
    file = re.compile('(\d+)\s(.+)')

    main_dir = Directory('/')
    all_directories = [main_dir]
    current_dir=main_dir
    current_line=1

    while(current_line<len(lines)):
        m=cd.match(lines[current_line])
        if(m):
            if(m.group(1)=='..'):
                current_dir=current_dir.parent
            else:
                current_dir=current_dir.directories[m.group(1)]
            current_line+=1
            continue
        m=dir.match(lines[current_line])
        if(m):
            if(m.group(1) not in current_dir.directories.keys()):
                current_dir.directories[m.group(1)]=Directory(m.group(1), current_dir)
                all_directories.append(current_dir.directories[m.group(1)])
            current_line+=1
            continue
        m=file.match(lines[current_line])
        if(m):
            current_dir.add_file(m.group(2), int(m.group(1)))
            current_line+=1
        else:
            current_line+=1
    return main_dir, all_directories

def part1(all_dirs):
    all_sizes=[]
    answer=0
    for dir in all_dirs:
        all_sizes.append(dir.get_size())
        if(dir.get_size()<=100000):
            answer+=dir.get_size()
    return answer, all_sizes

def part2(all_sizes, needed):
    all_sizes.sort()
    for i in all_sizes:
        if(i>=needed):
            return i

class Directory:
    def __init__(self, name, parent=None):
        self.files={}
        self.directories={}
        self.parent=parent
        self.name=name
        self.size=None

    def add_dir(self, dir_name, dir):
        self.directories[dir_name]=dir

    def add_file(self, name, size):
        self.files[name] = size

    def count_size(self):
        self.size=0     
        if(len(self.files)==0 and len(self.directories)==0):
            return

        for file_name, file_size in self.files.items():
            self.size+=file_size
        
        for dir_name, dir in self.directories.items():
            if(dir.get_size() is None):
                dir.count_size()
                self.size+=dir.get_size()
        return

    def get_size(self):
        return self.size

def main():
    file_name = os.path.join(os.path.dirname(__file__), "input.txt")
    lines = load_input(file_name)
    main_dir, all_dirs = get_structure(lines)
    main_dir.count_size()

    #Part 1
    answer, all_sizes = part1(all_dirs)
    print('Part 1:', answer)

    #Part 2
    max_space=40000000
    needed_space=main_dir.get_size()-max_space
    print('Part 2:', part2(all_sizes, needed_space))

if __name__ == '__main__':
    main()