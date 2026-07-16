import os
import plotly.graph_objects as go
import numpy as np


def risk_matrix_chart(likelihood, consequence):

    risk_matrix = np.array([
        [1, 2, 3, 4, 5],
        [2, 4, 6, 8, 10],
        [3, 6, 9, 12, 15],
        [4, 8, 12, 16, 20],
        [5, 10, 15, 20, 25]
    ])

    # Flip matrix so Likelihood = 5 appears at the top
    risk_matrix = np.flipud(risk_matrix)

    # Create heat map
    fig = go.Figure(
        data=go.Heatmap(
            z=risk_matrix,
            x=[1, 2, 3, 4, 5],
            y=[5, 4, 3, 2, 1],
            text=risk_matrix,
            texttemplate="%{text}",
            hovertemplate=
                "Likelihood: %{y}<br>"
                "Consequence: %{x}<br>"
                "Risk Score: %{z}<extra></extra>",
            colorscale=[
                [0.0, "green"],
                [0.30, "green"],
                [0.30, "yellow"],
                [0.55, "yellow"],
                [0.55, "orange"],
                [0.80, "orange"],
                [0.80, "red"],
                [1.00, "red"],
            ],
            showscale=False
        )
    )

    # Highlight current pipeline
    fig.add_trace(
        go.Scatter(
            x=[consequence],
            y=[likelihood],
            mode="markers",
            marker=dict(
                color="black",
                size=18,
                symbol="x"
            ),
            name="Current Pipeline"
        )
    )

    # Improve layout
    fig.update_layout(
        title="5×5 Pipeline Risk Matrix",
        xaxis_title="Consequence",
        yaxis_title="Likelihood",
        width=700,
        height=600
    )

    # Save latest matrix for PDF
    os.makedirs("assets/charts", exist_ok=True)

    fig.write_image(
        "assets/charts/risk_matrix.png",
        width=900,
        height=800
    )

    return fig

def pipeline_risk(corrosion_rate, fluid):

    # Likelihood
    if corrosion_rate < 0.10:
        likelihood = 1
    elif corrosion_rate < 0.25:
        likelihood = 2
    elif corrosion_rate < 0.50:
        likelihood = 3
    elif corrosion_rate < 1.00:
        likelihood = 4
    else:
        likelihood = 5

    # Consequence
    fluid = fluid.lower()

    if fluid in ["water", "air"]:
        consequence = 1
    elif fluid == "steam":
        consequence = 2
    elif fluid == "natural gas":
        consequence = 3
    elif fluid in ["crude oil", "diesel"]:
        consequence = 4
    elif fluid in ["acid", "hydrogen sulfide"]:
        consequence = 5
    else:
        consequence = 3

    # Risk Score
    score = likelihood * consequence

    # Risk Category
    if score <= 4:
        category = "Low"
    elif score <= 9:
        category = "Medium"
    elif score <= 16:
        category = "High"
    else:
        category = "Extreme"

    return {
        "Likelihood": likelihood,
        "Consequence": consequence,
        "Risk Score": score,
        "Risk Category": category,
        "Recommendation": category,
    }    