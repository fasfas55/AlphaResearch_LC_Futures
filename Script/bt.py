from backtesting import Backtest, Strategy
from backtesting.lib import crossover
import pandas as pd

# Load and prep data
df = pd.read_excel('LC.xlsx')
df = df.rename(columns={'Unnamed: 0':'Date'})
df['Date'] = pd.to_datetime(df['Date'])
df = df.sort_values("Date").reset_index(drop=True)

# Rename columns to OHLCV
df = df.rename(columns={
    'CLOSE': 'Close',
    'HIGH': 'High',
    'LOW': 'Low',
    'VOLUME': 'Volume'
})

# Create fake Open prices if not available
df['Open'] = df['Close']
df = df[['Date', 'Open', 'High', 'Low', 'Close', 'Volume']]

# Set datetime index
df.set_index("Date", inplace=True)

# Strategy for plotting bands
class BollingerGoldenStrategy(Strategy):
    def init(self):
        close = self.data.Close
        self.bb_mid = self.I(lambda x: pd.Series(x).rolling(20).mean(), close)
        std = self.I(lambda x: pd.Series(x).rolling(20).std(), close)
        self.bb_upper = self.I(lambda m, s: m + 2 * s, self.bb_mid, std)
        self.bb_lower = self.I(lambda m, s: m - 2 * s, self.bb_mid, std)
        self.bb_golden_upper = self.I(lambda m, u: m + 0.618 * (u - m), self.bb_mid, self.bb_upper)
        self.bb_golden_lower = self.I(lambda m, l: m - 0.618 * (m - l), self.bb_mid, self.bb_lower)

    def next(self):
        price = self.data.Close[-1]
        # if not self.position:
        if crossover(self.bb_golden_lower,price):
            self.sell()
        elif crossover(self.bb_mid,price):
            self.sell()
        elif crossover(price,self.bb_upper):
            self.sell()
        elif crossover(price,self.bb_lower):
            self.buy()
        elif crossover(price,self.bb_golden_upper):
            self.buy()
        elif crossover(price,self.bb_mid):
            self.buy()
        # if self.position.is_long:
        #     if crossover(price,self.bb_upper):
        #         self.position.close()
        #     else: pass
        # if self.position.is_short:
        #     if crossover(self.bb_lower,price):
        #         self.position.close()
        #     else: pass



# Run backtest and plot
bt = Backtest(df, BollingerGoldenStrategy, cash=1000000, commission=.002)
stats = bt.run()
print(stats)
bt.plot()
