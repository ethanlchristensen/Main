import sys
sys.path.append("..")

import random
from hash_table import hash_table

my_hash = hash_table.hash_table(10)
for i in range(20):
    my_hash[str(random.randint(1,10000))] = random.randint(1,10000)
my_hash.print_hash()