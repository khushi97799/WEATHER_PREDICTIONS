import pandas as pd

def load_data(path="data/weather.csv"):
    df = pd.read_csv(path)
    return df


def clean_data(df):
    # remove missing values
    df = df.dropna()

    # convert date if exists
    if "datetime" in df.columns:
        df["datetime"] = pd.to_datetime(df["datetime"])
        df = df.sort_values("datetime")

    return df


def feature_engineering(df):
    """
    Create ML features from raw weather data
    """

    # lag features (time series idea)
    if "temp" in df.columns:
        df["temp_lag1"] = df["temp"].shift(1)
        df["temp_lag2"] = df["temp"].shift(2)

        # rolling mean (trend feature)
        df["temp_ma3"] = df["temp"].rolling(3).mean()

    return df


def prepare_data(path="data/weather.csv"):
    df = load_data(path)
    df = clean_data(df)
    df = feature_engineering(df)

    df = df.dropna()  # final cleanup
    return df