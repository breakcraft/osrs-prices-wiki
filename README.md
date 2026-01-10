<h1 align="center">
  osrsprices.wiki
</h1>

<p align="center">
  OldSchool Runescape Live GE Prices Utilities
</p>

<div align="center">
  <img alt="Screenshot" width="800" src=https://github.com/nikosdaridis/osrs-prices-wiki/raw/main/Screenshot1.png>
  <img alt="Screenshot" width="800" src=https://github.com/nikosdaridis/osrs-prices-wiki/raw/main/Screenshot2.png>
</div>

## 🛠 Installation

1. Node.js has to be installed to build the project

2. Watch for TypeScript and Tailwind changes by opening a terminal in /Server and running

   ```sh
   npm run dev-watch
   ```

## UWM Price Forecast Script

A simple forecasting script is available under `scripts/uwm_price_forecast.py`.
It downloads historical prices using `yfinance`, fits an ARIMA model, and
predicts when UWM Holdings Corp (ticker `UWMC`) might exceed $6 per share.

The script is intended for educational purposes only and should not be
considered financial advice. Run it with:

```bash
python3 scripts/uwm_price_forecast.py
```
