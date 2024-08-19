import streamlit as st

st.set_page_config(layout="wide")
col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png")

with col2:
    st.title("Prosper Lin")
    content = """
    我是林禹安，現在在練習寫程式，以下是我的作品集
    """
    st.info(content)

st