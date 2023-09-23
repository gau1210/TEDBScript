import pandas as pd
from glob import glob

df_all_auto = pd.DataFrame(None)
for filename in glob("D:\\UNEB\\2023.2\\TEDB\\Trabalho Semestre\Bases\\Internação\\Combinada\\*.csv"):
    df = pd.read_csv(filename, sep='|', encoding='latin-1')

    df_all_auto = pd.concat([df_all_auto, df])

print(df_all_auto)

df_all_auto.to_csv('D:\\UNEB\\2023.2\\TEDB\\Trabalho Semestre\Bases\\Internação\\Combinada\\consolidado.csv', index=False)

