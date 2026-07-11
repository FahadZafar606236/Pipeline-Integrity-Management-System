import streamlit as st

st.title("📄 Reports")
st.write("Generate engineering reports.")


from src.charts import health_trend_chart

st.subheader("Pipeline Health Score Trend")

st.plotly_chart(
    health_trend_chart(),
    use_container_width=True
)