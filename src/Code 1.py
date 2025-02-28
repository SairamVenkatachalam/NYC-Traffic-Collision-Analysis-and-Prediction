#%%

import pandas as pd

file_path = "C:/Users/saira/OneDrive/Desktop/GWU Courses/Into to Data Mining/Project/Datasets/Crashes.csv"
df = pd.read_csv(file_path)

df.head(15)

# %%
df.shape
# %%
df.tail()
# %%
df['CRASH DATE'] = pd.to_datetime(df['CRASH DATE'])
df['Year'] = df['CRASH DATE'].dt.year
# %%
df.head()
# %%
df['Year'].unique()
# %%
df['Year'].value_counts()
# %%
import matplotlib.pyplot as plt
import seaborn as sns

yearly_counts = df['Year'].value_counts().reset_index()
yearly_counts.columns = ['Year', 'Count']

plt.figure(figsize=(10, 6))
sns.barplot(data=yearly_counts, x='Year', y='Count')
plt.title('Counts of Data Points by Year')
plt.xlabel('Year')
plt.ylabel('Count')
plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
plt.show()

# %%

df['CRASH TIME'] = pd.to_datetime(df['CRASH TIME'])
df['Hour'] = df['CRASH TIME'].dt.hour

plt.figure(figsize=(12, 6))
sns.violinplot(data=df, y='Hour')
plt.title('Distribution of Crash Times by Hour')
plt.xlabel('Hour of the Day')
plt.ylabel('Frequency')
plt.show()

# %%
df.head()


# %%

rush_hour_start = 7
rush_hour_end = 9

rush_hour_data = df[(df['Hour'] >= rush_hour_start) & (df['Hour'] <= rush_hour_end)]

location_counts = rush_hour_data['BOROUGH'].value_counts()

# Plot the accident hotspots
location_counts.plot(kind='bar')
plt.title("Accident Hotspots during Rush Hour")
plt.xlabel("Borough")
plt.ylabel("Number of Accidents")
plt.show()

# %%
import folium
from folium.plugins import HeatMap

rush_hour_data = df[(df['Hour'] >= rush_hour_start) & (df['Hour'] <= rush_hour_end)]

m = folium.Map(location=[40.7128, -74.0060], zoom_start=10)

locations = rush_hour_data[['LATITUDE', 'LONGITUDE']].dropna()

# Define the color gradient for the heatmap
gradient = {
    0.2: 'blue',
    0.4: 'green',
    0.6: 'orange',
    1.0: 'red'
}

# Create a heatmap layer with the color scale
HeatMap(data=locations, gradient=gradient, radius=15).add_to(m)

# Display the map
m

# %%
