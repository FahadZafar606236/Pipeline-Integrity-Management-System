"""
Engineering calculation functions
Pipeline Integrity Management System

This module contains:
- Corrosion Rate
- Minimum Required Thickness
- Remaining Life
- Next Inspection Date
- Corrosion Allowance
"""

from datetime import datetime, timedelta

"""
Calculate the corrosion rate of a pipeline.

Purpose:
    Determines the average wall thickness loss per year due to corrosion.

Formula:
    Corrosion Rate = (Initial Thickness - Current Thickness) / Years

Parameters:
    initial_thickness (float):
        Original pipe wall thickness in millimeters (mm).

    current_thickness (float):
        Current measured pipe wall thickness in millimeters (mm).

    years (float):
        Total years the pipeline has been in service.

Returns:
    float:
        Corrosion rate in millimeters per year (mm/year).

Units:
    Thickness : mm
    Time      : years
    Result    : mm/year

Raises:
    ValueError:
        If any input value is invalid.
"""
def corrosion_rate(
    initial_thickness: float,
    current_thickness: float,
    years: float,
) -> float:
    """
    Calculate the corrosion rate of a pipeline.
    """

    if initial_thickness <= 0:
        raise ValueError("Initial thickness must be greater than zero.")

    if current_thickness <= 0:
        raise ValueError("Current thickness must be greater than zero.")

    if years <= 0:
        raise ValueError("Years in service must be greater than zero.")

    if current_thickness > initial_thickness:
        raise ValueError(
            "Current thickness cannot be greater than initial thickness."
        )

    return (initial_thickness - current_thickness) / years

"""
Calculate the minimum required wall thickness using the
ASME B31.3 Pressure Design Equation.

Purpose:
    Determines the minimum pipe wall thickness required to
    safely withstand the operating pressure.

Formula:
    t = (P × D) / (2 × S × E + 2 × P × Y)

Parameters:
    pressure (float):
        Operating pressure (MPa).

    diameter (float):
        Outside pipe diameter (mm).

    allowable_stress (float):
        Allowable material stress (MPa).

    weld_efficiency (float):
        Weld joint efficiency (0–1).

    temperature_factor (float):
        Temperature coefficient (Y).

Returns:
    float:
        Minimum required wall thickness (mm).

Units:
    Pressure : MPa
    Diameter : mm
    Stress   : MPa
    Result   : mm

Raises:
    ValueError:
        If any input value is invalid.
"""
def minimum_required_thickness(
    pressure: float,
    diameter: float,
    allowable_stress: float,
    weld_efficiency: float,
    temperature_factor: float,
) -> float:
    """
    Calculate minimum required thickness using ASME B31.3.
    """

    if pressure <= 0:
        raise ValueError("Pressure must be greater than zero.")

    if diameter <= 0:
        raise ValueError("Diameter must be greater than zero.")

    if allowable_stress <= 0:
        raise ValueError("Allowable stress must be greater than zero.")

    if not (0 < weld_efficiency <= 1):
        raise ValueError("Weld efficiency must be between 0 and 1.")

    if temperature_factor < 0:
        raise ValueError("Temperature factor cannot be negative.")

    denominator = (
        2 * allowable_stress * weld_efficiency
        + 2 * pressure * temperature_factor
    )

    if denominator == 0:
        raise ValueError("Denominator cannot be zero.")

    return (pressure * diameter) / denominator

"""
Calculate the remaining service life of the pipeline.

Purpose:
    Estimates how many years remain before the pipeline wall
    reaches the minimum allowable thickness.

Formula:
    Remaining Life =
    (Current Thickness - Minimum Thickness) / Corrosion Rate

Parameters:
    current_thickness (float):
        Current measured wall thickness (mm).

    minimum_thickness (float):
        Minimum allowable wall thickness (mm).

    corrosion_rate (float):
        Corrosion rate (mm/year).

Returns:
    float:
        Remaining service life (years).

        Returns:
            float("inf") if corrosion rate is zero.
            0.0 if remaining life is negative.

Units:
    Thickness : mm
    Corrosion : mm/year
    Result    : years

Raises:
    ValueError:
        If any input value is invalid.
"""
def remaining_life(
    current_thickness: float,
    minimum_thickness: float,
    corrosion_rate: float,
) -> float:
    """
    Calculate remaining life.
    """

    if current_thickness <= 0:
        raise ValueError("Current thickness must be greater than zero.")

    if minimum_thickness <= 0:
        raise ValueError("Minimum thickness must be greater than zero.")

    if corrosion_rate < 0:
        raise ValueError("Corrosion rate cannot be negative.")

    if corrosion_rate == 0:
        return float("inf")

    remaining = (current_thickness - minimum_thickness) / corrosion_rate

    if remaining < 0:
        return 0.0

    return remaining

"""
Calculate the recommended next inspection date.

Purpose:
    Estimates the next inspection date based on one-half of
    the remaining service life.

Formula:
    Inspection Interval = Remaining Life / 2

    Next Inspection Date =
        Today's Date + Inspection Interval

Parameters:
    remaining_life (float):
        Remaining service life (years).

Returns:
    str:
        Inspection date formatted as YYYY-MM-DD.

        Returns a message if corrosion rate is zero.

Units:
    Remaining Life : years
    Date           : YYYY-MM-DD

Raises:
    ValueError:
        If remaining life is negative.
"""
def next_inspection_date(
    remaining_life: float,
) -> str:
    """
    Calculate the next inspection date.
    """

    if remaining_life < 0:
        raise ValueError("Remaining life cannot be negative.")

    if remaining_life == float("inf"):
        return "No inspection required (No corrosion detected)"

    inspection_interval = remaining_life / 2

    inspection_days = int(inspection_interval * 365)

    today = datetime.today()

    next_date = today + timedelta(days=inspection_days)

    return next_date.strftime("%Y-%m-%d")

"""
Calculate the corrosion allowance.

Purpose:
    Determines the available wall thickness that may be lost
    due to corrosion before reaching the minimum allowable
    thickness.

Formula:
    Corrosion Allowance =
        Nominal Thickness - Minimum Thickness

Parameters:
    nominal_thickness (float):
        Original pipe wall thickness (mm).

    minimum_thickness (float):
        Minimum allowable wall thickness (mm).

Returns:
    float:
        Corrosion allowance (mm).

Units:
    Thickness : mm
    Result    : mm

Raises:
    ValueError:
        If any input value is invalid.
"""
def corrosion_allowance(
    nominal_thickness: float,
    minimum_thickness: float,
) -> float:
    """
    Calculate corrosion allowance.
    """

    if nominal_thickness <= 0:
        raise ValueError("Nominal thickness must be greater than zero.")

    if minimum_thickness <= 0:
        raise ValueError("Minimum thickness must be greater than zero.")

    if minimum_thickness > nominal_thickness:
        raise ValueError(
            "Minimum thickness cannot be greater than nominal thickness."
        )

    return nominal_thickness - minimum_thickness