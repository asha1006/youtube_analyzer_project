import pandas as pd
import isodate

def preprocess():
    df = pd.read_csv("youtube_data.csv")

    # Convert ISO 8601 durations to seconds
    df["duration_sec"] = df["duration"].apply(lambda x: isodate.parse_duration(x).total_seconds())

    # Extract posting hour/day
    df["publishedAt"] = pd.to_datetime(df["publishedAt"])
    df["publish_hour"] = df["publishedAt"].dt.hour
    df["publish_day"] = df["publishedAt"].dt.day_name()

    df.to_csv("processed_data.csv", index=False)
    return df
