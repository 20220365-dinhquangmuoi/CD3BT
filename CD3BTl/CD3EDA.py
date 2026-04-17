# ==========================================
# KHÁM PHÁ DỮ LIỆU (EDA)
# File: social_media_cleaned.csv
# ==========================================

import pandas as pd

# 1. Đọc dữ liệu
df = pd.read_csv("social_media_cleaned.csv")

# ==========================================
# 2. Xem 5 dòng đầu
# ==========================================
print("5 dòng đầu:")
print(df.head())

# ==========================================
# 3. Thông tin dữ liệu
# ==========================================
print("\nThông tin dữ liệu:")
print(df.info())

# ==========================================
# 4. Thống kê mô tả
# ==========================================
print("\nThống kê mô tả:")
print(df.describe())

# ==========================================
# 5. Có bao nhiêu người dùng?
# ==========================================
print("\nTổng số người dùng:", len(df))

# ==========================================
# 6. Nền tảng nào phổ biến nhất?
# ==========================================
print("\nSố lượng người dùng theo nền tảng:")
print(df["Platform"].value_counts())

popular = df["Platform"].mode()[0]
print("Nền tảng phổ biến nhất:", popular)

# ==========================================
# 7. Tuổi trung bình
# ==========================================
avg_age = df["Age"].mean()
print("\nTuổi trung bình:", round(avg_age,2))

# ==========================================
# 8. Thời gian online trung bình/ngày
# ==========================================
avg_time = df["Daily_Usage_Time"].mean()
print("Thời gian online trung bình/ngày:", round(avg_time,2), "giờ")

# ==========================================
# 9. Giới tính
# ==========================================
print("\nPhân bố giới tính:")
print(df["Gender"].value_counts())

# ==========================================
# 10. Quốc gia
# ==========================================
print("\nTop quốc gia nhiều người dùng:")
print(df["Country"].value_counts())

# ==========================================
# 11. Followers trung bình
# ==========================================
avg_followers = df["Followers"].mean()
print("\nFollowers trung bình:", round(avg_followers,2))

# ==========================================
# 12. Engagement trung bình
# ==========================================
avg_eng = df["Engagement_Score"].mean()
print("Engagement Score trung bình:", round(avg_eng,2))