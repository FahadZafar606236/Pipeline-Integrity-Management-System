import streamlit as st

# ==========================================
# Page Configuration
# ==========================================

st.title("ℹ️ About PIMS PRO")
st.subheader("Pipeline Integrity Management System")

st.divider()

# ==========================================
# Project Objective
# ==========================================

st.markdown("## 🎯 Project Objective")

st.write("""
PIMS PRO (Pipeline Integrity Management System) is a mechanical engineering
application developed to assist engineers in monitoring pipeline integrity,
evaluating corrosion, estimating remaining service life, and supporting
maintenance decision-making through data-driven analysis.

The system aims to improve pipeline reliability, safety, and operational
efficiency by providing a professional dashboard for inspection management
and engineering assessment.
""")

st.divider()

# ==========================================
# Engineering Standards
# ==========================================

st.markdown("## 📚 Engineering Standards Used")

st.markdown("""
- **ASME B31.3** – Process Piping
- **API 570** – Piping Inspection Code
""")

st.divider()

# ==========================================
# Technologies
# ==========================================

st.markdown("## 💻 Technologies Used")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
- Python
- Streamlit
- Pandas
- NumPy
""")

with col2:
    st.markdown("""
- Plotly
- Matplotlib
- Git
- VS Code
""")

st.divider()

# ==========================================
# Version
# ==========================================

st.markdown("## 🚀 Version")

st.info("PIMS PRO Version 1.0")

st.divider()

# ==========================================
# Developer
# ==========================================

st.markdown("## 👨‍💻 Developer")

st.success("""
**Muhammad Fahad Zafar**

Mechanical Engineering Student

Pakistan Institute of Engineering and Applied Sciences (PIEAS)

Portfolio Project – Pipeline Integrity Management System
""")


st.divider()

st.markdown("## ⭐ Key Features")

st.markdown("""
- Corrosion assessment
- Pipeline health scoring
- Remaining life estimation
- Risk classification
- Inspection history management
- Engineering recommendations
- Interactive analytics dashboard
- Report generation
""")
















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