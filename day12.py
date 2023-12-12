import getinput

inp = getinput.fetchlines()


def match(s1, s2):
    return all(c == d or c == '?' for c, d in zip(s1, s2))


memoize = {}


def allcombos(nums, pattern):
    key = (len(nums), len(pattern))
    if key in memoize:
        return memoize[key]
    if not nums:
        out = '.'*len(pattern)
        memoize[key] = match(pattern, out)
        return memoize[key]
    valid = 0
    first, *rest = nums
    end = len(rest) > 0
    cap = len(pattern) - sum(rest) - len(rest) + end
    prefix = '#'*first + '.'*end
    while len(prefix) <= cap:
        if match(pattern[:len(prefix)], prefix):
            valid += allcombos(rest, pattern[len(prefix):])
        prefix = '.' + prefix
    memoize[key] = valid
    return valid


for i in (1, 5):
    total = 0
    for line in inp:
        memoize.clear()
        springstr, numstr = line.split()
        springs = '?'.join([springstr]*i)
        nums = [*map(int, numstr.split(','))]*i
        #print(springs, nums)
        total += allcombos(nums, springs)
    print(total)
