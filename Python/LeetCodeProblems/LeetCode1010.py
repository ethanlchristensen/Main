# LEET CODE 1010 Pairs of Songs
# Given an array of songs, return the pairs who's
# lengths summed are divisible by 60

def numPairsDivisibleBy60(time):
    res = 0
    tmp = [time[i] % 60 for i in range(len(time))]
    hits = set()
    for i in range(len(tmp)):
        print("{}\n{} <-> {}".format(hits, tmp[i], tmp[:i]+[-100]+tmp[i+1:len(tmp)]))
        if 60 - tmp[i] in (tmp[:i]+[-100]+tmp[i+1:len(tmp)]) and ((tmp[:i]+[-100]+tmp[i+1:len(tmp)]).index(60 - tmp[i]), i) not in hits:
            tmp2 = tmp[0:len(tmp)]
            while 60 - tmp[i] in (tmp2[:i]+[-100]+tmp2[i+1:len(tmp2)]):
                if ((tmp2[:i]+[-100]+tmp2[i+1:len(tmp2)]).index(60 - tmp[i]), i) not in hits:
                    res += 1
                    hits.add((i, (tmp2[:i]+[-100]+tmp2[i+1:len(tmp2)]).index(60 - tmp[i])))
                    break
                else:
                    tmp2[(tmp2[:i]+[-100]+tmp2[i+1:len(tmp2)]).index(60 - tmp[i])] = -100
        elif 30 - tmp[i] in (tmp[:i]+[-100]+tmp[i+1:len(tmp)]) and ((tmp[:i]+[-100]+tmp[i+1:len(tmp)]).index(30 - tmp[i]), i) not in hits:
            tmp2 = tmp[0:len(tmp)]
            while 30 - tmp[i] in (tmp2[:i]+[-100]+tmp2[i+1:len(tmp2)]):
                print(tmp[i])
                if ((tmp2[:i]+[-100]+tmp2[i+1:len(tmp2)]).index(30 - tmp[i]), i) not in hits:
                    if (times[i] + times[(tmp2[:i]+[-100]+tmp2[i+1:len(tmp2)]).index(30 - tmp[i])]) % 60 == 0:
                        res += 1
                        hits.add((i, (tmp2[:i]+[-100]+tmp2[i+1:len(tmp2)]).index(30 - tmp[i])))
                        break
                    else:
                        tmp2[(tmp2[:i]+[-100]+tmp2[i+1:len(tmp2)]).index(30 - tmp[i])] = -100 
                else:
                    tmp2[(tmp2[:i]+[-100]+tmp2[i+1:len(tmp2)]).index(30 - tmp[i])] = -100
        elif tmp[i] == 0 and tmp[i] in tmp[:i]+[-100]+tmp[i+1:len(tmp)]:
            tmp2 = tmp[0:len(tmp)]
            while 0 in (tmp2[:i]+[-100]+tmp2[i+1:len(tmp2)]):
                if ((tmp2[:i]+[-100]+tmp2[i+1:len(tmp2)]).index(0), i) not in hits:
                    res += 1
                    hits.add((i, (tmp2[:i]+[-100]+tmp2[i+1:len(tmp2)]).index(0)))
                    break
                else:
                    tmp2[(tmp2[:i]+[-100]+tmp2[i+1:len(tmp2)]).index(0)] = -100
    return res

times = [30, 20, 150, 100, 40]
print(numPairsDivisibleBy60(times))
times = [60,60,60]
print(numPairsDivisibleBy60(times))
times = [439,407,197,191,291,486,30,307,11]
print(numPairsDivisibleBy60(times))
times = [269,230,318,468,171,158,350,60,287,27,11,384,332,267,412,478,280,303,242,378,129,131,164,467,345,146,264,332,276,479,284,433,117,197,430,203,100,280,145,287,91,157,5,475,288,146,370,199,81,428,278,2,400,23,470,242,411,470,330,144,189,204,62,318,475,24,457,83,204,322,250,478,186,467,350,171,119,245,399,112,252,201,324,317,293,44,295,14,379,382,137,280,265,78,38,323,347,499,238,110,18,224,473,289,198,106,256,279,275,349,210,498,201,175,472,461,116,144,9,221,473]
print(numPairsDivisibleBy60(times))
