import pandas as pd3
import matplotlib.pyplot as plt3

url = "https://data.cityofnewyork.us/api/views/6fi9-q3ta/rows.csv?accessType=DOWNLOAD"
df3 = pd3.read_csv(url)

df3['hour_beginning'] = pd3.to_datetime(df3['hour_beginning'])
df3['hour'] = df3['hour_beginning'].dt.hour


def categorize_time_of_day(hour):
    if 5 <= hour < 12:
        return 'morning'
    elif 12 <= hour < 17:
        return 'afternoon'
    elif 17 <= hour < 20:
        return 'evening'
    else:
        return 'night'


df3['time_of_day'] = df3['hour'].apply(categorize_time_of_day)

ped_activity_patterns = df3.groupby('time_of_day')['Pedestrians'].sum().reindex(['morning', 'afternoon', 'evening', 'night'])
plt3.figure(figsize=(12, 6))
ped_activity_patterns.plot(kind='bar', color='orange')
plt3.title('Pedestrian Counts by Time of Day')
plt3.xlabel('Time of Day')
plt3.ylabel('Pedestrian Count')
plt3.xticks(rotation=0)
plt3.grid(axis='y')
plt3.tight_layout()
plt3.show()
