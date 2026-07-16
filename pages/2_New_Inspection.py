import streamlit as st

st.set_page_config(
    page_title="PIMS PRO",
    page_icon="🛢️",
    layout="wide"
)
from src.report_generator import generate_pdf_report

def load_css():
    with open("assets/styles.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css()
import pandas as pd
import os
CSV_COLUMNS = [
    "Pipe ID",
    "Material",
    "Fluid",
    "Outside Diameter (mm)",
    "Initial Thickness (mm)",
    "Current Thickness (mm)",
    "Operating Pressure (MPa)",
    "Allowable Stress (MPa)",
    "Inspection Date",
    "Inspector",
    "Corrosion Rate",
    "Minimum Required Thickness",
    "Remaining Life",
    "Corrosion Loss %",
    "Safety Factor",
    "Health Score",
    "Risk Level",
    "Likelihood",
    "Consequence",
    "Risk Score",
    "Risk Category",
    "Recommendation",
    "Priority",
    "Next Inspection",
    "Estimated Failure Year"
]
st.markdown("""
<style>

/* ===============================
   KPI Metric Cards - Dark Theme
================================ */

[data-testid="stMetric"]{
    background-color: #1E293B;
    border: 1px solid #334155;
    border-radius: 12px;
    padding: 16px;
    transition:
        border-color 0.20s ease,
        box-shadow 0.20s ease,
        transform 0.20s ease;
}

/* Hover Effect */

[data-testid="stMetric"]:hover{
    border-color: #3B82F6;
    box-shadow: 0 4px 12px rgba(59,130,246,0.20);
    transform: translateY(-2px);
}

/* Metric Label */

[data-testid="stMetricLabel"]{
    color: #CBD5E1 !important;
}

/* Metric Value */

[data-testid="stMetricValue"]{
    color: #F8FAFC !important;
}

/* Metric Delta */

[data-testid="stMetricDelta"]{
    color: inherit !important;
}

</style>
""", unsafe_allow_html=True)


from src.calculations import (
    corrosion_rate,
    minimum_required_thickness,
    remaining_life,
    next_inspection_date,
    corrosion_allowance,
    corrosion_loss_percentage,
    safety_factor,
    health_score,
    estimated_failure_year,
    risk_level,
)
from src.risk import pipeline_risk
st.title("📝 New Pipeline Inspection")

st.caption(
    "Enter pipeline inspection details to perform corrosion assessment and generate engineering recommendations."
)

st.divider()

with st.expander("📌 Section A – Pipeline Information", expanded=True):

    col1, col2, col3 = st.columns(3)

    with col1:
        pipe_id = st.text_input(
            "Pipe ID *",
            help="Unique identification number of the pipeline (e.g., PL-001)."
        )

    with col2:
        material = st.selectbox(
            "Material *",
            [
                "Carbon Steel",
                "Stainless Steel",
                "Duplex Steel",
                "Alloy Steel",
                "PVC",
                "HDPE"
            ],
            help="Select the pipeline construction material."
        )

    with col3:
        fluid = st.selectbox(
            "Fluid Type *",
            [
                "Crude Oil",
                "Natural Gas",
                "Produced Water",
                "Steam",
                "Diesel",
                "Chemical"
            ],
            help="Select the fluid currently transported through the pipeline."

        )

with st.expander("📏 Section B – Dimensions", expanded=True):

    col1, col2, col3 = st.columns(3)

    with col1:
        outside_diameter = st.number_input(
            "Outside Diameter (mm)",
            min_value=0.0,
            help="Enter the pipe outside diameter in millimetres. Typical range: 25–1500 mm."
        )

    with col2:
       initial_thickness = st.number_input(
            "Initial Thickness (mm)",
            min_value=0.0,
            help="Original wall thickness of the pipe when installed."
        )

    with col3:
        current_thickness = st.number_input(
            "Current Thickness (mm)",
            min_value=0.0,
            help="Measured wall thickness during the latest inspection."
        )

with st.expander("⚙ Section C – Operating Conditions", expanded=True):

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        operating_pressure = st.number_input(
            "Operating Pressure (MPa)",
            min_value=0.0,
            help="Normal pipeline operating pressure in megapascals (MPa)."
        )

    with col2:
       allowable_stress = st.number_input(
            "Allowable Stress (MPa)",
            min_value=0.0,
            help="Allowable material stress from ASME B31.3 design tables."
        )

    with col3:
        weld_efficiency = st.number_input(
            "Weld Joint Efficiency",
            value=1.0,
            help="Efficiency factor of the welded joint. Typical values: 0.7–1.0."
        )

    with col4:
        temperature_coefficient = st.number_input(
            "Temperature Coefficient (Y)",
            value=0.4,
            help="ASME B31.3 temperature coefficient used in thickness calculations."
        )

from datetime import date, datetime

with st.expander("📅 Section D – Inspection Information", expanded=True):

    col1, col2, col3 = st.columns(3)

    with col1:
       inspection_date = st.date_input(
            "Inspection Date",
            value=date.today(),
            help="Date when the inspection measurements were recorded."
        )

    with col2:
       years_service = st.number_input(
            "Years in Service",
            min_value=0,
            help="Total number of years the pipeline has been in operation."
        )

    with col3:
       inspector = st.text_input(
            "Inspector Name",
            help="Name of the engineer or inspector performing this inspection."
        )

with st.expander("🚀 Section E – Future Features"):

    st.info("These features will be available in future versions.")

    st.file_uploader(
        "UT Reading Upload",
        disabled=True
    )

    st.file_uploader(
        "Excel Import",
        disabled=True
    )

    st.text_area(
        "Inspection Notes",
        disabled=True
    )

st.divider()

st.markdown("## 🎛 Form Controls")

col1, col2, col3, col4 = st.columns(4)

with col1:
    calculate = st.button(
        "🧮 Calculate",
        use_container_width=True
    )

with col2:
    st.button(
        "🔄 Clear Form",
        use_container_width=True
    )

with col3:
    save = st.button(
        "💾 Save Inspection",
        use_container_width=True
    )

with col4:
    generate_report = st.button(
        "📄 Generate Report",
        use_container_width=True
    )

# Placeholder for Save / Report messages
message_placeholder = st.empty()

if calculate:
    with st.spinner("Performing engineering calculations... Please wait."):
        errors = []

        if not pipe_id.strip():
            errors.append("Pipe ID is required.")

        if not inspector.strip():
            errors.append("Inspector Name is required.")

        if outside_diameter <= 0:
            errors.append("Outside Diameter must be greater than zero.")

        if initial_thickness <= 0:
            errors.append("Initial Thickness must be greater than zero.")

        if current_thickness <= 0:
            errors.append("Current Thickness must be greater than zero.")

        if operating_pressure <= 0:
            errors.append("Operating Pressure must be greater than zero.")

        if allowable_stress <= 0:
            errors.append("Allowable Stress must be greater than zero.")

        if years_service <= 0:
            errors.append("Years in Service must be greater than zero.")



        if errors:

            st.error("Please correct the following errors:")

            for error in errors:
                st.write(f"• {error}")

        else:
            try:
                # Calculate corrosion rate
                corrosion = corrosion_rate(
                    initial_thickness,
                    current_thickness,
                    years_service
                )

                # Calculate minimum required thickness
                min_thickness = minimum_required_thickness(
                    operating_pressure,
                    outside_diameter,
                    allowable_stress,
                    weld_efficiency,
                    temperature_coefficient
                )

                # Calculate remaining life
                life = remaining_life(
                    current_thickness,
                    min_thickness,
                    corrosion
                )

                # Calculate corrosion loss percentage
                loss_percentage = corrosion_loss_percentage(
                    initial_thickness,
                    current_thickness
                )

                # Calculate safety factor
                sf = safety_factor(
                    current_thickness,
                    min_thickness
                )

                # Calculate health score
                
                score = health_score(
                    life,
                    corrosion,
                    sf,
                    loss_percentage
                )

                risk = risk_level(score)

                risk_result = pipeline_risk(
                    corrosion_rate=corrosion,
                    fluid=fluid
                )
                # Calculate next inspection date
                next_date = next_inspection_date(
                    inspection_date,
                    life
                )

                # Calculate corrosion allowance
                allowance = corrosion_allowance(
                    initial_thickness,
                    min_thickness
                )

                # Calculate estimated failure year
                failure_year = estimated_failure_year(
                    inspection_date.year,
                    life
                )

                # Store pipeline information
                st.session_state["pipe_id"] = pipe_id
                st.session_state["material"] = material
                st.session_state["inspection_date"] = inspection_date.strftime("%d %B %Y")
                st.session_state["inspector"] = inspector
                st.session_state["calculation_date"] = datetime.now().strftime("%d %B %Y")
                st.session_state["calculation_time"] = datetime.now().strftime("%H:%M")


               


                # Store engineering results
                st.session_state["corrosion_rate"] = corrosion
                st.session_state["minimum_required_thickness"] = min_thickness
                st.session_state["remaining_life"] = life
                st.session_state["corrosion_loss"] = loss_percentage
                st.session_state["safety_factor"] = sf
                st.session_state["health_score"] = score
                st.session_state["next_inspection_date"] = next_date
                st.session_state["corrosion_allowance"] = allowance
                st.session_state["estimated_failure_year"] = failure_year
                st.session_state["risk_level"] = risk
                st.session_state["Likelihood"] = risk_result["Likelihood"]
                st.session_state["Consequence"] = risk_result["Consequence"]
                st.session_state["Risk Score"] = risk_result["Risk Score"]
                st.session_state["Risk Category"] = risk_result["Risk Category"]
                st.session_state["Risk Recommendation"] = risk_result["Recommendation"]

                

            except Exception as e:
                 st.error(f"❌ {e}")

                
if st.session_state.get("health_score") is not None:
    st.divider()

    st.markdown("## 📊 Engineering Results")
    col1, col2 = st.columns(2)

    with col1:
        st.write(f"**🛢️ Pipe ID:** {st.session_state['pipe_id']}")
        st.write(f"**🔩 Material:** {st.session_state.get('material', '-')}")
        st.write(f"**📅 Inspection Date:** {st.session_state.get('inspection_date', '-')}")

    with col2:
        st.write(f"**👷 Inspector:** {st.session_state.get('inspector', '-')}")
        st.write(f"**📆 Calculation Date:** {st.session_state.get('calculation_date', '-')}")
        st.write(f"**🕒 Calculation Time:** {st.session_state.get('calculation_time', '-')}")

    st.success("✅ Engineering calculations completed successfully.")



   




    st.caption(
    "Calculated according to ASME B31.3 and API 570 engineering methodology."
    )

    col1, col2, col3 ,col4= st.columns(4)

    with col1:
        corrosion = st.session_state["corrosion_rate"]

        if corrosion <= 0.10:
            arrow = "🟢 ↓"
            status = "Low"

        elif corrosion <= 0.50:
            arrow = "🟡 →"
            status = "Medium"

        else:
            arrow = "🔴 ↑"
            status = "High"

        st.metric(
            "Corrosion Rate",
            f"{corrosion:.3f} mm/year",
            f"{arrow} {status}"
        )

    with col2:
        st.metric(
            "Remaining Life",
             f"{st.session_state['remaining_life']:.2f} Years"
        )

    with col3:
        st.metric(
            "Health Score",
            f"{st.session_state['health_score']:.1f}/100"
            
        )
        st.progress(st.session_state["health_score"] / 100)
    with col4:
        st.metric(
            "⚠ Risk Level",
            st.session_state["risk_level"]    
        )

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Minimum Required Thickness",
            f"{st.session_state['minimum_required_thickness']:.2f} mm"
        )

    with col2:
        st.metric(
            "Corrosion Loss",
            f"{st.session_state['corrosion_loss']:.2f}%"
        )

    with col3:
        st.metric(
            "Safety Factor",
            f"{st.session_state['safety_factor']:.2f}"
        )

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Corrosion Allowance",
            f"{st.session_state['corrosion_allowance']:.2f} mm"
        )

    with col2:
        st.metric(
            "Next Inspection",
            str(st.session_state["next_inspection_date"])
        )

    with col3:
        st.metric(
            "Estimated Failure Year",
            str(st.session_state["estimated_failure_year"])
            
        )

if st.session_state.get("health_score") is not None:
    st.markdown("## 💡 Engineering Recommendation")

    score = st.session_state["health_score"]
    risk = st.session_state["risk_level"]
    next_date = st.session_state["next_inspection_date"]
    life = st.session_state["remaining_life"]

    # Priority
    if score >= 90:
        priority = "LOW"
        priority_icon = "🟢"

    elif score >= 70:
        priority = "MEDIUM"
        priority_icon = "🟡"

    elif score >= 50:
        priority = "HIGH"
        priority_icon = "🟠"

    else:
        priority = "URGENT"
        priority_icon = "🔴"

    # Recommendation
    if score >= 90:

        recommendation = "Continue Normal Operation"

        condition = (
            "Pipeline condition is excellent. "
            "Corrosion is minimal and the asset remains fit for service."
        )

        action = (
            "Continue routine monitoring according to the existing inspection program."
        )

        icon = "🟢"

    elif score >= 70:

        recommendation = "Continue Monitoring"

        condition = (
            "Pipeline condition is satisfactory. "
            "Some corrosion has been detected but remains within acceptable engineering limits."
        )

        action = (
            "Continue operation and perform the next inspection according to API 570."
        )

        icon = "🟡"

    elif score >= 50:

        recommendation = "Schedule Maintenance"

        condition = (
            "Pipeline condition has deteriorated. "
            "Corrosion damage is becoming significant and requires planned maintenance."
        )

        action = (
            "Schedule inspection, repair, or preventive maintenance at the earliest opportunity "
            "to prevent further deterioration."
        )

        icon = "🟠"

    else:

        recommendation = "Immediate Shutdown / Repair Recommended"

        condition = (
            "Pipeline integrity is critically degraded. "
            "The remaining life is very limited and the risk of failure is high."
        )

        action = (
            "Immediately stop operation if required by engineering assessment. "
            "Perform detailed inspection and repair or replace the affected pipeline section "
            "before returning it to service."
        )

        icon = "🔴"

    # Save recommendation information
    st.session_state["recommendation"] = recommendation
    st.session_state["condition"] = condition
    st.session_state["recommended_action"] = action
    st.session_state["priority"] = priority
    st.session_state["priority_icon"] = priority_icon


    with st.container(border=True):

        st.markdown(f"### {priority_icon} Priority: **{priority}**")

        st.divider()

        st.markdown(f"### {icon} {recommendation}")

        st.markdown("#### Maintenance Priority")
        st.write(
            f"This inspection has been classified as **{priority}** priority "
            "based on the calculated health score."
        )

        st.markdown("#### ⚠ Risk Level")
        st.write(f"**{risk}**")

        st.markdown("#### Current Condition")
        st.write(condition)

        st.markdown("#### Recommended Action")
        st.write(action)

        st.markdown("#### Next Inspection")
        st.write(next_date)

        st.markdown("#### Remaining Life")
        st.write(f"{life:.2f} Years")

        st.caption(
            "Recommendation generated automatically using "
            "ASME B31.3 and API 570 engineering methodology."
        )

    st.divider()

if save:

    if st.session_state.get("health_score") is None:
        message_placeholder.error(
            "Please calculate the inspection before saving."
        )

    else:

        record = {
            "Pipe ID": st.session_state["pipe_id"],
            "Material": material,
            "Fluid": fluid,
            "Outside Diameter (mm)": outside_diameter,
            "Initial Thickness (mm)": initial_thickness,
            "Current Thickness (mm)": current_thickness,
            "Operating Pressure (MPa)": operating_pressure,
            "Allowable Stress (MPa)": allowable_stress,
            "Inspection Date": inspection_date,
            "Inspector": inspector,
            "Corrosion Rate": st.session_state["corrosion_rate"],
            "Minimum Required Thickness": st.session_state["minimum_required_thickness"],
            "Remaining Life": st.session_state["remaining_life"],
            "Corrosion Loss %": st.session_state["corrosion_loss"],
            "Safety Factor": st.session_state["safety_factor"],
            "Health Score": st.session_state["health_score"],
            "Risk Level": st.session_state["risk_level"],
            "Likelihood": st.session_state["Likelihood"],
            "Consequence": st.session_state["Consequence"],
            "Risk Score": st.session_state["Risk Score"],
            "Risk Category": st.session_state["Risk Category"],
            "Recommendation": st.session_state["recommendation"],
            "Priority": st.session_state["priority"],
            "Next Inspection": st.session_state["next_inspection_date"],
            "Estimated Failure Year": st.session_state["estimated_failure_year"],
        }
        # Save latest inspection in session
        st.session_state["saved_record"] = record
        
        df = pd.DataFrame([record], columns=CSV_COLUMNS)

        os.makedirs("data", exist_ok=True)

        filename = "data/inspection_history.csv"

        if os.path.exists(filename):
            df.to_csv(
                filename,
                mode="a",
                header=False,
                index=False
            )
        else:
            df.to_csv(
                filename,
                index=False
            )

        message_placeholder.success(
            "✅ Inspection saved successfully."
        )


if generate_report:

    if "saved_record" not in st.session_state:

       message_placeholder.error(
            "⚠ Please save the inspection before generating the report."
        )
    else:

        record = st.session_state["saved_record"]

        report_data = {

            "pipe_id": record["Pipe ID"],

            "pipeline_name": record["Pipe ID"],

            "material": record["Material"],

            "fluid": record["Fluid"],

            "inspector": record["Inspector"],

            "inspection_date": str(record["Inspection Date"]),

            "pressure": record["Operating Pressure (MPa)"],

            "corrosion_rate": record["Corrosion Rate"],

            "minimum_thickness": record["Minimum Required Thickness"],

            "remaining_life": record["Remaining Life"],

            "corrosion_loss": record["Corrosion Loss %"],

            "safety_factor": record["Safety Factor"],

            "health_score": record["Health Score"],

            "failure_year": record["Estimated Failure Year"],

            "risk_level": record["Risk Level"],

            "likelihood": record["Likelihood"],

            "consequence": record["Consequence"],

            "risk_score": record["Risk Score"]

        }

        try:

            pdf_path = generate_pdf_report(report_data)

            message_placeholder.success(
                "✅ PDF Report Generated Successfully!"
            )

            message_placeholder.success(
                f"✅ Report saved successfully.\n\nLocation:\n{pdf_path}"
            )

        except Exception as e:

            message_placeholder.error(
                f"❌ Report generation failed.\n\n{e}"
            )