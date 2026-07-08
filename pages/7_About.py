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