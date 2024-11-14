import pandas as pd 
df=pd.read_csv('input.csv')
df['NewColumn']=df['ExistingColumn']*2
df_filtered=df[df['ExistingColumn']>10]
df_filtered.to_csv('output.csv',index=False)