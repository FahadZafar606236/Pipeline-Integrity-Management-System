import streamlit as st


def load_css():
    with open("assets/styles.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css()
import pandas as pd
import os

st.title("📋 Inspection History")

st.caption(
    "View, search, filter and manage previous pipeline inspections."
)

st.divider()

filename = "data/inspection_history.csv"

if os.path.exists(filename):
    df = pd.read_csv(filename)
else:
    df = pd.DataFrame()

if df.empty:
    st.info("No inspection history available.")
    st.stop()
# Convert date column
df["Inspection Date"] = pd.to_datetime(df["Inspection Date"])


# ==========================================
# Reset Function
# ==========================================

def reset_filters():
    st.session_state.pipe_search = ""
    st.session_state.risk_filter = "All"
    st.session_state.health_filter = 0
    st.session_state.sort_order = "Newest First"
    st.session_state.start_date = df["Inspection Date"].min().date()
    st.session_state.end_date = df["Inspection Date"].max().date()
# ==========================================
# Sidebar Filters
# ==========================================

st.sidebar.header("🔍 Filter Inspections")

pipe_search = st.sidebar.text_input(
    "Pipe ID",
    placeholder="PL-001",
    key="pipe_search"
)

risk_filter = st.sidebar.selectbox(
    "Risk Category",
    ["All"] + sorted(df["Risk Category"].dropna().unique()),
    key="risk_filter"
)

health_filter = st.sidebar.slider(
    "Minimum Health Score",
    0,
    100,
    0,
    key="health_filter"
)



start_date = st.sidebar.date_input(
    "From",
    df["Inspection Date"].min().date(),
    key="start_date"
)

end_date = st.sidebar.date_input(
    "To",
    df["Inspection Date"].max().date(),
    key="end_date"
)

sort_order = st.sidebar.radio(
    "Sort",
    ["Newest First", "Oldest First"],
    key="sort_order"
)

st.sidebar.button(
    "🔄 Reset Filters",
    on_click=reset_filters
)

    
filtered_df = df.copy()

if pipe_search:
    filtered_df = filtered_df[
        filtered_df["Pipe ID"].str.contains(
            pipe_search,
            case=False,
            na=False
        )
    ]

if risk_filter != "All":
    filtered_df = filtered_df[
        filtered_df["Risk Category"] == risk_filter
    ]

filtered_df = filtered_df[
    filtered_df["Health Score"] >= health_filter
]

filtered_df = filtered_df[
    (filtered_df["Inspection Date"] >= pd.to_datetime(start_date))
    &
    (filtered_df["Inspection Date"] <= pd.to_datetime(end_date))
]

filtered_df = filtered_df.sort_values(
    "Inspection Date",
    ascending=(sort_order == "Oldest First")
)

st.markdown("## 📊 Summary")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Records", len(filtered_df))

with col2:
    st.metric(
        "Pipelines",
        filtered_df["Pipe ID"].nunique()
    )

with col3:
    st.metric(
        "Average Health",
        f"{filtered_df['Health Score'].mean():.1f}"
    )

with col4:
    st.metric(
        "Highest Risk",
        filtered_df["Risk Category"].mode().iloc[0]
        if not filtered_df.empty else "-"
    )


st.divider()

st.markdown("## 📄 Inspection Records")

st.dataframe(
    filtered_df,
    use_container_width=True,
    hide_index=True
)


st.divider()

csv = filtered_df.to_csv(index=False).encode("utf-8")

st.download_button(
    "📥 Export Filtered CSV",
    csv,
    "inspection_history.csv",
    "text/csv",
    use_container_width=True
)