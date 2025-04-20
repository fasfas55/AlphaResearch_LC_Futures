# LC Futures Quantitative Strategy (2411 Contract)

This is a self-directed quant research project built on my real manual trades in Lithium Carbonate (LC) futures during June–July 2024. The goal is to understand price behavior, test trading logic, and explore whether statistical models can support short-term trend strategies.

---

## 📌 Project Overview

- **Instrument**: Lithium Carbonate Futures (LC2411), traded on GFE
- **Period Studied**: July 2023 – April 2025 (focus on 2024.06–2024.07 for live trades)
- **Data Source**: Wind API – daily futures & spot prices, open interest data
- **Tools**: Python (`pandas`, `statsmodels`, `backtesting.py`), WindPy

---

## 📈 Strategy Summary

My original trading idea was based on:
- A visible **downtrend** in LC futures after the contract launched
- **Low correlation** with other metals + high price autocorrelation
- Observed **short-dominant institutional positions**
- Supporting **macroeconomic sentiment**: EV demand, battery oversupply, weak spot prices

---

## 🧠 Quantitative Research Goals

- Engineer technical factors: **Bollinger bands**, **Golden Ratio bands**, trend zones
- Create BB_ZONE to label price structure
- Define and test `TARGET_DROP`: binary and multi-day return targets
- Fit **logistic regression (logit)** model to evaluate signal significance
- Backtest basic rule-based strategies using **backtesting.py**

---

## 🔬 Work in Progress

- Investigating stronger alpha factors (volume, momentum, OI delta)
- Improving statistical significance of zone-based logic
- Expanding to multi-day return targets and rolling windows
- Preparing generalized framework to apply across other futures contracts

---

## 📊 Real Trading Performance

| Metric | Value |
|--------|-------|
| Period | ~June 2024 – July 2024  
| Return | +42% (42,000 → 60,000 CNY)  
| Largest gain | 6,100 CNY in a single short  
| Strategy type | Short-biased, trend following, based on mean reversion signals

---

## 🗂️ Folder Structure
📁 data/ # Cleaned LC futures + spot + OI data 📁 scripts/ # Python files (backtest, model, indicators) 📁 images/ # Charts, visualizations README.md # Project summary

---

## 🤝 Credit

Built as a personal research and skill-building project to prepare for quantitative finance internships and MFE grad programs. Real trades and ideas are self-developed and based on Wind API data.



