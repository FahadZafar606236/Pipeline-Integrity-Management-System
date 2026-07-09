import streamlit as st


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
)
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

from datetime import date

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
    st.button(
        "💾 Save Inspection",
        disabled=True,
        use_container_width=True,
        help="This feature will be enabled in a later phase."
    )

with col4:
    st.button(
        "📤 Export",
        disabled=True,
        use_container_width=True,
        help="Export functionality will be implemented later."
    )


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

                # Store results
                st.session_state["corrosion_rate"] = corrosion
                st.session_state["minimum_required_thickness"] = min_thickness
                st.session_state["remaining_life"] = life
                st.session_state["corrosion_loss"] = loss_percentage
                st.session_state["safety_factor"] = sf
                st.session_state["health_score"] = score
                st.session_state["next_inspection_date"] = next_date
                st.session_state["corrosion_allowance"] = allowance
                st.session_state["estimated_failure_year"] = failure_year

                st.success("✅ Engineering calculations completed successfully.")

            except Exception:

                st.error("❌ Unable to complete engineering calculations.")

                st.info(
                    "Please check the entered values and try again."
                )
if "health_score" in st.session_state:
    st.divider()

    st.markdown("## 📊 Engineering Results")
    st.caption(
    "Calculated according to ASME B31.3 and API 570 engineering methodology."
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Corrosion Rate",
            f"{st.session_state['corrosion_rate']:.3f} mm/year"
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

    st.markdown("## 💡 Engineering Recommendation")

    score = st.session_state["health_score"]

    if score >= 90:
        st.success("✅ Continue normal operation. Pipeline condition is excellent.")

    elif score >= 70:
        st.warning("⚠ Pipeline is operating safely. Schedule inspection according to API 570.")

    else:
        st.error("🚨 Critical condition detected. Immediate maintenance or pipeline replacement is recommended.")

    st.divider()

# ======================================================
# Future Dashboard Components
# ======================================================

st.markdown("## 📈 Future Engineering Dashboard")

col1, col2 = st.columns(2)

with col1:
    st.info("📉 Corrosion Trend Chart\n\n(Coming in Phase 12)")

with col2:
    st.info("🧭 Remaining Thickness Gauge\n\n(Coming in Phase 12)")

col3, col4 = st.columns(2)

with col3:
    st.info("⚠ Risk Matrix\n\n(Coming in Phase 13)")

with col4:
    st.info("📋 Recommendation Panel\n\n(Coming in Phase 13)")

st.divider()