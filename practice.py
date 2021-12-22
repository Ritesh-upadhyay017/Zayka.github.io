import pandas as pd

s1 = pd.Series([1,2,3,4,5])
s2 = pd.Series([11,22,33,44,55])
s3 = pd.Series([111,222,333,444,555])

df = pd.DataFrame([s1,s2,s3], index = ['a','b','c'], columns = ['v','w','x','y','z'])

print(df)
print(s1)
