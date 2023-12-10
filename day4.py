inp = open('day4input.txt').readlines()

total = 0

copies = [1]*len(inp)

for i, line in enumerate(inp):
    win, have = [nums.split() for nums in line.split(':')[1].split('|')]
    winning = sum(num in win for num in have)
    if winning > 0:
        total += 1 << winning - 1
        for j in range(i+1, i+winning+1):
            copies[j] += copies[i]

print(total)
print(sum(copies))