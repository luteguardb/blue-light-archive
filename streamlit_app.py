import streamlit as st
import pandas as pd
from pathlib import Path

# 페이지 설정
st.set_page_config(
    page_title="Blue Light Archive",
    page_icon="💡",
    layout="wide"
)

# 제목
st.title("BLUE LIGHT ARCHIVE")
st.caption("A public archive of blue light exposure data.")

# Excel 파일 자동 찾기
excel_files = list(Path(".").glob("*.xlsx"))

if not excel_files:
    st.error("Excel database file was not found.")
    st.stop()

excel_file = excel_files[0]

# 데이터 읽기
@st.cache_data
def load_data(file):
    return pd.read_excel(file)

df = load_data(excel_file)

# 상단 정보
col1, col2 = st.columns(2)

with col1:
    st.metric("Total records", len(df))

with col2:
    st.metric("Data fields", len(df.columns))

st.divider()

# 검색창
search = st.text_input(
    "🔎 Search the archive",
    placeholder="Search place, device, distance, environment..."
)

# 검색
filtered_df = df.copy()

if search:
    mask = filtered_df.astype(str).apply(
        lambda row: row.str.contains(
            search,
            case=False,
            na=False
        ).any(),
        axis=1
    )

    filtered_df = filtered_df[mask]

st.write(f"**{len(filtered_df):,} records found**")

# 데이터 표
st.dataframe(
    filtered_df,
    use_container_width=True,
    hide_index=True,
    height=650
)
