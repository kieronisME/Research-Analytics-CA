import pandas as pd 
print("\nis this thing on?\n")

df = pd.read_csv('Customers_list.csv')

print(df.to_string()) 