from datetime import datetime, timedelta
import random
import pandas as pd

start_date = datetime.strptime('2025-04-01', "%Y-%m-%d")
end_date = datetime.strptime('2025-05-01', "%Y-%m-%d")

timestamps = [start_date + timedelta(minutes=i) for i in range(int((end_date - start_date).total_seconds() / 60))]

data = []
for ts in timestamps:
    hour = ts.hour

    # Simulate output
    if 7 <= hour <= 19:
        output = random.randint(9, 10)
    else:
        output = random.randint(8, 10)

    # Simulate input (must be >= output)
    input_val = max(output + random.randint(0, 2), 1)

    # Calculate yield
    yield_percent = round((output / input_val) * 100, 2)

    data.append((ts, ts.date(), input_val, output, yield_percent))

# Create DataFrame
df = pd.DataFrame(data, columns=["timestamp", "date", "input", "output", "yield_percent"])
df.to_csv("production_output.csv", index=False)

print(df.head())
