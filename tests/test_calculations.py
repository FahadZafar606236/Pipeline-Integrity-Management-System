from src.calculations import (
    corrosion_rate,
    minimum_required_thickness,
    remaining_life,
    next_inspection_date,
    corrosion_allowance,
)


# =====================================================
# Corrosion Rate Tests
# =====================================================

def test_corrosion_rate():
    rate = corrosion_rate(12, 10.8, 6)

    print(f"Corrosion Rate = {rate:.2f} mm/year")

    assert round(rate, 2) == 0.20


# =====================================================
# Minimum Required Thickness Tests
# =====================================================

def test_minimum_required_thickness():
    thickness = minimum_required_thickness(
        pressure=5,
        diameter=323.9,
        allowable_stress=138,
        weld_efficiency=1.0,
        temperature_factor=0.4,
    )

    print(f"Minimum Required Thickness = {thickness:.2f} mm")

    assert thickness > 0


# =====================================================
# Remaining Life Tests
# =====================================================

def test_remaining_life():
    life = remaining_life(
        current_thickness=10.8,
        minimum_thickness=5.78,
        corrosion_rate=0.20,
    )

    print(f"Remaining Life = {life:.2f} years")

    assert round(life, 2) == 25.10


def test_zero_corrosion():
    life = remaining_life(
        current_thickness=10,
        minimum_thickness=8,
        corrosion_rate=0,
    )

    print(f"Zero Corrosion Remaining Life = {life}")

    assert life == float("inf")


def test_negative_remaining_life():
    life = remaining_life(
        current_thickness=5,
        minimum_thickness=7,
        corrosion_rate=0.2,
    )

    print(f"Negative Remaining Life = {life}")

    assert life == 0.0


# =====================================================
# Next Inspection Date Tests
# =====================================================

def test_next_inspection_date():
    date = next_inspection_date(25.1)

    print(f"Next Inspection Date = {date}")

    assert isinstance(date, str)


def test_no_corrosion_inspection():
    date = next_inspection_date(float("inf"))

    print(date)

    assert date == "No inspection required (No corrosion detected)"


# =====================================================
# Corrosion Allowance Tests
# =====================================================

def test_corrosion_allowance():
    allowance = corrosion_allowance(12, 5.78)

    print(f"Corrosion Allowance = {allowance:.2f} mm")

    assert round(allowance, 2) == 6.22


def test_zero_corrosion_allowance():
    allowance = corrosion_allowance(8, 8)

    print(f"Zero Corrosion Allowance = {allowance:.2f} mm")

    assert allowance == 0


# =====================================================
# Input Validation Tests
# =====================================================

def test_invalid_initial_thickness():
    try:
        corrosion_rate(-12, 10, 5)
    except ValueError as e:
        print(f"Validation Passed: {e}")
        assert str(e) == "Initial thickness must be greater than zero."


def test_invalid_years():
    try:
        corrosion_rate(12, 10, 0)
    except ValueError as e:
        print(f"Validation Passed: {e}")
        assert str(e) == "Years in service must be greater than zero."


def test_invalid_pressure():
    try:
        minimum_required_thickness(
            pressure=-5,
            diameter=323.9,
            allowable_stress=138,
            weld_efficiency=1,
            temperature_factor=0.4,
        )
    except ValueError as e:
        print(f"Validation Passed: {e}")
        assert str(e) == "Pressure must be greater than zero."


def test_invalid_allowable_stress():
    try:
        minimum_required_thickness(
            pressure=5,
            diameter=323.9,
            allowable_stress=0,
            weld_efficiency=1,
            temperature_factor=0.4,
        )
    except ValueError as e:
        print(f"Validation Passed: {e}")
        assert str(e) == "Allowable stress must be greater than zero."


def test_invalid_weld_efficiency():
    try:
        minimum_required_thickness(
            pressure=5,
            diameter=323.9,
            allowable_stress=138,
            weld_efficiency=1.5,
            temperature_factor=0.4,
        )
    except ValueError as e:
        print(f"Validation Passed: {e}")
        assert str(e) == "Weld efficiency must be between 0 and 1."


def test_invalid_corrosion_allowance():
    try:
        corrosion_allowance(5, 8)
    except ValueError as e:
        print(f"Validation Passed: {e}")
        assert (
            str(e)
            == "Minimum thickness cannot be greater than nominal thickness."
        )


# =====================================================
# Edge Case Tests
# =====================================================

def test_zero_corrosion_rate():
    life = remaining_life(10, 8, 0)

    print(f"Edge Case - Zero Corrosion Rate = {life}")

    assert life == float("inf")


def test_zero_service_years():
    try:
        corrosion_rate(12, 10, 0)
    except ValueError as e:
        print(f"Edge Case - Zero Years = {e}")
        assert str(e) == "Years in service must be greater than zero."


def test_negative_thickness():
    try:
        corrosion_rate(-10, 8, 5)
    except ValueError as e:
        print(f"Edge Case - Negative Thickness = {e}")
        assert str(e) == "Initial thickness must be greater than zero."


def test_current_greater_than_initial():
    try:
        corrosion_rate(8, 10, 5)
    except ValueError as e:
        print(f"Edge Case - Current > Initial = {e}")
        assert (
            str(e)
            == "Current thickness cannot be greater than initial thickness."
        )


def test_extremely_high_pressure():
    thickness = minimum_required_thickness(
        pressure=100,
        diameter=323.9,
        allowable_stress=138,
        weld_efficiency=1,
        temperature_factor=0.4,
    )

    print(f"Edge Case - High Pressure Thickness = {thickness:.2f} mm")

    assert thickness > 0


def test_invalid_weld_efficiency_edge():
    try:
        minimum_required_thickness(
            pressure=5,
            diameter=323.9,
            allowable_stress=138,
            weld_efficiency=-0.5,
            temperature_factor=0.4,
        )
    except ValueError as e:
        print(f"Edge Case - Invalid Weld Efficiency = {e}")
        assert str(e) == "Weld efficiency must be between 0 and 1."


def test_missing_values():
    try:
        corrosion_rate(None, 10, 5)
    except (TypeError, ValueError) as e:
        print(f"Edge Case - Missing Values = {e}")
        assert True


# =====================================================
# Main
# =====================================================

if __name__ == "__main__":

    print("Test file started\n")

    test_corrosion_rate()
    test_minimum_required_thickness()
    test_remaining_life()
    test_zero_corrosion()
    test_negative_remaining_life()
    test_next_inspection_date()
    test_no_corrosion_inspection()
    test_corrosion_allowance()
    test_zero_corrosion_allowance()

    print("\n----- Input Validation Tests -----")

    test_invalid_initial_thickness()
    test_invalid_years()
    test_invalid_pressure()
    test_invalid_allowable_stress()
    test_invalid_weld_efficiency()
    test_invalid_corrosion_allowance()

    print("\n----- Edge Case Tests -----")

    test_zero_corrosion_rate()
    test_zero_service_years()
    test_negative_thickness()
    test_current_greater_than_initial()
    test_extremely_high_pressure()
    test_invalid_weld_efficiency_edge()
    test_missing_values()

    print("\n✅ All engineering calculation tests passed successfully!")