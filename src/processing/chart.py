import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.dates as mdates
import matplotlib.ticker as ticker  # Thêm thư viện để định dạng số
import numpy as np

def returns_histogram(df):
    """Biểu đồ phân phối lợi nhuận rõ nét hơn"""
    fig, ax = plt.subplots(figsize=(12, 6))  # Tăng chiều rộng

    # Vẽ Histogram với viền đen nhạt để phân tách các cột
    n, bins, patches = ax.hist(df['Returns'].dropna(), bins=80, color='#3498db',
                               edgecolor='#2c3e50', alpha=0.6, density=True)

    # Đường phân phối chuẩn
    mu = df['Returns'].mean()
    sigma = df['Returns'].std()
    y = ((1 / (np.sqrt(2 * np.pi) * sigma)) *
         np.exp(-0.5 * (1 / sigma * (bins - mu)) ** 2))
    ax.plot(bins, y, color='#e67e22', linewidth=3, label='Đường mật độ (KDE)')

    ax.axvline(mu, color='#e74c3c', linestyle='--', linewidth=2, label=f'Trung bình: {mu:.4f}')

    ax.set_title("PHÂN PHỐI LỢI NHUẬN", fontsize=16, fontweight='bold', pad=20)
    ax.set_xlabel("Tỷ suất sinh lời (%)", fontsize=12)
    ax.set_ylabel("Mật độ xuất hiện", fontsize=12)
    ax.legend(fontsize=10)
    ax.grid(True, linestyle='--', alpha=0.4)

    return fig


def price_volume_chart(df):
    """Biểu đồ Giá & Volume với cột khối lượng to và rõ hơn"""
    # Sử dụng layout="constrained" để các thành phần không bị đè lên nhau
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(14, 10), sharex=True,
                                   gridspec_kw={'height_ratios': [2.5, 1]},
                                   layout="constrained")

    # --- 1. BIỂU ĐỒ GIÁ ---
    ax1.plot(df.index, df['Close'], color='#2980b9', linewidth=2, label='Giá đóng cửa')
    ax1.fill_between(df.index, df['Close'], color='#3498db', alpha=0.15)

    ax1.set_title("DIỄN BIẾN GIÁ & KHỐI LƯỢNG GIAO DỊCH", fontsize=16, fontweight='bold', pad=15)
    ax1.set_ylabel('Giá (USD)', fontsize=12, fontweight='bold')
    ax1.grid(True, which='both', linestyle=':', alpha=0.5)

    # Định dạng trục Y cho giá (thêm dấu phẩy ngăn cách hàng nghìn)
    ax1.get_yaxis().set_major_formatter(ticker.FuncFormatter(lambda x, p: format(int(x), ',')))
    ax1.legend(loc='upper left', frameon=True)

    # --- 2. BIỂU ĐỒ KHỐI LƯỢNG (VOLUME) ---
    colors = np.where(df['Close'] >= df['Open'], '#26a69a', '#ef5350')

    # QUAN TRỌNG: Bỏ width=0.03 hoặc tăng lên để cột to hơn
    # Nếu dùng khung 1h (nhiều dữ liệu), bỏ width để Matplotlib tự tính là đẹp nhất
    ax2.bar(df.index, df['Volume'], color=colors, alpha=0.8)

    ax2.set_ylabel('Khối lượng', fontsize=12, fontweight='bold')
    ax2.set_xlabel('Thời gian', fontsize=12)
    ax2.grid(True, linestyle=':', alpha=0.5)

    # Định dạng trục Y cho Volume (Ví dụ: 1.0B thay vì 1e10)
    def format_volume(x, pos):
        if x >= 1e9: return f'{x * 1e-9:.1f}B'
        if x >= 1e6: return f'{x * 1e-6:.1f}M'
        return f'{x:,.0f}'

    ax2.yaxis.set_major_formatter(ticker.FuncFormatter(format_volume))

    # Định dạng trục X
    ax1.xaxis.set_major_formatter(mdates.DateFormatter('%d/%m/%Y'))
    ax1.xaxis.set_major_locator(mdates.AutoDateLocator())

    # Chú thích
    up_patch = mpatches.Patch(color='#26a69a', label='Giá tăng (Buy Volume)')
    down_patch = mpatches.Patch(color='#ef5350', label='Giá giảm (Sell Volume)')
    ax2.legend(handles=[up_patch, down_patch], loc='upper left', fontsize=10)

    return fig
