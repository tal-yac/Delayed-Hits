import sys

sys.stdout = open(sys.argv[2], 'w')
index = 0
key = " fh "

max = 1 << 25

with open(sys.argv[1]) as f:
    while True:
        if index > max:
            break
        line = f.readline()
        if not line:
            break
        key_index = line.find(key)
        if key_index == -1:
            continue
        line = line[key_index + key.__len__():].strip()
        line = line[:line.find(" ")].strip()
        print(f"{index};{line}")
        index += 1