from game import character
import random

def test_stat_iter():
    c = character.Character('desc', 'test', 0)
    stats = c.stats
    print(c.stats.__dict__)
    for x,y in stats:
        print (y)

def test_stat_assign():
    c = character.Character('desc', 'test', 0)
    for x, y in c.stats:
        base = int(1 + random.random() * 10)
        mod = int(random.random() * 10)
        c.stats.__dict__[x] = (base, mod, base+mod)

    for x, y in c.stats:
        print((x,y))

