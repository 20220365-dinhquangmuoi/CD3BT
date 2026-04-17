# ==========================================
# TIỀN XỬ LÝ DỮ LIỆU - CODE ĐÃ FIX
# File: social_media_cleaned.csv
# ==========================================

import pandas as pd
from sklearn.preprocessing import LabelEncoder, MinMaxScaler
from sklearn.model_selection import train_test_split

# 1. Đọc file
df = pd.read_csv("social_media_cleaned.csv")

# ==========================================
# 2. MÃ HÓA DỮ LIỆU CHỮ
# ==========================================
text_cols = ["Gender", "Platform", "Country"]

for col in text_cols:
    le = LabelEncoder()
    df[col] = le.fit_transform(df[col].astype(str))

# ==========================================
# 3. CHUẨN HÓA DỮ LIỆU SỐ
# ==========================================
num_cols = [
    "Age",
    "Daily_Usage_Time",
    "Posts_Per_Week",
    "Likes_Received",
    "Comments_Received",
    "Messages_Sent",
    "Followers"
]

scaler = MinMaxScaler()
df[num_cols] = scaler.fit_transform(df[num_cols])

# ==========================================
# 4. TẠO CỘT MỚI
# ==========================================
# Popular nếu followers >= 0.5
df["User_Level"] = df["Followers"].apply(
    lambda x: 1 if x >= 0.5 else 0
)

# Active nếu dùng > 0.6
df["Active_User"] = df["Daily_Usage_Time"].apply(
    lambda x: 1 if x >= 0.6 else 0
)

# ==========================================
# 5. CHIA TRAIN / TEST
# ==========================================
X = df.drop(columns=["Engagement_Score"])
y = df["Engagement_Score"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42
)

# ==========================================
# 6. KẾT QUẢ
# ==========================================
print("X_train:", X_train.shape)
print("X_test :", X_test.shape)
print("y_train:", y_train.shape)
print("y_test :", y_test.shape)

print("\n5 dòng đầu:")
print(df.head())

# ==========================================
# 7. LƯU FILE
# ==========================================
df.to_csv("social_media_preprocessed.csv", index=False, encoding="utf-8-sig")

print("\nĐã lưu file social_media_preprocessed.csv")