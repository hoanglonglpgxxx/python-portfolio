import streamlit as st
import pandas

st.set_page_config(page_title='Mits123', page_icon='images/1.png', layout='wide', initial_sidebar_state='auto')

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

col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])
df = pandas.read_csv('data.csv', sep=';')

with col3:
    for index, row in df[:10].iterrows():
        st.header(row['title'])
        st.info(row['description'])
        st.image('images/'+row['image'], width=200)
        st.write(f'[Source code](https://{row["url"]})')

with col4:
    for index, row in df[10:].iterrows():
        st.header(row['title'])
        st.info(row['description'])
        st.image('images/'+row['image'], width=200)
        st.write(f'[Source code](https://{row["url"]})')
