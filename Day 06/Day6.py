import os

def load_input(file):
    f = open(file, 'r')
    return f.readline()

def get_first_packet_marker(data):
    characters = ''
    unique = {}
    for i in range(4, len(data)):
        characters = data[i-4:i]
        unique = set(characters)
        if(len(characters)==len(unique)):
            return i
    return -1

def get_first_message_marker(data):
    characters = ''
    unique = {}
    for i in range(14, len(data)):
        characters = data[i-14:i]
        unique = set(characters)
        if(len(characters)==len(unique)):
            return i
    return -1

def main():
    file_name = os.path.join(os.path.dirname(__file__), "input.txt")
    data = load_input(file_name)

    #Part 1
    print('Part 1:', get_first_packet_marker(data))

    #Part 2
    print('Part 2:', get_first_message_marker(data))

if __name__ == '__main__':
    main()