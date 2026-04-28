# SKN31-1st-1Team

## 팀 및 팀원 소개

### 팀 명
- **NULL(널) 위한 차**

### 팀원
| 안영선 | 김효민 | 이용혁 | 전서연 
| :---: | :---: | :---: | :---: |
| <a href="https://github.com/dksdudtjs94"><img src="https://img.shields.io/badge/GitHub-181717?style=flat-square&logo=GitHub&logoColor=white"/> | <a href="https://github.com/hyomin0357"><img src="https://img.shields.io/badge/GitHub-181717?style=flat-square&logo=GitHub&logoColor=white"/> | <a href="https://github.com/leeyonghyok"><img src="https://img.shields.io/badge/GitHub-181717?style=flat-square&logo=GitHub&logoColor=white"/> | <a href="https://github.com/sxoxyn"><img src="https://img.shields.io/badge/GitHub-181717?style=flat-square&logo=GitHub&logoColor=white"/> |
|<img src="images\마크.png" width="150" height="150"> | <img src="images\클리니.png" width="150" height="150"> | <img src="images\머스티.png" width="150" height="150"> | <img src="images\캠프.png" width="150" height="150"> |
| PM          | DB desing | Crawling          | Streamlit |
| DB, Data preprocessing|           | |          |                     | 

---

## 프로젝트 개요

### 프로젝트명

### 프로젝트 소개

### 프로젝트 배경 및 목표

### 프로젝트 구조
```
SKN31-1st-1Team
├─ data
│  ├─ hyundai_faq.csv
│  ├─ kcar_cars_cleaned.csv
│  ├─ kcar_cars_raw.csv
│  ├─ kcar_cars_raw_euc.csv
│  ├─ kcar_centers_raw.csv
│  ├─ kia_faq.csv
│  ├─ kia_faq_utf-8.csv
│  └─ run.ipynb
├─ FAQ_Data.py
├─ images
│  └─ erd.png
├─ pages
│  ├─ .DS_Store
│  ├─ DB_Query.sql
│  ├─ 가격대별_매물_수.py
│  ├─ 연식별_가격_변화.py
│  ├─ 중고차_정보_조회.py
│  ├─ 지점_찾기.py
│  └─ 질의응답.py
├─ README.md
├─ Car_Info_Data.py
└─ 메인_페이지.py

```

---

## 기술 스택

### Frontend
<img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white" alt="Streamlit">
<img src="https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html&logoColor=white" alt="HTML">
<img src="https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css&logoColor=white" alt="CSS">

### Backend & Database
<img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
<img src="https://img.shields.io/badge/MySQL-00618A?style=for-the-badge&logo=mysql&logoColor=white" alt="MySQL">

### Data Processing & Analysis
<img src="https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white" alt="Pandas">
<img src="https://img.shields.io/badge/Plotly-3F4F75?style=for-the-badge&logo=plotly&logoColor=white" alt="Plotly">
<img src="https://img.shields.io/badge/Folium-3F8F75?style=for-the-badge&logo=folium&logoColor=white" alt="Folium">


### Web Scraping
<img src="https://img.shields.io/badge/Requests-2F5F75?style=for-the-badge&logo=requests&logoColor=white" alt="Requests">
<img src="https://img.shields.io/badge/BeautifulSoup-18F75?style=for-the-badge&logo=beautifulsoup&logoColor=white" alt="BeautifulSoup">


---

## WBS

1단계: 데이터 수집 및 전처리
| 작업명 | 담당자 | 기간 | 상태 |
|--------|--------|------|------|
| 자동차 크롤링 | 이용혁 | 2026-04-27 | ✅  |
| FAQ 크롤링 | 이용혁 | 2026-04-27 | ✅  |
| 데이터 정제 | 이용혁, 안영선 | 2026-04-27 | ✅  |

2단계: 데이터베이스 설계 및 구축
| 작업명 | 담당자 | 기간 | 상태 |
|--------|--------|------|------|
| DB설계 | 안영선 | 2026-04-27 | ✅  |
| DB기획 | 김효민 | 2026-04-27 | ✅  |
| DB구현 | 김효민 | 2026-04-27 | ✅  |
| 데이터삽입 | 안영선 | 2026-04-27 | ✅  |
| DB테스트 | 김효민 | 2026-04-27 | ✅  |

3단계: UI 개발
| 작업명 | 담당자 | 기간 | 상태 |
|--------|--------|------|------|
| 퍼블리싱 | 전서연 | 2026-04-28 | ✅ |
| 프로그램개발 | 안영선, 전서연, 김효민 | 2026-04-28 | ✅ |
| 테스트 | 전체 | 2026-04-28 | ✅ |
| 산출물 정리 | 안영선, 전서연 | 2026-04-28 | ✅ |

---


## 데이터베이스 설계

### ERD
<img src="images\erd.png">

---

## 수행 결과
### 1) 메인 페이지 - 시장 현황
<img src="images\main_page.png">

### 2) 가격대별 매물 수
<img src="images\price.png">

### 3) 연식별 가격 변화
<img src="images\year.png">

### 4) 중고차 정보 조회
<img src="images\car_info.png">

### 5) 지점 찾기
<img src="images\car_branch.png">

### 6) 질의응답
<img src="images\faq.png">

## 한 줄 회고
#### 안영선
 - 데이터를 웹에서 크롤링하여 저장하고 이를 화면에 표현하는 것을 처음해봤는데 신기하였고, 여러가지를 표현하고 싶었지만 아쉽게도 아직 실력이 부족하여 하지 못한 것이 아쉬워서 다음에는 더 많은 것을 표현할 수 있게 노력하겠습니다.

#### 김효민
 - 프로젝트를 진행하며 배운 내용을 직접 적용해볼 수 있어서 좋은 경험이었습니다. 부족함이 많았지만 팀원들의 도움으로 한층 더 성장하게 된 것 같습니다. 다음에는 더 공부해서 프로젝트의 참여성을 더욱 높이고 싶습니다.

#### 이용혁
 - 중고차  판매 사이트에 있는 웹 데이터를 정적 및  동적 크롤링을 통해  수집하였습니다.  API를 통한 데이터 수집과 비교해 웹 크롤링을 통한 데이터 수집이 훨씬 더 어려웠습니다.  데이터 수집 이후 정제 과정에서도 마찬가지였습니다. 힘든  과정을 거친 후 수집한 데이터가 데이터베이스에 옮겨졌고,   팀 동료들의  수고 덕분에  훌륭한 정보로 구현되었습니다.  동료들과 함께 한 팀 프로젝트 과정을 통해 시간은 짧고,  비록 프로젝트 규모는 작았지만  상당한 성취감을 느낀 좋은 경험이었습니다.
 
#### 전서연
 - Streamlit을 복습하며 전체적인 화면을 설계하고, DB와 연결하여 통계를 표현하는 등의 경험을 해보았습니다. 간단하면서도 본격적인 단위 프로젝트에서 팀원분들의 도움도 받고 소통하며 성장을 느낀 것 같습니다. 다음 프로젝트에서는 복습과 공부에 시간을 더욱 들여 의미있는 기여를 하고 싶습니다.