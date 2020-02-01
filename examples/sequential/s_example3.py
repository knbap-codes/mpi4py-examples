import random

n = 1024
result = [0] * 100

def generate_input_file():
    f = open('in.txt', 'w')
    for i in range(n):
        f.write('{}\n'.format(random.randrange(0, 100)))

    f.close()

generate_input_file()

with open('in.txt') as f:
    numbers = [line.rstrip() for line in f]

for number in numbers:
    for j in range(100):
        if int(number) == j:
            result[j-1] += 1


print(result)