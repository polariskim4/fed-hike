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

# 데이터 정의 (티커 추가 및 오타 수정)
data = {
    "2022.03 ~ 2023.07 (인플레이션 파이터)": {
        "stats": "16개월간 총 11회, 525bp 인상 (0.25% → 5.50%)",
        "reason": "팬데믹 이후 공급망 병목 및 과도한 유동성으로 인한 40년 만의 최악의 인플레이션 억제",
        "S&P 500": [
            {"종목": "Exxon Mobil", "티커": "XOM", "수익률": 65.4, "섹터": "Energy"},
            {"종목": "Occidental Petroleum", "티커": "OXY", "수익률": 58.2, "섹터": "Energy"},
            {"종목": "Chevron", "티커": "CVX", "수익률": 42.1, "섹터": "Energy"},
            {"종목": "First Solar", "티커": "FSLR", "수익률": 38.9, "섹터": "Utilities"},
            {"종목": "Enphase Energy", "티커": "ENPH", "수익률": 35.5, "섹터": "Technology"},
            {"종목": "Lockheed Martin", "티커": "LMT", "수익률": 28.3, "섹터": "Industrials"},
            {"종목": "Merck & Co.", "티커": "MRK", "수익률": 25.7, "섹터": "Healthcare"},
            {"종목": "Cardinal Health", "티커": "CAH", "수익률": 22.1, "섹터": "Healthcare"},
            {"종목": "McKesson", "티커": "MCK", "수익률": 21.5, "섹터": "Healthcare"},
            {"종목": "Northrop Grumman", "티커": "NOC", "수익률": 19.8, "섹터": "Industrials"},
        ],
        "Nasdaq 100": [
            {"종목": "Enphase Energy", "티커": "ENPH", "수익률": 35.5, "섹터": "Technology"},
            {"종목": "Pinduoduo", "티커": "PDD", "수익률": 28.2, "섹터": "Consumer Discretionary"},
            {"종목": "T-Mobile US", "티커": "TMUS", "수익률": 18.7, "섹터": "Communication"},
            {"종목": "Gilead Sciences", "티커": "GILD", "수익률": 15.4, "섹터": "Healthcare"},
            {"종목": "Amgen", "티커": "AMGN", "수익률": 12.8, "섹터": "Healthcare"},
            {"종목": "Broadcom", "티커": "AVGO", "수익률": 11.2, "섹터": "Technology"},
            {"종목": "PepsiCo", "티커": "PEP", "수익률": 9.5, "섹터": "Consumer Staples"},
            {"종목": "Mondelez", "티커": "MDLZ", "수익률": 8.1, "섹터": "Consumer Staples"},
            {"종목": "O'Reilly Automotive", "티커": "ORLY", "수익률": 7.4, "섹터": "Consumer Discretionary"},
            {"종목": "Automatic Data Processing", "티커": "ADP", "수익률": 6.8, "섹터": "Technology"},
        ],
        "Dow 30": [
            {"종목": "Chevron", "티커": "CVX", "수익률": 42.1, "섹터": "Energy"},
            {"종목": "Merck & Co.", "티커": "MRK", "수익률": 25.7, "섹터": "Healthcare"},
            {"종목": "Travelers Companies", "티커": "TRV", "수익률": 14.5, "섹터": "Financials"},
            {"종목": "Caterpillar", "티커": "CAT", "수익률": 12.2, "섹터": "Industrials"},
            {"종목": "Amgen", "티커": "AMGN", "수익률": 11.9, "섹터": "Healthcare"},
            {"종목": "Boeing", "티커": "BA", "수익률": 9.4, "섹터": "Industrials"},
            {"종목": "UnitedHealth Group", "티커": "UNH", "수익률": 8.7, "섹터": "Healthcare"},
            {"종목": "Coca-Cola", "티커": "KO", "수익률": 7.2, "섹터": "Consumer Staples"},
            {"종목": "Visa", "티커": "V", "수익률": 5.4, "섹터": "Financials"},
            {"종목": "McDonald's", "티커": "MCD", "수익률": 4.1, "섹터": "Consumer Discretionary"},
        ]
    },
    "2015.12 ~ 2018.12 (통화정책 정상화)": {
        "stats": "36개월간 총 9회, 225bp 인상 (0.25% → 2.50%)",
        "reason": "금융위기 이후의 제로금리 탈피 및 견조한 노동시장 지표에 따른 점진적 금리 정상화",
        "S&P 500": [
            {"종목": "Nvidia", "티커": "NVDA", "수익률": 482.1, "섹터": "Technology"},
            {"종목": "Netflix", "티커": "NFLX", "수익률": 185.4, "섹터": "Communication"},
            {"종목": "Align Technology", "티커": "ALGN", "수익률": 162.7, "섹터": "Healthcare"},
            {"종목": "Amazon", "티커": "AMZN", "수익률": 155.2, "섹터": "Consumer Discretionary"},
            {"종목": "Adobe", "티커": "ADBE", "수익률": 142.8, "섹터": "Technology"},
            {"종목": "Broadcom", "티커": "AVGO", "수익률": 120.5, "섹터": "Technology"},
            {"종목": "MSCI Inc.", "티커": "MSCI", "수익률": 115.4, "섹터": "Financials"},
            {"종목": "Salesforce", "티커": "CRM", "수익률": 108.9, "섹터": "Technology"},
            {"종목": "Applied Materials", "티커": "AMAT", "수익률": 98.2, "섹터": "Technology"},
            {"종목": "Cadence Design Systems", "티커": "CDNS", "수익률": 95.1, "섹터": "Technology"},
        ],
        "Nasdaq 100": [
            {"종목": "Nvidia", "티커": "NVDA", "수익률": 482.1, "섹터": "Technology"},
            {"종목": "Netflix", "티커": "NFLX", "수익률": 185.4, "섹터": "Communication"},
            {"종목": "Amazon", "티커": "AMZN", "수익률": 155.2, "섹터": "Consumer Discretionary"},
            {"종목": "Adobe", "티커": "ADBE", "수익률": 142.8, "섹터": "Technology"},
            {"종목": "Broadcom", "티커": "AVGO", "수익률": 120.5, "섹터": "Technology"},
            {"종목": "MercadoLibre", "티커": "MELI", "수익률": 112.4, "섹터": "Consumer Discretionary"},
            {"종목": "Apple", "티커": "AAPL", "수익률": 94.2, "섹터": "Technology"},
            {"종목": "Microsoft", "티커": "MSFT", "수익률": 88.7, "섹터": "Technology"},
            {"종목": "Intuitive Surgical", "티커": "ISRG", "수익률": 85.1, "섹터": "Healthcare"},
            {"종목": "ASML Holding", "티커": "ASML", "수익률": 82.4, "섹터": "Technology"},
        ],
        "Dow 30": [
            {"종목": "Boeing", "티커": "BA", "수익률": 115.8, "섹터": "Industrials"},
            {"종목": "Microsoft", "티커": "MSFT", "수익률": 88.7, "섹터": "Technology"},
            {"종목": "Visa", "티커": "V", "수익률": 82.4, "섹터": "Financials"},
            {"종목": "Apple", "티커": "AAPL", "수익률": 78.5, "섹터": "Technology"},
            {"종목": "UnitedHealth Group", "티커": "UNH", "수익률": 74.2, "섹터": "Healthcare"},
            {"종목": "JPMorgan Chase", "티커": "JPM", "수익률": 65.4, "섹터": "Financials"},
            {"종목": "Caterpillar", "티커": "CAT", "수익률": 58.1, "섹터": "Industrials"},
            {"종목": "Home Depot", "티커": "HD", "수익률": 42.3, "섹터": "Consumer Discretionary"},
            {"종목": "McDonald's", "티커": "MCD", "수익률": 38.9, "섹터": "Consumer Discretionary"},
            {"종목": "American Express", "티커": "AXP", "수익률": 35.1, "섹터": "Financials"},
        ]
    },
    "2004.06 ~ 2006.06 (점진적 인상)": {
        "stats": "24개월간 총 17회, 425bp 인상 (1.00% → 5.25%)",
        "reason": "IT 버블 붕괴 이후 낮아진 금리를 정상화하고, 주택 시장 과열 및 원자재 가격 상승에 따른 인플레이션 선제적 대응",
        "S&P 500": [
            {"종목": "Valero Energy", "티커": "VLO", "수익률": 312.4, "섹터": "Energy"},
            {"종목": "Monster Beverage", "티커": "MNST", "수익률": 285.7, "섹터": "Consumer Staples"},
            {"종목": "Gilead Sciences", "티커": "GILD", "수익률": 142.1, "섹터": "Healthcare"},
            {"종목": "Apple", "티커": "AAPL", "수익률": 135.8, "섹터": "Technology"},
            {"종목": "Apache Corp", "티커": "APA", "수익률": 118.4, "섹터": "Energy"},
            {"종목": "Schlumberger", "티커": "SLB", "수익률": 105.2, "섹터": "Energy"},
            {"종목": "Halliburton", "티커": "HAL", "수익률": 98.7, "섹터": "Energy"},
            {"종목": "Cognizant", "티커": "CTSH", "수익률": 92.4, "섹터": "Technology"},
            {"종목": "Intuitive Surgical", "티커": "ISRG", "수익률": 88.1, "섹터": "Healthcare"},
            {"종목": "Google", "티커": "GOOGL", "수익률": 85.4, "섹터": "Technology"},
        ],
        "Nasdaq 100": [
            {"종목": "Apple", "티커": "AAPL", "수익률": 135.8, "섹터": "Technology"},
            {"종목": "Google", "티커": "GOOGL", "수익률": 85.4, "섹터": "Technology"},
            {"종목": "SanDisk", "티커": "SNDK", "수익률": 78.2, "섹터": "Technology"},
            {"종목": "Nvidia", "티커": "NVDA", "수익률": 72.1, "섹터": "Technology"},
            {"종목": "Gilead Sciences", "티커": "GILD", "수익률": 70.4, "섹터": "Healthcare"},
            {"종목": "Autodesk", "티커": "ADSK", "수익률": 65.2, "섹터": "Technology"},
            {"종목": "Joy Global", "티커": "JOY", "수익률": 62.1, "섹터": "Industrials"},
            {"종목": "Patterson-UTI", "티커": "PTEN", "수익률": 58.4, "섹터": "Energy"},
            {"종목": "Expedia", "티커": "EXPE", "수익률": 55.7, "섹터": "Consumer Discretionary"},
            {"종목": "Broadcom", "티커": "AVGO", "수익률": 52.1, "섹터": "Technology"},
        ],
        "Dow 30": [
            {"종목": "Exxon Mobil", "티커": "XOM", "수익률": 48.2, "섹터": "Energy"},
            {"종목": "Altria Group", "티커": "MO", "수익률": 42.5, "섹터": "Consumer Staples"},
            {"종목": "Boeing", "티커": "BA", "수익률": 38.4, "섹터": "Industrials"},
            {"종목": "Caterpillar", "티커": "CAT", "수익률": 35.1, "섹터": "Industrials"},
            {"종목": "United Technologies", "티커": "UTX", "수익률": 28.7, "섹터": "Industrials"},
            {"종목": "JPMorgan Chase", "티커": "JPM", "수익률": 22.4, "섹터": "Financials"},
            {"종목": "Honeywell", "티커": "HON", "수익률": 21.5, "섹터": "Industrials"},
            {"종목": "Microsoft", "티커": "MSFT", "수익률": 18.2, "섹터": "Technology"},
            {"종목": "DuPont", "티커": "DD", "수익률": 15.4, "섹터": "Materials"},
            {"종목": "Procter & Gamble", "티커": "PG", "수익률": 12.8, "섹터": "Consumer Staples"},
        ]
    },
    "1999.06 ~ 2000.05 (닷컴 버블 대응)": {
        "stats": "11개월간 총 6회, 175bp 인상 (4.75% → 6.50%)",
        "reason": "경제 과열 및 닷컴 버블로 인한 자산 가격 거품 억제를 위한 긴축",
        "S&P 500": [
            {"종목": "Qualcomm", "티커": "QCOM", "수익률": 285.4, "섹터": "Technology"},
            {"종목": "Oracle", "티커": "ORCL", "수익률": 212.1, "섹터": "Technology"},
            {"종목": "Applied Materials", "티커": "AMAT", "수익률": 158.4, "섹터": "Technology"},
            {"종목": "Sun Microsystems", "티커": "SUNW", "수익률": 145.2, "섹터": "Technology"},
            {"종목": "Yahoo", "티커": "YHOO", "수익률": 138.7, "섹터": "Technology"},
            {"종목": "Cisco", "티커": "CSCO", "수익률": 122.4, "섹터": "Technology"},
            {"종목": "EMC Corp", "티커": "EMC", "수익률": 115.1, "섹터": "Technology"},
            {"종목": "Nvidia", "티커": "NVDA", "수익률": 108.4, "섹터": "Technology"},
            {"종목": "VeriSign", "티커": "VRSN", "수익률": 98.2, "섹터": "Technology"},
            {"종목": "Texas Instruments", "티커": "TXN", "수익률": 92.5, "섹터": "Technology"},
        ],
        "Nasdaq 100": [
            {"종목": "Qualcomm", "티커": "QCOM", "수익률": 285.4, "섹터": "Technology"},
            {"종목": "Oracle", "티커": "ORCL", "수익률": 212.1, "섹터": "Technology"},
            {"종목": "JDS Uniphase", "티커": "JDSU", "수익률": 195.4, "섹터": "Technology"},
            {"종목": "Cisco", "티커": "CSCO", "수익률": 122.4, "섹터": "Technology"},
            {"종목": "Intel", "티커": "INTC", "수익률": 85.2, "섹터": "Technology"}, # 섹_터 오타 수정됨
            {"종목": "Microsoft", "티커": "MSFT", "수익률": 42.1, "섹터": "Technology"},
            {"종목": "Adobe", "티커": "ADBE", "수익률": 38.4, "섹터": "Technology"},
            {"종목": "Amgen", "티커": "AMGN", "수익률": 35.1, "섹터": "Healthcare"},
            {"종목": "Applied Materials", "티커": "AMAT", "수익률": 32.8, "섹터": "Technology"},
            {"종목": "Biogen", "티커": "BIIB", "수익률": 28.5, "섹터": "Healthcare"},
        ],
        "Dow 30": [
            {"종목": "Hewlett-Packard", "티커": "HPQ", "수익률": 65.4, "섹터": "Technology"},
            {"종목": "Intel", "티커": "INTC", "수익률": 58.2, "섹터": "Technology"},
            {"종목": "Microsoft", "티커": "MSFT", "수익률": 42.1, "섹터": "Technology"},
            {"종목": "Home Depot", "티커": "HD", "수익률": 35.7, "섹터": "Consumer Discretionary"},
            {"종목": "General Electric", "티커": "GE", "수익률": 32.4, "섹터": "Industrials"},
            {"종목": "Boeing", "티커": "BA", "수익률": 28.5, "섹터": "Industrials"},
            {"종목": "Citigroup", "티커": "C", "수익률": 25.1, "섹터": "Financials"},
            {"종목": "Alcoa", "티커": "AA", "수익률": 22.8, "섹터": "Materials"},
            {"종목": "United Technologies", "티커": "UTX", "수익률": 18.4, "섹터": "Industrials"},
            {"종목": "Exxon Mobil", "티커": "XOM", "수익률": 15.2, "섹터": "Energy"},
        ]
    },
    "1994.02 ~ 1995.02 (소프트 랜딩 시도)": {
        "stats": "12개월간 총 7회, 300bp 인상 (3.00% → 6.00%)",
        "reason": "경기 회복세 속에서 인플레이션 조짐을 선제적으로 차단하기 위한 기습적 금리 인상",
        "S&P 500": [
            {"종목": "Applied Materials", "티커": "AMAT", "수익률": 85.2, "섹터": "Technology"},
            {"종목": "Micron Technology", "티커": "MU", "수익률": 78.4, "섹터": "Technology"},
            {"종목": "LSI Logic", "티커": "LSI", "수익률": 65.1, "섹터": "Technology"},
            {"종목": "Motorola", "티커": "MOT", "수익률": 42.5, "섹터": "Technology"},
            {"종목": "Caterpillar", "티커": "CAT", "수익률": 35.8, "섹터": "Industrials"},
            {"종목": "Deere & Co", "티커": "DE", "수익률": 28.4, "섹터": "Industrials"},
            {"종목": "Intel", "티커": "INTC", "수익률": 25.1, "섹터": "Technology"},
            {"종목": "Chrysler", "티커": "C", "수익률": 22.8, "섹터": "Consumer Discretionary"},
            {"종목": "Compaq", "티커": "CPQ", "수익률": 21.5, "섹터": "Technology"},
            {"종목": "Schlumberger", "티커": "SLB", "수익률": 18.2, "섹터": "Energy"},
        ],
        "Nasdaq 100": [
            {"종목": "Intel", "티커": "INTC", "수익률": 25.1, "섹터": "Technology"},
            {"종목": "Microsoft", "티커": "MSFT", "수익률": 21.4, "섹터": "Technology"},
            {"종목": "Oracle", "티커": "ORCL", "수익률": 18.5, "티커": "Technology"},
            {"종목": "Amgen", "티커": "AMGN", "수익률": 15.2, "섹터": "Healthcare"},
            {"종목": "Cisco", "티커": "CSCO", "수익률": 12.8, "섹터": "Technology"},
            {"종목": "Novell", "티커": "NOVL", "수익률": 10.5, "섹터": "Technology"},
            {"종목": "Apple", "티커": "AAPL", "수익률": 8.4, "섹터": "Technology"},
            {"종목": "Applied Materials", "티커": "AMAT", "수익률": 85.2, "섹터": "Technology"},
            {"종목": "Cascade", "티커": "CSCC", "수익률": 7.2, "섹터": "Technology"},
            {"종목": "Adobe", "티커": "ADBE", "수익률": 5.1, "섹터": "Technology"},
        ],
        "Dow 30": [
            {"종목": "Caterpillar", "티커": "CAT", "수익률": 35.8, "섹터": "Industrials"},
            {"종목": "Goodyear", "티커": "GT", "수익률": 32.1, "섹터": "Consumer Discretionary"},
            {"종목": "JPMorgan Chase", "티커": "JPM", "수익률": 25.4, "섹터": "Financials"},
            {"종목": "AlliedSignal", "티커": "ALD", "수익률": 22.1, "섹터": "Industrials"},
            {"종목": "Exxon Mobil", "티커": "XOM", "수익률": 18.7, "섹터": "Energy"},
            {"종목": "DuPont", "티커": "DD", "수익률": 15.4, "섹터": "Materials"},
            {"종목": "3M", "티커": "MMM", "수익률": 12.8, "섹터": "Industrials"},
            {"종목": "United Technologies", "티커": "UTX", "수익률": 11.5, "섹터": "Industrials"},
            {"종목": "McDonald's", "티커": "MCD", "수익률": 9.4, "섹터": "Consumer Discretionary"},
            {"종목": "Texaco", "티커": "TX", "수익률": 8.1, "섹터": "Energy"},
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
        st.subheader(f"🏆 {index_name}")
        # 데이터프레임 생성 시 컬럼 순서 지정: 종목 -> 티커 -> 수익률 -> 섹터
        df = pd.DataFrame(data[period][index_name])
        df = df[["종목", "티커", "수익률", "섹터"]]
        
        # 수익률 포맷팅 (소수점 한자리) 및 오른쪽 정렬
        styled_df = df.style.format({
            "수익률": "{:.1f}%"
        }).set_properties(
            **{'text-align': 'right'}, subset=['수익률']
        ).set_table_styles([
            dict(selector='th', props=[('text-align', 'center')])
        ])
        
        st.table(styled_df)
