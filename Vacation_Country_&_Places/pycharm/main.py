import streamlit as st
import langchain_helper
st.title("Tour Place Guide")

continent=st.sidebar.selectbox("Pick a Continent",("Asia","Europe","North America","South America","Africa","Antarctica"))

if continent:
    response=langchain_helper.must_visit_place(continent)
    st.header(response['Country'].strip())
    Places=response['Places'].strip().split(",")
    st.write("**Places**")
    for place in Places:
        st.write("-",place)



