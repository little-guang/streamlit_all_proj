import streamlit as st


st.set_page_config(
    page_title="專案作品集",
    page_icon="📊",
    layout="centered",
)

st.title("專案作品集")
st.markdown(
    """
    歡迎來到我的資料分析作品集。從下方選擇專案，前往閱讀完整文件或瀏覽分析成果。
    """
)

credit_card, olist = st.columns(2, gap="medium")

with credit_card:
    with st.container(border=True):
        st.subheader("信用卡消費分析")
        st.write("探索信用卡消費資料、分析方法與專案成果。")
        st.link_button(
            "前往信用卡分析文件",
            "https://little-guang.github.io/credit_card/docs/index.html",
            use_container_width=True,
        )

with olist:
    with st.container(border=True):
        st.subheader("Olist 電商分析")
        st.write("瀏覽 Olist 電商資料分析專案與相關成果。")
        st.link_button(
            "前往 Olist 專案",
            "https://little-guang.github.io/olist_proj/",
            use_container_width=True,
        )
