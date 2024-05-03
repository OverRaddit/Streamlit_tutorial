import streamlit as st


st.set_page_config(
  page_title="Streamlit Tutorial",
  page_icon="🚀",
)
st.title("title2")


# 기본적으로 위젯 사용하기.
# st.title("Hello, Streamlit!")
# st.subheader("Welcome to Streamlit!!")
# st.markdown("""
#   # asdfasdf
#   This is a simple Streamlit app that displays a title, subheader, and a markdown message.
#         """)

# 사이드 바 사용하기.
# with st.sidebar:
#   # 외부에서 st.sidebar.title을 쓴것과 같은 효과.
#   st.title("Navigation")
#   st.text_input("xx")

# 멀티페이지 사용하기.
# tab_one, tab_two, tab_three = st.tabs(["A","B","C"])
# with tab_one:
#   st.write("This is the first tab")

# with tab_two:
#   st.write("This is the second tab")

# with tab_three:
#   st.write("This is the third tab")
