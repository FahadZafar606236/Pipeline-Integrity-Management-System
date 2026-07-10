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


from datetime import timedelta

def next_inspection_date(
    inspection_date,
    remaining_life: float,
) -> str:

    if remaining_life < 0:
        raise ValueError("Remaining life cannot be negative.")

    if remaining_life == float("inf"):
        return "No inspection required (No corrosion detected)"

    inspection_interval = remaining_life / 2

    inspection_days = round(inspection_interval * 365)

    next_date = inspection_date + timedelta(days=inspection_days)

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


def corrosion_loss_percentage(
    initial_thickness: float,
    current_thickness: float,
) -> float:
    """
    Calculate the percentage of wall thickness lost due to corrosion.

    Parameters:
        initial_thickness (float): Original pipe wall thickness
        current_thickness (float): Current measured wall thickness

    Returns:
        float: Corrosion loss percentage
    """

    # Validate inputs
    if initial_thickness <= 0:
        raise ValueError("Initial thickness must be greater than zero.")

    if current_thickness < 0:
        raise ValueError("Current thickness cannot be negative.")

    if current_thickness > initial_thickness:
        raise ValueError("Current thickness cannot be greater than initial thickness.")

    loss = initial_thickness - current_thickness
    loss_percentage = (loss / initial_thickness) * 100

    return round(loss_percentage, 2)    
"""
Calculate the safety factor.

Purpose:
    Determines how much thicker the current pipeline wall is
    compared to the minimum required wall thickness.

Formula:
    Safety Factor =
        Current Thickness / Minimum Required Thickness

Parameters:
    current_thickness (float):
        Current measured wall thickness (mm).

    minimum_required_thickness (float):
        Minimum required wall thickness (mm).

Returns:
    float:
        Safety factor.

Raises:
    ValueError:
        If any input value is invalid.
"""


def safety_factor(
    current_thickness: float,
    minimum_required_thickness: float,
) -> float:
    """
    Calculate pipeline safety factor.
    """

    if current_thickness <= 0:
        raise ValueError("Current thickness must be greater than zero.")

    if minimum_required_thickness <= 0:
        raise ValueError(
            "Minimum required thickness must be greater than zero."
        )

    factor = current_thickness / minimum_required_thickness

    return round(factor, 2)


def health_score(
    remaining_life: float,
    corrosion_rate: float,
    safety_factor: float,
    corrosion_loss_percentage: float,
) -> int:
    """
    Calculate an overall pipeline health score (0–100).
    """

    score = 0

    # Remaining Life (35 points)
    if remaining_life < 0:
        raise ValueError("Remaining life cannot be negative.")
    elif remaining_life >= 25:
        score += 35
    elif remaining_life >= 15:
        score += 28
    elif remaining_life >= 10:
        score += 21
    elif remaining_life >= 5:
        score += 14
    else:
        score += 7

    """
Determine the pipeline risk level based on the calculated health score.

Purpose:
    Classifies the overall pipeline condition into an engineering risk category.

Parameters:
    score (float):
        Pipeline health score (0–100).

Returns:
    str:
        One of the following risk levels:
        - Low
        - Moderate
        - High
        - Critical
"""

   

    # Corrosion Rate (25 points)
    if corrosion_rate < 0:
        raise ValueError("Corrosion rate cannot be negative.")
    elif corrosion_rate <= 0.10:
        score += 25
    elif corrosion_rate <= 0.20:
        score += 20
    elif corrosion_rate <= 0.50:
        score += 15
    elif corrosion_rate <= 1.00:
        score += 8
    else:
        score += 3

    # Safety Factor (20 points)
    if safety_factor < 0:
        raise ValueError("Safety factor cannot be negative.")
    elif safety_factor >= 2.0:
        score += 20
    elif safety_factor >= 1.5:
        score += 16
    elif safety_factor >= 1.2:
        score += 12
    elif safety_factor >= 1.0:
        score += 8
    else:
        score += 2

    # Corrosion Loss % (20 points)
    if corrosion_loss_percentage < 0:
        raise ValueError("Corrosion loss percentage cannot be negative.")
    elif corrosion_loss_percentage <= 10:
        score += 20
    elif corrosion_loss_percentage <= 20:
        score += 16
    elif corrosion_loss_percentage <= 40:
        score += 12
    elif corrosion_loss_percentage <= 60:
        score += 8
    else:
        score += 2

    # Keep score between 0 and 100
    score = max(0, min(score, 100))

    return score  

def risk_level(score):
    """
    Determine the engineering risk level.
    """

    if score >= 90:
        return "Low"

    elif score >= 70:
        return "Moderate"

    elif score >= 50:
        return "High"

    else:
        return "Critical" 

def estimated_failure_year(current_year: int, remaining_life: float) -> int:
    """
    Estimate the calendar year when the pipeline reaches failure condition.

    Parameters:
        current_year (int):
            Base year of evaluation.

        remaining_life (float):
            Remaining service life in years.

    Returns:
        int:
            Estimated failure year.

    Engineering Formula:
        Failure Year = Current Year + Remaining Life
    """
    if current_year < 1900:
        raise ValueError("Current year cannot be before 1900.")
    if remaining_life < 0:
        raise ValueError("Remaining life cannot be negative.")

    if remaining_life == float("inf"):
        raise ValueError("Infinite life means no failure prediction.")

    return current_year + int(round(remaining_life))