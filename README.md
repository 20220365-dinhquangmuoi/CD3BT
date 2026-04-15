# CD3BT
:

📌 Quy trình thực hiện đề tài theo 7 bước
1. Thu thập dữ liệu

Chọn dataset có ý nghĩa về mạng xã hội.

Ví dụ:

Social media users dataset
TikTok engagement dataset
Instagram influencer dataset
Twitter sentiment dataset

👉 có file social_media_dataset.csv nên dùng luôn.

2. Làm sạch dữ liệu

Mục tiêu: loại lỗi và chuẩn hóa dữ liệu.

Công việc:

Xóa dòng trùng
Xử lý giá trị thiếu
Sửa kiểu dữ liệu
Chuẩn hóa tên cột
Xử lý ngoại lệ

Ví dụ:

df.isnull().sum()
df.drop_duplicates()
3. Tiền xử lý dữ liệu

Chuẩn bị dữ liệu để phân tích / machine learning.

Công việc:

Mã hóa dữ liệu chữ
Chuẩn hóa dữ liệu số
Tạo cột mới
Chia train/test nếu dự báo

Ví dụ:

df["User_Level"] = ...
4. Khám phá dữ liệu (EDA)

Tìm hiểu dữ liệu ban đầu.

Câu hỏi:

Có bao nhiêu người dùng?
Nền tảng nào phổ biến nhất?
Tuổi trung bình bao nhiêu?
Người dùng online bao lâu/ngày?

Ví dụ:

df.describe()
df["Platform"].value_counts()
5. Trực quan hóa dữ liệu

Dùng biểu đồ để dễ hiểu.

Nên làm:

Bar chart: số người dùng theo nền tảng
Histogram: độ tuổi
Pie chart: giới tính
Boxplot: followers
Heatmap: tương quan

Dùng Matplotlib hoặc Seaborn

6. Phân tích dữ liệu

Rút insight từ biểu đồ và số liệu.

Ví dụ:

TikTok có thời gian dùng/ngày cao nhất
Người nhiều followers thường có engagement cao
Nhóm tuổi 18–25 dùng Instagram nhiều
7. Dự báo

Dự đoán chỉ số quan trọng.

Ví dụ:

Dự báo Engagement Score
Dự báo Likes
Dự báo thời gian sử dụng

Mô hình:

Linear Regression
Random Forest

Dùng Scikit-learn

