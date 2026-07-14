import streamlit as st
from pathlib import Path
from streamlit_lottie import st_lottie
import requests
import json
# ==========================
# Page Configuration
# ==========================
st.set_page_config(
    page_title="PIMS PRO | Pipeline Integrity Management System",
    page_icon="🛢️",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ==========================
# Load CSS
# ==========================
def load_css():
    with open("assets/styles.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css()

def load_lottie(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        return json.load(f)


hero = st.container(border=True)

with hero:
    col1, col2 = st.columns([1, 8])

    with col1:
        st.markdown(
            "<h1 style='text-align:center;'>🛢️</h1>",
            unsafe_allow_html=True
        )

    with col2:
        st.title("PIMS PRO")
        st.subheader("Pipeline Integrity Management System")

        st.write(
            """
            A professional engineering platform for pipeline integrity
            management, corrosion assessment, remaining life prediction,
            inspection planning, risk analysis, and asset monitoring
            according to **API 570** and **ASME B31.3**.
            """
        )

        st.caption("Version 1.0")


st.markdown("## 🚀 Quick Actions")

col1, col2 = st.columns(2)

with col1:
    if st.button("📊 Open Dashboard", use_container_width=True):
        st.switch_page("pages/1_Dashboard.py")

with col2:
    if st.button("➕ New Inspection", use_container_width=True):
        st.switch_page("pages/2_New_Inspection.py")


left, right = st.columns([2,1])

with left:
    st.title("PIMS PRO")
    st.subheader("Pipeline Integrity Management System")

    st.write("""
    Professional engineering platform for pipeline integrity,
    corrosion assessment, remaining life prediction,
    inspection management and risk analysis.
    """)

    st.success("Version 1.0")

with right:

   lottie = load_lottie("assets/oil refinery animation.json")

st_lottie(
    lottie,
    height=350,
    key="oil_refinery"
)

st.divider()
st.markdown("## 🚀 Core Features")

row1 = st.columns(3)
row2 = st.columns(3)

features = [
    ("🛢", "Pipeline Monitoring",
     "Monitor pipeline condition, thickness and operational status."),

    ("📉", "Corrosion Assessment",
     "Calculate corrosion rate, remaining life and metal loss."),

    ("📊", "Analytics",
     "Interactive charts, KPIs and engineering insights."),

    ("⚠️", "Risk Analysis",
     "Evaluate pipeline risk and prioritize maintenance."),

    ("📄", "PDF Reports",
     "Generate professional inspection and assessment reports."),

    ("🕒", "Inspection History",
     "View and manage previous inspection records.")
]

for col, feature in zip(row1 + row2, features):
    icon, title, desc = feature

    with col:
        st.markdown(f"""
        <div class="feature-card">
            <div class="feature-icon">{icon}</div>
            <div class="feature-title">{title}</div>
            <div class="feature-desc">{desc}</div>
        </div>
        """, unsafe_allow_html=True)


st.divider()

st.markdown("## 🔄 Engineering Workflow")

steps = [
    "🔍 Inspection",
    "📉 Corrosion\nCalculation",
    "⚠️ Risk\nAssessment",
    "⏳ Remaining\nLife",
    "📊 Dashboard",
    "📄 Report"
]

cols = st.columns(len(steps))

for i, col in enumerate(cols):
    with col:
        st.markdown(
            f"""
            <div class="workflow-card">
                <div class="workflow-icon">{steps[i].split()[0]}</div>
                <div class="workflow-title">
                    {" ".join(steps[i].split()[1:])}
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

        if i != len(steps) - 1:
            st.markdown(
                "<h2 style='text-align:center;color:#00B4D8;'>↓</h2>",
                unsafe_allow_html=True,
            )


st.divider()

st.markdown("## 🛠 Technology Stack")

techs = [
    ("🐍", "Python"),
    ("🚀", "Streamlit"),
    ("🐼", "Pandas"),
    ("📊", "Plotly"),
    ("📄", "ReportLab"),
    ("📘", "API 570"),
    ("📐", "ASME B31.3"),
]

cols = st.columns(4)

for i, (icon, name) in enumerate(techs):
    with cols[i % 4]:
        st.markdown(f"""
        <div class="tech-card">
            <div class="tech-icon">{icon}</div>
            <div class="tech-name">{name}</div>
        </div>
        """, unsafe_allow_html=True)


st.divider()

st.markdown("## 🛢️ PIMS PRO")

st.caption("Pipeline Integrity Management System")

st.write(
    """
    Professional engineering software for pipeline integrity,
    corrosion assessment, remaining life prediction,
    inspection management, and risk analysis.
    """
)

col1, col2, col3 = st.columns(3)

with col1:
    st.info("📌 Version 1.0")

with col2:
    st.info("👨‍💻 M. Fahad Zafar")

with col3:
    st.info("🎓 Mechanical Engineering | PIEAS")

st.caption("© 2026 PIMS PRO | All Rights Reserved.")