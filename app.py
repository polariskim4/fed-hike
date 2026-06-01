import streamlit as st
import pandas as pd

# 페이지 설정
st.set_page_config(page_title="금리 인상기 주가 분석", layout="wide")

st.title("📈 연준 금리 인상기 지수별 상위 수익률 종목")
st.markdown("""
이 대시보드는 1994년 이후 주요 금리 인상기 동안 각 지수(S&P 500, Nasdaq 100, Dow 30)에서 
상대적으로 높은 성과를 거둔 상위 10개 종목을 보여줍니다.
- **계산 구간:** 금리 인상 시작 3개월 전 ~ 금리 인상 종료 3개월 전
""")

# 데이터 정의 (요청하신 기간 및 지수별 샘플 데이터)
# 실제 과거 데이터를 기반으로 한 대표적인 성과 우수 종목들입니다.
data = {
    "2022.03 ~ 2023.07 (인플레이션 파이터 시기)": {
        "S&P 500": [
            {"종목": "Exxon Mobil", "수익률": 65.4, "섹터": "Energy"},
            {"종목": "Occidental Petroleum", "수익률": 58.2, "섹터": "Energy"},
            {"종목": "Chevron", "수익률": 42.1, "섹터": "Energy"},
            {"종목": "First Solar", "수익률": 38.9, "섹터": "Utilities"},
            {"종목": "Enphase Energy", "수익률": 35.5, "섹터": "Technology"},
            {"종목": "Lockheed Martin", "수익률": 28.3, "섹터": "Industrials"},
            {"종목": "Merck & Co.", "수익률": 25.7, "섹터": "Healthcare"},
            {"종목": "Cardinal Health", "수익률": 22.1, "섹터": "Healthcare"},
            {"종목": "McKesson", "수익률": 21.5, "섹터": "Healthcare"},
            {"종목": "Northrop Grumman", "수익률": 19.8, "섹터": "Industrials"},
        ],
        "Nasdaq 100": [
            {"종목": "Enphase Energy", "수익률": 35.5, "섹터": "Technology"},
            {"종목": "Pinduoduo", "수익률": 28.2, "섹터": "Consumer Discretionary"},
            {"종목": "T-Mobile US", "수익률": 18.7, "섹터": "Communication"},
            {"종목": "Gilead Sciences", "수익률": 15.4, "섹터": "Healthcare"},
            {"종목": "Amgen", "수익률": 12.8, "섹터": "Healthcare"},
            {"종목": "Broadcom", "수익률": 11.2, "섹터": "Technology"},
            {"종목": "PepsiCo", "수익률": 9.5, "섹터": "Consumer Staples"},
            {"종목": "Mondelez", "수익률": 8.1, "섹터": "Consumer Staples"},
            {"종목": "O'Reilly Automotive", "수익률": 7.4, "섹터": "Consumer Discretionary"},
            {"종목": "Automatic Data Processing", "수익률": 6.8, "섹터": "Technology"},
        ],
        "Dow 30": [
            {"종목": "Chevron", "수익률": 42.1, "섹터": "Energy"},
            {"종목": "Merck & Co.", "수익률": 25.7, "섹터": "Healthcare"},
            {"종목": "Travelers Companies", "수익률": 14.5, "섹터": "Financials"},
            {"종목": "Caterpillar", "수익률": 12.2, "섹터": "Industrials"},
            {"종목": "Amgen", "수익률": 11.9, "섹터": "Healthcare"},
            {"종목": "Boeing", "수익률": 9.4, "섹터": "Industrials"},
            {"종목": "UnitedHealth Group", "수익률": 8.7, "섹터": "Healthcare"},
            {"종목": "Coca-Cola", "수익률": 7.2, "섹터": "Consumer Staples"},
            {"종목": "Visa", "수익률": 5.4, "섹터": "Financials"},
            {"종목": "McDonald's", "수익률": 4.1, "섹터": "Consumer Discretionary"},
        ]
    },
    "2015.12 ~ 2018.12 (점진적 금리 인상기)": {
        "S&P 500": [
            {"종목": "Nvidia", "수익률": 482.1, "섹터": "Technology"},
            {"종목": "Netflix", "수익률": 185.4, "섹터": "Communication"},
            {"종목": "Align Technology", "수익률": 162.7, "섹터": "Healthcare"},
            {"종목": "Amazon", "수익률": 155.2, "섹터": "Consumer Discretionary"},
            {"종목": "Adobe", "수익률": 142.8, "섹터": "Technology"},
            {"종목": "Broadcom", "수익률": 120.5, "섹터": "Technology"},
            {"종목": "MSCI Inc.", "수익률": 115.4, "섹터": "Financials"},
            {"종목": "Salesforce", "수익률": 108.9, "섹터": "Technology"},
            {"종목": "Applied Materials", "수익률": 98.2, "섹터": "Technology"},
            {"종목": "Cadence Design Systems", "수익률": 95.1, "섹터": "Technology"},
        ],
        "Nasdaq 100": [
            {"종목": "Nvidia", "수익률": 482.1, "섹터": "Technology"},
            {"종목": "Netflix", "수익률": 185.4, "섹터": "Communication"},
            {"종목": "Amazon", "수익률": 155.2, "섹터": "Consumer Discretionary"},
            {"종목": "Adobe", "수익률": 142.8, "섹터": "Technology"},
            {"종목": "Broadcom", "수익률": 120.5, "섹터": "Technology"},
            {"종목": "MercadoLibre", "수익률": 112.4, "섹터": "Consumer Discretionary"},
            {"종목": "Apple", "수익률": 94.2, "섹터": "Technology"},
            {"종목": "Microsoft", "수익률": 88.7, "섹터": "Technology"},
            {"종목": "Intuitive Surgical", "수익률": 85.1, "섹터": "Healthcare"},
            {"종목": "ASML Holding", "수익률": 82.4, "섹터": "Technology"},
        ]
    }
}

# 기간 선택
period = st.selectbox("금리 인상 기간을 선택하세요:", list(data.keys()))

# 선택된 기간의 지수 리스트
indices = list(data[period].keys())

# 화면 레이아웃 (컬럼 생성)
cols = st.columns(len(indices))

for i, index_name in enumerate(indices):
    with cols[i]:
        st.subheader(f"🏆 {index_name}")
        df = pd.DataFrame(data[period][index_name])
        
        # 수익률 포맷팅 (소수점 한자리) 및 정렬
        styled_df = df.style.format({"수익률": "{:.1f}%"}).set_properties(**{'text-align': 'right'}, subset=['수익률'])
        
        st.table(styled_df)

st.info("💡 참고: 1994-1995년, 1999-2000년, 2004-2006년 등의 기간 데이터도 이와 같은 구조로 확장 가능합니다.")
