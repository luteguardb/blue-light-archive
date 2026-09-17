import streamlit as st

st.title("LUTEGUARD-B™")

st.subheader("Light-conscious skincare for everyday life")

st.write("""
우리는 야외의 자외선뿐 아니라
일상 속에서 반복적으로 마주하는 다양한 빛 환경에 주목합니다.
""")

st.divider()

col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("MARIGOLD")
    st.write("""
    강화 교동도에서 시작한
    메리골드 원료 이야기
    """)

with col2:
    st.subheader("LUTEIN")
    st.write("""
    메리골드에서 유래한
    지용성 카로티노이드
    """)

with col3:
    st.subheader("DELIVERY")
    st.write("""
    리포좀과 나노에멀전 기술을 통한
    포뮬레이션 연구
    """)

st.divider()

st.header("Photo Repair")

st.write("""
일상적인 빛 환경에 노출된 피부를 위한
Luteguard-B의 스킨케어 접근입니다.
""")

st.header("Photo Protect")

st.write("""
생활광과 자외선 환경을 고려한
Luteguard-B의 프로텍션 라인입니다.
""")
