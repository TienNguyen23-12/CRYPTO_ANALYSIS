import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from src.analysis.forecast import moving_average_forecast
from src.processing.chart import returns_histogram, price_volume_chart
from src.processing.load_time import get_time_range
from src.processing.ingestion import fetch_data
from src.processing.cleaning import clean_data
from src.analysis.statistics import calculate_metrics

# Cấu hình trang
st.set_page_config(page_title="CRYPTO_ANALYSIS", layout="wide")

st.title("💰 Phân Tích Dữ Liệu Tiền Ảo Bằng Python")
st.markdown("Đồ án môn học: Lập Trình Python")

# --- PHẦN 1: SIDEBAR (ĐIỀU KHIỂN) ---
with st.sidebar:
    st.header("Cấu hình dữ liệu")

    coin_map = {
        "Bitcoin (BTC)": "BTC-USD",
        "Ethereum (ETH)": "ETH-USD",
        "Binance Coin (BNB)": "BNB-USD",
        "Solana (SOL)": "SOL-USD",
    }

    selected_type = st.selectbox("Chọn đồng bạn muốn:", list(coin_map.keys()))
    coin_type_value = coin_map[selected_type]

    # ✅ Chọn theo TUẦN - tối đa 2 năm (104 tuần)
    weeks = st.slider(
        "Chọn số tuần (tối đa 104 tuần = 2 năm):",
        min_value=1,
        max_value=104,
        value=52,
        step=1,
    )

    selected_period = f"{weeks} tuần (Khung 1h)"
    period_value = f"{weeks}w"

    if st.button("🔄 Cập nhật dữ liệu mới nhất"):
        with st.spinner(f"Đang tải dữ liệu {selected_period}..."):
            success = fetch_data(coin_type=coin_type_value, period=period_value)

            if success:
                clean_data()
                st.success(f"Dữ liệu {selected_period} đã được cập nhật!")
                st.rerun()
            else:
                st.error("Tải dữ liệu thất bại!")

# --- PHẦN 2: LOAD DỮ LIỆU ---
try:
    # Đọc dữ liệu sạch
    df = pd.read_csv('data/cleaned_coin.csv', index_col=0, parse_dates=True)

    # Lấy mốc thời gian
    start_time, end_time = get_time_range()
    st.subheader(f"⏱ Thời điểm bắt đầu: {start_time}")
    st.subheader(f"⏱ Thời điểm kết thúc: {end_time}")

    # Tính toán chỉ số
    metrics, df_with_returns = calculate_metrics(df) # Nhận 2 giá trị
    
    # --- PHẦN 3: HIỂN THỊ CHỈ SỐ (METRICS) ---

    col1, col2, col3, col4, col5 = st.columns(5)
    col1.metric("Giá mở cửa", f"${metrics['first_open']:,.2f}")

    col2.metric("Giá hiện tại",
                f"${metrics['last_price']:,.2f}",
                delta=f"{metrics['price_change']:.2f}%")
    col3.metric(f"Đỉnh ({selected_period})",
                f"${metrics['max_price']:,.2f}")
    col4.metric("Rủi ro (Std Dev)",
                f"{metrics['volatility']:.2f}%")
    col5.metric("Sụt giảm từ đỉnh (MDD)",
                f"{metrics['max_drawdown']:.2f}%",
                delta_color="inverse")

    # --- PHẦN 4: BIỂU ĐỒ (VISUALIZATION) ---
    with st.sidebar:
        show_price = st.checkbox("📈 Biểu đồ giá", value=True)
        show_price_volume = st.checkbox("📊 Giá & khối lượng", value=False)
        show_returns = st.checkbox("📉 Phân phối lợi nhuận", value=False)
        show_forecast = st.checkbox("🔮 Dự báo xu hướng", value=False)
        show_data = st.checkbox("Dữ liệu ban đầu", value=False)

    # Tab 1: Biểu đồ giá
    if show_price:
        st.subheader("Biểu đồ giá")
        st.line_chart(df['Close'])

    # Tab 2: Khối lượng giao dịch theo giá
    if show_price_volume:
        fig1 = price_volume_chart(df)
        st.pyplot(fig1)

    # Tab 3: Phân phối lợi nhuận
    if show_returns:
        fig2 = returns_histogram(df_with_returns)
        st.pyplot(fig2)
        
    # Tab 4: Dự đoán
    if show_forecast: 
        st.subheader("🔮 Dự báo 7 ngày tiếp theo")

        forecast_df = moving_average_forecast(
            df,
            end_time=end_time,
            window=20,
            horizon=7
        )

        zoom_days = 60
        df_zoom = df.tail(zoom_days)

        fig, ax = plt.subplots(figsize=(10, 5))

        ax.plot(
            df_zoom.index,
            df_zoom["Close"],
            label="Giá thực tế",
            linewidth=2
        )

        ax.plot(
            forecast_df.index,
            forecast_df["Forecast"],
            linestyle="--",
            linewidth=2,
            label="Dự báo (MA)"
        )

        ax.axvline(
            end_time,
            linestyle=":",
            linewidth=2,
            label="Thời điểm hiện tại"
        )

        ax.legend()
        ax.set_title("Dự báo 7 ngày (Zoom 60 ngày gần nhất)")
        ax.set_xlabel("Thời gian")
        ax.set_ylabel("Giá")

        st.pyplot(fig)
        
        
        st.info(
        "⚠️ Dự báo được tính từ ngày cuối cùng của dữ liệu lịch sử "
        "đến 7 ngày tiếp theo. Kết quả chỉ mang tính học thuật."
        )

    # Dữ liệu thô
    if show_data:
        st.subheader('10 giá trị dữ liệu đầu tiên')
        st.write(df.head(10))
        st.subheader('10 giá trị dữ liệu cuối cùng')
        st.write(df.tail(10))

except FileNotFoundError:
    st.warning("⚠️ Chưa có dữ liệu. Vui lòng bấm nút 'Cập nhật dữ liệu mới nhất' ở bên trái.")
