def calculate_totals(data):
    total_sales = 0
    total_customers = 0
    for record in data:
        total_sales += record['sales']
        total_customers += record['customers']
    return total_sales, total_customers

def calculate_averages(total_sales, total_customers, num_days):
    average_sales = total_sales / num_days
    average_customers = total_customers / num_days
    return average_sales, average_customers

def create_report(total_sales, total_customers, average_sales, average_customers):
    report = f"Total Sales: {total_sales}\n"
    report += f"Total Customers: {total_customers}\n"
    report += f"Average Sales per Day: {average_sales:.2f}\n"
    report += f"Average Customers per Day: {average_customers:.2f}\n"
    return report

def generate_report(data):
    # データの集計
    total_sales, total_customers = calculate_totals(data)

    # データの平均計算
    average_sales, average_customers = calculate_averages(total_sales, total_customers, len(data))

    # レポート生成
    report = create_report(total_sales, total_customers, average_sales, average_customers)

    return report

data = [
    {"sales": 100, "customers": 10},
    {"sales": 150, "customers": 20},
    {"sales": 200, "customers": 15},
]

print(generate_report(data))
