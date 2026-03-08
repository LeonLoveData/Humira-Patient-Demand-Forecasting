def plot_prophet(prophet_df, forecast):
    import matplotlib.pyplot as plt
    import os

    plt.figure(figsize=(10, 6))
    plt.plot(prophet_df["ds"], prophet_df["y"], label="Historical (Total Claims)", marker="o")
    plt.plot(forecast["ds"], forecast["yhat"], label="Prophet Forecast", linestyle="--")
    plt.fill_between(
        forecast["ds"],
        forecast["yhat_lower"],
        forecast["yhat_upper"],
        color="gray",
        alpha=0.2,
        label="Prophet Uncertainty",
    )
    plt.title("Humira – Total Claims (Medicare + Medicaid) – Prophet Forecast")
    plt.xlabel("Year")
    plt.ylabel("Total Claims")
    plt.legend()
    plt.tight_layout()

    out_path = os.path.join(OUTPUT_DIR, "humira_prophet_forecast.png")
    plt.savefig(out_path, dpi=300)
    plt.close()
    print(f"Prophet forecast figure saved to: {out_path}")


def plot_xgboost(xgb_df, future_years, future_pred):
    import matplotlib.pyplot as plt
    import os

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(xgb_df["year"], xgb_df["total_claims_all"], label="Historical", marker="o")
    ax.plot(future_years["year"], future_pred, label="XGBoost Forecast", marker="x", linestyle="--")

    ax.set_title("Humira – Total Claims (Medicare + Medicaid) – XGBoost Forecast")
    ax.set_xlabel("Year")
    ax.set_ylabel("Total Claims")
    ax.legend()

    plt.tight_layout()

    out_path = os.path.join(OUTPUT_DIR, "humira_xgboost_forecast.png")
    plt.savefig(out_path, dpi=300)
    plt.close()
    print(f"XGBoost forecast figure saved to: {out_path}")
