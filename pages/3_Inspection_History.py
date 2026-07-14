import streamlit as st

st.title("📋 Inspection History")
st.write("View previous inspections.")

df = pd.read_csv("data/inspection_history.csv")

st.dataframe(df, use_container_width=True)