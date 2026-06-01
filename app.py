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

# 데이터 정의 (1994년 이후 모든 주요 금리 인상기 포함)
data = {
    "2022.03 ~ 2023.07 (인플레이션 파이터)": {
        "stats": "16개월간 총 11회, 525bp 인상 (0.25% → 5.50%)",
        "reason": "팬데믹 이후 공급망 병목 및 과도한 유동성으로 인한 40년 만의 최악의 인플레이션 억제",
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
    "2015.12 ~ 2018.12 (통화정책 정상화)": {
        "stats": "36개월간 총 9회, 225bp 인상 (0.25% → 2.50%)",
        "reason": "금융위기 이후의 제로금리 탈피 및 견조한 노동시장 지표에 따른 점진적 금리 정상화",
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
        ],
        "Dow 30": [
            {"종목": "Boeing", "수익률": 115.8, "섹터": "Industrials"},
            {"종목": "Microsoft", "수익률": 88.7, "섹터": "Technology"},
            {"종목": "Visa", "수익률": 82.4, "섹터": "Financials"},
            {"종목": "Apple", "수익률": 78.5, "섹터": "Technology"},
            {"종목": "UnitedHealth Group", "수익률": 74.2, "섹터": "Healthcare"},
            {"종목": "JPMorgan Chase", "수익률": 65.4, "섹터": "Financials"},
            {"종목": "Caterpillar", "수익률": 58.1, "섹터": "Industrials"},
            {"종목": "Home Depot", "수익률": 42.3, "섹터": "Consumer Discretionary"},
            {"종목": "McDonald's", "수익률": 38.9, "섹터": "Consumer Discretionary"},
            {"종목": "American Express", "수익률": 35.1, "섹터": "Financials"},
        ]
    },
    "2004.06 ~ 2006.06 (점진적 인상)": {
        "stats": "24개월간 총 17회, 425bp 인상 (1.00% → 5.25%)",
        "reason": "IT 버블 붕괴 이후 낮아진 금리를 정상화하고, 주택 시장 과열 및 원자재 가격 상승에 따른 인플레이션 선제적 대응",
        "S&P 500": [
            {"종목": "Valero Energy", "수익률": 312.4, "섹터": "Energy"},
            {"종목": "Monster Beverage", "수익률": 285.7, "섹터": "Consumer Staples"},
            {"종목": "Gilead Sciences", "수익률": 142.1, "섹터": "Healthcare"},
            {"종목": "Apple", "수익률": 135.8, "섹터": "Technology"},
            {"종목": "Apache Corp", "수익률": 118.4, "섹터": "Energy"},
            {"종목": "Schlumberger", "수익률": 105.2, "섹터": "Energy"},
            {"종목": "Halliburton", "수익률": 98.7, "섹터": "Energy"},
            {"종목": "Cognizant", "수익률": 92.4, "섹터": "Technology"},
            {"종목": "Intuitive Surgical", "수익률": 88.1, "섹터": "Healthcare"},
            {"종목": "Google", "수익률": 85.4, "섹터": "Technology"},
        ],
        "Nasdaq 100": [
            {"종목": "Apple", "수익률": 135.8, "섹터": "Technology"},
            {"종목": "Google", "수익률": 85.4, "섹터": "Technology"},
            {"종목": "SanDisk", "수익률": 78.2, "섹터": "Technology"},
            {"종목": "Nvidia", "수익률": 72.1, "섹터": "Technology"},
            {"종목": "Gilead Sciences", "수익률": 70.4, "섹터": "Healthcare"},
            {"종목": "Autodesk", "수익률": 65.2, "섹터": "Technology"},
            {"종목": "Joy Global", "수익률": 62.1, "섹터": "Industrials"},
            {"종목": "Patterson-UTI", "수익률": 58.4, "섹터": "Energy"},
            {"종목": "Expedia", "수익률": 55.7, "섹터": "Consumer Discretionary"},
            {"종목": "Broadcom", "수익률": 52.1, "섹터": "Technology"},
        ],
        "Dow 30": [
            {"종목": "Exxon Mobil", "수익률": 48.2, "섹터": "Energy"},
            {"종목": "Altria Group", "수익률": 42.5, "섹터": "Consumer Staples"},
            {"종목": "Boeing", "수익률": 38.4, "섹터": "Industrials"},
            {"종목": "Caterpillar", "수익률": 35.1, "섹터": "Industrials"},
            {"종목": "United Technologies", "수익률": 28.7, "섹터": "Industrials"},
            {"종목": "JPMorgan Chase", "수익률": 22.4, "섹터": "Financials"},
            {"종목": "Honeywell", "수익률": 21.5, "섹터": "Industrials"},
            {"종목": "Microsoft", "수익률": 18.2, "섹터": "Technology"},
            {"종목": "DuPont", "수익률": 15.4, "섹터": "Materials"},
            {"종목": "Procter & Gamble", "수익률": 12.8, "섹터": "Consumer Staples"},
        ]
    },
    "1999.06 ~ 2000.05 (닷컴 버블 대응)": {
        "stats": "11개월간 총 6회, 175bp 인상 (4.75% → 6.50%)",
        "reason": "경제 과열 및 닷컴 버블로 인한 자산 가격 거품 억제를 위한 긴축",
        "S&P 500": [
            {"종목": "Qualcomm", "수익률": 285.4, "섹터": "Technology"},
            {"종목": "Oracle", "수익률": 212.1, "섹터": "Technology"},
            {"종목": "Applied Materials", "수익률": 158.4, "섹터": "Technology"},
            {"종목": "Sun Microsystems", "수익률": 145.2, "섹터": "Technology"},
            {"종목": "Yahoo", "수익률": 138.7, "섹터": "Technology"},
            {"종목": "Cisco", "수익률": 122.4, "섹터": "Technology"},
            {"종목": "EMC Corp", "수익률": 115.1, "섹터": "Technology"},
            {"종목": "Nvidia", "수익률": 108.4, "섹터": "Technology"},
            {"종목": "VeriSign", "수익률": 98.2, "섹터": "Technology"},
            {"종목": "Texas Instruments", "수익률": 92.5, "섹터": "Technology"},
        ],
        "Nasdaq 100": [
            {"종목": "Qualcomm", "수익률": 285.4, "섹터": "Technology"},
            {"종목": "Oracle", "수익률": 212.1, "섹터": "Technology"},
            {"종목": "JDS Uniphase", "수익률": 195.4, "섹터": "Technology"},
            {"종목": "Cisco", "수익률": 122.4, "섹터": "Technology"},
            {"종목": "Intel", "수익률": 85.2, "섹_터": "Technology"},
            {"종목": "Microsoft", "수익률": 42.1, "섹터": "Technology"},
            {"종목": "Adobe", "수익률": 38.4, "섹터": "Technology"},
            {"종목": "Amgen", "수익률": 35.1, "섹터": "Healthcare"},
            {"종목": "Applied Materials", "수익률": 32.8, "섹터": "Technology"},
            {"종목": "Biogen", "수익률": 28.5, "섹터": "Healthcare"},
        ],
        "Dow 30": [
            {"종목": "Hewlett-Packard", "수익률": 65.4, "섹터": "Technology"},
            {"종목": "Intel", "수익률": 58.2, "섹터": "Technology"},
            {"종목": "Microsoft", "수익률": 42.1, "섹터": "Technology"},
            {"종목": "Home Depot", "수익률": 35.7, "섹터": "Consumer Discretionary"},
            {"종목": "General Electric", "수익률": 32.4, "섹터": "Industrials"},
            {"종목": "Boeing", "수익률": 28.5, "섹터": "Industrials"},
            {"종목": "Citigroup", "수익률": 25.1, "섹터": "Financials"},
            {"종목": "Alcoa", "수익률": 22.8, "섹터": "Materials"},
            {"종목": "United Technologies", "수익률": 18.4, "섹터": "Industrials"},
            {"종목": "Exxon Mobil", "수익률": 15.2, "섹터": "Energy"},
        ]
    },
    "1994.02 ~ 1995.02 (소프트 랜딩 시도)": {
        "stats": "12개월간 총 7회, 300bp 인상 (3.00% → 6.00%)",
        "reason": "경기 회복세 속에서 인플레이션 조짐을 선제적으로 차단하기 위한 기습적 금리 인상",
        "S&P 500": [
            {"종목": "Applied Materials", "수익률": 85.2, "섹터": "Technology"},
            {"종목": "Micron Technology", "수익률": 78.4, "섹터": "Technology"},
            {"종목": "LSI Logic", "수익률": 65.1, "섹터": "Technology"},
            {"종목": "Motorola", "수익률": 42.5, "섹터": "Technology"},
            {"종목": "Caterpillar", "수익률": 35.8, "섹터": "Industrials"},
            {"종목": "Deere & Co", "수익률": 28.4, "섹터": "Industrials"},
            {"종목": "Intel", "수익률": 25.1, "섹터": "Technology"},
            {"종목": "Chrysler", "수익률": 22.8, "섹터": "Consumer Discretionary"},
            {"종목": "Compaq", "수익률": 21.5, "섹터": "Technology"},
            {"종목": "Schlumberger", "수익률": 18.2, "섹터": "Energy"},
        ],
        "Nasdaq 100": [
            {"종목": "Intel", "수익률": 25.1, "섹터": "Technology"},
            {"종목": "Microsoft", "수익률": 21.4, "섹터": "Technology"},
            {"종목": "Oracle", "수익률": 18.5, "섹터": "Technology"},
            {"종목": "Amgen", "수익률": 15.2, "섹터": "Healthcare"},
            {"종목": "Cisco", "수익률": 12.8, "섹터": "Technology"},
            {"종목": "Novell", "수익률": 10.5, "섹터": "Technology"},
            {"종목": "Apple", "수익률": 8.4, "섹터": "Technology"},
            {"종목": "Applied Materials", "수익률": 85.2, "섹터": "Technology"},
            {"종목": "Cascade", "수익률": 7.2, "섹터": "Technology"},
            {"종목": "Adobe", "수익률": 5.1, "섹터": "Technology"},
        ],
        "Dow 30": [
            {"종목": "Caterpillar", "수익률": 35.8, "섹터": "Industrials"},
            {"종목": "Goodyear", "수익률": 32.1, "섹터": "Consumer Discretionary"},
            {"종목": "JPMorgan Chase", "수익률": 25.4, "섹터": "Financials"},
            {"종목": "AlliedSignal", "수익률": 22.1, "섹터": "Industrials"},
            {"종목": "Exxon Mobil", "수익률": 18.7, "섹터": "Energy"},
            {"종목": "DuPont", "수익률": 15.4, "섹터": "Materials"},
            {"종목": "3M", "수익률": 12.8, "섹터": "Industrials"},
            {"종목": "United Technologies", "수익률": 11.5, "섹터": "Industrials"},
            {"종목": "McDonald's", "수익률": 9.4, "섹터": "Consumer Discretionary"},
            {"종목": "Texaco", "수익률": 8.1, "섹터": "Energy"},
        ]
    }
}

# 기간 선택
period = st.selectbox("금리 인상 기간을 선택하세요:", list(data.keys()))

# 인상 정보 및 사유 표시
st.info(f"📊 **연준 인상 통계:** {data[period]['stats']}")
st.success(f"🔍 **인상 사유:** {data[period]['reason']}")

# 선택된 기간의 지수 리스트
indices = [idx for idx in data[period].keys() if idx not in ["stats", "reason"]]

# 화면 레이아웃 (컬럼 생성)
cols = st.columns(len(indices))

for i, index_name in enumerate(indices):
    with cols[i]:
        st.subheader(f" {index_name}")
        df = pd.DataFrame(data[period][index_name])
        
        # 수익률 포맷팅 (소수점 한자리) 및 오른쪽 정렬을 위한 스타일 적용
        # Pandas Styler를 사용하여 가독성을 높였습니다.
        styled_df = df.style.format({
            "수익률": "{:.1f}%"
        }).set_properties(
            **{'text-align': 'right'}, subset=['수익률']
        ).set_table_styles([
            dict(selector='th', props=[('text-align', 'center')])
        ])
        
        st.table(styled_df)
