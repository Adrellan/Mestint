## Nem informált keresési stratégiák

---

Példák a nem informált keresési stratégiákhoz:

- Szélességi keresés (Breadt first)
- Mélységi keresés (Depth first)
- Egyenletes költségű keresés (Uniform cost)
- Mélységkorlátozott keresés (Depth limited)
- Interatívan mélyülő mélységi keresés (Iteratie depth first)


````python
#FIFO -> Azt vesszük ki elsőnek, amit beraktunk. 
from collections import deque

que = deque([1,2,3,4])

for i in range (2):
    print(que.popleft())

print(que)
````