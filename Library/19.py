import pandas as pd
df=pd.DataFrame({
    'A': [10, 20, 30, 40, 50],
    'B': [15, 25, 35, 45, 55],
    'C': [20, 30, 40, 50, 60]
})
print("Column A:\n",df['A'])
print("\nRow 2:\n", df.iloc[2])
print("\nSubset:\n", df.loc[1:3, ['A', 'B']])