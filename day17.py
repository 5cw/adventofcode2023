import getinput

inp = getinput.fetch().strip()

line_len = inp.find('\n') + 1
for mx, mn in [(3, 0), (10, 4)]:
    searched = [{} for _ in range(len(inp))]
    searching = [(len(inp) - 1, -1, 0, int(inp[-1])), (len(inp) - 1, -1, 0, int(inp[-1]))]

    while searching:
        new_searching = []
        for sq, direction, places, heat in searching:
            for d in [-line_len, line_len, -1, 1]:
                if d == -direction or (d == direction and places >= mx - 1) or (d != direction and places < mn - 1):
                    continue
                nsq = sq + d
                if nsq < 0 or nsq >= len(inp) or inp[nsq] == '\n':
                    continue
                nheat = heat + int(inp[nsq])
                p = places + 1 if d == direction else 0
                if (d, p) in searched[nsq] and searched[nsq][(d, p)] <= nheat:
                    continue
                else:
                    searched[nsq][(d, p)] = nheat
                    new_searching.append((nsq, d, p, nheat))
        searching = new_searching
        #print(searching)
    print(min(searched[0].values())-int(inp[0]))