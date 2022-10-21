import os
import pandas as pd 

data_arquivo_pasta = 'data'

df = []

for file in os.listdir(data_arquivo_pasta):
    if file.endswith('xlsx'):
        print('Carregando arquivo {0}...'.format(file))
        df.append(pd.read_excel(os.path.join(data_arquivo_pasta, file)))

print(len(df))

df_principal = pd.concat(df, axis=0)
df_principal.to_excel('data/planilhas-unificadas.xlsx', index=False) 