from src.data_model import (
    add_inspection,
    load_data,
    search_pipe,
    inspection_history,
    latest_inspection,
)

# ---------------------------
# Test 1: Add a valid inspection
# ---------------------------

record = {
    "Pipe ID": "PL-006",
    "Inspection Date": "2026-08-01",
    "Inspector": "Test Engineer",
    "Material": "Carbon Steel",
    "Fluid": "Crude Oil",
    "Outside Diameter (mm)": 508,
    "Initial Thickness (mm)": 12.0,
    "Current Thickness (mm)": 11.5,
    "Operating Pressure (MPa)": 5.5,
    "Corrosion Rate (mm/year)": 0.15,
    "Remaining Life (years)": 20,
    "Health Score": 90,
    "Risk Category": "Low",
    "Recommendation": "Routine Inspection"
}

print("\n===== Test 1: Add Inspection =====")
add_inspection(record)

# ---------------------------
# Test 2: Load Data
# ---------------------------

print("\n===== Test 2: Load Data =====")
df = load_data()
print(df)

# ---------------------------
# Test 3: Search by Pipe ID
# ---------------------------

print("\n===== Test 3: Search PL-001 =====")
print(search_pipe("PL-001"))

# ---------------------------
# Test 4: Inspection History
# ---------------------------

print("\n===== Test 4: History of PL-001 =====")
print(inspection_history("PL-001"))

# ---------------------------
# Test 5: Latest Inspection
# ---------------------------

print("\n===== Test 5: Latest Inspection =====")
print(latest_inspection("PL-001"))

# ---------------------------
# Test 6: Invalid Data
# ---------------------------

bad_record = {
    "Pipe ID": "",
    "Inspection Date": "07/08/2026",
    "Inspector": "",
    "Material": "Carbon Steel",
    "Fluid": "Crude Oil",
    "Outside Diameter (mm)": 508,
    "Initial Thickness (mm)": -12,
    "Current Thickness (mm)": -10,
    "Operating Pressure (MPa)": -5,
    "Corrosion Rate (mm/year)": 0.20,
    "Remaining Life (years)": 18,
    "Health Score": 85,
    "Risk Category": "Moderate",
    "Recommendation": "Monitor"
}

print("\n===== Test 6: Invalid Record =====")
add_inspection(bad_record)