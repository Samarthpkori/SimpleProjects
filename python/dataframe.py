import pandas as pd
df=pd.read_excel("expy.xlsx")

print("dataframe from xl file")
print(df)
print("--------")

df[marks]=pd.series([10,20,30,40,50,60])
print("dataframe after adding one column")
print(df)
print("------------")

print("dataframe after deleting particular column")
del df("rno")
print(df)

print("------------")
print("selected row")
print(df.d[3]) 