print("File started: Calculation Tests\n")

from src.calculations import (
    corrosion_loss_percentage,
    safety_factor,
    health_score,
    estimated_failure_year,
)

from src.recommendations import generate_recommendation


# -----------------------------
# Test 1: Corrosion Loss %
# -----------------------------
def test_corrosion_loss():
    result = corrosion_loss_percentage(12, 9)
    print("Corrosion Loss %:", result)
    assert result == 25.0


# -----------------------------
# Test 2: Safety Factor
# -----------------------------
def test_safety_factor():
    result = safety_factor(10, 8)
    print("Safety Factor:", result)
    assert result == 1.25


# -----------------------------
# Test 3: Health Score
# -----------------------------
def test_health_score():
    result = health_score(0.2, 15, 0.9, 20)
    print("Health Score:", result)
    assert 0 <= result <= 100


# -----------------------------
# Test 4: Failure Year
# -----------------------------
def test_failure_year():
    result = estimated_failure_year(2026, 5)
    print("Failure Year:", result)
    assert result == 2031


# -----------------------------
# Test 5: Recommendation Logic
# -----------------------------
def test_recommendation():
    result = generate_recommendation(
        health_score=85,
        corrosion_rate=0.2,
        remaining_life=15,
        safety_factor=1.5,
        corrosion_loss_percentage=20,
    )

    print("Recommendation:", result)

    assert "status" in result
    assert "priority" in result


# -----------------------------
# Run manually
# -----------------------------
if __name__ == "__main__":

    test_corrosion_loss()
    test_safety_factor()
    test_health_score()
    test_failure_year()
    test_recommendation()

    print("\n✅ All calculation tests passed!")