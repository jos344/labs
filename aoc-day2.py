# advent of code 2021, day2
f = open('input', 'r')

l = [x.split() for x in f]

# part 1
horizontal_position = 0
depth = 0

for count, value in enumerate(l):
    if l[count][0] == 'forward':
        horizontal_position += int(l[count][1])
    elif l[count][0] == 'up':
        depth -= int(l[count][1])
    elif l[count][0] == 'down':
        depth += int(l[count][1])

result = horizontal_position * depth
print(result)
#result=1480518

aim = 0
horizontal_position2 = 0
depth2 = 0
# part 2
for count, value in enumerate(l):
    if l[count][0] == 'forward':
        horizontal_position2 += int(l[count][1])
        depth2 += aim * int(l[count][1])
    elif l[count][0] == 'up':
        aim -= int(l[count][1])
    elif l[count][0] == 'down':
        aim += int(l[count][1])

result2 = depth2 * horizontal_position2
print(result2)
#result2=1282809906 
