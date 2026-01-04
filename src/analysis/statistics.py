import numpy as np
import pandas as pd

def calculate_metrics(df):
    if df.empty:
        return None
    """Tính toán các chỉ số tài chính cơ bản"""
    
    # 1. Tính lợi nhuận (Returns)
    data = df.copy()
    data['Returns'] = data['Close'].pct_change()
    
    # 2. Tính các chỉ số
    # Lấy giá mở cửa của phiên đầu tiên trong khoảng thời gian chọn
    first_open = data['Open'].iloc[0]
    # Lấy giá đóng cửa mới nhất
    last_price = data['Close'].iloc[-1]

    max_price = data['Close'].max()
    min_price = data['Close'].min()
    
    # Volatility (Độ biến động - rủi ro)
    volatility = data['Returns'].std() * 100 # Đổi ra %
    
    # 3. Tính Drawdown (Mức sụt giảm từ đỉnh)
    rolling_max = data['Close'].cummax()
    drawdown = (data['Close'] - rolling_max) / rolling_max
    max_drawdown = drawdown.min() * 100
    price_change = ((last_price - data['Close'].iloc[0]) / data['Close'].iloc[0]) * 100

    metrics_dict = {
        'first_open': first_open,
        'last_price': last_price,
        'max_price': max_price,
        'volatility': volatility,
        'max_drawdown': max_drawdown,
        'price_change': price_change,
        'min_price': min_price
    }

    return metrics_dict, data