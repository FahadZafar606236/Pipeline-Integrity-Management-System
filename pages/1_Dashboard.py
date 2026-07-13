import streamlit as st
import pandas as pd
from src.gauges import (
    health_gauge,
    thickness_gauge,
    corrosion_gauge,
    remaining_life_gauge,
    safety_factor_gauge,
)
from src.risk import risk_matrix_chart
from datetime import datetime

st.set_page_config(
    page_title="Dashboard | PIMS PRO",
    page_icon="🛢️",
    layout="wide",
    initial_sidebar_state="expanded"
)



col_logo, col_title, col_info = st.columns([1.2, 5, 1.8])

with col_logo:
    st.image("assets/logo/pims_logo.png", width=130)

with col_title:
    st.title("Pipeline Integrity Management System")
    st.markdown("### PIMS PRO")
    st.caption(
        "Professional software for corrosion assessment, "
        "remaining life prediction, risk classification, "
        "inspection management, and maintenance recommendations."
    )

with col_info:
    st.markdown("### Version")
    st.write("**v1.0**")

    st.markdown("### Date")
    st.write(datetime.now().strftime("%d %B %Y"))

st.divider()


# ==========================================
# KPI Cards (Placeholder Data)
# ==========================================

st.markdown("## 📊 Pipeline Performance Overview")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        label="🛢️ Total Pipelines",
        value="24"
    )

with col2:
    st.metric(
        label="📋 Total Inspections",
        value="156"
    )

with col3:
    st.metric(
        label="🟢 Safe Pipelines",
        value="18"
    )

col4, col5, col6 = st.columns(3)

with col4:
    st.metric(
        label="🟡 Warning Pipelines",
        value="4"
    )

with col5:
    st.metric(
        label="🔴 Critical Pipelines",
        value="2"
    )

with col6:
    st.metric(
        label="📈 Average Health Score",
        value="91%"
    )


st.divider()





      



# ==========================================
# Engineering Gauges
# ==========================================

st.markdown("## ⚙️ Engineering Gauges")

col1, col2 = st.columns(2)

with col1:
    fig = health_gauge(92)
    st.plotly_chart(fig, use_container_width=True)

with col2:
    fig = thickness_gauge(
        current_thickness=8.2,
        minimum_thickness=6.5
    )

    st.plotly_chart(fig, use_container_width=True)

col3, col4 = st.columns(2)

with col3:
    fig = corrosion_gauge(0.22)

    st.plotly_chart(fig, use_container_width=True)

with col4:
    fig = remaining_life_gauge(18.2)

    st.plotly_chart(fig, use_container_width=True)



st.divider()

st.markdown("## 🛡️ Engineering Safety Assessment")

fig = safety_factor_gauge(2.15)

st.plotly_chart(fig, use_container_width=True)
st.divider()

# ==========================================
# Pipeline Integrity Summary
# ==========================================

st.markdown("## 📋 Pipeline Integrity Summary")

col1, col2 = st.columns(2)

with col1:
    st.success(
        """
### 🟢 Overall Pipeline Status

## SAFE

Pipeline integrity is within acceptable engineering limits.
"""
    )

with col2:
    st.info(
        """
### 💡 Engineering Decision

**Continue Normal Operation**

📅 Recommended Next Inspection

24 Months
"""
    )  



st.divider()


# ==========================================
# Pipeline Risk Assessment
# ==========================================

st.markdown("## 🚨 Pipeline Risk Assessment")

with st.container():

    if "Likelihood" in st.session_state and "Consequence" in st.session_state:

        likelihood = st.session_state["Likelihood"]
        consequence = st.session_state["Consequence"]

        fig = risk_matrix_chart(likelihood, consequence)
        st.plotly_chart(fig, use_container_width=True)

    else:
        st.info("Run a pipeline inspection first to display the Risk Matrix.")


st.divider()

st.markdown("### 📋 Risk Summary")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Likelihood", st.session_state["Likelihood"])

with col2:
    st.metric("Consequence", st.session_state["Consequence"])

with col3:
    st.metric("Risk Score", st.session_state["Risk Score"])

with col4:
    st.metric("Category", st.session_state["Risk Category"])

category = st.session_state["Risk Category"]

if category == "Low":
    st.success("🟢 LOW")

elif category == "Medium":
    st.warning("🟡 MEDIUM")

elif category == "High":
    st.warning("🟠 HIGH")

elif category == "Extreme":
    st.error("🔴 EXTREME")    

st.divider()
# ==========================================
# Corrosion Trend (Placeholder)
# ==========================================

st.markdown("## 📈 Pipeline Corrosion Trend")

with st.container():
    st.write("")
    st.info("Corrosion Trend Chart Placeholder")
    st.write("")
    st.write("This section will display the pipeline thickness trend over time.")
    st.write("")
    
st.divider()

# ==========================================
# Recent Inspection History (Placeholder)
# ==========================================



st.markdown("## 📋 Recent Inspection History")

placeholder_df = pd.DataFrame({
    "Pipeline ID": ["PL-001", "PL-002", "PL-003"],
    "Inspection Date": ["08-Jul-2026", "01-Jul-2026", "25-Jun-2026"],
    "Health Score": ["92%", "88%", "95%"],
    "Risk Level": ["Moderate", "Low", "Low"]
})

st.dataframe(
    placeholder_df,
    use_container_width=True,
    hide_index=True
)

st.divider()


# ==========================================
# System Status
# ==========================================

st.markdown("## 🟢 System Status")

col1, col2, col3 = st.columns(3)

with col1:
    st.success("System Ready")

with col2:
    st.success("Database Connected")

with col3:
    st.success("Inspection Module Available")

st.divider()

st.divider()

col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    st.markdown(
        """
        <div style="text-align:center;">
            <h4 style="margin-bottom:5px;">🛢️ PIMS PRO</h4>
            <p style="margin:0;">
                Developed by <b>Muhammad Fahad Zafar</b>
            </p>
            <p style="margin:0;">
                Mechanical Engineering Student
            </p>
            <p style="margin:0;">
                Pakistan Institute of Engineering and Applied Sciences (PIEAS)
            </p>
            <br>
            <p style="font-size:13px;color:gray;">
                Version 1.0 | © 2026
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )