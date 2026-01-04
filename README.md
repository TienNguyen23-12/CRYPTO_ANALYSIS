ĐỒ ÁN PYTHON

Thành viên 1

•	Họ và tên: Trương Tấn Phát

•	MSSV: 24110298

•	Vai trò: Tích hợp chương trình chính, xây dựng giao diện chạy ứng dụng (app.py), trực quan hóa dữ liệu (chart.py), quản lý thư viện phụ thuộc (requirements.txt), viết tài liệu hướng dẫn (README.md).

Thành viên 2

•	Họ và tên: Nguyễn Thanh Tiến

•	MSSV: 24110352

•	Vai trò: Phân tích thống kê dữ liệu và xây dựng mô hình dự báo xu hướng giá tiền điện tử (statistics.py, forecast.py).

Thành viên 3

•	Họ và tên: Trương Hoàng Long

•	MSSV: 24110273

•	Vai trò: Làm sạch dữ liệu (xử lý giá trị null, trùng lặp, dữ liệu bất thường) và xuất dữ liệu sau xử lý ra file cleaned_coin.csv (cleaning.py).

Thành viên 4

•	Họ và tên: Phạm Minh Luân

•	MSSV: 24110277

•	Vai trò: Chuẩn hóa dữ liệu thời gian (parse datetime, sắp xếp, định dạng thời gian) phục vụ cho phân tích và trực quan (load_time.py).

Thành viên 5

•	Họ và tên: Đặng Duy Quang

•	MSSV: 24110307

•	Vai trò: Đọc dữ liệu đầu vào từ file raw_coin.csv, kiểm tra schema, phát hiện lỗi cột và chuẩn hóa cấu trúc dữ liệu ban đầu (ingestion.py).

# CRYPTO ANALYSIS

1.Giới thiệu

CRYPTO ANALYSIS là dự án Python dùng để phân tích và dự báo giá tiền điện tử (Crypto) dựa trên dữ liệu lịch sử.  
Dự án hỗ trợ xử lý dữ liệu, trực quan hóa biểu đồ và dự báo xu hướng ngắn hạn thông qua giao diện Streamlit.



2.Cài đặt

Cài đặt các thư viện cần thiết
Dự án sử dụng một số thư viện Python phổ biến để phân tích dữ liệu và xây dựng giao diện.



Bước 1: Cài đặt Python
Tải và cài đặt Python (phiên bản 3.9 trở lên) tại:
https://www.python.org/downloads/

Khi cài đặt, nhớ chọn Add Python to PATH.



Bước 2: Cài đặt thư viện
Mở Terminal (hoặc Command Prompt) tại thư mục dự án và chạy lệnh:

pip install -r requirements.txt



3.Hướng dẫn sử dung

Chạy chương trình bằng lệnh:

streamlit run app.py

Ngừng chương trình bằng ctrl + c
