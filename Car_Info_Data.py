import csv
import os
import pandas as pd
import pymysql
from dotenv import load_dotenv


"""
DB 연결
- MySQL 데이터베이스에 CSV 데이터를 삽입
- DB에서 데이터를 조회하여 DataFrame으로 반환
"""

CSV_FILE1 = "data/kcar_cars_cleaned.csv"      # brand, model, year, mileage, price

# 데이터베이스 설정 (MYSQL)
load_dotenv()
db_config = {
    'user': os.getenv("DB_USER"),           # MySQL 사용자 이름
    'password': os.getenv("DB_PASSWORD"),   # MySQL 비밀번호
    'host': os.getenv("DB_HOST"),           # MySQL 호스트
    'port': int(os.getenv("DB_PORT")),
    'db': os.getenv("DB_NAME")        # 사용할 데이터베이스 이름
}
print(db_config)

# FAQ 데이터 삽입
def insert_car_info_to_db():

    conn = pymysql.connect(host=db_config['host'],
                           user=db_config['user'],
                           password=db_config['password'],
                           db=db_config['db'],
                           port=db_config['port'])
    cursor = conn.cursor()
    

    # car in 파일 읽기 및 데이터 삽입
    print("Car info inserting...")
    with open(CSV_FILE1, mode='r', encoding='utf-8-sig') as file:
        reader = csv.DictReader(file)
        for row in reader:
            cursor.execute(
                "INSERT INTO car_info (brand, model, car_year, mileage, price) VALUES (%s, %s, %s, %s, %s)",
                (row['Brand'], row['Model'], row['Year'], row['Mileage'], row['Price'])  
            )

    conn.commit()
    cursor.close()
    conn.close()
    print("FAQ data inserted successfully.")

# DB에서 데이터 조회하여 DataFrame으로 반환
def load_data_to_db(query):
    # MySQL 데이터베이스 연결
    conn = pymysql.connect(**db_config)

    df = pd.read_sql(query, conn)

    conn.close()
    return df

if __name__ == "__main__":
    insert_car_info_to_db()