import plotly.graph_objects as go


def health_gauge(health_score):

    # Determine health status
    if health_score >= 90:
        status = "Excellent"
    elif health_score >= 75:
        status = "Good"
    elif health_score >= 60:
        status = "Fair"
    elif health_score >= 40:
        status = "Poor"
    else:
        status = "Critical"

    fig = go.Figure(
        go.Indicator(
            mode="gauge+number",
            value=health_score,

            number={
                "suffix": "%",
                "font": {"size": 42}
            },

           title={
                "text": (
                    "<span style='font-size:28px;'><b>Pipeline Health</b></span>"
                    "<br><br>"
                    f"<span style='font-size:20px'>{status}</span>"
                )
            },

            gauge={
                "axis": {
                    "range": [0, 100]
                },

                "bar": {
                    "color": "darkgreen"
                },

                "steps": [
                    {"range": [0, 40], "color": "#d62728"},
                    {"range": [40, 60], "color": "#ff7f0e"},
                    {"range": [60, 75], "color": "#ffd92f"},
                    {"range": [75, 90], "color": "#90ee90"},
                    {"range": [90, 100], "color": "#2ca02c"},
                ],
            },
        )
    )

    fig.update_layout(
        height=300,
        margin=dict(l=20, r=20, t=70, b=20)
    )

    return fig


def thickness_gauge(current_thickness, minimum_thickness):

    safe_margin = current_thickness - minimum_thickness

    maximum = max(current_thickness * 1.2, minimum_thickness * 1.5)

    fig = go.Figure(
        go.Indicator(
            mode="gauge+number",

            value=current_thickness,

            number={
                "suffix": " mm",
                "font": {"size": 38}
            },

            title= {
                "text": (
                    "<span style='font-size:26px;'><b>Remaining Thickness</b></span>"
                    "<br><span style='font-size:8px;'>&nbsp;</span><br>"
                    f"<span style='font-size:18px;'>Safe Margin : {safe_margin:.2f} mm</span>"
                    
                )
            },

            gauge={
                "axis": {
                    "range": [0, maximum]
                },

                "bar": {
                    "color": "#1f77b4"
                },

                "steps": [
                    {
                        "range": [0, minimum_thickness],
                        "color": "#d62728"      # 🔴 Below Minimum
                    },
                    {
                        "range": [minimum_thickness, minimum_thickness * 1.15],
                        "color": "#ffd92f"      # 🟡 Approaching Limit
                    },
                    {
                        "range": [minimum_thickness * 1.15, maximum],
                        "color": "#2ca02c"      # 🟢 Safe
                    }
                ],
                "threshold": {
    "line": {
        "color": "black",
        "width": 4
    },
    "thickness": 0.9,
    "value": minimum_thickness
},
            }
        )
    )

    fig.update_layout(
        height=300,
        margin=dict(l=20, r=20, t=80, b=20)
    )

    return fig


def corrosion_gauge(corrosion_rate):

    # Engineering category
    if corrosion_rate < 0.10:
        status = "Low"
    elif corrosion_rate < 0.30:
        status = "Medium"
    elif corrosion_rate < 0.60:
        status = "High"
    else:
        status = "Severe"

    maximum = 1.0

    fig = go.Figure(
        go.Indicator(
            mode="gauge+number",

            value=corrosion_rate,

            number={
                "suffix": " mm/y",
                "font": {"size": 38}
            },

            title={
                "text": (
                    "<span style='font-size:26px;'><b>Corrosion Rate</b></span>"
                    "<br><br>"
                    f"<span style='font-size:20px'>{status}</span>"
                )
            },

            gauge={
                "axis": {
                    "range": [0, maximum]
                },

                "bar": {
                    "color": "#1f77b4"
                },

                "steps": [

                    {
                        "range": [0.00, 0.10],
                        "color": "#2ca02c"      # 🟢 Low
                    },

                    {
                        "range": [0.10, 0.30],
                        "color": "#ffd92f"      # 🟡 Medium
                    },

                    {
                        "range": [0.30, 0.60],
                        "color": "#ff7f0e"      # 🟠 High
                    },

                    {
                        "range": [0.60, 1.00],
                        "color": "#d62728"      # 🔴 Severe
                    }

                ],
                "threshold": {
    "line": {
        "color": "black",
        "width": 4
    },
    "thickness": 0.9,
    "value": 0.30
},
            }
        )
    )

    fig.update_layout(
        height=300,
        margin=dict(l=20, r=20, t=70, b=20)
    )

    return fig



def remaining_life_gauge(remaining_life):

    # Engineering condition
    if remaining_life >= 15:
        status = "Excellent"
    elif remaining_life >= 5:
        status = "Good"
    elif remaining_life >= 2:
        status = "Warning"
    else:
        status = "Critical"

    maximum = 25

    fig = go.Figure(
        go.Indicator(
            mode="gauge+number",

            value=remaining_life,

            number={
                "suffix": " Years",
                "valueformat": ".0f",
                "font": {"size": 38}
            },

            title={
                "text": (
                    "<span style='font-size:26px;'><b>Remaining Life</b></span>"
                    "<br><br>"
                    f"<span style='font-size:20px'>{status}</span>"
                )
            },

            gauge={
                "axis": {
                    "range": [0, maximum]
                },

                "bar": {
                    "color": "#1f77b4"
                },

                "steps": [
                    {
                        "range": [0, 2],
                        "color": "#d62728"      # 🔴 Critical
                    },
                    {
                        "range": [2, 5],
                        "color": "#ff7f0e"      # 🟠 Warning
                    },
                    {
                        "range": [5, 15],
                        "color": "#ffd92f"      # 🟡 Good
                    },
                    {
                        "range": [15, 25],
                        "color": "#2ca02c"      # 🟢 Excellent
                    }
                ],

                "threshold": {
                    "line": {
                        "color": "black",
                        "width": 4
                    },
                    "thickness": 0.9,
                    "value": 2
                }
            }
        )
    )

    fig.update_layout(
        height=300,
        margin=dict(l=20, r=20, t=70, b=20)
    )

    return fig



def safety_factor_gauge(safety_factor):

    if safety_factor >= 2.0:
        status = "Excellent"
    elif safety_factor >= 1.5:
        status = "Good"
    elif safety_factor >= 1.2:
        status = "Low"
    else:
        status = "Critical"

    maximum = 3.0

    fig = go.Figure(
        go.Indicator(
            mode="gauge+number",

            value=safety_factor,

            number={
                "valueformat": ".2f",
                "font": {"size": 38}
            },

            title={
                "text": (
                    "<span style='font-size:26px;'><b>Safety Factor</b></span>"
                    "<br><br>"
                    f"<span style='font-size:20px'>{status}</span>"
                )
            },

            gauge={

                "axis": {
                    "range": [0, maximum]
                },

                "bar": {
                    "color": "#1f77b4"
                },

                "steps": [

                    {
                        "range": [0, 1.2],
                        "color": "#d62728"
                    },

                    {
                        "range": [1.2, 1.5],
                        "color": "#ff7f0e"
                    },

                    {
                        "range": [1.5, 2.0],
                        "color": "#ffd92f"
                    },

                    {
                        "range": [2.0, 3.0],
                        "color": "#2ca02c"
                    }

                ],

                "threshold": {
                    "line": {
                        "color": "black",
                        "width": 4
                    },
                    "thickness": 0.9,
                    "value": 1.5
                }

            }

        )
    )

    fig.update_layout(
        height=330,
        margin=dict(l=20, r=20, t=100, b=20)
    )

    return fig        