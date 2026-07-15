import streamlit as st

def load_css():
    with open("assets/styles.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css()

import streamlit as st
import os
from datetime import datetime

st.title("📄 Reports")
st.write("Generate engineering reports.")

REPORT_FOLDER = "reports/inspection_reports"

if not os.path.exists(REPORT_FOLDER):

    os.makedirs(REPORT_FOLDER)


reports = []

for file in os.listdir(REPORT_FOLDER):

    if file.endswith(".pdf"):

        path = os.path.join(
            REPORT_FOLDER,
            file
        )

        reports.append(
            {
                "name": file,
                "path": path
            }
        )
st.metric(
    "Total Reports",
    len(reports)
)

search = st.text_input(
    "🔍 Search Report by Pipe ID"
)

if search:

    reports = [
        r for r in reports
        if search.lower() in r["name"].lower()
    ]
    
if reports:

    for report in reports:

        with st.container():

            col1, col2, col3 = st.columns(
                [4,1,1]
            )


            with col1:

                st.write(
                    "📄",
                    report["name"]
                )


            with col2:

                with open(
                    report["path"],
                    "rb"
                ) as pdf:

                    st.download_button(
                        label="⬇️ Download",
                        data=pdf,
                        file_name=report["name"],
                        mime="application/pdf"
                    )


            with col3:

                if st.button(
                    "🗑 Delete",
                    key=report["name"]
                ):

                    os.remove(
                        report["path"]
                    )

                    st.success(
                        "Report deleted"
                    )

                    st.rerun()

else:

    st.info(
        "No reports available."
    )
