customer_queue = ["Sen", "Ben", "John"]
customer_queue.sort()

for i, name in enumerate(customer_queue):
    row = f"{i + 1}. {name}"
    print(row)
