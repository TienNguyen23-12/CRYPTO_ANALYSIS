## Thành viên 1

•	Họ và tên: Trương Tấn Phát

•	MSSV: 24110298

•	Vai trò: Tích hợp chương trình chính, xây dựng giao diện chạy ứng dụng (app.py), trực quan hóa dữ liệu (chart.py), quản lý thư viện phụ thuộc (requirements.txt), viết tài liệu hướng dẫn (README.md).

## Thành viên 2

•	Họ và tên: Nguyễn Thành Tiến

•	MSSV: 24110352

•	Vai trò: Phân tích thống kê dữ liệu và xây dựng mô hình dự báo xu hướng giá tiền điện tử (statistics.py, forecast.py).

## Thành viên 3

•	Họ và tên: Trương Hoàng Long

•	MSSV: 24110273

•	Vai trò: Làm sạch dữ liệu (xử lý giá trị null, trùng lặp, dữ liệu bất thường) và xuất dữ liệu sau xử lý ra file cleaned_coin.csv (cleaning.py).

## Thành viên 4

•	Họ và tên: Phạm Minh Luân

•	MSSV: 24110277

•	Vai trò: Chuẩn hóa dữ liệu thời gian (parse datetime, sắp xếp, định dạng thời gian) phục vụ cho phân tích và trực quan (load_time.py).

## Thành viên 5

•	Họ và tên: Đặng Duy Quang

•	MSSV: 24110307

•	Vai trò: Đọc dữ liệu đầu vào từ file raw_coin.csv, kiểm tra schema, phát hiện lỗi cột và chuẩn hóa cấu trúc dữ liệu ban đầu (ingestion.py).

# CRYPTO ANALYSIS

## Cấu trúc thư mục đồ án

CRYPTO_ANALYSIS
├── data
│   ├── cleaned_coin.csv
│   └── raw_coin.csv
│
├── src
│   ├── analysis
│   │   ├── __init__.py
│   │   ├── forecast.py
│   │   └── statistics.py
│   │
│   ├── processing
│   │   ├── __init__.py
│   │   ├── chart.py
│   │   ├── cleaning.py
│   │   ├── ingestion.py
│   │   └── load_time.py
│   │
│   └── __init__.py
│
├── .gitignore
├── README.md
├── app.py
└── requirements.txt

# 1.Giới thiệu

CRYPTO ANALYSIS là dự án Python dùng để phân tích và dự báo giá tiền điện tử (Crypto) dựa trên dữ liệu lịch sử.  
Dự án hỗ trợ xử lý dữ liệu, trực quan hóa biểu đồ và dự báo xu hướng ngắn hạn thông qua giao diện Streamlit.


# 2.Cài đặt

## Bước 1: Cài đặt Python
Tải và cài đặt Python (phiên bản 3.9 trở lên) tại:
https://www.python.org/downloads/

Khi cài đặt, nhớ chọn Add Python to PATH.

## Bước 2: Cài đặt thư viện

Để có thể chạy chương trình, phải thông qua quá trình cài đặt các thư viện cần thiết. Để cài đặt có 2 cách:

Cách 1: Cài đặt các thư viện tự động

Các thư viện cần thiết liên quan đến đồ án đã được tích hợp bên trong requirements.txt, mở Terminal chạy lệnh:

pip install -r requirements.txt

Cách 2: Cài đặt thủ công từng thư viện

Phải cài đặt các thư viện cần thiết để có thể chạy đồ án, mở Terminal tải từng thư viện như sau:

pip install pandas

pip install numpy

pip install matplotlib

pip install streamlit

pip install yfinance 

# 3. Hướng dẫn sử dụng
Sau khi hoàn tất việc cài đặt python và thư viện cần thiết. Mở Terminal trong VS Code, dẫn đường đến thư mục chứa phần code theo lệnh (nếu đường dẫn trong Terminal chưa đúng):

cd CRYPTO_ANALYSIS

đường dẫn đúng sẽ có dạng .../CRYPTO_ANALYSIS>

Sau đó thực hiện lệnh:

streamlit run app.py

Giao diện sẽ được hiện ra, sau đó chỉ cần thao tác trên giao diện. Để dừng chương trình, về lại VS Code -> Nhấn Ctrl + C.
