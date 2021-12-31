import math

input = open('input.txt').read().splitlines()
binary = ''
for c in input:
    binary += bin(int(c, 16))[2:].zfill(4)

def decode_headers(s):
    version = int(s[:3],2)
    id = int(s[3:6],2)
    return version, id, s[6:]

def get_length(s):
    return int(s[1:16],2), s[16:]

def get_n_packages(s):
    return int(s[1:12],2), s[12:]

def get_value(s):
    return s[1:5], s[5:], s[0] == '0'

methods = {
    '0': lambda x: sum(x),
    '1': lambda x: math.prod(x),
    '2': lambda x: min(x),
    '3': lambda x: max(x),
    '5': lambda x: int(x[0]>x[1]),
    '6': lambda x: int(x[0]<x[1]),
    '7': lambda x: int(x[0]==x[1])
}

def decode_package(s): 
    v_sum = 0
    v, id, s = decode_headers(s)
    v_sum += v
    lvalue = 0
    if id == 4:
        done = False
        total_binary = ''
        while not done:
            value, s, done = get_value(s)
            total_binary += value
        lvalue = int(total_binary, 2)
    else:
        values = []
        if s[0] == '1':
            np, s = get_n_packages(s)
            for i in range(np):
                s, vs, lv = decode_package(s)
                values.append(lv)
                v_sum += vs
        elif s[0] == '0':
            length, s = get_length(s)
            substr = s[:length]
            while substr:
                substr, vs, lv = decode_package(substr)
                values.append(lv)
                v_sum += vs
            s = s[length:]
        lvalue = methods[str(id)](values)
    return s, v_sum, lvalue
_, v_sum, value = decode_package(binary)

print("Day 16, part 1, answer:", v_sum)
print("Day 16, part 2, answer:", value)