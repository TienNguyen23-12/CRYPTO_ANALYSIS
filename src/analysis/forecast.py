import pandas as pd

def moving_average_forecast(df, end_time, window=20, horizon=7):
    """
    Dự báo giá từ end_time (ngày cuối dữ liệu)
    đến horizon ngày sau, dựa trên Moving Average
    """

    last_ma = df["Close"].rolling(window=window).mean().iloc[-1]

    future_dates = pd.date_range(
        start=end_time + pd.Timedelta(days=1),
        periods=horizon,
        freq="D"
    )

    forecast_df = pd.DataFrame(
        {"Forecast": [last_ma] * horizon},
        index = future_dates
    )

    return forecast_df
