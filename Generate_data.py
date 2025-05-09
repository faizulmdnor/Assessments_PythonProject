import pandas as pd
import pytz
from datetime import datetime, timedelta
import random

# Define local timezone (e.g., New York for DST)
local_tz = pytz.timezone("America/New_York")

# Simulate timestamps that include the DST transition (fall back)
# DST ends on 2023-11-05 at 2 AM, so 1:00 to 1:59 AM appears twice
naive_times = [datetime(2023, 11, 5, 0, 0) + timedelta(minutes=i) for i in range(540)]

# Prepare data lists
localized_times = []
utc_times = []
machine_names = []
machine_outputs = []

# Sample inverter names
machine_list = ['Machine_A', 'Machine_B', 'Machine_C']

for machine in machine_list:
    for dt in naive_times:
        try:
            # Try both is_dst True and False to handle ambiguous times (like 1:30 AM)
            for is_dst in [True, False]:
                try:
                    local_dt = local_tz.localize(dt, is_dst=is_dst)
                    utc_dt = local_dt.astimezone(pytz.utc)
                    localized_times.append(local_dt)
                    utc_times.append(utc_dt)
                    machine_names.append(machine)
                    machine_outputs.append(round(random.uniform(95.0, 105.0), 2))
                except pytz.AmbiguousTimeError:
                    continue  # skip if truly ambiguous even with is_dst flag
                except pytz.NonExistentTimeError:
                    continue  # skip nonexistent times (during spring forward)

        except Exception as e:
            continue  # fail-safe for any other unexpected errors

# Create DataFrame
df = pd.DataFrame({
    "timestamp_utc": utc_times,
    "timestamp": localized_times,
    "machine_name": machine_names,
    "machine_output": machine_outputs
}).sort_values(['timestamp_utc'])

# Save to CSV
csv_path = "E:/Assessments_PythonProject/machine_output_with_dst.csv"
df.to_csv(csv_path, index=False)
