import streamlit as st
from datetime import datetime

col_logo, col_title, col_info = st.columns([1, 5, 2])

with col_logo:
    st.image("assets/logo/pims_logo.png", width=90)

with col_title:
    st.title("PIMS PRO")
    st.subheader("Pipeline Integrity Management System")
    st.caption("Professional Corrosion Monitoring Dashboard")

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

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        label="🟢 Pipeline Health",
        value="92%",
        delta="Today"
    )

with col2:
    st.metric(
        label="⚠️ Risk Level",
        value="Moderate"
    )

with col3:
    st.metric(
        label="⏳ Remaining Life",
        value="18 Years"
    )

with col4:
    st.metric(
        label="🛢️ Corrosion Rate",
        value="0.18 mm/year"
    )

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
# Remaining Thickness Gauge & Risk Matrix
# ==========================================

col1, col2 = st.columns(2)

with col1:
    st.markdown("## 🛢️ Remaining Thickness Assessment")
    st.info("Gauge Placeholder")
    st.write("This section will display the remaining wall thickness gauge.")

with col2:
    st.markdown("## 🚨 Pipeline Risk Assessment")
    st.info("Risk Matrix Placeholder")
    st.write("This section will display the pipeline risk matrix.")

st.divider()

# ==========================================
# Engineering Recommendation (Placeholder)
# ==========================================

st.markdown("## 💡 Engineering Recommendation")

with st.container():
    st.success("""
**Recommendation Placeholder**

Engineering recommendations will appear here based on
pipeline health, corrosion rate, remaining life,
and risk assessment.

Examples:

• Continue normal operation

• Schedule next inspection

• Reduce operating pressure

• Repair damaged section

• Replace pipeline segment
""")

st.divider()

# ==========================================
# Recent Inspection History (Placeholder)
# ==========================================

import pandas as pd

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