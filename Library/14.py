import pandas as pd
series=pd.Series([1,2,3,4,5])
print(series)
df=pd.DataFrame({
    'A':[10,20,30,40,50,],
    'B':[15,20,25,30,35,],
    'C':[100,200,300,400,500,]
})
print("\nDataFrame:\n",df)