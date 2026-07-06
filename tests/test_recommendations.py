print("File started")

from src.recommendations import generate_recommendation


def test_excellent():
    result = generate_recommendation(95, 0.05, 30, 2.5, 5)

    print(result)

    assert result["status"] == "Excellent"


def test_good():
    result = generate_recommendation(80, 0.15, 20, 1.8, 15)

    print(result)

    assert result["status"] == "Good"


def test_monitor():
    result = generate_recommendation(60, 0.30, 10, 1.3, 35)

    print(result)

    assert result["status"] == "Monitor"


def test_high_corrosion():
    result = generate_recommendation(80, 0.8, 20, 1.8, 20)

    print(result)

    assert result["priority"] == "High"


def test_low_remaining_life():
    result = generate_recommendation(80, 0.20, 3, 1.8, 20)

    print(result)

    assert result["priority"] == "High"


def test_unsafe_pipeline():
    result = generate_recommendation(90, 0.10, 15, 0.8, 20)

    print(result)

    assert result["priority"] == "Emergency"


def test_critical_pipeline():
    result = generate_recommendation(40, 0.40, 8, 1.2, 35)

    print(result)

    assert result["priority"] == "Emergency"


def test_invalid_health_score():
    try:
        generate_recommendation(120, 0.2, 10, 1.5, 20)
    except ValueError as e:
        print(e)

        assert str(e) == "Health score must be between 0 and 100."


if __name__ == "__main__":

    print("Recommendation Tests\n")

    test_excellent()
    test_good()
    test_monitor()
    test_high_corrosion()
    test_low_remaining_life()
    test_unsafe_pipeline()
    test_critical_pipeline()
    test_invalid_health_score()

    print("\n✅ Recommendation engine tests passed successfully!")