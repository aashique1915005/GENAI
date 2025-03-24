import pandas as pd

states = ["California","Texas","Florida","New York"]
population = [45678923,45671223,8793456,12334578]

dict_states = {'States':states, 'Population':population }

df_states = pd.DataFrame.from_dict(dict_states)

print(df_states)

# df_states.to_csv('statespopulationdetails.csv')
df_states.to_csv('statespopulationdetails.csv' , index=False)