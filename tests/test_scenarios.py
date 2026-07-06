print("File started: Realistic Scenario Tests\n")

from src.calculations import (
    corrosion_loss_percentage,
    safety_factor,
    health_score,
    estimated_failure_year,
)

from src.recommendations import generate_recommendation


# -------------------------------------------------
# Scenario 1: New Pipeline (Healthy condition)
# -------------------------------------------------
def test_new_pipeline():
    print("\nScenario 1: New Pipeline")

    result = generate_recommendation(
        health_score=95,
        corrosion_rate=0.02,
        remaining_life=30,
        safety_factor=2.5,
        corrosion_loss_percentage=2,
    )

    print(result)
    assert result["status"] in ["Excellent", "Good"]


# -------------------------------------------------
# Scenario 2: Moderate Corrosion
# -------------------------------------------------
def test_moderate_corrosion():
    print("\nScenario 2: Moderate Corrosion")

    result = generate_recommendation(
        health_score=75,
        corrosion_rate=0.25,
        remaining_life=15,
        safety_factor=1.6,
        corrosion_loss_percentage=20,
    )

    print(result)
    assert result["priority"] in ["Low", "Medium"]


# -------------------------------------------------
# Scenario 3: Severe Corrosion
# -------------------------------------------------
def test_severe_corrosion():
    print("\nScenario 3: Severe Corrosion")

    result = generate_recommendation(
        health_score=55,
        corrosion_rate=0.8,
        remaining_life=8,
        safety_factor=1.2,
        corrosion_loss_percentage=60,
    )

    print(result)
    assert result["priority"] in ["High", "Emergency"]


# -------------------------------------------------
# Scenario 4: Near Failure Condition
# -------------------------------------------------
def test_near_failure():
    print("\nScenario 4: Near Failure")

    result = generate_recommendation(
        health_score=35,
        corrosion_rate=1.0,
        remaining_life=2,
        safety_factor=0.9,
        corrosion_loss_percentage=75,
    )

    print(result)
    assert result["status"] in ["Critical", "Unsafe"]


# -------------------------------------------------
# Scenario 5: Invalid Inputs (Validation test)
# -------------------------------------------------
def test_invalid_inputs():
    print("\nScenario 5: Invalid Inputs")

    try:
        generate_recommendation(
            health_score=120,   # invalid
            corrosion_rate=-0.2,
            remaining_life=-5,
            safety_factor=-1,
            corrosion_loss_percentage=-10,
        )
    except ValueError as e:
        print("Caught Error:", e)
        assert "Health score" in str(e) or "cannot" in str(e)


# -------------------------------------------------
# RUN ALL SCENARIOS
# -------------------------------------------------
if __name__ == "__main__":

    test_new_pipeline()
    test_moderate_corrosion()
    test_severe_corrosion()
    test_near_failure()
    test_invalid_inputs()

    print("\n✅ All realistic scenario tests passed!")