import panads as pd

df1 = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3', 'K4', 'K5'],
                   'A': ['A0', 'A1', 'A2', 'A3', 'A4', 'A5'],
                   'age':[10,20,30,40,50,60]
                   })                    '
df2 = pd.DataFrame({'keys': ['K0', 'K1', 'K2'],
                      'B': ['B0', 'B1', 'B2'],
                      'dept':['IT','HR','REMIT']
                })
                      '
                                               
df3=pd.merge(df1,df2, how='left', left_on='key', right_on='keys')
df3

#get speficic columns on 
df4=pd.merge(df1.loc[''],df2, how='left', left_on='key', right_on='keys').loc['A','B','key']
df3

df1.loc[:,['A','age','key']]
df2.loc[:,['B','keys']]
df4=pd.merge(df1.loc[:,['A','age','key']],df2.loc[:,['B','keys']]
             ,how='left',left_on='key', right_on='keys').drop(columns=['keys'])
df4

mergedCSV.to_csv('output.csv',index = False)