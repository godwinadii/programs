import pandas as pd
technologies = {
    'Courses': ["Python", "DBMS", "JAVA", "Python", "Spark"],
    'Fee': [70000,45000,36000,88000,17000],
    'Duration': ['30day', '40days', '35days', '60days', '30days'],
    'Discount': [1000, 2300, 1200, 2500, 2000]
                }
df = pd.DataFrame (technologies)
print(df)