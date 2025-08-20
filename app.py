import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="테스트 대시보드", layout="wide")

# 복잡한 샘플 데이터 생성
np.random.seed(42) # 재현성을 위해 시드 설정

data = {
    "날짜": pd.to_datetime(pd.date_range("2024-01-01", periods=100, freq="D")),
    "카테고리": np.random.choice(["전자제품", "의류", "식품", "생활용품"], 100),
    "지역": np.random.choice(["서울", "경기", "부산", "제주"], 100),
    "판매량": np.random.randint(10, 100, 100),
    "매출액": np.random.randint(50000, 500000, 100),
    "할인율": np.random.uniform(0.0, 0.3, 100).round(2)
}
df = pd.DataFrame(data)

# '날짜' 컬럼을 인덱스로 설정
df = df.set_index("날짜")

# '매출액' 컬럼에 할인율 적용
df['실제매출액'] = df['매출액'] * (1 - df['할인율'])

# 데이터프레임 표시
st.dataframe(df)

# 추가 정보 표시
# st.write("데이터프레임 크기:", df.shape)
# st.write("데이터프레임 컬럼 정보:")
# st.write(df.info())