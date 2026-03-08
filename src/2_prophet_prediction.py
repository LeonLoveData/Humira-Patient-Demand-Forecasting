def run_prophet_forecast(combined_ts):
    import pandas as pd
    from prophet import Prophet

    prophet_df = combined_ts.rename(columns={"year": "ds", "total_claims_all": "y"})
    prophet_df["ds"] = pd.to_datetime(prophet_df["ds"].astype(str) + "-01-01")

    m = Prophet(
        yearly_seasonality=False,
        weekly_seasonality=False,
        daily_seasonality=False,
    )
    m.fit(prophet_df)

    future = m.make_future_dataframe(periods=5, freq="YE")
    forecast = m.predict(future)

    return prophet_df, forecast
