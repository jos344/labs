#advent of code 2021, day 1
#part 1
f = open("input", "r")

l = [int(x.strip()) for x in f]

count = 0
for i in range(len(l)-1):
    if l[i+1] > l[i]:
        count+=1

print(count)
#count=1681

#part 2
count2 = 0
for i in range(len(l)-3):
    if l[i+3] > l[i]:
        count2+=1
    
print(count2)
#count2=1704
