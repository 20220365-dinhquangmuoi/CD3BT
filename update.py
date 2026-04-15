
#  PHÂN TÍCH DATASET MẠNG XÃ HỘI
# File: social_media_dataset.csv


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# ===============================
# 1. Đọc dữ liệu
# ===============================
df = pd.read_csv("social_media_dataset.csv")

print("5 dòng đầu:")
print(df.head())

print("\nThông tin dữ liệu:")
print(df.info())

print("\nKích thước:", df.shape)

# ===============================
# 2. Thống kê mô tả
# ===============================
print("\nThống kê mô tả:")
print(df.describe())

# ===============================
# 3. Kiểm tra dữ liệu thiếu
# ===============================
print("\nMissing values:")
print(df.isnull().sum())

# ===============================
# 4. Top nền tảng MXH nhiều user nhất
# ===============================
platform_count = df["Platform"].value_counts()

plt.figure(figsize=(8,5))
platform_count.plot(kind="bar")
plt.title("Số lượng User theo Platform")
plt.xlabel("Platform")
plt.ylabel("Số User")
plt.xticks(rotation=45)
plt.show()

# ===============================
# 5. Phân bố giới tính
# ===============================
gender_count = df["Gender"].value_counts()

plt.figure(figsize=(6,6))
plt.pie(gender_count, labels=gender_count.index, autopct='%1.1f%%')
plt.title("Tỷ lệ giới tính")
plt.show()

# ===============================
# 6. Followers trung bình theo quốc gia
# ===============================
country_follow = df.groupby("Country")["Followers"].mean().sort_values(ascending=False)

plt.figure(figsize=(10,5))
country_follow.plot(kind="bar")
plt.title("Followers trung bình theo quốc gia")
plt.ylabel("Followers")
plt.xticks(rotation=45)
plt.show()

# ===============================
# 7. Tuổi và Engagement
# ===============================
plt.figure(figsize=(8,5))
plt.scatter(df["Age"], df["Engagement_Score"])
plt.title("Age vs Engagement Score")
plt.xlabel("Age")
plt.ylabel("Engagement")
plt.show()

# ===============================
# 8. User nổi tiếng
# ===============================
df["User_Level"] = np.where(df["Followers"] >= 1000, "Popular", "Normal")

print("\nSố lượng User nổi tiếng:")
print(df["User_Level"].value_counts())

# ===============================
# 9. Top 10 user Followers cao nhất
# ===============================
top10 = df.sort_values("Followers", ascending=False).head(10)

print("\nTop 10 User Followers cao nhất:")
print(top10[["User_ID","Platform","Followers","Country"]])

# ===============================
# 10. Tương quan dữ liệu số
# ===============================
corr = df.select_dtypes(include=np.number).corr()

print("\nCorrelation:")
print(corr)

# ===============================
# 11. Lưu file mới
# ===============================
df.to_csv("social_media_analysis.csv", index=False, encoding="utf-8-sig")

print("\nĐã lưu file social_media_analysis.csv")