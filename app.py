import streamlit as st

st.title("TDS Week 8 Graded Assignment")

n1 = st.number_input('Insert first number', value=0)
n2 = st.number_input('Insert second number', value=0)
n3 = st.number_input('Insert third number', value=0)

st.write("The largest number is: ", max([n1,n2,n3]))
