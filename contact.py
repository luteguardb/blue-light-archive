import streamlit as st

st.title("CONTACT")

st.write("""
Luteguard-B 및 Blue Light Archive에 관한
협업, 연구, 제품 관련 문의를 받고 있습니다.
""")

st.divider()

st.subheader("Business & Partnership")

st.write("📧 Email: luteguard.b@gmail.com")

st.subheader("Inquiry")

name = st.text_input("Name")
email = st.text_input("Email")
message = st.text_area(
    "Message",
    height=180
)

st.info(
    "현재 문의 폼은 화면 구성 단계입니다. "
    "메일 발송 기능은 다음 단계에서 연결합니다."
)
