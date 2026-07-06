"""
Pipeline Integrity Recommendation Engine

This module provides engineering recommendations
based on pipeline integrity calculations.
"""


def generate_recommendation(
    health_score: int,
    corrosion_rate: float,
    remaining_life: float,
    safety_factor: float,
    corrosion_loss_percentage: float,
) -> dict:
    """
    Generate engineering recommendations for pipeline integrity.

    Parameters:
        health_score (int): Overall pipeline health score (0-100)
        corrosion_rate (float): Corrosion rate (mm/year)
        remaining_life (float): Remaining service life (years)
        safety_factor (float): Current safety factor
        corrosion_loss_percentage (float): Wall thickness loss (%)

    Returns:
        dict:
            {
                "status": ...,
                "recommendation": ...,
                "priority": ...
            }
    """

    # -----------------------------
    # Input Validation
    # -----------------------------

    if not (0 <= health_score <= 100):
        raise ValueError("Health score must be between 0 and 100.")

    if corrosion_rate < 0:
        raise ValueError("Corrosion rate cannot be negative.")

    if remaining_life < 0:
        raise ValueError("Remaining life cannot be negative.")

    if safety_factor < 0:
        raise ValueError("Safety factor cannot be negative.")

    if corrosion_loss_percentage < 0:
        raise ValueError("Corrosion loss percentage cannot be negative.")

    # -----------------------------
    # Highest Priority Conditions
    # -----------------------------

    if safety_factor < 1:
        return {
            "status": "Unsafe",
            "recommendation": (
                "Immediate engineering review required. "
                "Pipeline wall thickness is below the minimum safe limit."
            ),
            "priority": "Emergency",
        }

    if health_score < 50:
        return {
            "status": "Critical",
            "recommendation": (
                "Replace or repair the affected pipeline section immediately."
            ),
            "priority": "Emergency",
        }

    if remaining_life < 5:
        return {
            "status": "Poor",
            "recommendation": (
                "Prepare a maintenance or replacement plan."
            ),
            "priority": "High",
        }

    if corrosion_rate > 0.50:
        return {
            "status": "High Corrosion",
            "recommendation": (
                "Increase inspection frequency and investigate corrosion."
            ),
            "priority": "High",
        }

    if corrosion_loss_percentage > 50:
        return {
            "status": "High Metal Loss",
            "recommendation": (
                "Perform detailed thickness inspection and assess repair options."
            ),
            "priority": "Medium",
        }

    # -----------------------------
    # General Health Score Rules
    # -----------------------------

    if health_score >= 90:
        return {
            "status": "Excellent",
            "recommendation": (
                "Continue routine operation and scheduled inspections."
            ),
            "priority": "Low",
        }

    elif health_score >= 75:
        return {
            "status": "Good",
            "recommendation": (
                "Continue operation and monitor corrosion regularly."
            ),
            "priority": "Low",
        }

    else:
        return {
            "status": "Monitor",
            "recommendation": (
                "Schedule preventive maintenance and detailed inspection."
            ),
            "priority": "Medium",
        }


def get_health_status(health_score: int) -> str:
    """
    Return pipeline health status based on health score.

    Parameters:
        health_score (int): Pipeline health score (0-100)

    Returns:
        str: Health status
    """

    if not (0 <= health_score <= 100):
        raise ValueError("Health score must be between 0 and 100.")

    if health_score >= 90:
        return "🟢 Safe"

    elif health_score >= 75:
        return "🟡 Monitor"

    elif health_score >= 50:
        return "🟠 Warning"

    else:
        return "🔴 Critical"     

def get_risk_category(
    corrosion_rate: float,
    remaining_life: float,
    health_score: int,
) -> str:
    """
    Determine the pipeline risk category.

    Parameters:
        corrosion_rate (float): Corrosion rate (mm/year)
        remaining_life (float): Remaining life (years)
        health_score (int): Health score (0-100)

    Returns:
        str: Risk category
    """

    # -----------------------------
    # Input Validation
    # -----------------------------
    if corrosion_rate < 0:
        raise ValueError("Corrosion rate cannot be negative.")

    if remaining_life < 0:
        raise ValueError("Remaining life cannot be negative.")

    if not (0 <= health_score <= 100):
        raise ValueError("Health score must be between 0 and 100.")

    # -----------------------------
    # Extreme Risk
    # -----------------------------
    if (
        health_score < 50
        or remaining_life < 5
        or corrosion_rate > 0.50
    ):
        return "Extreme"

    # -----------------------------
    # High Risk
    # -----------------------------
    elif (
        health_score < 75
        or remaining_life < 10
        or corrosion_rate > 0.30
    ):
        return "High"

    # -----------------------------
    # Moderate Risk
    # -----------------------------
    elif (
        health_score < 90
        or remaining_life < 20
        or corrosion_rate > 0.10
    ):
        return "Moderate"

    # -----------------------------
    # Low Risk
    # -----------------------------
    else:
        return "Low"           