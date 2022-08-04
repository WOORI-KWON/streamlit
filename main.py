import streamlit as st
view = [300, 200, 100, 500, 600, 700]
show_raw  = st.checkbox('show raw date')
if show_raw == True:
    st.write('# raw data')
    view
st.write('# table')
st.table(view)
st.write('# bar graph')
st.bar_chart(view)
