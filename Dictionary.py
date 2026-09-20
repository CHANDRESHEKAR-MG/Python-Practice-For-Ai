fin = {"revenue": 1000, "expenses": 400}
print(type(fin))
print(fin)

fin['profit'] = fin['revenue'] - fin['expenses']
print(fin)

# Dictionary inside a list
financial = [
    {'revenue': 50, 'expenses': 10},
    {'revenue': 60, 'expenses': 20},
    {'revenue': 70, 'expenses': 30}
]

for item in financial:
    profit = item['revenue'] - item['expenses']
    item['margin'] = (profit * 100) / item['revenue']
    print(profit)

print(financial)

# Dictionary with quarter names as keys
financial_report = {
    'Q1': {'revenue': 50, 'expenses': 10},
    'Q2': {'revenue': 60, 'expenses': 20},
    'Q3': {'revenue': 70, 'expenses': 30}
}

for quarter, data in financial_report.items():
    profit = data['revenue'] - data['expenses']
    data['margin'] = (profit * 100) / data['revenue']
    print(f"{quarter}: profit = {profit}, margin = {data['margin']}%")

print(financial_report)

for quarter, data in financial_report.items():
    if data["revenue"] < 0 :
        print(f"Invalid revenue for {quarter}.skipping...")
        continue
    margin = (data['revenue'] - data['expenses']) * 100 / data['revenue']
    print(f"{quarter}: margin = {margin:.2f}%")
        