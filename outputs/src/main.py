def main():
    print("Loading data...")
    medicare, medicaid = load_data()

    print("Building Humira time series...")
    medicare_ts, medicaid_ts, combined_ts = build_time_series(medicare, medicaid)
    print("Combined time series:")
    print(combined_ts)

    print("Running Prophet forecast...")
    prophet_df, forecast = run_prophet_forecast(combined_ts)
    plot_prophet(prophet_df, forecast)

    print("Running XGBoost forecast...")
    xgb_df, future_years, future_pred, forecast_df = run_xgboost_forecast(combined_ts)
    plot_xgboost(xgb_df, future_years, future_pred)

    print("Done.")


if __name__ == "__main__":
    main()
