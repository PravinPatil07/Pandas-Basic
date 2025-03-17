import pandas as pd

x = [1, 2, 3, 4, 5]

# Create a Series
series = pd.Series(x)
print(series)

'''
Output:
0    1
1    2
2    3
3    4
4    5
dtype: int64
'''

print("3rd index no. is : ",series[3])

y = [6, 7, 8, 9, 10]

# Create a Series with custom index
series_custom_index = pd.Series(y, index=['a', 'b', 'c', 'd', 'e'],dtype=float)
print(series_custom_index)
'''
Output:
a     6
b     7
c     8
d     9
e    10
dtype: float64
'''

