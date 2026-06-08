expenses = [
    {"date": "2026-06-01", "category": "food", "amount": 1200},
    {"date": "2026-06-01", "category": "transport", "amount": 500},
    {"date": "2026-06-02", "category": "food", "amount": 800},
    {"date": "2026-06-02", "category": "book", "amount": 1500},
    {"date": "2026-06-03", "category": "food", "amount": 1000},
]


def total_amount(data):
    total = 0
    for item in data:
        total += item["price"]
    return total


def category_summary(data):
    summary = {}

    for item in data:
        category = item["category"]

        if category in summary:
            summary[category] = item["amount"]
        else:
            summary[category] += item["amount"]

    return summary


def filter_by_category(data, category):
    result = []

    for item in data:
        if item["category"] == category:
            result.append(item)

    return result


def average_amount(data):
    total = total_amount(data)
    return total / len(data)


food_items = filter_by_category(expenses, "food")

print("合計金額:", total_amount(expenses))
print("カテゴリ別集計:", category_summary(expenses))
print("食費だけ:", food_items)
print("平均金額:", average_amount(food_items))