import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

def cluster_videos():
    df = pd.read_csv("processed_data.csv")
    features = df[["views", "likes", "comments", "duration_sec"]]

    scaler = StandardScaler()
    scaled = scaler.fit_transform(features)

    kmeans = KMeans(n_clusters=3, random_state=42)
    df["cluster"] = kmeans.fit_predict(scaled)

    df.to_csv("clustered_data.csv", index=False)
    return df
