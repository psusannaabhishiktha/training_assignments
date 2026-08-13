#A CSV import job fails when one row has bad data. How would you handle the error without stopping the whole job?​
rows = [{"user": "Amit", "amount": "1200"},
{"user": "Riya", "amount": ""},
{"user": "Dev", "amount": "900"},]
for row in rows:
    try:
        amount = int(row["amount"])
        print(row["user"], amount)
    except ValueError:
        print(f"Error: Invalid amount for user {row['user']}. Skipping this row.")