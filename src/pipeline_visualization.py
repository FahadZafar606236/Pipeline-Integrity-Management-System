import plotly.graph_objects as go
import streamlit as st


def get_section_color(health_score):

    if health_score >= 90:
        return "green"

    elif health_score >= 75:
        return "orange"

    else:
        return "red"



def pipeline_visualization(df, selected_pipe):

    pipeline_data = df[df["pipe_id"] == selected_pipe]

    st.subheader("📋 Pipeline Information")


    col1, col2, col3 = st.columns(3)

    with col1:
        st.write(f"**Pipeline ID:** {selected_pipe}")
        st.write(f"**Material:** {pipeline_data['Material'].iloc[0]}")

    with col2:
        st.write(f"**Fluid:** {pipeline_data['Fluid'].iloc[0]}")
        st.write("**Length:** 1000 m")

    with col3:
        st.write(
            f"**Operating Pressure:** {pipeline_data['Operating Pressure (MPa)'].iloc[0]} MPa"
        )

        st.write(
            f"**Inspection Date:** {pipeline_data['inspection_date'].max().date()}"
        )


    # Pipeline Visualization starts here
    health = pipeline_data["health_score"].iloc[0]

    color = get_section_color(health)


    st.subheader("🛢️ Pipeline Condition Map")


    fig = go.Figure()


    fig.add_trace(
        go.Scatter(
            x=[0,100],
            y=[0,0],
            mode="lines",
            line=dict(
                width=20,
                color=color
            )
        )
    )
    # Multiple inspection points

    inspection_x = []
    inspection_text = []
    inspection_colors = []


    for index, row in pipeline_data.iterrows():

        inspection_x.append(index * 10)

        inspection_text.append(
            f"Date: {row['inspection_date'].date()}<br>"
            f"Thickness: {row['current_thickness']} mm<br>"
            f"Health: {row['health_score']}%"
        )

        inspection_colors.append(
            get_section_color(row["health_score"])
        )


    fig.add_trace(
    go.Scatter(
        x=inspection_x,
        y=[0] * len(inspection_x),
        mode="markers+text",
        marker=dict(
            size=18,
            color=inspection_colors
        ),
        text=[
            "Inspection"
            for _ in inspection_x
        ],
        textposition="top center",
        hovertext=inspection_text,
        hoverinfo="text",
        name="Inspection Points"
    )
)


    fig.update_layout(
        height=300,
        xaxis=dict(visible=False),
        yaxis=dict(visible=False)
    )


    st.plotly_chart(
        fig,
        use_container_width=True
    )