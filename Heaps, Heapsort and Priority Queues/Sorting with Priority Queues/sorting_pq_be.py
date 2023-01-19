from easyinput import read
from heapq import heappush, heappop
"""
Use priority queues to sort a sequence of integer numbers, in nondecreasing order and also in nonincreasing order.
"""

n = read(int)
pq_s = []
pq_l = []
while n is not None:    # Anar ficant per a mantenir min heap
    heappush(pq_s, n)
    heappush(pq_l, -n)
    n = read(int)
if len(pq_s) > 0:   # Primer a banda i després tots els que queden
    print(heappop(pq_s), end='')
while len(pq_s) > 0:
    print(' ' + str(heappop(pq_s)), end='')
print()
if len(pq_l) > 0:
    print(-heappop(pq_l), end='')
while len(pq_l) > 0:
    print(' ' + str(-heappop(pq_l)), end='')
print()