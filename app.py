import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter

# -----------------------------
# Load Dataset
# -----------------------------
df = pd.read_csv("news_with_sentiment.csv")

# -----------------------------
# Title and Description
# -----------------------------
st.title("NewsPulse Dashboard")
st.header("Global News Trend Analyzer")
st.write("Student Name: Shravya Challa")
st.write("This dashboard displays global news trends, sentiment analysis, and source-level insights.")

# -----------------------------
# Sample Headlines
# -----------------------------
st.subheader("5 Sample News Headlines")
st.write(df["Title"].head(5))

# -----------------------------
# Top 10 Trending Keywords
# -----------------------------
all_words = " ".join(df["processed_text"].dropna()).split()
word_count = Counter(all_words)
top_words = word_count.most_common(10)

words = [word[0] for word in top_words]
counts = [word[1] for word in top_words]

st.subheader("Top 10 Trending Keywords")
for i, (word, count) in enumerate(top_words, start=1):
    st.write(f"{i}. {word} - {count}")

# -----------------------------
# Trend Bar Chart
# -----------------------------
st.subheader("Trending Keywords Frequency Chart")
fig1, ax1 = plt.subplots()
ax1.bar(words, counts)
plt.xticks(rotation=45)
plt.xlabel("Keywords")
plt.ylabel("Frequency")
plt.title("Top 10 Trending Keywords")
st.pyplot(fig1)

# -----------------------------
# Sentiment Distribution
# -----------------------------
sentiment_count = df["sentiment"].value_counts()
labels = sentiment_count.index
values = sentiment_count.values

# -----------------------------
# Sentiment Bar Chart
# -----------------------------
st.subheader("Sentiment Distribution - Bar Chart")
fig2, ax2 = plt.subplots()
ax2.bar(labels, values)
plt.xlabel("Sentiment")
plt.ylabel("Number of Articles")
plt.title("Sentiment Distribution")
st.pyplot(fig2)

# -----------------------------
# Sentiment Pie Chart
# -----------------------------
st.subheader("Sentiment Distribution - Pie Chart")
fig3, ax3 = plt.subplots()
ax3.pie(values, labels=labels, autopct='%1.1f%%')
plt.title("Sentiment Share")
st.pyplot(fig3)

# -----------------------------
# Top News Sources
# -----------------------------
st.subheader("Top News Sources")
source_counts = df["Source"].value_counts().head(10)

fig4, ax4 = plt.subplots()
ax4.bar(source_counts.index, source_counts.values)
plt.xticks(rotation=45)
plt.xlabel("Source")
plt.ylabel("Articles")
plt.title("Top News Sources")
st.pyplot(fig4)

# -----------------------------
# System Summary
# -----------------------------
st.subheader("System Summary")
st.write("Total News Articles:", len(df))
st.write("Top Trending Keyword:", words[0])
st.write("Most Common Sentiment:", sentiment_count.idxmax())
st.write("Unique News Sources:", df["Source"].nunique())