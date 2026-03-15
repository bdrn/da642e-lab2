import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('IOT-temp.csv')

# Convert noted_date to datetime objects for processing
# dayfirst=True is used as the format in the CSV is DD-MM-YYYY
df['noted_date'] = pd.to_datetime(df['noted_date'], dayfirst=True)

# Filter for the last week (02-12-2018 to 08-12-2018)
last_week_df = df[(df['noted_date'] >= '2018-12-02') & (df['noted_date'] < '2018-12-09')]

# Separate In and Out for plotting
indoor = last_week_df[last_week_df['out/in'] == 'In'].sort_values('noted_date')
outdoor = last_week_df[last_week_df['out/in'] == 'Out'].sort_values('noted_date')

plt.figure(figsize=(12, 6))
plt.plot(indoor['noted_date'], indoor['temp'], label='Indoor', color='blue')
plt.plot(outdoor['noted_date'], outdoor['temp'], label='Outdoor', color='red')
plt.xlabel('Time')
plt.ylabel('Temperature (degrees Celsius)')
plt.title('Indoor and Outdoor Temperatures (2018-12-02 to 2018-12-08)')
plt.legend()
plt.grid(True)
plt.savefig('last_week_temp.png')
plt.show()

# make a copy for modifications
df_mod = df.copy()

# A. Change In/Out to 1/0
df_mod['out/in'] = df_mod['out/in'].replace({'In': 1, 'Out': 0})

# B. Separate Date and Time into two columns
df_mod['Date'] = df_mod['noted_date'].dt.date
df_mod['Time'] = df_mod['noted_date'].dt.time

# C. Keep only data of the last day (08-12-2018)
target_date = pd.to_datetime('2018-12-08').date()
df_final = df_mod[df_mod['Date'] == target_date]

# Save the modified CSV
df_final.to_csv('modified_iot_data.csv', index=False)