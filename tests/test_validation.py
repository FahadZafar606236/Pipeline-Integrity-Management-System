from src.utilities import validate_pipeline_inputs

print("Validation Tests\n")

# Valid input
print(
    validate_pipeline_inputs(
        12,
        10,
        0.15,
        15,
        85,
    )
)

# Invalid initial thickness
try:
    validate_pipeline_inputs(
        0,
        10,
        0.15,
        15,
        85,
    )
except ValueError as e:
    print(e)

# Invalid current thickness
try:
    validate_pipeline_inputs(
        12,
        -1,
        0.15,
        15,
        85,
    )
except ValueError as e:
    print(e)

# Invalid health score
try:
    validate_pipeline_inputs(
        12,
        10,
        0.15,
        15,
        120,
    )
except ValueError as e:
    print(e)

# Missing value
try:
    validate_pipeline_inputs(
        None,
        10,
        0.15,
        15,
        85,
    )
except ValueError as e:
    print(e)

print("\n✅ Validation tests passed!")