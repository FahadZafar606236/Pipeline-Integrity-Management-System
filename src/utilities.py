"""
Utility functions for Pipeline Integrity Management System.
"""


def validate_pipeline_inputs(
    initial_thickness,
    current_thickness,
    corrosion_rate,
    remaining_life,
    health_score,
):
    """
    Validate common pipeline engineering inputs.

    Raises:
        ValueError: If any input is invalid.
    """

    # -----------------------------
    # Missing values
    # -----------------------------
    values = {
        "Initial thickness": initial_thickness,
        "Current thickness": current_thickness,
        "Corrosion rate": corrosion_rate,
        "Remaining life": remaining_life,
        "Health score": health_score,
    }

    for name, value in values.items():
        if value is None:
            raise ValueError(f"{name} cannot be empty.")

    # -----------------------------
    # Thickness validation
    # -----------------------------
    if initial_thickness <= 0:
        raise ValueError("Initial thickness must be greater than zero.")

    if current_thickness < 0:
        raise ValueError("Current thickness cannot be negative.")

    if current_thickness > initial_thickness:
        raise ValueError(
            "Current thickness cannot be greater than initial thickness."
        )

    # -----------------------------
    # Corrosion Rate
    # -----------------------------
    if corrosion_rate < 0:
        raise ValueError("Corrosion rate cannot be negative.")

    # -----------------------------
    # Remaining Life
    # -----------------------------
    if remaining_life < 0:
        raise ValueError("Remaining life cannot be negative.")

    # -----------------------------
    # Health Score
    # -----------------------------
    if not (0 <= health_score <= 100):
        raise ValueError(
            "Health score must be between 0 and 100."
        )

    return True