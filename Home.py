import streamlit as st
from pathlib import Path

# Page Configuration (must be the first Streamlit command)
st.set_page_config(
    page_title="PIMS PRO | Pipeline Integrity Management System",
    page_icon="🛢️",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Load Global CSS
def load_css():
    css_file = Path("assets/styles.css")
    if css_file.exists():
        with open(css_file) as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    else:
        st.warning("styles.css not found!")

load_css()









st.title("PIMS PRO Dashboard")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Health Score", "94%")

with col2:
    st.metric("Risk Level", "Low")

with col3:
    st.metric("Remaining Life", "12.6 Years")

st.button("Run Corrosion Analysis")

st.text_input("Pipeline ID")

st.dataframe({
    "Pipeline": ["PL-001", "PL-002"],
    "Risk": ["Low", "High"]
})