import pandas as pd
# state_name = input('input state: ')
df = pd.read_csv('fips-by-state.csv', encoding = 'unicode_escape')
for state in df['state'].unique():
    print('"'+state+'": ' + str(list(df[df['state'] == state]['name'])))