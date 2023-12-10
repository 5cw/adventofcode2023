inp = open('day7input.txt').readlines()


def process(hand):
    p = hand.translate(str.maketrans('TJQKA', 'ABCDE'))
    unique = set(hand)
    counts = sorted(hand.count(c) for c in unique)
    if len(counts) > 1:
        *_, s, l = counts
        return chr(65+l*5+s)+p
    else:
        return 'z' + p


def jprocess(hand):
    p = hand.translate(str.maketrans('TJQKA', 'A1CDE'))
    unique = set(hand) - {'J'}
    counts = sorted(hand.count(c) for c in unique)
    if len(counts) > 1:
        *_, s, l = counts
        l += hand.count('J')
        return chr(65+l*5+s)+p
    else:
        return 'z' + p


for func in [process, jprocess]:
    hands = [(func(line[:5]), int(line[6:])) for line in inp]
    hands.sort()
    total = 0
    for i, (_, rank) in enumerate(hands):
        total += (i+1) * rank

    print(total)


