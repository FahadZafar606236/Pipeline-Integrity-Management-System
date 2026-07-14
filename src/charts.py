"""
Pipeline Integrity Management System
Visualization Module

Author:
Muhammad Fahad Zafar

Description:
This module contains all Plotly visualization functions
used throughout the application.

Engineering Standards
---------------------
• ASME B31.3
• API 570

Future Charts
-------------
• Corrosion Trend Chart
• Thickness History Chart
• Remaining Life Trend
• Health Score Trend
• Gauge Chart
• Risk Matrix
"""
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px

history = pd.read_csv("data/inspection_history.csv")

history.rename(
    columns={
        "Pipe ID": "pipe_id",
        "Inspection Date": "inspection_date",
        "Current Thickness (mm)": "current_thickness",
        "Corrosion Rate": "corrosion_rate",
        "Remaining Life": "remaining_life",
        "Health Score": "health_score",
        "Minimum Required Thickness": "minimum_required_thickness",
    },
    inplace=True
)

history["inspection_date"] = pd.to_datetime(
    history["inspection_date"]
)

def corrosion_trend_chart(data):

    data = data.rename(columns={
    "Pipe ID": "pipe_id",
    "Inspection Date": "inspection_date",
    "Current Thickness (mm)": "current_thickness",
    "Corrosion Rate": "corrosion_rate",
    "Remaining Life": "remaining_life",
    "Health Score": "health_score",
    "Minimum Required Thickness": "minimum_required_thickness",
})

    data["inspection_date"] = pd.to_datetime(data["inspection_date"])
    """
    Displays the corrosion rate trend over time.
    """
    data = data.sort_values(["pipe_id", "inspection_date"])

    fig = go.Figure()

    for pipe, df in data.groupby("pipe_id"):

        df = df.sort_values("inspection_date")

        fig.add_trace(
            go.Scatter(
                x=df["inspection_date"],
                y=df["corrosion_rate"],
                mode="lines+markers",
                name=pipe
            )
        )

    fig.update_layout(
        
        title="Pipeline Corrosion Rate Trend",
        template="plotly_dark",
        paper_bgcolor="#111827",
        plot_bgcolor="#111827",
        font=dict(
            family="Arial",
            size=14,
            color="white"
        ),
        title_font=dict(
            size=22,
            color="#00E5FF"
        ),
        xaxis_title="Inspection Date",
        yaxis_title="Corrosion Rate (mm/year)",
        hovermode="x unified",
        showlegend=True,
        height=500
    )

    
    fig.update_xaxes(
            showgrid=True,
            gridcolor="#374151",
            zeroline=False
    )

    fig.update_yaxes(
            showgrid=True,
            gridcolor="#374151",
            zeroline=False
    )

    return fig

def thickness_history_chart(data):

    data = data.rename(columns={
    "Pipe ID": "pipe_id",
    "Inspection Date": "inspection_date",
    "Current Thickness (mm)": "current_thickness",
    "Corrosion Rate": "corrosion_rate",
    "Remaining Life": "remaining_life",
    "Health Score": "health_score",
    "Minimum Required Thickness": "minimum_required_thickness",
})

    data["inspection_date"] = pd.to_datetime(data["inspection_date"])
    """
    Displays pipeline wall thickness history.
    """

    # Sort data
    data = data.sort_values(["pipe_id", "inspection_date"])

    # Pipeline thickness trend
    fig = px.line(
        data,
        x="inspection_date",
        y="current_thickness",
        color="pipe_id",
        markers=True,
        title="Pipeline Wall Thickness History"
    )

    # Minimum Required Thickness
    fig.add_trace(
        go.Scatter(
            x=data["inspection_date"],
            y=data["minimum_required_thickness"],
            mode="lines",
            name="Minimum Required Thickness",
            line=dict(
                color="red",
                dash="dash",
                width=3
            )
        )
    )

    # Make only pipeline lines thicker
    fig.for_each_trace(
        lambda trace: trace.update(line=dict(width=3))
        if trace.name != "Minimum Required Thickness"
        else None
    )

    fig.update_layout(
        template="plotly_dark",
        paper_bgcolor="#111827",
        plot_bgcolor="#111827",
        font=dict(
            family="Arial",
            size=14,
            color="white"
        ),
        title_font=dict(
            size=22,
            color="#00E5FF"
        ),
        xaxis_title="Inspection Date",
        yaxis_title="Wall Thickness (mm)",
        hovermode="x unified",
        showlegend=True,
        height=500
    )

    fig.update_xaxes(
        showgrid=True,
        gridcolor="#374151",
        zeroline=False
    )

    fig.update_yaxes(
        showgrid=True,
        gridcolor="#374151",
        zeroline=False
    )

    return fig

def remaining_life_chart(data):

    data = data.rename(columns={
    "Pipe ID": "pipe_id",
    "Inspection Date": "inspection_date",
    "Current Thickness (mm)": "current_thickness",
    "Corrosion Rate": "corrosion_rate",
    "Remaining Life": "remaining_life",
    "Health Score": "health_score",
    "Minimum Required Thickness": "minimum_required_thickness",
})

    data["inspection_date"] = pd.to_datetime(data["inspection_date"])
    """
    Displays the remaining service life trend.
    """

    # Sort data
    data = data.sort_values(["pipe_id", "inspection_date"])

    # Plot one line per pipeline
    fig = px.line(
        data,
        x="inspection_date",
        y="remaining_life",
        color="pipe_id",
        markers=True,
        title="Pipeline Remaining Service Life Trend"
    )

    # Make pipeline lines thicker
    fig.for_each_trace(
        lambda trace: trace.update(line=dict(width=3))
    )

    # Highlight inspections with remaining life below 5 years
    critical = data[data["remaining_life"] < 5]

    if not critical.empty:
        fig.add_trace(
            go.Scatter(
                x=critical["inspection_date"],
                y=critical["remaining_life"],
                mode="markers",
                name="Critical (<5 Years)",
                marker=dict(
                    color="red",
                    size=12,
                    symbol="diamond"
                )
            )
        )

    # Critical limit line
    fig.add_hline(
        y=5,
        line_color="red",
        line_dash="dash",
        annotation_text="Critical Limit (5 Years)"
    )

    fig.update_layout(
        template="plotly_dark",
        paper_bgcolor="#111827",
        plot_bgcolor="#111827",
        font=dict(
            family="Arial",
            size=14,
            color="white"
        ),
        title_font=dict(
            size=22,
            color="#FFD60A"
        ),
        xaxis_title="Inspection Date",
        yaxis_title="Remaining Life (Years)",
        hovermode="x unified",
        showlegend=True,
        height=500
    )

    fig.update_xaxes(
        showgrid=True,
        gridcolor="#374151",
        zeroline=False
    )

    fig.update_yaxes(
        showgrid=True,
        gridcolor="#374151",
        zeroline=False
    )

    return fig

def health_trend_chart(data):
    """
    Displays pipeline health score trend.
    """

    fig = px.line(
        data.sort_values(["pipe_id", "inspection_date"]),
        x="inspection_date",
        y="health_score",
        color="pipe_id",   # ✅ Correct
        markers=True,
        title="Pipeline Health Score Trend"
    )



    # Good Health Zone (80–100)
    fig.add_hrect(
        y0=80,
        y1=100,
        fillcolor="green",
        opacity=0.12,
        line_width=0,
        annotation_text="Good"
    )

    # Warning Zone (50–80)
    fig.add_hrect(
        y0=50,
        y1=80,
        fillcolor="yellow",
        opacity=0.12,
        line_width=0,
        annotation_text="Warning"
    )

    # Critical Zone (0–50)
    fig.add_hrect(
        y0=0,
        y1=50,
        fillcolor="red",
        opacity=0.12,
        line_width=0,
        annotation_text="Critical"
    )


    fig.update_layout(
    template="plotly_dark",
    paper_bgcolor="#111827",
    plot_bgcolor="#111827",
    font=dict(
        family="Arial",
        size=14,
        color="white"
    ),
    title_font=dict(
        size=22,
        color="#00FF9D"
    ),
    xaxis_title="Inspection Date",
    yaxis_title="Health Score",
    hovermode="x unified",
    showlegend=True,
    height=500
)

    fig.update_xaxes(
        showgrid=True,
        gridcolor="#374151",
        zeroline=False
    )

    fig.update_yaxes(
        showgrid=True,
        gridcolor="#374151",
        zeroline=False
    )
    return fig


def gauge_chart(data):
    """
    Displays pipeline health gauge.
    """

    pass


def risk_matrix_chart(data):
    """
    Displays engineering risk matrix.
    """

    pass        