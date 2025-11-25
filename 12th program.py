import pandas as pd

data = {
    'Student': ['Alice', 'Bob', 'Charlie', 'David'],
    'Chemistry': [85, 78, 90, 88],
    'Physics': [92, 80, 85, 91],
    'Mathematics': [88, 82, 87, 90],
    'English': [75, 85, 80, 78],
    'Total': [340, 325, 342, 347]
}

df = pd.DataFrame(data)

if 'Total' in df.columns:
    df = df.drop(columns=['Total'])

total_marks = df[['Chemistry', 'Physics', 'Mathematics', 'English']].sum()
print(total_marks)
