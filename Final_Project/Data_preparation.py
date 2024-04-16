import folium
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from folium.plugins import HeatMap

df = pd.read_csv('Motor_Vehicle_Collisions_-_Crashes_20240409.csv')

#Dropping NaN for longitude and latitude:
df = df.dropna(subset=['LONGITUDE'])

#Changing Crash Date to datetime format:
df['CRASH DATE'] = pd.to_datetime(df['CRASH DATE'])
df = df.sort_values(by='CRASH DATE')
#Removing years 2012 and 2024
df['YEAR'] = df['CRASH DATE'].dt.year
df = df[(df['YEAR'] != 2012) & (df['YEAR'] != 2024)]






