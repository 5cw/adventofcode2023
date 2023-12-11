inp = open('day9input.txt').readlines()


def extrapolate(nums, reverse=False):
    if all(num == 0 for num in nums): return 0
    diffs = [j - i for i, j in zip(nums, nums[1:])]
    return nums[0 if reverse else -1] + (-1 if reverse else 1)*extrapolate(diffs, reverse)


total = 0
rtotal = 0
for line in inp:
    nums = [*map(int, line.split())]
    total += extrapolate(nums)
    rtotal += extrapolate(nums, True)

print(total)

print(rtotal)