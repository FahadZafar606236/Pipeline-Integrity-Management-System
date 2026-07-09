import streamlit as st
import pandas as pd
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



st.markdown("## 👋 Welcome to PIMS PRO")

st.info(
    """
PIMS PRO is a professional Pipeline Integrity Management System developed to support
inspection engineers, maintenance teams, and asset integrity professionals in monitoring
pipeline condition and making informed engineering decisions.

The application assists with corrosion assessment, remaining life prediction, risk
classification, inspection management, and maintenance planning to improve safety,
reliability, and operational efficiency.
"""
)

st.divider()

st.markdown("## 📖 Project Overview")

st.write(
    """
PIMS PRO is an engineering application that supports pipeline integrity management by
monitoring pipeline health, performing corrosion calculations, estimating remaining service
life, managing inspection records, analyzing operational risk, and generating engineering
reports. The system provides actionable insights to help engineers improve asset reliability,
enhance safety, and support informed maintenance decisions.
"""
)

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

# ==========================================
# Key Features
# ==========================================

st.markdown("## 🚀 Key Features")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.info("🛢️ Corrosion Loss\n\nCalculation")

with col2:
    st.info("⏳ Remaining Life\n\nPrediction")

with col3:
    st.info("💚 Health Score\n\nEvaluation")

with col4:
    st.info("⚠️ Risk\n\nClassification")

col5, col6, col7, col8 = st.columns(4)

with col5:
    st.info("📋 Inspection\n\nHistory")

with col6:
    st.info("📊 Analytics\n\nDashboard")

with col7:
    st.info("📄 PDF Report\n\nGeneration")

with col8:
    st.info("💾 Data\n\nExport")

col9 = st.columns(1)[0]

with col9:
    st.success("💡 Engineering Recommendation System")

st.divider()

# ==========================================
# Getting Started
# ==========================================

st.markdown("## 🚀 Getting Started")

col1, col2 = st.columns(2)

with col1:
    st.info("""
### Step 1
📝 Open **New Inspection**

### Step 2
🛢️ Enter pipeline details

### Step 3
🧮 Calculate corrosion assessment

### Step 4
💾 Save the inspection
""")

with col2:
    st.info("""
### Step 5
📋 Review inspection history

### Step 6
📈 Analyze pipeline trends

### Step 7
📄 Generate engineering reports

### Step 8
💡 Review maintenance recommendations
""")

st.success(
    "💡 Tip: Complete inspections regularly to maintain accurate "
    "pipeline health records and improve maintenance planning."
)

st.divider()

# ==========================================
# Engineering Standards
# ==========================================

st.markdown("## 📚 Engineering Standards")

col1, col2 = st.columns([1, 2])

with col1:
    st.info(
        """
### Standards

• ASME B31.3

• API 570
"""
    )

with col2:
    st.success(
        """
Engineering calculations and integrity assessment concepts used in
PIMS PRO are inspired by widely recognized industry practices.

This project is developed for educational and demonstration purposes
and should not be considered a certified engineering design or
inspection tool.
"""
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