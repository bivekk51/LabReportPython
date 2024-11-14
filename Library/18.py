import pandas as pd
import numpy as np
df=pd.DataFrame({
    'A:':[1,2,np.nan,4,5],
    'B:':[np.nan,2,3,4,5],
    'C:':[1,2,3,np.nan,5]
})
df.fillna(df.mean(),inplace=True)
print("dataFrame with NaNs filled:\n",df)