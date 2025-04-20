import pandas as pd

df = pd.read_excel('LC2.xlsx')
df = df.rename(columns={'Unnamed: 0':'Date'})
df['Date'] = pd.to_datetime(df['Date'])
df = df.sort_values("Date").reset_index(drop=True)

# Bollinger Bands
df["BB_MID"] = df["CLOSE"].rolling(window=20).mean()
df["BB_STD"] = df["CLOSE"].rolling(window=20).std()
df["BB_UPPER"] = df["BB_MID"] + 2 * df["BB_STD"]
df["BB_LOWER"] = df["BB_MID"] - 2 * df["BB_STD"]

df["BB_GOLDEN_UPPER"] = df["BB_MID"] + 0.618 * (df["BB_UPPER"] - df["BB_MID"])
df["BB_GOLDEN_LOWER"] = df["BB_MID"] - 0.618 * (df["BB_MID"] - df["BB_LOWER"])

def bbzone(row):
    if row['CLOSE'] > row['BB_UPPER']:
        return 6 # significantly overbuy
    elif row['BB_GOLDEN_UPPER'] < row['CLOSE'] <= row['BB_UPPER']:
        return 5 # breaking
    elif row['BB_MID'] < row['CLOSE'] <= row['BB_GOLDEN_UPPER']:
        return 4 # recovery
    elif row['BB_GOLDEN_LOWER'] < row['CLOSE'] <= row['BB_MID']:
        return 3 # recession
    elif row['BB_LOWER'] < row['CLOSE'] <= row['BB_GOLDEN_LOWER']:
        return 2 #  depressing
    elif row['CLOSE'] <= row['BB_LOWER']:
        return 1 # significant oversell
    else:
        pass
df["BB_ZONE"] = df.apply(bbzone, axis=1)

# Calculate returns and shifted targets
df["RETURN"] = df["CLOSE"].pct_change()
df["RETURN_t+1"] = df["RETURN"].shift(-1)
df["TARGET_DROP"] = (df["RETURN_t+1"] < 0).astype(int)

# Rolling high
df["ROLLING_HIGH_5"] = df["HIGH"].rolling(window=5).max()
df["DROP_FROM_HIGH_5"] = (df["CLOSE"] - df["ROLLING_HIGH_5"]) / df["ROLLING_HIGH_5"]

# Institutional position delta and basis
df["DELTA_NET_OI"] = df["OI_NVOI"].diff()
df["BASIS"] = df["CLOSE"] - df["spot_price"]

# Volatility feature: intraday range scaled by close
df["VOLATILITY"] = (df["HIGH"] - df["LOW"]) / df["CLOSE"]

# dependent and independent variables
X = ["DROP_FROM_HIGH_5", "TREND_FLAG", "DELTA_NET_OI", "BASIS", "VOLATILITY"]
Y = "TARGET_DROP"

df.to_stata("LC2.dta", write_index=False)