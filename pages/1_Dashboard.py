import streamlit as st

st.set_page_config(
    page_title="PIMS PRO",
    page_icon="🛢️",
    layout="wide"
)


def load_css():
    with open("assets/styles.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css()
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

if "Likelihood" not in st.session_state:
    st.session_state["Likelihood"] = 0

if "Consequence" not in st.session_state:
    st.session_state["Consequence"] = 0

if "Risk Score" not in st.session_state:
    st.session_state["Risk Score"] = 0

if "Risk Category" not in st.session_state:
    st.session_state["Risk Category"] = "Not Calculated"



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

import os

filename = "data/inspection_history.csv"

if os.path.exists(filename):
    history_df = pd.read_csv(filename)
else:
    history_df = pd.DataFrame()

if not history_df.empty:

    total_pipelines = history_df["Pipe ID"].nunique()

    total_inspections = len(history_df)

    average_health = history_df["Health Score"].mean()

    safe_pipelines = len(
        history_df[history_df["Health Score"] >= 90]
    )

    warning_pipelines = len(
        history_df[
            (history_df["Health Score"] >= 70) &
            (history_df["Health Score"] < 90)
        ]
    )

    critical_pipelines = len(
        history_df[history_df["Health Score"] < 70]
    )

else:

    total_pipelines = 0
    total_inspections = 0
    average_health = 0
    safe_pipelines = 0
    warning_pipelines = 0
    critical_pipelines = 0    
# ==========================================
# KPI Cards (Placeholder Data)
# ==========================================

st.markdown("## 📊 Pipeline Performance Overview")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        label="🛢️ Total Pipelines",
        value=total_pipelines
    )

with col2:
    st.metric(
        label="📋 Total Inspections",
        value=total_inspections
    )

with col3:
    st.metric(
        label="🟢 Safe Pipelines",
        value=safe_pipelines
    )

col4, col5, col6 = st.columns(3)

with col4:
    st.metric(
        label="🟡 Warning Pipelines",
        value=warning_pipelines
    )

with col5:
    st.metric(
        label="🔴 Critical Pipelines",
        value=critical_pipelines
    )

with col6:
    st.metric(
        label="📈 Average Health Score",
        value=f"{average_health:.1f}%"
    )


st.divider()





      


# Latest inspection
if not history_df.empty:
   history_df["Inspection Date"] = pd.to_datetime(history_df["Inspection Date"])
   latest = history_df.sort_values("Inspection Date").iloc[-1]
# ==========================================
# Engineering Gauges
# ==========================================

st.markdown("## ⚙️ Engineering Gauges")

col1, col2 = st.columns(2)

with col1:
    fig = health_gauge(latest["Health Score"])
    st.plotly_chart(fig, use_container_width=True)

with col2:
    fig = thickness_gauge(
        current_thickness=latest["Current Thickness (mm)"],
        minimum_thickness=latest["Minimum Required Thickness"]
    )

    st.plotly_chart(fig, use_container_width=True)

col3, col4 = st.columns(2)

with col3:
    fig = corrosion_gauge(
        latest["Corrosion Rate"]
    )

    st.plotly_chart(fig, use_container_width=True)

with col4:
    fig = remaining_life_gauge(
        latest["Remaining Life"]
    )

    st.plotly_chart(fig, use_container_width=True)



st.divider()

st.markdown("## 🛡️ Engineering Safety Assessment")

fig = safety_factor_gauge(
    latest["Safety Factor"]
)
st.plotly_chart(fig, use_container_width=True)
st.divider()

# ==========================================
# Pipeline Integrity Summary
# ==========================================

st.markdown("## 📋 Pipeline Integrity Summary")

col1, col2 = st.columns(2)

with col1:
    priority = latest["Priority"]

    if priority == "LOW":

        st.success("""
### 🟢 Overall Pipeline Status

## SAFE

Pipeline integrity is within acceptable engineering limits.
""")

    elif priority == "MEDIUM":

        st.warning("""
### 🟡 Overall Pipeline Status

## WARNING

Pipeline requires increased monitoring.
""")

    elif priority == "HIGH":

        st.warning("""
### 🟠 Overall Pipeline Status

## HIGH RISK

Maintenance should be scheduled.
""")

    else:

        st.error("""
### 🔴 Overall Pipeline Status

## CRITICAL

Immediate engineering action is required.
""")

with col2:
    st.info(f"""
### 💡 Engineering Decision

**{latest["Recommendation"]}**

📅 Recommended Next Inspection

{latest["Next Inspection"]}
""")



st.divider()


# ==========================================
# Pipeline Risk Assessment
# ==========================================

st.markdown("## 🚨 Pipeline Risk Assessment")

if not history_df.empty:

    fig = risk_matrix_chart(
        latest["Likelihood"],
        latest["Consequence"]
    )

    st.plotly_chart(fig, use_container_width=True)

else:
    st.info("Run a pipeline inspection first.")

st.divider()

st.markdown("### 📋 Risk Summary")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Likelihood", latest["Likelihood"])

with col2:
    st.metric("Consequence", latest["Consequence"])

with col3:
    st.metric("Risk Score", latest["Risk Score"])

with col4:
    st.metric("Category", latest["Risk Category"])

category = latest["Risk Category"]

if category == "Low":
    st.success("🟢 LOW")

elif category == "Medium":
    st.warning("🟡 MEDIUM")

elif category == "High":
    st.warning("🟠 HIGH")

elif category == "Extreme":
    st.error("🔴 EXTREME")    

st.divider()

import os

st.markdown("## 📋 Recent Inspection History")

filename = "data/inspection_history.csv"

if os.path.exists(filename):

    history_df = pd.read_csv(filename)

    # Show newest inspections first
    history_df = history_df.iloc[::-1]

    # Show only latest 5 inspections
    history_df = history_df.head(5)

    display_df = history_df[
        [
            "Pipe ID",
            "Inspection Date",
            "Health Score",
            "Risk Category"
        ]
    ]

    st.dataframe(
        display_df,
        use_container_width=True,
        hide_index=True
    )

else:

    st.info("No inspections have been saved yet.")

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

