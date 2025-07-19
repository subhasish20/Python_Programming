import numpy as np
import pandas as pd

a = 'asedresaedtfeaaasedftreaa'

l = []
for i in a:
    l.append(i)
    

arr = np.array(sorted(l))


print(np.unique(arr))