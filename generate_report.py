def generate_report(data):
    # データの集計
    total_sales = 0
    total_customers = 0
    for record in data:
        total_sales += record['sales']
        total_customers += record['customers']

    # データの平均計算
    average_sales = total_sales / len(data)
    average_customers = total_customers / len(data)

    # レポート生成
    report = f"Total Sales: {total_sales}\n"
    report += f"Total Customers: {total_customers}\n"
    report += f"Average Sales per Day: {average_sales:.2f}\n"
    report += f"Average Customers per Day: {average_customers:.2f}\n"

    return report

data = [
    {"sales": 100, "customers": 10},
    {"sales": 150, "customers": 20},
    {"sales": 200, "customers": 15},
]

print(generate_report(data))