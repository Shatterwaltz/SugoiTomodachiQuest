from game import character
from game import stats
import random
import pprint

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

def test_stat_gen():
    print('\nTEST: test_stat_gen, CLASS: Character, FUNCTION: genStats')
    c = character.Character('desc', 'test', 0)
    s = stats.Stats()

    s.health        = (5,0)
    s.armor         = (4,0)
    s.power         = (3,0)
    s.evasion       = (6,0)
    s.accuracy      = (4,0)
    s.speed         = (6,0)
    s.strength      = (3,0)
    s.luck          = (4,0)
    s.resistance    = (5,0)

    c.genStats(s)
    
    print('\nbase stats')
    #print(s.__dict__.items())
    for s, v in s:
        pprint.pprint((s,v))
    print('\ncharacter stats')    
    for s, v in c.stats:
        pprint.pprint((s,v))

def test_stat_apply():
    print('\nTEST: test_stat_apply, CLASS: Character, FUNCTION: applyStats')

    c = character.Character('desc', 'test', 0)
    s = stats.Stats()

    s.health        = (5,0)
    s.armor         = (4,0)
    s.power         = (3,0)
    s.evasion       = (6,0)
    s.accuracy      = (4,0)
    s.speed         = (6,0)
    s.strength      = (3,0)
    s.luck          = (4,0)
    s.resistance    = (5,0)

    statMod = stats.Stats()
        
    statMod.health        = (0,5)
    statMod.armor         = (0,1094987498798739875098209809409875630938709270)
    statMod.power         = (0,0)
    statMod.evasion       = (0,0)
    statMod.accuracy      = (0,10)
    statMod.speed         = (0,0)
    statMod.strength      = (0,10000)
    statMod.luck          = (0,0)
    statMod.resistance    = (0,0)
    
    c.genStats(s)

    print('\ncharacter stats')    
    for s, v in c.stats:
        pprint.pprint((s,v))

    c.applyStats(statMod)

    print('\nmodded character stats')
    for s, v in c.stats:
        pprint.pprint((s,v))


