from datetime import datetime, timedelta
import random
import pandas as pd

start_date = '2025-04-1'
start_date = datetime.strptime(start_date, "%Y-%m-%d")
end_date = '2025-05-1'
end_date = datetime.strptime(end_date, "%Y-%m-%d")

diff_date = (end_date - start_date).total_seconds() / 60
timestamps = [start_date + timedelta(minutes=i) for i in range(int(diff_date))]

timestamp_utc = []
date_day = []
output = []
output_number = 0
previous_date = None

for d in range(len(timestamps)):
    timestamp_utc.append(timestamps[d])
    current_date = timestamps[d].date()
    date_day.append(current_date)

    output_number = random.randint(1, 3)
    output.append(output_number)

    previous_date = current_date

df = pd.DataFrame({
    "timestamp": timestamp_utc,
    "date": date_day,
    "output": output
    })

df.to_csv("production_output.csv", index=False)