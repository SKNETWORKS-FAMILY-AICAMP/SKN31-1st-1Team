import streamlit as st
import pandas as pd

st.set_page_config(page_title="NULL 위한 차", layout="wide")

def extract_price(x):
    if pd.isnull(x): return 0
    
    last_word = str(x).split()[-1] 
    clean_num = last_word.replace('만원', '').replace(',', '')
    
    return int(clean_num)

@st.cache_data
def get_data():
    df = pd.read_csv("data/kcar_cars_raw.csv")
    # 제조사/모델 분리
    df['제조사'] = df['차량명'].apply(lambda x: x.split()[0])
    df['모델'] = df['차량명'].apply(lambda x: x.split()[1] if len(x.split()) > 1 else "기타")

    # 연식 전처리
    df['연식_년도'] = df['연식'].apply(lambda x: int("20" + x.split()[0][:2]) if len(str(x).split()) > 0 else 0)

    # 주행거리 전처리
    df['주행거리_숫자'] = df['주행거리'].apply(lambda x: int(str(x).replace('km', '').replace(',', '')) if pd.notnull(x) else 0)

    # 가격 전처리
    df['가격_숫자'] = df['가격'].apply(extract_price)

    # 필터링 오류를 막기 위해 타입을 숫자로 강제 고정
    df['연식_년도'] = df['연식_년도'].astype(int)
    df['주행거리_숫자'] = df['주행거리_숫자'].astype(int)
    df['가격_숫자'] = df['가격_숫자'].astype(int)

    return df

df = get_data()

with st.sidebar:
    st.header("상세 필터")

    # 제조사 선택
    brand_list = ["전체"] + sorted(df['제조사'].unique().tolist())
    select_brand = st.selectbox("제조사", brand_list)

    # 모델 선택
    if select_brand == "전체":
        model_list = ["전체"]
    else:
        model_fiter = df[df['제조사'] == select_brand]['모델'].unique().tolist()
        model_list = ["전체"] + sorted(model_fiter)

    select_model = st.selectbox("모델", model_list)

    # 연식 범위
    min_year, max_year = int(df['연식_년도'].min()), int(df['연식_년도'].max())
    year_range = st.slider("연식", min_year, max_year, (min_year, max_year))

    # 주행 거리 범위
    min_dist, max_dist = int(df['주행거리_숫자'].min()), int(df['주행거리_숫자'].max())
    dist_range = st.slider("주행 거리(km)", min_dist, max_dist, (min_dist, max_dist))

    # 가격 범위 
    min_price, max_price = int(df['가격_숫자'].min()), int(df['가격_숫자'].max())
    price_range = st.slider("가격(만 원)", min_price, max_price, (min_price, max_price))

# 필터링 로직
filtered_df = df.copy()

if select_brand != "전체":
    filtered_df = filtered_df[filtered_df['제조사'] == select_brand]

if select_model != "전체":
    filtered_df = filtered_df[filtered_df['모델'] == select_model]

# 슬라이더 범위 필터링
filtered_df = filtered_df[
    (filtered_df['연식_년도'].between(year_range[0], year_range[1])) &
    (filtered_df['가격_숫자'].between(price_range[0], price_range[1])) &
    (filtered_df['주행거리_숫자'].between(dist_range[0], dist_range[1]))
]

# 레이아웃 구성
empty_l, content, empty_r = st.columns([0.1, 0.8, 0.1])

with content:
    st.markdown(f"<h3 style='margin-bottom: 20px;'>🚗 검색 결과</h3>", unsafe_allow_html=True)
    st.info(f"검색된 매물: **{len(filtered_df)}** 대")
    
    # 데이터 표 출력
    st.dataframe(
        filtered_df[['차량명', '연식', '주행거리', '가격']], 
        hide_index=True
    )
    
    if filtered_df.empty:
        st.error("조건에 맞는 차량이 없습니다.")

    



