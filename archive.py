import streamlit as st
import pandas as pd

# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------

st.set_page_config(
    page_title="Blue Light Archive",
    page_icon="💡",
    layout="wide"
)

# --------------------------------------------------
# GOOGLE SHEETS URL
# --------------------------------------------------

SHEET_URL = (
    "https://docs.google.com/spreadsheets/d/"
    "1LiiTw-ytMjJAtpsd6OqYH5_84yiFBj_v4zTKs1FDDDA"
    "/gviz/tq?tqx=out:csv&gid=0"
)

# --------------------------------------------------
# LOAD DATA
# --------------------------------------------------

@st.cache_data(ttl=60)
def load_data():

    df = pd.read_csv(SHEET_URL)

    # 완전히 빈 행 제거
    df = df.dropna(how="all")

    # 컬럼명의 앞뒤 공백 제거
    df.columns = [
        str(col).strip()
        for col in df.columns
    ]

    # 첫 번째 열의 긴 주의문을 "번호"로 변경
    first_column = df.columns[0]

    df = df.rename(
        columns={
            first_column: "번호"
        }
    )

    return df


# --------------------------------------------------
# HEADER
# --------------------------------------------------

st.title("BLUE LIGHT ARCHIVE")

st.caption(
    "A public archive of blue light exposure data."
)

st.write(
    "실내 환경에서의 블루라이트 노출 데이터를 "
    "검색하고 비교할 수 있는 공개 아카이브입니다."
)

# --------------------------------------------------
# NOTICE
# --------------------------------------------------

st.warning(
    "⚠️ 주의: 아래 블루라이트 값은 현장 실측값이 아니라, "
    "공개된 조도 기준/현장 조도 자료와 문헌의 실내 청색광-조도 관계를 "
    "이용한 ‘비교용 추정치’입니다. 실제 수치는 조명 SPD, 색온도, 거리, "
    "방향, 창문 자연광, 디스플레이 밝기에 따라 크게 달라집니다."
)

# --------------------------------------------------
# REFRESH BUTTON
# --------------------------------------------------

if st.button("🔄 Refresh data"):
    st.cache_data.clear()
    st.rerun()

# --------------------------------------------------
# LOAD DATA
# --------------------------------------------------

try:
    df = load_data()

except Exception as e:

    st.error(
        "Google Sheets 데이터를 불러오지 못했습니다."
    )

    st.code(str(e))

    st.stop()

# --------------------------------------------------
# SUMMARY
# --------------------------------------------------

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Total Records",
        f"{len(df):,}"
    )

with col2:

    if "대분류" in df.columns:

        category_count = (
            df["대분류"]
            .dropna()
            .nunique()
        )

        st.metric(
            "Categories",
            category_count
        )

    else:

        st.metric(
            "Categories",
            "-"
        )

with col3:

    if "장소" in df.columns:

        location_count = (
            df["장소"]
            .dropna()
            .nunique()
        )

        st.metric(
            "Locations",
            location_count
        )

    else:

        st.metric(
            "Locations",
            "-"
        )

st.divider()

# --------------------------------------------------
# SEARCH
# --------------------------------------------------

st.subheader("Search the Archive")

search = st.text_input(
    "🔎 Search",
    placeholder="장소, 대분류, 조명 톤, 노출 수준 등을 검색하세요"
)

# --------------------------------------------------
# FILTERS
# --------------------------------------------------

filtered_df = df.copy()

filter_col1, filter_col2 = st.columns(2)

# 대분류
with filter_col1:

    if "대분류" in df.columns:

        categories = (
            df["대분류"]
            .dropna()
            .astype(str)
            .unique()
            .tolist()
        )

        categories = sorted(categories)

        selected_category = st.selectbox(
            "대분류",
            ["전체"] + categories
        )

        if selected_category != "전체":

            filtered_df = filtered_df[
                filtered_df["대분류"].astype(str)
                == selected_category
            ]

# 상대 노출 수준
with filter_col2:

    if "상대 노출 수준" in df.columns:

        exposure_levels = (
            df["상대 노출 수준"]
            .dropna()
            .astype(str)
            .unique()
            .tolist()
        )

        exposure_levels = sorted(exposure_levels)

        selected_exposure = st.selectbox(
            "상대 노출 수준",
            ["전체"] + exposure_levels
        )

        if selected_exposure != "전체":

            filtered_df = filtered_df[
                filtered_df[
                    "상대 노출 수준"
                ].astype(str)
                == selected_exposure
            ]

# --------------------------------------------------
# TEXT SEARCH
# --------------------------------------------------

if search:

    search_mask = (
        filtered_df
        .astype(str)
        .apply(
            lambda row:
            row.str.contains(
                search,
                case=False,
                na=False
            ).any(),
            axis=1
        )
    )

    filtered_df = filtered_df[
        search_mask
    ]

# --------------------------------------------------
# RESULT COUNT
# --------------------------------------------------

st.write(
    f"**{len(filtered_df):,} records found**"
)

# --------------------------------------------------
# DATA TABLE
# --------------------------------------------------

st.dataframe(
    filtered_df,
    use_container_width=True,
    hide_index=True,
    height=650
)

# --------------------------------------------------
# FOOTNOTE
# --------------------------------------------------

st.divider()

st.caption(
    "Blue Light Archive · LuteguardB"
)
