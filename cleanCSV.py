#!/home/codespace/.python/current/bin/python
import pandas as pd
import sys

csv_file=sys.argv[1]
clean_file=sys.argv[2]
df=pd.read_csv(csv_file)
print(f"Initial row count: {len(df)}")

df_noNaN = df.dropna(inplace=True)
print (f"Row count after removing NaNs: {len(df_noNaN)}")

duplicate_count=df_noNan.duplicated().sum()
print (f"Number of duplicate rows: {duplicate_count}")
df_clean=df_noNan.drop_duplicates(inplace=True)
print (f"Row count after removing duplicates: {len(df_clean)}"

df_clean.to_csv(df_clean, index=False)
print(f"Cleaned file saved as: {df_clean}")
