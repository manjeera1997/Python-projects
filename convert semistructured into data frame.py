import pandas as pd
import matplotlib.pyplot as plt
import requests
import io
url = 'https://www.metoffice.gov.uk/pub/data/weather/uk/climate/stationdata/heathrowdata.txt'
file = io.StringIO(requests.get(url).text)
col_names = ('Year','Month','Tmax','Tmin','AF','Rain','Sun')
comment_lines = 4
header = 2
weather = pd.read_csv(file,
   skiprows=comment_lines + header,
   header=0,
   names=col_names,
   delimiter=' ',
   skipinitialspace=True,
   error_bad_lines=False)

file.seek(0)
col_names = ('Year','Month','Tmax','Tmin','AF','Rain','Sun', 'Status')
rows_to_skip = comment_lines+header+len(weather)
weather2 = pd.read_csv(file,
   skiprows=rows_to_skip,
   header=0,
   names=col_names,
   delimiter=' ',
   skipinitialspace=True,
   error_bad_lines=False)
weather['Status']='Final'
weather = weather.append(weather2, ignore_index=True)
print(weather)
weather.dtypes
weather['Sun']=weather['Sun'].str.replace('#','')
weather['AF']=pd.to_numeric(weather['AF'], errors='coerce')
weather['Sun']=pd.to_numeric(weather['Sun'], errors='coerce')
weather[weather.Year==2000].plot(x='Month', y='Rain')
ax = weather[weather.Year==1950].plot(x='Month', y='Tmax',
   label='1950')
ax = weather[weather.Year==1960].plot(x='Month', y='Tmax', 
   label='1960',ax=ax)
ax = weather[weather.Year==1970].plot(x='Month', y='Tmax',  
   label='1970',ax=ax)
ax = weather[weather.Year==1980].plot(x='Month', y='Tmax', 
   label='1980',ax=ax)
ax = weather[weather.Year==1990].plot(x='Month', y='Tmax', 
   label='1990',ax=ax)
ax = weather[weather.Year==2000].plot(x='Month', y='Tmax', 
   label='2000',ax=ax)
weather[weather.Year==2019].plot(x='Month', y='Tmax', label = 
   '2010', ax=ax, figsize=(15,10))
