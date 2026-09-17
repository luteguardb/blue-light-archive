import streamlit as st

# --------------------------------------------------
# SITE CONFIG
# --------------------------------------------------

st.set_page_config(
    page_title="LUTEGUARD-B™ | Blue Light Archive",
    page_icon="💡",
    layout="wide"
)

# --------------------------------------------------
# PAGES
# --------------------------------------------------

archive = st.Page(
    "archive.py",
    title="ARCHIVE",
    default=True
)

our_story = st.Page(
    "brand_story.py",
    title="OUR STORY"
)

luteguard = st.Page(
    "luteguard.py",
    title="LUTEGUARD-B™"
)

contact = st.Page(
    "contact.py",
    title="CONTACT"
)

# --------------------------------------------------
# TOP NAVIGATION
# --------------------------------------------------

page = st.navigation(
    [
        archive,
        our_story,
        luteguard,
        contact
    ],
    position="top"
)

page.run()
