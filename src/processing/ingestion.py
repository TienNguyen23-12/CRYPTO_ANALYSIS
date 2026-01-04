import yfinance as yf
import re
import os
from datetime import datetime, timedelta


def _period_to_days(period) -> int:
    """
    Hỗ trợ:
      - 'Nw' (tuần)  -> N*7 ngày
      - 'Nd' (ngày)  -> N ngày
      - '1y', '2y'
      - int (ngày)
    """
    if period is None:
        return 365

    if isinstance(period, int):
        return max(1, period)

    p = str(period).strip().lower()

    if p.endswith("w") and p[:-1].isdigit():
        return max(1, int(p[:-1]) * 7)

    if p.endswith("d") and p[:-1].isdigit():
        return max(1, int(p[:-1]))

    if p == "1y":
        return 365

    if p == "2y":
        return 730

    # fallback: nếu ai truyền linh tinh -> mặc định 365 ngày
    m = re.match(r"^(\d+)$", p)
    if m:
        return max(1, int(m.group(1)))

    return 365


def fetch_data(coin_type, period="1y", interval=None):
    """
    ✅ Yêu cầu mới:
    - Chọn theo TUẦN
    - Tối đa 2 năm (730 ngày ~ 104 tuần)
    - Mỗi mốc dữ liệu là GIỜ => interval = '1h'

    period: ví dụ '1w', '8w', '52w', ... (từ app.py truyền sang)
    """
    # Ép khung giờ
    interval = "1h" if interval is None else interval

    days = _period_to_days(period)

    # Yahoo Finance giới hạn dữ liệu 1h tối đa khoảng 730 ngày
    if interval == "1h" and days > 730:
        days = 730

    end = datetime.utcnow()
    start = end - timedelta(days=days)

    print(f">>> Đang tải dữ liệu {coin_type} ({days} ngày, khung: {interval}) từ Yahoo Finance...")

    df = yf.download(
        tickers=coin_type,
        start=start,
        end=end,
        interval=interval,
        progress=False,
        auto_adjust=True,
    )

    if df.empty:
        print(">>> Lỗi: Không thể tải dữ liệu. Vui lòng kiểm tra lại kết nối hoặc tham số.")
        return False

    os.makedirs("data", exist_ok=True)
    df.to_csv("data/raw_coin.csv")
    print(f">>> Đã lưu file: data/raw_coin.csv (Khung: {interval})")
    return True
