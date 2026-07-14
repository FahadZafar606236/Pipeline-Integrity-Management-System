import streamlit as st

def load_css():
    with open("assets/styles.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css()

st.title("📄 Reports")
st.write("Generate engineering reports.")


from src.charts import health_trend_chart

st.subheader("Pipeline Health Score Trend")

st.plotly_chart(
    health_trend_chart(),
    use_container_width=True
)