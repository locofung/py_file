import pandas as pd
df=pd.read_csv(r'C:\Users\loco_fung\StudentsPerformance.csv')
df.head(5)



df=pd.DataFrame({'Name':['JOHN','ALLEN','BOB','NIKI','CHARLIE','CHANG'],
              'Age':[35,42,63,29,47,51],
              'Salary_in_1000':[100,93,78,120,64,115],
             'FT_Team':['STEELERS','SEAHAWKS','FALCONS','FALCONS','PATRIOTS','STEELERS']})
df

df.loc[0:3,['Name','Age']]
df.loc[:,['Name','Age','FT_Team']]

df.query('Age<=60 & Salary_in_1000 >= 100')
df.query('Age<=60 and Salary_in_1000 >= 100')

df.query('Age<=60 | Salary_in_1000 >= 100')
df.query('Age<=60 or Salary_in_1000 >= 100')

#like function
df.query('FT_Team.str.contains("P")')
df.query('(Age<=60 or Salary_in_1000 >= 100) and FT_Team.str.contains("P")')

#subquery
df.query('Age==Age.max()')

#combine condition
#data.groupby('company').agg({'salary':'median','age':'mean'})
#gkk = df.groupby(['Team', 'Position'])
#df.groupby('A').agg({'B': ['min', 'max'], 'C': 'sum'})
df.groupby('FT_Team').first() # add to .first() 
df.groupby('FT_Team').agg({'Age':'mean'})





