from src.report_generator import generate_pdf_report

sample_data = {
    "pipe_id": "PL-001",
    "pipeline_name": "Crude Oil Transfer Line",
    "material": "API 5L X52",
    "fluid": "Crude Oil",
    "inspector": "M. Fahad Zafar",
    "inspection_date": "15 July 2026",
    "pressure": 5.5,

    "corrosion_rate": 0.15,
    "minimum_thickness": 8.34,
    "remaining_life": 22.10,
    "safety_factor": 1.42,
    "corrosion_loss": 5.60,
    "health_score": 91.35,
    "failure_year": 2048,
    "risk_level": "LOW",
    "likelihood": 2,
    "consequence": 3,
    "risk_score": 6,
    "risk_level": "Medium",
}

pdf = generate_pdf_report(sample_data)

print("PDF Created Successfully")
print(pdf)