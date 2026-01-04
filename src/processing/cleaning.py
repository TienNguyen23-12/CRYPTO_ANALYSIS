import pandas as pd
import numpy as np

def clean_data():
    """Đọc file raw, làm sạch và lưu thành file cleaned"""
    print(">>> Đang xử lý làm sạch dữ liệu...")
    
    try:
        # 1. Đọc dữ liệu thô
        df = pd.read_csv('data/raw_coin.csv', index_col=0, parse_dates=True)
        
        # 2. Xử lý MultiIndex (Lỗi phổ biến của yfinance mới)
        # Nếu cột có dạng ('Close', 'BTC-USD') -> chuyển thành 'Close'
        if isinstance(df.columns, pd.MultiIndex):
            df.columns = df.columns.get_level_values(0)
            
        # 3. Loại bỏ các dòng không có dữ liệu (NaN)
        df = df.dropna()
        
        # 4. Loại bỏ dữ liệu rác (Giá <= 0)
        # 4. Loại bỏ dữ liệu rác và ép kiểu cho cả Open và Close
        for col in ['Close', 'Open', 'High', 'Low', 'Volume']:
            if col in df.columns:
                df[col] = pd.to_numeric(df[col], errors='coerce')

        df = df.dropna()
        # Lọc giá dương cho cả Open và Close
        df = df[(df['Close'] > 0) & (df['Open'] > 0)]

        # 5. Lưu file sạch
        df.to_csv('data/cleaned_coin.csv')
        print(">>> Đã lưu file: data/cleaned_coin.csv")
        return df
        
    except FileNotFoundError:
        print("Lỗi: Không tìm thấy file raw. Hãy chạy ingestion trước.")
        return None