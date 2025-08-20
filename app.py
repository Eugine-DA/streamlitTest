import streamlit as st
import pandas as pd

st.set_page_config(page_title="테스트 대시보드", layout="wide")

# st.title("📊 테스트 대시보드")

# 샘플 데이터
data = {
    "월": ["1월", "2월", "3월", "4월", "5월"],
    "매출": [100, 150, 200, 250, 300]
}
df = pd.DataFrame(data)

# 테이블 표시
# st.subheader("매출 데이터")
st.dataframe(df)

# 차트 표시
# st.subheader("매출 추이")
st.line_chart(df.set_index("월"))

# st.success("대시보드 실행 성공 🎉")