# # import streamlit as st
# # import pandas as pd
# # import matplotlib.pyplot as plt

# # df = pd.read_csv("clustered_data.csv")

# # st.title("📊 YouTube Content Strategy Analyzer")

# # st.subheader("📈 Video Performance Clusters")
# # st.bar_chart(df["cluster"].value_counts())

# # st.subheader("📆 Posting Day vs Views")
# # day_views = df.groupby("publish_day")["views"].mean().sort_values()
# # st.bar_chart(day_views)

# # st.subheader("⏱️ Duration vs Views")
# # st.scatter_chart(df[["duration_sec", "views"]])

# # st.subheader("📌 Top Recommendations:")
# # st.markdown("""
# # - ✅ Post between **X AM to Y PM**.
# # - ✅ Ideal title length: **40–60 characters**
# # - ✅ Avoid uploading on **Sunday evenings**
# # - ✅ Most engaging videos are around **5–8 minutes**
# # """)

# import streamlit as st
# import pandas as pd

# df = pd.read_csv("clustered_data.csv")

# st.title("📊 YouTube Content Strategy Analyzer")

# # 📌 Insights from data
# st.subheader("📌 Top Recommendations:")

# # 1. Best posting time (hour with highest avg views)
# best_hour = df.groupby("publish_hour")["views"].mean().idxmax()

# # Suggest a posting window (e.g., best hour ±2 hours)
# recommended_start = max(best_hour - 2, 0)
# recommended_end = min(best_hour + 2, 23)

# # 2. Best title length range
# df["title_length"] = df["title"].apply(len)
# avg_title_len = int(df["title_length"].mean())
# ideal_title_range = (avg_title_len - 10, avg_title_len + 10)

# # 3. Avoid worst posting day
# worst_day = df.groupby("publish_day")["views"].mean().idxmin()

# # 4. Most engaging video duration range
# best_duration = df.groupby("duration_sec")["views"].mean().idxmax()
# best_duration_min = int(best_duration // 60)
# recommended_range = f"{max(1, best_duration_min - 2)}–{best_duration_min + 2} minutes"

# # 🟩 Show Recommendations
# st.markdown(f"""
# - ✅ Post between **{recommended_start} AM to {recommended_end} PM**
# - ✅ Ideal title length: **{ideal_title_range[0]}–{ideal_title_range[1]} characters**
# - ✅ Avoid uploading on **{worst_day}**
# - ✅ Most engaging videos are around **{recommended_range}**
# """)
import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("clustered_data.csv")

st.title("📊 YouTube Content Strategy Analyzer")

# --------------------------------------------
# 📌 Top Recommendations (Dynamic)
st.subheader("📌 Top Recommendations:")

# 1. Best posting time
best_hour = df.groupby("publish_hour")["views"].mean().idxmax()
recommended_start = max(best_hour - 2, 0)
recommended_end = min(best_hour + 2, 23)

# 2. Ideal title length
df["title_length"] = df["title"].apply(len)
avg_title_len = int(df["title_length"].mean())
ideal_title_range = (avg_title_len - 10, avg_title_len + 10)

# 3. Worst day to post
worst_day = df.groupby("publish_day")["views"].mean().idxmin()

# 4. Best video duration
best_duration = df.groupby("duration_sec")["views"].mean().idxmax()
best_duration_min = int(best_duration // 60)
recommended_range = f"{max(1, best_duration_min - 2)}–{best_duration_min + 2} minutes"

# Show recommendations
st.markdown(f"""
- ✅ Post between **{recommended_start} AM to {recommended_end} PM**
- ✅ Ideal title length: **{ideal_title_range[0]}–{ideal_title_range[1]} characters**
- ✅ Avoid uploading on **{worst_day}**
- ✅ Most engaging videos are around **{recommended_range}**
""")

# --------------------------------------------
# 📊 Visualizations

st.subheader("📈 Posting Hour vs Average Views")
hourly_views = df.groupby("publish_hour")["views"].mean().reset_index()
fig1, ax1 = plt.subplots()
sns.barplot(data=hourly_views, x="publish_hour", y="views", ax=ax1)
st.pyplot(fig1)

st.subheader("📈 Posting Day vs Average Views")
daily_views = df.groupby("publish_day")["views"].mean().reset_index()
fig2, ax2 = plt.subplots()
sns.barplot(data=daily_views, x="publish_day", y="views", ax=ax2)
st.pyplot(fig2)

st.subheader("📈 Title Length vs Views")
fig3, ax3 = plt.subplots()
sns.scatterplot(data=df, x="title_length", y="views", ax=ax3)
st.pyplot(fig3)

st.subheader("📈 Duration vs Views")
fig4, ax4 = plt.subplots()
sns.scatterplot(data=df, x="duration_sec", y="views", ax=ax4)
st.pyplot(fig4)
