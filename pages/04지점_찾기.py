import streamlit as st
import folium
from streamlit_folium import st_folium
import pandas as pd

df = pd.read_csv("data/kcar_centers_raw.csv", encoding='cp949')
df[['lat', 'lon']] = df['위경도'].str.split(',', expand=True).astype(float)

col1, col2 = st.columns([0.7, 0.3])

with col1:
    st.subheader("📍 지점 지도")
    
    m = folium.Map(location=[df.lat.mean(), df.lon.mean()], zoom_start=10)

    for i, row in df.iterrows():
        # 마커 추가
        folium.Marker(
            [row['lat'], row['lon']], 
            tooltip=row['직영점명'],
            icon=folium.Icon(color='red', icon='info-sign'),
            name=row['직영점명'] 
        ).add_to(m)

    # 지도 출력 및 클릭 이벤트 수신
    output = st_folium(m, height=500, use_container_width=True, key="center_map")

with col2:
    st.subheader("")
    
    # 마커 클릭 확인
    loc = output.get("last_object_clicked_tooltip")

    if loc:
        # 클릭한 지점 데이터 찾기
        branch_info = df[df['직영점명'] == loc].iloc[0]
        
        st.info(f"##### {branch_info['직영점명']}")
        st.write(f"📞 전화번호  \n: {branch_info['전화번호']}")
        st.write(f"🚗 보유 차량  \n: {branch_info['차량대수']} 대")
        st.write(f"🏠 주소  \n: {branch_info['주소1']} {branch_info['주소2']}")