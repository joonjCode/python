import pickle
import pandas as pd 
data = [{'name':'Niz'}]
# with open('users.pkl', 'wb') as f:
# 	pickle.dump(data,f) # no dumps 

data_from_pkl = pickle.load(open('users.pkl', 'rb'))
# print(data_from_pkl)


df = pd.DataFrame(data)
# df.head()
df.to_pickle('df_pkl')
df2 = pd.read_pickle('df_pkl')
# print(df2)