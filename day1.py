inp = open('day1input.txt').readlines()
total = 0
for line in inp:
    digits = [int(c) for c in line if '0'<=c<='9']
    total += digits[0]*10+digits[-1]
print(total)

nums = 'zero one two three four five six seven eight nine'.split()
total = 0
for line in inp:
    first = len(line)
    last = -1
    for i,n in enumerate(nums):
        new_first = min(line.find(str(i))%len(line), line.find(n)%len(line))
        new_last = max(line.rfind(str(i)), line.rfind(n))
        if new_first < first:
            first = new_first
            fn = i
        if new_last > last:
            last = new_last
            ln = i
    total += fn*10 + ln
print(total)