import pandas as pd
import os

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

df = pd.read_excel(r'C:/Users/Alex/Desktop/SENECA/Semester 4/BDB 400/case study/bankOfCanadaLoans.xlsx', sheet_name='factTable')

df[['Year','Quarter']] = df.Date.str.split("Q",expand=True,)
df = df.iloc[: , 1:]

with pd.ExcelWriter('bankOfCanadaLoans.xlsx', engine="openpyxl", mode='a') as writer:  
    df.to_excel(writer, sheet_name='cleanFactTable')