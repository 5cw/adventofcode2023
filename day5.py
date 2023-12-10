inp = open('day5input.txt').readlines()

seeds = [int(i) for i in inp[0].split()[1:]]
source = seeds.copy()
destination = []

for line in inp[3:]:
    nums = line.split()
    if len(nums) == 3:
        dst, src, n = map(int, nums)
        for val in source.copy():
            diff = val - src
            if 0 <= diff < n:
                destination.append(dst + diff)
                source.remove(val)
    elif len(nums) == 0:
        source += destination
        destination = []
print(sorted(destination)[0])

seed_ranges = [(start, length) for start, length in zip(seeds[::2],seeds[1::2])]
source = {*seed_ranges}
destination = set()

for line in inp[3:]:
    nums = line.split()
    if len(nums) == 3:
        dst, src, n = map(int, nums)
        for start, length in source.copy():
            end = start + length
            send = src + n
            if not end <= src and not start >= send:
                source.remove((start, length))
                s_in = start >= src
                e_in = end <= send
                diff = start - src
                dest_start = dst + diff

                if s_in and e_in:
                    destination.add((dest_start, length))
                elif s_in:
                    destination.add((dest_start, n - diff))
                    source.add((start + (n - diff), length - (n - diff)))
                elif e_in:
                    destination.add((dst, diff + length))
                    source.add((start, -diff))
                else:
                    destination.add((dst, n))
                    source.add((start + (n - diff), length - (n - diff)))
                    source.add((start, -diff))
            #print(destination)
    elif len(nums) == 0:
        source |= destination
        destination = set()
print(sorted(destination))