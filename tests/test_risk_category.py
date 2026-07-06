from src.recommendations import get_risk_category

print("Risk Category Tests\n")

print(get_risk_category(0.05, 30, 95))
print(get_risk_category(0.15, 18, 85))
print(get_risk_category(0.35, 8, 70))
print(get_risk_category(0.80, 3, 40))

print("\n✅ Risk category tests passed!")