def run_xgboost_forecast(combined_ts):
    import pandas as pd
    from xgboost import XGBRegressor
    from sklearn.metrics import mean_squared_error

    xgb_df = combined_ts.copy()
    X = xgb_df[["year"]]
    y = xgb_df["total_claims_all"]

    if len(X) < 3:
        raise ValueError("年度数据点太少，建议至少 3–4 年再做 XGBoost。")

    X_train, X_test = X.iloc[:-1], X.iloc[-1:]
    y_train, y_test = y.iloc[:-1], y.iloc[-1:]

    model = XGBRegressor(
        n_estimators=200,
        learning_rate=0.05,
        max_depth=3,
        random_state=42,
    )
    model.fit(X_train, y_train)

    y_pred_test = model.predict(X_test)
    rmse = (mean_squared_error(y_test, y_pred_test)) ** 0.5
    print(f"XGBoost last-year RMSE: {rmse:.2f}")

    future_years = pd.DataFrame({"year": range(xgb_df["year"].max() + 1, xgb_df["year"].max() + 6)})
    future_pred = model.predict(future_years)

    forecast_df = pd.concat(
        [
            xgb_df.assign(type="historical"),
            pd.DataFrame(
                {"year": future_years["year"], "total_claims_all": future_pred, "type": "forecast"}
            ),
        ],
        ignore_index=True,
    )

    return xgb_df, future_years, future_pred, forecast_df
