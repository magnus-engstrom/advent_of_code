# f = open("signals.txt", "r")
# signals = []
# for row in f.read().split('\n'):
#     signal_data = row.split('|')
#     signals.append({
#         'singals': signal_data[0].strip().split(' '),
#         'output': signal_data[1].strip().split(' ')
#     })
# counter = 0
# for signal in signals:
#     for output in signal['output']:
#         if len(output) in [3, 2, 4, 7]:
#             counter += 1
# print(counter)

f = open("signals.txt", "r")
signals = []
for row in f.read().split('\n'):
    signal_data = row.split('|')
    signals.append({
        'inputs': signal_data[0].strip().split(' '),
        'output': signal_data[1].strip().split(' ')
    })
sum = 0
for signal in signals:
    numbers = [['']]*10
    while [''] in numbers:
        for input in signal['inputs']:
            if len(input) == 2:
                numbers[1] = list(input)
            if len(input) == 3:
                numbers[7] = list(input)
            if len(input) == 4:
                numbers[4] = list(input)
            if len(input) == 7:
                numbers[8] = list(input)
            if len(input) == 6:
                if len(set(list(input)) - set(numbers[1])) == 5:
                    numbers[6] = list(input)
                else:
                    if len(set(list(input)) - set(numbers[4])) == 2:
                        numbers[9] = list(input)
                    if len(set(list(input)) - set(numbers[4])) == 3:
                        numbers[0] = list(input)
            if len(input) == 5:
                if len(set(list(input)) - set(numbers[1])) == 3:
                    numbers[3] = list(input)
                else:
                    if len(set(list(input)) - set(numbers[4])) == 3:
                        numbers[2] = list(input)
                    if len(set(list(input)) - set(numbers[4])) == 2:
                        numbers[5] = list(input)
    value = ''
    for output in signal['output']:
        for i, number in enumerate(numbers):
            if set(list(output)) == set(number):
                value += str(i)
    print(value)
    sum += int(value)
    print("#####")
print(sum)