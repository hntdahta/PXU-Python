import pandas as pd

a = pd.read_excel("C:\Desktop\Test.xlsx")
a1 = a.head(10)
print(a)

url = r'https://www1.ncdc.noaa.gov/pub/data/cdo/samples/PRECIP_HLY_sample_csv.csv'
df = pd.read_csv(url)
df1 = df.head(10)
print(df1)

js = pd.read_json("https://raw.githubusercontent.com/domoritz/maps/master/data/iris.json")
js1 = js.head(10)
print(js1)
