import pandas as pd 
#1.create df from 2 Sep list
list_values = ['English', 'Hindi', 'Mathematics', 'Science', 'Social Science']  
list_index = [20, 21, 22, 23, 24]  
df1=pd.DataFrame(data=list(zip(list_values,list_index)),columns=['values','inx'])
df1

#2.Creating Pandas DataFrame from Multidimensional List
data=[['Tokyo', 'West', 110], ['Paris', 'West', 103], ['Osaka', 'South', 145], ['Sidney', 'East', 190]]
df2=pd.DataFrame(data=data,columns=['city','name','age'])
df2



#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#simple dict to df
data = {'name': ['nick', 'david', 'joe', 'ross'],
        'age': ['5', '10', '7', '6']} 
new = pd.DataFrame.from_dict(data)
new #columns=['names','ages'] canot use




#3.create df from dict
data ={'area': ['new-hills', 'cape-town', 'mumbai'],
       'rainfall':[100, 70, 200],
       'temperature':[20, 25, 39]}
  
df3=pd.DataFrame.from_dict(data=data)
df3

#orient='index' ,column names can be specified manually
df3a=pd.DataFrame.from_dict(data=data,orient ='index',columns=
                            ['c1','c2','c3'])
df3a


#skill full solution
df3b=pd.DataFrame(data=data.values(),columns=['c1','c2','c3'])
df3b

#4 speicfial case 
data = {
    '2022-01-01': [5, 7, 5],
    '2022-01-02': [7, 5, 6],
    '2022-01-03': [7, 4, 4],
    '2022-01-04': [7, 2, 10]
}
data_new=[(k,val) for k,val in data.items()]
data_new

data_new_2=data_new=[(k,val) for k,vals in data.items() for val in vals ]
data_new_2
df4=pd.DataFrame.from_dict(data=data_new)
df4
