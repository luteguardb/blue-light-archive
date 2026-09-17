import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Blue Light Archive",
    page_icon="💡",
    layout="wide"
)

# -----------------------------
# Google Sheets
# -----------------------------
SHEET_URL = (
    "https://docs.google.com/spreadsheets/d/"
    "1LiiTw-ytMjJAtpsd6OqYH5_84yiFBj_v4zTKs1FDDDA"
    "/gviz/tq?tqx=out:csv&gid=0"
)

@st.cache_data(ttl=60)
def load_data():
    return pd.read_csv(SHEET_URL)

# -----------------------------
# Header
# -----------------------------
st.title("BLUE LIGHT ARCHIVE")
st.caption("A public archive of blue light exposure data.")

# 수동 새로고침
if st.button("🔄 Refresh data"):
    st.cache_data.clear()
    st.rerun()

try:
    df = load_data()
except Exception as e:
    st.error("Google Sheets 데이터를 불러오지 못했습니다.")
    st.error(str(e))
    st.stop()

# -----------------------------
# Summary
# -----------------------------
col1, col2 = st.columns(2)

with col1:
    st.metric("Total records", f"{len(df):,}")

with col2:
    st.metric("Data fields", len(df.columns))

st.divider()

# -----------------------------
# Search
# -----------------------------
search = st.text_input(
    "🔎 Search the archive",
    placeholder="장소, 카테고리, 조명, 거리 등을 검색하세요"
)

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

# -----------------------------
# Database
# -----------------------------
st.dataframe(
    filtered_df,
    use_container_width=True,
    hide_index=True,
    height=650
)
