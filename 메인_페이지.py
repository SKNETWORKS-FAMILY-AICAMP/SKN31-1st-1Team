import streamlit as st
import pandas as pd

@st.cache_data
def get_data():
    df = pd.read_csv("data/kcar_cars_raw.csv")
    df['제조사'] = df['차량명'].apply(lambda x: x.split()[0])
    df['가격_숫자'] = df['가격'].str.split().str[-1].str.replace('[만원,]', '', regex=True).fillna(0).astype(int)
    return df

st.set_page_config(page_title="중고차 정보 조회", layout="wide")

df = get_data()

# 시장 요약 데이터
total_count = len(df) # 총 매물 수
avg_price = int(df['가격_숫자'].mean()) # 평균 가격
top_maker = df['제조사'].value_counts().idxmax() # 인기 제조사

empty_left, center_content, empty_right = st.columns([1, 2, 1])

with center_content:
    # 타이틀
    st.markdown("<h2 style='text-align: center; margin-bottom: 10px;'>🚗 중고 자동차 정보 조회 🚗</h1>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center; margin-bottom: 20px;'>< 시장 요약 ></h2>", unsafe_allow_html=True)

    # 시장 요약
    st.markdown(f"<p style='text-align: center; font-size: 20px; font-weight: bold;'>총 수집 매물 : {total_count:,} 대</p>", unsafe_allow_html=True)
    st.markdown(f"<p style='text-align: center; font-size: 20px; font-weight: bold;'>평균 가격 : {avg_price:,} 만원</p>", unsafe_allow_html=True)
    st.markdown(f"<p style='text-align: center; font-size: 20px; font-weight: bold; '>인기 제조사 : {top_maker}</p>", unsafe_allow_html=True)

    st.divider()

    # 페이지 링크
    st.page_link("pages/가격대별_매물_수.py", label="가격대별 매물 수 보러 가기", icon='📊')
    st.page_link("pages/연식별_가격_변화.py", label="연식별 평균 가격 변화 보러 가기", icon='📈')
    st.page_link("pages/중고차_정보_조회.py", label="내가 찾는 중고차 보러 가기", icon='🔍')
    st.page_link("pages/지점_찾기.py", label="전국 지점 찾기", icon='🗺️')