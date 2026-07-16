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

st.title("⚙️ Settings")
st.caption(
    "Configure application preferences, engineering standards, "
    "report options, and system settings."
)

st.divider()

st.sidebar.header("Settings Menu")

section = st.sidebar.radio(
    "Select Section",
    [
        "👤 User Preferences",
        "📋 Inspection Defaults",
        "🧮 Engineering Standards",
        "📄 Report Settings",
        "💾 Data Management",
        "🎨 Appearance",
        "ℹ️ System Information"
    ]
)

if section == "👤 User Preferences":

    st.subheader("👤 User Preferences")

    st.write(
        "Configure default user information that will appear "
        "in generated inspection reports."
    )

    st.divider()

    col1, col2 = st.columns(2)

    with col1:

        company = st.text_input(
            "Company Name",
            placeholder="ABC Pipeline Company"
        )

        department = st.text_input(
            "Department",
            placeholder="Integrity Management"
        )

    with col2:

        engineer = st.text_input(
            "Engineer Name",
            placeholder="Muhammad Fahad Zafar"
        )

        registration = st.text_input(
            "Registration Number",
            placeholder="PEC-XXXXX"
        )

    st.markdown("### Company Branding")

    logo = st.file_uploader(
        "Upload Company Logo",
        type=["png", "jpg", "jpeg"]
    )

    signature = st.file_uploader(
        "Upload Engineer Signature",
        type=["png", "jpg", "jpeg"]
    )

    st.divider()

    if st.button("💾 Save User Preferences", width="stretch"):

        st.session_state["company"] = company
        st.session_state["department"] = department
        st.session_state["engineer"] = engineer
        st.session_state["registration"] = registration

        st.success("✅ User preferences saved successfully.")
        



if section == "📋 Inspection Defaults":

    st.subheader("📋 Inspection Defaults")

    st.write(
        "Configure the default engineering values used when creating a new inspection."
    )

    st.divider()

    col1, col2 = st.columns(2)

    with col1:

        default_material = st.selectbox(
            "Default Material",
            [
                "Carbon Steel",
                "Stainless Steel",
                "Duplex Steel",
                "Alloy Steel",
                "PVC",
                "HDPE"
            ]
        )

    with col2:

        default_fluid = st.selectbox(
            "Default Fluid",
            [
                "Crude Oil",
                "Natural Gas",
                "Produced Water",
                "Steam",
                "Diesel",
                "Chemical"
            ]
        )

    st.markdown("### Default Engineering Parameters")

    col1, col2, col3 = st.columns(3)

    with col1:

        default_weld = st.number_input(
            "Weld Efficiency",
            value=1.0
        )

    with col2:

        default_temperature = st.number_input(
            "Temperature Coefficient",
            value=0.4
        )

    with col3:

        default_stress = st.number_input(
            "Allowable Stress (MPa)",
            value=138.0
        )

    st.divider()

    if st.button(
        "💾 Save Inspection Defaults",
        width="stretch"
    ):

        st.session_state["default_material"] = default_material
        st.session_state["default_fluid"] = default_fluid
        st.session_state["default_weld"] = default_weld
        st.session_state["default_temperature"] = default_temperature
        st.session_state["default_stress"] = default_stress

        st.success("✅ Inspection defaults saved successfully.")
        





if section == "🧮 Engineering Standards":

    st.subheader("🧮 Engineering Standards")

    st.write(
        "Select the engineering standards and calculation options used throughout the application."
    )

    st.divider()

    standard = st.selectbox(
        "Primary Engineering Standard",
        [
            "ASME B31.3",
            "ASME B31.4",
            "ASME B31.8",
            "API 570"
        ]
    )

    corrosion_standard = st.selectbox(
        "Corrosion Assessment Standard",
        [
            "API 570",
            "API 579",
            "ASME PCC-2"
        ]
    )

    st.markdown("### Engineering Parameters")

    col1, col2 = st.columns(2)

    with col1:

        design_factor = st.number_input(
            "Design Factor",
            min_value=0.1,
            max_value=1.0,
            value=0.72,
            step=0.01
        )

    with col2:

        corrosion_allowance = st.number_input(
            "Default Corrosion Allowance (mm)",
            min_value=0.0,
            value=3.0,
            step=0.5
        )

    st.markdown("### Units")

    col1, col2 = st.columns(2)

    with col1:

        pressure_unit = st.selectbox(
            "Pressure Unit",
            [
                "MPa",
                "bar",
                "psi"
            ]
        )

    with col2:

        length_unit = st.selectbox(
            "Length Unit",
            [
                "mm",
                "inch"
            ]
        )

    st.divider()

    if st.button(
        "💾 Save Engineering Standards",
        width="stretch"
    ):

        st.session_state["standard"] = standard
        st.session_state["corrosion_standard"] = corrosion_standard
        st.session_state["design_factor"] = design_factor
        st.session_state["default_corrosion_allowance"] = corrosion_allowance
        st.session_state["pressure_unit"] = pressure_unit
        st.session_state["length_unit"] = length_unit

        st.success("✅ Engineering standards saved successfully.")








if section == "📄 Report Settings":

    st.subheader("📄 Report Settings")

    st.write(
        "Configure the appearance and content of generated PDF reports."
    )

    st.divider()

    col1, col2 = st.columns(2)

    with col1:

        report_title = st.text_input(
            "Report Title",
            value="Pipeline Inspection Report"
        )

    with col2:

        report_author = st.text_input(
            "Author",
            value="Muhammad Fahad Zafar"
        )

    st.markdown("### Report Contents")

    include_logo = st.checkbox(
        "Include Company Logo",
        value=True
    )

    include_charts = st.checkbox(
        "Include Engineering Charts",
        value=True
    )

    include_gauges = st.checkbox(
        "Include Gauge Charts",
        value=True
    )

    include_risk = st.checkbox(
        "Include Risk Matrix",
        value=True
    )

    include_summary = st.checkbox(
        "Include Executive Summary",
        value=True
    )

    st.markdown("### PDF Layout")

    col1, col2 = st.columns(2)

    with col1:

        page_size = st.selectbox(
            "Page Size",
            [
                "A4",
                "Letter"
            ]
        )

    with col2:

        orientation = st.selectbox(
            "Orientation",
            [
                "Portrait",
                "Landscape"
            ]
        )

    report_prefix = st.text_input(
        "Report Number Prefix",
        value="PIMS"
    )

    auto_number = st.checkbox(
        "Enable Automatic Report Numbering",
        value=True
    )

    st.divider()

    if st.button(
        "💾 Save Report Settings",
        width="stretch"
    ):

        st.session_state["report_title"] = report_title
        st.session_state["report_author"] = report_author
        st.session_state["include_logo"] = include_logo
        st.session_state["include_charts"] = include_charts
        st.session_state["include_gauges"] = include_gauges
        st.session_state["include_risk"] = include_risk
        st.session_state["include_summary"] = include_summary
        st.session_state["page_size"] = page_size
        st.session_state["orientation"] = orientation
        st.session_state["report_prefix"] = report_prefix
        st.session_state["auto_number"] = auto_number

        st.success("✅ Report settings saved successfully.")
        
        
        





if section == "🎨 Appearance":

    st.subheader("🎨 Appearance")

    st.write(
        "Customize the appearance of the application."
    )

    st.divider()

    theme = st.selectbox(
        "Theme",
        [
            "Dark",
            "Light"
        ]
    )

    accent = st.selectbox(
        "Accent Color",
        [
            "Blue",
            "Green",
            "Orange",
            "Red",
            "Purple"
        ]
    )

    sidebar = st.checkbox(
        "Expand Sidebar by Default",
        value=True
    )

    animations = st.checkbox(
        "Enable Animations",
        value=True
    )

    compact = st.checkbox(
        "Compact Layout",
        value=False
    )

    tooltips = st.checkbox(
        "Show Tooltips",
        value=True
    )

    st.divider()

    if st.button(
        "💾 Save Appearance",
        width="stretch"
    ):

        st.session_state["theme"] = theme
        st.session_state["accent"] = accent
        st.session_state["sidebar"] = sidebar
        st.session_state["animations"] = animations
        st.session_state["compact"] = compact
        st.session_state["tooltips"] = tooltips

        st.success("✅ Appearance settings saved successfully.")
        
        









import os
import pandas as pd

if section == "💾 Data Management":

    st.subheader("💾 Data Management")

    st.write(
        "Manage inspection history, reports, backups and application data."
    )

    st.divider()

    # ==========================
    # Storage Statistics
    # ==========================

    history_file = "data/inspection_history.csv"
    reports_folder = "reports"

    total_inspections = 0
    total_reports = 0
    database_size = "0 KB"

    if os.path.exists(history_file):

        df = pd.read_csv(history_file)

        total_inspections = len(df)

        database_size = (
            f"{os.path.getsize(history_file)/1024:.1f} KB"
        )

    if os.path.exists(reports_folder):

        total_reports = len([
            file for file in os.listdir(reports_folder)
            if file.endswith(".pdf")
        ])

    col1, col2, col3 = st.columns(3)

    with col1:

        st.metric(
            "Saved Inspections",
            total_inspections
        )

    with col2:

        st.metric(
            "Generated Reports",
            total_reports
        )

    with col3:

        st.metric(
            "Database Size",
            database_size
        )

    st.divider()

    # ==========================
    # Storage Locations
    # ==========================

    st.markdown("### 📂 Storage Locations")

    st.code("data/inspection_history.csv")

    st.code("reports/")

    st.code("assets/charts/")

    st.divider()

    # ==========================
    # Export Database
    # ==========================

    st.markdown("### 📤 Export Inspection History")

    if os.path.exists(history_file):

        with open(history_file, "rb") as file:

            st.download_button(
                "⬇ Download Inspection History",
                data=file,
                file_name="inspection_history.csv",
                mime="text/csv",
                width="stretch"
            )

    else:

        st.info("No inspection history found.")

    st.divider()

    # ==========================
    # Backup Information
    # ==========================

    st.markdown("### 💾 Backup")

    st.info(
        """
It is recommended to back up your inspection history
before clearing or modifying application data.
"""
    )

    st.divider()

    # ==========================
    # Maintenance
    # ==========================

    st.markdown("### 🛠 Maintenance")

    col1, col2 = st.columns(2)

    with col1:

        if st.button(
            "🗑 Clear Inspection History",
            width="stretch"
        ):

            if os.path.exists(history_file):

                pd.DataFrame().to_csv(
                    history_file,
                    index=False
                )

                st.success(
                    "Inspection history cleared successfully."
                )

            else:

                st.warning("History file not found.")

    with col2:

        if st.button(
            "🧹 Clear Generated Charts",
            width="stretch"
        ):

            chart_folder = "assets/charts"

            if os.path.exists(chart_folder):

                removed = 0

                for file in os.listdir(chart_folder):

                    if file.endswith(".png"):

                        os.remove(
                            os.path.join(chart_folder, file)
                        )

                        removed += 1

                st.success(
                    f"{removed} chart images removed successfully."
                )

            else:

                st.warning("Chart folder not found.")

    st.divider()

    # ==========================
    # Reset Settings
    # ==========================

    st.markdown("### ⚙ Application")

    if st.button(
        "🔄 Reset Session Settings",
        width="stretch"
    ):

        st.session_state.clear()

        st.success(
            "Application settings have been reset."
        )

    st.divider()

    st.caption(
        "PIMS PRO automatically stores all inspections "
        "inside the local CSV database."
    )
    
    
    
    
    
    
    
if section == "ℹ️ System Information":

    st.subheader("ℹ️ System Information")

    st.write(
        "View application information and current system status."
    )

    st.divider()

    col1, col2 = st.columns(2)

    with col1:

        st.metric(
            "Application",
            "PIMS PRO"
        )

        st.metric(
            "Version",
            "1.0"
        )

        st.metric(
            "Developer",
            "Muhammad Fahad Zafar"
        )

        st.metric(
            "Framework",
            "Streamlit"
        )

    with col2:

        st.metric(
            "Python",
            "3.x"
        )

        st.metric(
            "Engineering Standard",
            "ASME B31.3"
        )

        st.metric(
            "Inspection Standard",
            "API 570"
        )

        st.metric(
            "Database",
            "CSV Storage"
        )

    st.divider()

    st.markdown("### Installed Features")

    st.success("✔ Pipeline Corrosion Assessment")

    st.success("✔ Remaining Life Prediction")

    st.success("✔ Health Score Calculation")

    st.success("✔ Risk Assessment")

    st.success("✔ PDF Report Generation")

    st.success("✔ Engineering Charts")

    st.success("✔ Gauge Charts")

    st.success("✔ Inspection History")

    st.success("✔ Analytics Dashboard")

    st.divider()

    st.markdown("### Storage")

    st.code("data/inspection_history.csv")

    st.code("reports/")

    st.code("assets/charts/")

    st.divider()

    st.info(
        """
PIMS PRO

Pipeline Integrity Management System

Developed for Mechanical Engineering
Final Year Project

Engineering Standards

• ASME B31.3
• API 570
"""
    )