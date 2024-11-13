import pandas as pd

df = pd.DataFrame({
    "student": ['Angela', 'James', 'Lily'],
    "score": [56, 76, 98]
})

# for (col_name, col_values) in df.items():
#     print(col_values)

for (row_index,row_values) in df.iterrows():
    print(row_index)
    print(row_values.student)
    print(row_values.score)