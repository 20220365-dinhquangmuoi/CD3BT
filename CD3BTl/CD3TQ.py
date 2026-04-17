# ==========================================
# TRỰC QUAN HÓA DỮ LIỆU MẠNG XÃ HỘI
# File: social_media_cleaned.csv
# ==========================================

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Đọc dữ liệu
df = pd.read_csv("social_media_cleaned.csv")

# Giao diện đẹp hơn
sns.set_style("whitegrid")

# ==========================================
# 1. BAR CHART - Số người dùng theo nền tảng
# ==========================================
plt.figure(figsize=(8,5))
df["Platform"].value_counts().plot(kind="bar")
plt.title("Số người dùng theo nền tảng")
plt.xlabel("Nền tảng")
plt.ylabel("Số lượng")
plt.show()

# ==========================================
# 2. HISTOGRAM - Phân bố độ tuổi
# ==========================================
plt.figure(figsize=(8,5))
plt.hist(df["Age"], bins=10)
plt.title("Phân bố độ tuổi người dùng")
plt.xlabel("Tuổi")
plt.ylabel("Tần suất")
plt.show()

# ==========================================
# 3. PIE CHART - Giới tính
# ==========================================
plt.figure(figsize=(7,7))
df["Gender"].value_counts().plot(
    kind="pie",
    autopct="%1.1f%%",
    startangle=90
)
plt.title("Tỷ lệ giới tính")
plt.ylabel("")
plt.show()

# ==========================================
# 4. BOXPLOT - Followers
# ==========================================
plt.figure(figsize=(8,5))
sns.boxplot(x=df["Followers"])
plt.title("Phân bố Followers")
plt.show()

# ==========================================
# 5. HEATMAP - Ma trận tương quan
# ==========================================
plt.figure(figsize=(10,6))

num_df = df.select_dtypes(include=["int64","float64"])

sns.heatmap(
    num_df.corr(),
    annot=True,
    cmap="coolwarm",
    fmt=".2f"
)

plt.title("Ma trận tương quan")
plt.show()