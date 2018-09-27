
import collections

def thg435(l):
    return [x for x, y in collections.Counter(l).items() if y > 1]

def moooeeeep(l):
    seen = set()
    seen_add = seen.add
    seen_twice = set( x for x in l if x in seen or seen_add(x) )
    return list( seen_twice )

def RiteshKumar(l):
    return list(set([x for x in l if l.count(x) > 1]))

def JohnLaRooy(L):
    seen = set()
    seen2 = set()
    seen_add = seen.add
    seen2_add = seen2.add
    for item in L:
        if item in seen:
            seen2_add(item)
        else:
            seen_add(item)
    return list(seen2)

l = [1,2,3,2,1,5,6,5,5,5]*100
