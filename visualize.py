import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def plot_publish_hour_vs_views():
    df = pd.read_csv("processed_data.csv")
    sns.barplot(data=df, x="publish_hour", y="views")
    plt.title("Best Time to Post (by Views)")
    plt.xlabel("Hour of Day")
    plt.ylabel("Average Views")
    plt.savefig("post_time_analysis.png")
    plt.show()

def plot_title_length_vs_engagement():
    df = pd.read_csv("processed_data.csv")
    df["title_length"] = df["title"].apply(len)
    sns.scatterplot(data=df, x="title_length", y="views")
    plt.title("Title Length vs Views")
    plt.savefig("title_length.png")
    plt.show()
