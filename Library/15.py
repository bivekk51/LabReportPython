import pandas as pd
data={
    "Name:":['Dino', 'Bhakka', 'Bibek'],
    "Age:":[25, 30, 28],
    "City:":["Delhi", "Mumbai", "Chennai"]
}
df=pd.DataFrame(data)
print("DataFrame:\n",df)