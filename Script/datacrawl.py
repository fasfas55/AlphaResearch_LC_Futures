from WindPy import w
import pandas as pd

w.start()
w.isconnected()

data1 = w.wsd("LC01.GFE", "close,oi,volume,high,low,oi_nvoi",
              "2023-7-21", "2024-08-01", "order=40;")
data2 = w.edb("C6154032", "2023-11-21", "2024-08-01")

df = pd.DataFrame(data1.Data,index=data1.Fields,columns=data1.Times)
df2 = pd.DataFrame(data2.Data,index=["spot_price"],columns=data2.Times)

df = df.T
df2 = df2.T

df = df.merge(df2, left_index=True, right_index=True, how='left')
df["spot_price"] = df["spot_price"].fillna(0)
df['OI_NVOI'] = df['OI_NVOI'].fillna(0)

df.to_excel('LC2.xlsx')
