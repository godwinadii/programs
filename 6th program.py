import pandas as pd
df = pd.DataFrame([[9,4,8,9],
                [8,10,7,6],
                [7,6,8,5]],
                columns=['maths','english',
                         'science','history'])

print(df)
df.agg(['sum','min','max','mean','median','std','count','size',])