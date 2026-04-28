import streamlit as st
import pandas as pd
import Car_Info_Data as ci
import plotly.express as px

st.set_page_config(page_title="NULL 위한 차", layout="wide")

df = ci.load_data_to_db("SELECT * FROM car_info")

st.title("Car Info")
st.markdown("---")

df['price'] = pd.to_numeric(df['price'], errors='coerce')
df['car_year'] = pd.to_numeric(df['car_year'], errors='coerce')
df = df.dropna(subset=['price', 'car_year'])

# @st.cache_data
# def get_data():
#     df = pd.read_csv("data/kcar_cars_raw.csv")
    
#     df['제조사'] = df['model'].str.split().str[0]
#     df['연식_년도'] = df['car_year'].str.split().str[0].str[:2].apply(lambda x: int("20" + x) if x.isdigit() else None)
#     df['가격_숫자'] = df['price'].str.split().str[-1].str.replace('[만원,]', '', regex=True).astype(int)
    
#     return df

# df = get_data()

# 페이지 레이아웃
st.subheader("📈 연식별 가격 변화")
st.write("연식별로 변하는 가격을 확인하세요!")

# 사이드바 필터
with st.sidebar:
    st.header("상세 필터")
    brand_list = ["전체"] + sorted(df['brand'].unique().tolist())
    selected_brand = st.selectbox("제조사 선택", brand_list)

# 데이터 그룹화 
filtered_df = df.copy()
if selected_brand != "전체":
    filtered_df = filtered_df[filtered_df['brand'] == selected_brand]

trend_df = filtered_df.groupby('car_year')['price'].mean().reset_index()
trend_df = trend_df.sort_values('car_year')

fig = px.line(
    trend_df, 
    x='car_year', 
    y='price',
    markers=True, # 점 표시
    title=f"[{selected_brand}]",
    labels={'car_year': '연식(년)', 'price': '평균 가격(만 원)'},
    color_discrete_sequence=['#FF4B4B'] # K Car 레드 컬러 적용
)

fig.update_layout(
    hovermode="x unified", # 마우스 올렸을 때 수치 한꺼번에 보기
    xaxis=dict(dtick=1),   # 연도 간격을 1년 단위로
    plot_bgcolor='rgba(0,0,0,0)'
)

st.plotly_chart(fig, use_container_width=True)

# 하단 : 데이터 분석
if not trend_df.empty:
    oldest_price = trend_df.iloc[0]['price']
    newest_price = trend_df.iloc[-1]['price']
    diff = newest_price - oldest_price
    
    st.info(f"💡 {trend_df['car_year'].min()}년 대비 {trend_df['car_year'].max()}년식의 평균 가격은 약 **{int(diff):,}만원** 차이가 납니다.")