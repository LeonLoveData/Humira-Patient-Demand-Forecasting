def load_data():
    import pandas as pd
    medicare = pd.read_csv(MEDICARE_FILE)
    medicaid = pd.read_csv(MEDICAID_FILE)
    return medicare, medicaid

def filter_humira(df, source_label):
    df = df.copy()
    df["Brnd_Name_upper"] = df["Brnd_Name"].astype(str).str.upper()
    sub = df[df["Brnd_Name_upper"] == TARGET_DRUG].copy()
    sub["source"] = source_label
    return sub

def wide_to_long_claims(df, source_label):
    import pandas as pd
    records = []
    for year in range(2019, 2024):
        col = f"Tot_Clms_{year}"
        if col in df.columns:
            total_claims = df[col].sum()
            records.append({"year": year, "total_claims": total_claims, "source": source_label})
    return pd.DataFrame(records)

def build_time_series(medicare, medicaid):
    import pandas as pd

    medicare_h = filter_humira(medicare, "Medicare Part D")
    medicaid_h = filter_humira(medicaid, "Medicaid")

    if medicare_h.empty and medicaid_h.empty:
        raise ValueError("在 Medicare 和 Medicaid 中都没有找到 HUMIRA，请检查 Brnd_Name。")

    medicare_ts = wide_to_long_claims(medicare_h, "Medicare Part D")
    medicaid_ts = wide_to_long_claims(medicaid_h, "Medicaid")

    combined = (
        pd.concat([medicare_ts, medicaid_ts], ignore_index=True)
        .groupby("year", as_index=False)["total_claims"]
        .sum()
        .rename(columns={"total_claims": "total_claims_all"})
    )

    return medicare_ts, medicaid_ts, combined
