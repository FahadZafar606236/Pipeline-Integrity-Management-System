import streamlit as st
import pandas as pd
from src.pipeline_visualization import pipeline_visualization
from src.charts import corrosion_trend_chart
st.title("📈 Analytics")

history = pd.read_csv("data/inspection_history.csv")

history["Inspection Date"] = pd.to_datetime(
    history["Inspection Date"]
)





period = st.sidebar.selectbox(
    "Inspection Period",
    (
        "Last 6 Months",
        "Last Year",
        "Last 5 Years",
        "All Data"
    )
)


pipe = st.sidebar.selectbox(
    "Pipeline",
    ["All"] + list(history["Pipe ID"].unique())
)




today = pd.Timestamp.today()

if period == "Last 6 Months":
    filtered = history[
        history["Inspection Date"] >=
        today - pd.DateOffset(months=6)
    ]

elif period == "Last Year":
    filtered = history[
        history["Inspection Date"] >=
        today - pd.DateOffset(years=1)
    ]

elif period == "Last 5 Years":
    filtered = history[
        history["Inspection Date"] >=
        today - pd.DateOffset(years=5)
    ]

else:
    filtered = history

if pipe != "All":
    filtered = filtered[
        filtered["Pipe ID"] == pipe
    ]

filtered = filtered.rename(
    columns={
        "Pipe ID": "pipe_id",
        "Inspection Date": "inspection_date",
        "Current Thickness (mm)": "current_thickness",
        "Corrosion Rate (mm/year)": "corrosion_rate",
        "Remaining Life (years)": "remaining_life",
        "Health Score": "health_score",
        "Minimum Required Thickness (mm)": "minimum_required_thickness"
    }
)

filtered["inspection_date"] = pd.to_datetime(
    filtered["inspection_date"]
)

st.caption(f"Available inspections: {len(filtered)}")

if len(filtered) < 2:

    st.info(
        """
### 📊 Trend Analysis Unavailable

There is insufficient inspection history to generate engineering trends.

Minimum Requirement:
- ✔ At least 2 inspection records
- ✔ Same pipeline
- ✔ Within selected period

Please perform additional inspections to enable trend analysis.
"""
    )

    st.stop()

# ==========================
# Dashboard Summary
# ==========================

latest_inspection = filtered["inspection_date"].max()

avg_corrosion = filtered["Corrosion Rate"].mean()

max_corrosion = filtered["Corrosion Rate"].max()

min_remaining = filtered["Remaining Life"].min()

st.subheader("📊 Dashboard Summary")

col1, col2, col3, col4 = st.columns(4)

with col1:

    st.metric(
        "Latest Inspection",
        latest_inspection.strftime("%d-%b-%Y")
    )

with col2:

    st.metric(
        "Average Corrosion Rate",
        f"{avg_corrosion:.3f} mm/year"
    )

with col3:

    st.metric(
        "Highest Corrosion Rate",
        f"{max_corrosion:.3f} mm/year"
    )

with col4:

    st.metric(
        "Lowest Remaining Life",
        f"{min_remaining:.1f} Years"
    )

st.subheader("Pipeline Corrosion Rate Trend")


st.plotly_chart(
    corrosion_trend_chart(filtered),
    use_container_width=True
)

from src.charts import thickness_history_chart

st.subheader("Pipeline Wall Thickness History")

st.plotly_chart(
    thickness_history_chart(filtered),
    use_container_width=True
)

from src.charts import remaining_life_chart

st.subheader("Pipeline Remaining Service Life Trend")

st.plotly_chart(
    remaining_life_chart(filtered),
    use_container_width=True
)

from src.charts import health_trend_chart

st.subheader("Pipeline Health Score Trend")

st.plotly_chart(
    health_trend_chart(filtered),
    use_container_width=True
)


st.markdown("---")

st.subheader("🛢️ Interactive Pipeline Visualization")


if pipe != "All":

    pipeline_visualization(
        filtered,
        pipe
    )

else:

    st.info(
        "Please select a pipeline from the sidebar to view visualization."
    )