import pandas as pd
import matplotlib.pyplot as plt

url = "https://data.cityofnewyork.us/api/views/6fi9-q3ta/rows.csv?accessType=DOWNLOAD"
df = pd.read_csv(url)

df['hour_beginning'] = pd.to_datetime(df['hour_beginning'])

df['hour'] = df['hour_beginning'].dt.hour
df['month'] = df['hour_beginning'].dt.month
df['date'] = df['hour_beginning'].dt.date
df['day_name'] = df['hour_beginning'].dt.day_name()

weekday_data = df[df['day_name'].isin(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'])]
weekday = weekday_data.groupby('day_name')['Pedestrians'].sum()

weekdays_ordered = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
weekday = weekday.reindex(weekdays_ordered)

plt.figure(figsize=(12, 6))
plt.plot(weekday.index, weekday.values, color='blue')
plt.title('Pedestrian Count (Mon-Fri)')
plt.xlabel('Day of the Week')
plt.ylabel('Pedestrian Count')
plt.grid(True)
plt.tight_layout()
plt.show()
