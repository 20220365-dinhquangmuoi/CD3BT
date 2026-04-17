# ===============================
# LÀM SẠCH DATASET MẠNG XÃ HỘI
# File: social_media_dataset.csv
# ===============================

import pandas as pd
import numpy as np

# 1. Đọc dữ liệu
df = pd.read_csv("social_media_dataset.csv")

# 2. Xem dữ liệu ban đầu
print("5 dòng đầu:")
print(df.head())

print("\nThông tin dữ liệu:")
print(df.info())

print("\nSố dòng, số cột:", df.shape)

# ===============================
# 3. Kiểm tra dữ liệu thiếu
# ===============================
print("\nDữ liệu thiếu:")
print(df.isnull().sum())

# Nếu có giá trị thiếu số -> thay bằng trung bình
num_cols = df.select_dtypes(include=np.number).columns

for col in num_cols:
    df[col].fillna(df[col].mean(), inplace=True)

# Nếu có giá trị thiếu chữ -> thay bằng mode
cat_cols = df.select_dtypes(include='object').columns

for col in cat_cols:
    df[col].fillna(df[col].mode()[0], inplace=True)

# ===============================
# 4. Xóa dòng trùng lặp
# ===============================
print("\nSố dòng trùng:", df.duplicated().sum())
df.drop_duplicates(inplace=True)

# ===============================
# 5. Chuẩn hóa dữ liệu text
# ===============================
for col in cat_cols:
    df[col] = df[col].str.strip().str.title()

# ===============================
# 6. Ép kiểu dữ liệu
# ===============================
df["Age"] = pd.to_numeric(df["Age"], errors="coerce")
df["Followers"] = pd.to_numeric(df["Followers"], errors="coerce")

# ===============================
# 7. Xử lý ngoại lệ (Outliers)
# ===============================
# Ví dụ: tuổi từ 15 đến 60
df = df[(df["Age"] >= 15) & (df["Age"] <= 60)]

# Followers > 0
df = df[df["Followers"] > 0]

# ===============================
# 8. Tạo cột mới
# ===============================
df["User_Level"] = np.where(df["Followers"] >= 1000, "Popular", "Normal")

# ===============================
# 9. Kiểm tra sau làm sạch
# ===============================
print("\nSau làm sạch:")
print(df.info())

print("\n5 dòng cuối:")
print(df.tail())

# ===============================
# 10. Lưu file mới
# ===============================
df.to_csv("social_media_cleaned.csv", index=False, encoding="utf-8-sig")

print("\nĐã lưu file: social_media_cleaned.csv")