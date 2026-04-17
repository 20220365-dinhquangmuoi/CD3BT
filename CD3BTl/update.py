import pandas as pd

df = pd.read_csv('social_media_dataset.csv')
print("Tên các cột trong file CSV:")
print(df.columns.tolist())
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# === ĐỌC DỮ LIỆU ===
df = pd.read_csv('social_media_dataset.csv')

# === HIỂN THỊ TÊN CỘT GỐC ĐỂ KIỂM TRA ===
print("="*60)
print("TÊN CỘT TRONG FILE CSV GỐC:")
print("="*60)
for i, col in enumerate(df.columns, 1):
    print(f"{i}. '{col}'")

# === CHUYỂN TIÊU ĐỀ SANG TIẾNG VIỆT (DÙNG TÊN CHÍNH XÁC) ===
# Tạo dictionary ánh xạ dựa trên tên cột thực tế
column_mapping = {}
for col in df.columns:
    if col == 'User_ID':
        column_mapping[col] = 'Mã_người_dùng'
    elif col == 'Age':
        column_mapping[col] = 'Tuổi'
    elif col == 'Gender':
        column_mapping[col] = 'Giới_tính'
    elif col == 'Platform':
        column_mapping[col] = 'Nền_tảng'
    elif col == 'Daily_Usage_Time':
        column_mapping[col] = 'Thời_gian_dùng_hàng_ngày'
    elif col == 'Posts_Per_Week':
        column_mapping[col] = 'Số_bài_viết_mỗi_tuần'
    elif col == 'Likes_Received':
        column_mapping[col] = 'Lượt_thích_nhận_được'
    elif col == 'Comments_Received':
        column_mapping[col] = 'Lượt_bình_luận_nhận_được'
    elif col == 'Messages_Sent':
        column_mapping[col] = 'Số_tin_nhắn_đã_gửi'
    elif col == 'Followers':
        column_mapping[col] = 'Lượng_theo_dõi'
    elif col == 'Country':
        column_mapping[col] = 'Quốc_gia'
    elif col == 'Engagement_Score':
        column_mapping[col] = 'Điểm_tương_tác'

df.rename(columns=column_mapping, inplace=True)

# === KIỂM TRA LẠI TÊN CỘT SAU KHI RENAME ===
print("\n" + "="*60)
print("TÊN CỘT SAU KHI RENAME:")
print("="*60)
for i, col in enumerate(df.columns, 1):
    print(f"{i}. '{col}'")

# === DANH SÁCH CÁC TRƯỜNG SỐ (DÙNG TÊN TIẾNG VIỆT) ===
numerical_cols = ['Tuổi', 'Thời_gian_dùng_hàng_ngày', 'Số_bài_viết_mỗi_tuần',
                  'Lượt_thích_nhận_được', 'Lượt_bình_luận_nhận_được',
                  'Số_tin_nhắn_đã_gửi', 'Lượng_theo_dõi', 'Điểm_tương_tác']

# === PHẦN 1: BIỂU ĐỒ PHÂN BỐ CHO CÁC TRƯỜNG SỐ ===
plt.figure(figsize=(16, 12))
for i, col in enumerate(numerical_cols, 1):
    if col in df.columns:
        plt.subplot(3, 3, i)
        sns.histplot(df[col], bins=20, kde=True, color='skyblue', edgecolor='black')
        plt.title(f'Phân bố của {col}', fontsize=12, fontweight='bold')
        plt.xlabel(col)
        plt.ylabel('Tần suất')
plt.tight_layout()
plt.suptitle('BIỂU ĐỒ PHÂN BỐ CÁC TRƯỜNG SỐ', y=1.02, fontsize=16, fontweight='bold')
plt.show()

# === PHẦN 2: BIỂU ĐỒ CHO CÁC TRƯỜNG PHÂN LOẠI ===
categorical_cols = ['Giới_tính', 'Nền_tảng', 'Quốc_gia']

plt.figure(figsize=(15, 5))
for i, col in enumerate(categorical_cols, 1):
    if col in df.columns:
        plt.subplot(1, 3, i)
        df[col].value_counts().plot(kind='bar', color=['coral', 'lightgreen', 'gold', 'lightblue', 'pink', 'purple'])
        plt.title(f'Phân bố của {col}', fontsize=12, fontweight='bold')
        plt.xlabel(col)
        plt.ylabel('Số lượng')
        plt.xticks(rotation=45)
plt.tight_layout()
plt.suptitle('BIỂU ĐỒ PHÂN BỐ CÁC TRƯỜNG PHÂN LOẠI', y=1.02, fontsize=16, fontweight='bold')
plt.show()

# === PHẦN 3: BOXPLOT PHÁT HIỆN NGOẠI LỆ ===
plt.figure(figsize=(16, 8))
for i, col in enumerate(numerical_cols, 1):
    if col in df.columns:
        plt.subplot(3, 3, i)
        sns.boxplot(y=df[col], color='lightcoral')
        plt.title(f'Boxplot của {col}', fontsize=10)
        plt.ylabel(col)
plt.tight_layout()
plt.suptitle('PHÁT HIỆN NGOẠI LỆ BẰNG BOXPLOT', y=1.02, fontsize=16, fontweight='bold')
plt.show()

# === PHẦN 4: MA TRẬN TƯƠNG QUAN ===
# Chỉ lấy các cột số có trong dataframe
available_numerical = [col for col in numerical_cols if col in df.columns]
plt.figure(figsize=(12, 10))
correlation_matrix = df[available_numerical].corr()
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', center=0,
            fmt='.2f', square=True, linewidths=0.5)
plt.title('MA TRẬN TƯƠNG QUAN GIỮA CÁC BIẾN SỐ', fontsize=14, fontweight='bold')
plt.tight_layout()
plt.show()

# === PHẦN 5: CÁC CẶP TƯƠNG QUAN MẠNH NHẤT ===
print("\n" + "="*60)
print("CÁC CẶP TƯƠNG QUAN MẠNH NHẤT (|r| > 0.3)")
print("="*60)

corr_pairs = correlation_matrix.unstack()
corr_pairs = corr_pairs[corr_pairs != 1]
corr_pairs = corr_pairs.abs().sort_values(ascending=False).drop_duplicates()

for pair, corr_value in corr_pairs.head(10).items():
    if corr_value > 0.3:
        print(f"{pair[0]} ↔ {pair[1]}: {corr_value:.3f}")

# === PHẦN 6: SCATTER PLOT CHO CÁC CẶP TƯƠNG QUAN CAO ===
high_corr_pairs = [
    ('Lượt_thích_nhận_được', 'Lượng_theo_dõi'),
    ('Lượt_bình_luận_nhận_được', 'Lượt_thích_nhận_được'),
    ('Số_bài_viết_mỗi_tuần', 'Lượt_thích_nhận_được'),
    ('Điểm_tương_tác', 'Lượt_thích_nhận_được')
]

# Lọc chỉ giữ các cặp có cả hai cột tồn tại
valid_pairs = [(x, y) for x, y in high_corr_pairs if x in df.columns and y in df.columns]

if valid_pairs:
    plt.figure(figsize=(14, 10))
    for i, (x, y) in enumerate(valid_pairs, 1):
        plt.subplot(2, 2, i)
        sns.scatterplot(data=df, x=x, y=y, alpha=0.6, color='teal')
        plt.title(f'Tương quan giữa {x} và {y}\n(r = {df[x].corr(df[y]):.3f})', fontweight='bold')
        plt.xlabel(x)
        plt.ylabel(y)
    plt.tight_layout()
    plt.suptitle('BIỂU ĐỒ PHÂN TÁN CÁC CẶP TƯƠNG QUAN CAO', y=1.02, fontsize=14, fontweight='bold')
    plt.show()

# === PHẦN 7: ĐIỂM TƯƠNG TÁC THEO NỀN TẢNG ===
if 'Nền_tảng' in df.columns and 'Điểm_tương_tác' in df.columns:
    plt.figure(figsize=(10, 6))
    platform_engagement = df.groupby('Nền_tảng')['Điểm_tương_tác'].mean().sort_values(ascending=False)
    sns.barplot(x=platform_engagement.values, y=platform_engagement.index, palette='viridis')
    plt.title('ĐIỂM TƯƠNG TÁC TRUNG BÌNH THEO NỀN TẢNG', fontsize=14, fontweight='bold')
    plt.xlabel('Điểm tương tác trung bình')
    plt.ylabel('Nền tảng')
    for i, v in enumerate(platform_engagement.values):
        plt.text(v + 0.5, i, f'{v:.1f}', va='center')
    plt.tight_layout()
    plt.show()

# === PHẦN 8: ĐIỂM TƯƠNG TÁC THEO QUỐC GIA ===
if 'Quốc_gia' in df.columns and 'Điểm_tương_tác' in df.columns:
    plt.figure(figsize=(12, 6))
    country_engagement = df.groupby('Quốc_gia')['Điểm_tương_tác'].mean().sort_values(ascending=False)
    sns.barplot(x=country_engagement.values, y=country_engagement.index, palette='coolwarm')
    plt.title('ĐIỂM TƯƠNG TÁC TRUNG BÌNH THEO QUỐC GIA', fontsize=14, fontweight='bold')
    plt.xlabel('Điểm tương tác trung bình')
    plt.ylabel('Quốc gia')
    for i, v in enumerate(country_engagement.values):
        plt.text(v + 0.5, i, f'{v:.1f}', va='center')
    plt.tight_layout()
    plt.show()

# === PHẦN 9: ĐIỂM TƯƠNG TÁC THEO NHÓM TUỔI ===
if 'Tuổi' in df.columns and 'Điểm_tương_tác' in df.columns:
    plt.figure(figsize=(12, 6))
    age_bins = [15, 20, 25, 30, 35, 40, 46]
    age_labels = ['16-20', '21-25', '26-30', '31-35', '36-40', '41-45']
    df['Nhóm_tuổi'] = pd.cut(df['Tuổi'], bins=age_bins, labels=age_labels, right=False)
    age_engagement = df.groupby('Nhóm_tuổi')['Điểm_tương_tác'].mean()
    sns.lineplot(x=age_engagement.index, y=age_engagement.values, marker='o', linewidth=2, markersize=10)
    plt.title('ĐIỂM TƯƠNG TÁC TRUNG BÌNH THEO NHÓM TUỔI', fontsize=14, fontweight='bold')
    plt.xlabel('Nhóm tuổi')
    plt.ylabel('Điểm tương tác trung bình')
    plt.grid(True, alpha=0.3)
    for i, v in enumerate(age_engagement.values):
        plt.text(i, v + 0.5, f'{v:.1f}', ha='center')
    plt.tight_layout()
    plt.show()

# === PHẦN 10: THỐNG KÊ MÔ TẢ ===
print("\n" + "="*60)
print("THỐNG KÊ MÔ TẢ CHI TIẾT CÁC TRƯỜNG SỐ")
print("="*60)
print(df[available_numerical].describe())

# === PHẦN 11: PHÁT HIỆN NGOẠI LỆ ===
print("\n" + "="*60)
print("PHÁT HIỆN NGOẠI LỆ (IQR METHOD)")
print("="*60)

for col in available_numerical:
    Q1 = df[col].quantile(0.25)
    Q3 = df[col].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    outliers = df[(df[col] < lower_bound) | (df[col] > upper_bound)]
    print(f"\n{col}:")
    print(f"  - Ngưỡng dưới: {lower_bound:.2f}")
    print(f"  - Ngưỡng trên: {upper_bound:.2f}")
    print(f"  - Số lượng ngoại lệ: {len(outliers)}")
    if len(outliers) > 0:
        print(f"  - Giá trị ngoại lệ (5 đầu): {outliers[col].head(5).tolist()}")