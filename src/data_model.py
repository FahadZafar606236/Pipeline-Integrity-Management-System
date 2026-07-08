import pandas as pd
from datetime import datetime
from pathlib import Path

# Path to the CSV file
DATA_FILE = Path("data/inspection_history.csv")

# Column names
COLUMNS = [
    "Pipe ID",
    "Inspection Date",
    "Inspector",
    "Material",
    "Fluid",
    "Outside Diameter (mm)",
    "Initial Thickness (mm)",
    "Current Thickness (mm)",
    "Operating Pressure (MPa)",
    "Corrosion Rate (mm/year)",
    "Remaining Life (years)",
    "Health Score",
    "Risk Category",
    "Recommendation"
]


def load_data():
    """
    Load inspection history from the CSV file.
    If the file doesn't exist, return an empty DataFrame
    with the correct columns.
    """
    if DATA_FILE.exists():
        return pd.read_csv(DATA_FILE)
    else:
        return pd.DataFrame(columns=COLUMNS)


def save_data(df):
    """
    Save the DataFrame to the CSV file.
    Overwrites the existing file safely.
    """
    # Create the data folder if it doesn't exist
    DATA_FILE.parent.mkdir(parents=True, exist_ok=True)

    # Save the DataFrame to the CSV file
    df.to_csv(DATA_FILE, index=False)



def validate_record(record):
    """
    Validate an inspection record.
    Returns (True, "Valid") if the record is valid.
    Otherwise returns (False, error_message).
    """

    # Required fields
    required_fields = [
        "Pipe ID",
        "Inspection Date",
        "Inspector",
        "Material",
        "Fluid",
        "Outside Diameter (mm)",
        "Initial Thickness (mm)",
        "Current Thickness (mm)",
        "Operating Pressure (MPa)"
    ]

    # Check required fields
    for field in required_fields:
        if field not in record or record[field] in ("", None):
            return False, f"{field} is required."

    # Pipe ID cannot be empty
    if not str(record["Pipe ID"]).strip():
        return False, "Pipe ID cannot be empty."

    # Thickness values must be positive
    if record["Initial Thickness (mm)"] <= 0:
        return False, "Initial Thickness must be greater than zero."

    if record["Current Thickness (mm)"] <= 0:
        return False, "Current Thickness must be greater than zero."

    # Outside Diameter must be positive
    if record["Outside Diameter (mm)"] <= 0:
        return False, "Outside Diameter must be greater than zero."

# Current Thickness cannot exceed Initial Thickness
    if (
        record["Current Thickness (mm)"] > record["Initial Thickness (mm)"]):
        return (
            False,
            "Current Thickness cannot exceed Initial Thickness."
        )
    # Pressure must be positive
    if record["Operating Pressure (MPa)"] <= 0:
        return False, "Operating Pressure must be greater than zero."

    # Validate date format (YYYY-MM-DD)
    try:
        datetime.strptime(record["Inspection Date"], "%Y-%m-%d")
    except ValueError:
        return False, "Inspection Date must be in YYYY-MM-DD format."

    return True, "Valid"


def add_inspection(record):
    """
    Add a new inspection record.
    Prevent duplicate inspections with the same Pipe ID and Inspection Date.
    """
    # Validate the record
    is_valid, message = validate_record(record)

    if not is_valid:
        print(f"Validation Error: {message}")
        return
        
    # Load existing data
    df = load_data()

    # Check for duplicate record
    duplicate = (
        (df["Pipe ID"] == record["Pipe ID"]) &
        (df["Inspection Date"] == record["Inspection Date"])
    )

    if duplicate.any():
        print("Duplicate inspection found. Record was not added.")
        return

    # Add new record
    new_row = pd.DataFrame([record])
    df = pd.concat([df, new_row], ignore_index=True)

    # Save updated data
    save_data(df)

    print("Inspection record added successfully.")

def search_pipe(pipe_id):
    """
    Return all inspection records for a given Pipe ID.
    """

    # Load the inspection data
    df = load_data()

    # Filter records matching the Pipe ID
    results = df[df["Pipe ID"] == pipe_id]

    return results

def latest_inspection(pipe_id):
    """
    Return the most recent inspection for a given Pipe ID.
    """

    # Get all inspections for the pipeline
    df = search_pipe(pipe_id)

    # If no records exist, return None
    if df.empty:
        return None

    # Convert Inspection Date to datetime
    df["Inspection Date"] = pd.to_datetime(df["Inspection Date"])

    # Sort by date (newest first)
    df = df.sort_values(by="Inspection Date", ascending=False)

    # Return the newest inspection
    return df.iloc[0]

def inspection_history(pipe_id):
    """
    Return all inspection records for a given Pipe ID,
    sorted by inspection date.
    """

    # Get all inspections for the pipeline
    df = search_pipe(pipe_id)

    # If no records exist, return an empty DataFrame
    if df.empty:
        return df

    # Convert Inspection Date to datetime
    df["Inspection Date"] = pd.to_datetime(df["Inspection Date"])

    # Sort by inspection date (oldest to newest)
    df = df.sort_values(by="Inspection Date")

    return df            