import streamlit as st

st.set_page_config(page_title='Mits123', page_icon=':shark:', layout='wide', initial_sidebar_state='auto')

col1, col2 = st.columns(2)

with  col1:
    st.image('images/photo.png', width=500)

with col2:
    st.title('Mits123')
    content = """"
    This is a simple web app that demonstrates how to use Streamlit to build a simple web app.
    and it is a simple web app that demonstrates how to use Streamlit to build a simple web app.
    """
    st.info(content)

st.write('Below you can find some of the apps I have built in Python. Feel free to contact!')