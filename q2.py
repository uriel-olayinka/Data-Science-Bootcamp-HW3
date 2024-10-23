import pandas as pd2
import matplotlib.pyplot as plt2
import seaborn as sns

url = "https://data.cityofnewyork.us/api/views/6fi9-q3ta/rows.csv?accessType=DOWNLOAD"
df2 = pd2.read_csv(url)

df2['hour_beginning'] = pd2.to_datetime(df2['hour_beginning'])

df2['hour'] = df2['hour_beginning'].dt.hour
df2['month'] = df2['hour_beginning'].dt.month
df2['date'] = df2['hour_beginning'].dt.date
df2['day_name'] = df2['hour_beginning'].dt.day_name()

df2_2019 = df2[(df2['hour_beginning'].dt.year == 2019) & (df2['location'] == 'Brooklyn Bridge')]
df2_2019_filtered = df2_2019[['hour_beginning', 'Pedestrians', 'weather_summary', 'temperature', 'precipitation']]
df2_2019_encoded = pd2.get_dummies(df2_2019_filtered, columns=['weather_summary'], prefix="weather")

corr_matrix = df2_2019_encoded[['Pedestrians', 'temperature', 'precipitation']].corr()

plt2.figure(figsize=(8, 6))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt=".2f")
plt2.title('Correlation Matrix of Weather Patterns and Pedestrian Counts on Brooklyn Bridge in 2019')
plt2.tight_layout()
plt2.show()

