#!/usr/bin/env python3
"""Simple forecast for UWM Holdings Corp (UWMC) price hitting $6.

This script downloads historical price data using yfinance, fits an ARIMA
model, forecasts future prices, and estimates the first date the closing
price is predicted to exceed $6. The forecast is purely educational and
not financial advice.
"""
import pandas as pd
import yfinance as yf
from statsmodels.tsa.arima.model import ARIMA

TICKER = "UWMC"
PRICE_TARGET = 6.0
FORECAST_DAYS = 365

# Download two years of daily data
history = yf.download(TICKER, period="2y")
if history.empty:
    raise SystemExit("No data downloaded")

# Use closing prices
series = history["Close"].dropna()
series.index = pd.to_datetime(series.index)

# Fit simple ARIMA(1,1,1)
model = ARIMA(series, order=(1,1,1))
fit = model.fit()

# Forecast future closing prices
forecast = fit.forecast(steps=FORECAST_DAYS)
forecast.index = pd.date_range(series.index[-1] + pd.Timedelta(days=1), periods=FORECAST_DAYS)

# Find first date price predicted to exceed target
above_target = forecast[forecast >= PRICE_TARGET]
if not above_target.empty:
    target_date = above_target.index[0].date()
    print(f"Predicted date price exceeds ${PRICE_TARGET}: {target_date}")
else:
    print(f"Forecast does not reach ${PRICE_TARGET} in next {FORECAST_DAYS} days")
