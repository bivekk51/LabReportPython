import pandas as pd
import numpy as np
df=pd.DataFrame(np.random.randn(10,3),columns=['x','y','z'])
print("First 3 rows\n:",df.head(3))
print("\nLast 2 rows:\n",df.tail(2))