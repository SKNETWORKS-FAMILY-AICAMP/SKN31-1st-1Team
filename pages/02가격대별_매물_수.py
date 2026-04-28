import streamlit as st
import pandas as pd
import Car_Info_Data as ci
import plotly.express as px

st.set_page_config(page_title="NULL 위한 차", layout="wide")

# DB 데이터 로드
df = ci.load_data_to_db("SELECT * FROM car_info")

# 데이터 전처리(DB price컬럼 데이터를 숫자로 변환)
df['price'] = pd.to_numeric(df['price'], errors='coerce')

# 가격 구간 설정
bins = [0, 1000, 2000, 3000, 4000, 5000, 10000, 30000]
labels = ['1천 미만', '1~2천', '2~3천', '3~4천', '4~5천', '5천~1억', '1억 이상']

df['가격대'] = pd.cut(df['price'], bins=bins, labels=labels, right=False)

# 가격대별 매물 수 집계
price_counts = df['가격대'].value_counts().reindex(labels).reset_index()
price_counts.columns = ['가격대', '매물수']

# 페이지 레이아웃
st.subheader("📊 가격대별 매물 수")
st.write("현재 등록된 중고차의 가격 분포를 확인하세요!")

fig = px.bar(
    price_counts, 
    x='가격대', 
    y='매물수',
    text='매물수', 
    color='매물수', 
    color_continuous_scale='Reds',
    labels={'매물수': '매물 수(대)', '가격대': '가격대'},
    title='K Car 직영점 가격대별 매물 분포'
)

fig.update_layout(
    xaxis_tickangle=0, 
    plot_bgcolor='rgba(0,0,0,0)',
    
)

st.plotly_chart(fig, use_container_width=True)

# 하단 : 데이터 요약 정보
st.divider()
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("총 매물 수", f"{len(df):,} 대")
with col2:
    st.metric("평균 가격", f"{int(df['price'].mean()):,} 만원")
with col3:
    st.metric("최고가 매물", f"{int(df['price'].max())/10000:} 억원")