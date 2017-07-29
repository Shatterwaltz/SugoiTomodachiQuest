"""from test import charactertest
from test import configtest
from test import mapGenTest"""
from test import gearTest

from game import stats
from game import character
from game import gear

# tests or whatever
"""
# Test the character class
charactertest.test_stat_assign()
charactertest.test_stat_gen()
charactertest.test_stat_apply()

# Test the config files
configtest.test_config_read()

#Test mapGen class
mapGenTest.test_map_gen()
gearTest.gear_test(10)"""

#Test char stuff

boy = character.Character(0,0,0)
for stat in boy.stats:
    print(stat)


