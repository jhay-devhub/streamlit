import streamlit as st


st.set_page_config(page_title="My Personal Webpage", layout="wide")

#header section
with st.container():
    st.subheader("Hello, I am Jhay Lord Rivera :wave:")
    st.title("Bachelor of Science in Information Technology from Laguna University")
    st.write("I'm currently 2nd year student")

with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What I do")
        st.write(
            """
            - I'm studying python language
            """
        )
    with right_column:
        st.header("SOCIAL MEDIA ACCOUNTS")
        st.write("""
                - [FACEBOOK](https://www.facebook.com/profile.php?id=100092556163752)
                - [INSTRAGRAM](https://www.instagram.com/jhylrdrvr/?next=%2F)
                 """)

with st.container():
    st.write("---")
    st.header("My Python Activities")
    st.write("[GOOGLE COLAB >](https://colab.research.google.com/drive/1CHOIIWQ4xO_j2wJe37LaSkYfeAZr7hSm)")
