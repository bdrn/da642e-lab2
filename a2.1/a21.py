"""
Lab 2 – Assignment A2.1, sub‑exercise I.
Plots temperature vs time from `temperature_data.csv`.

Author: Mohamad Badran
Date: 2026-03-15

How to run:
- Ensure `temperature_data.csv` is in the same folder.
- Run:  python3 a21.py

Required libraries (install if needed):
- matplotlib  ->  pip install matplotlib
"""

import csv
import matplotlib.pyplot as plt

timesteps, temps = [], []
with open('temperature_data.csv') as f:
    reader = csv.DictReader(f)
    for row in reader:
        timesteps.append(int(row['Timesteps']))
        temps.append(float(row['Temperature']))

plt.figure(figsize=(10, 6))

plt.plot(timesteps, temps, color='orange', label='temperature')

plt.xlabel('Time(seconds)')
plt.ylabel('Temperature (degrees Celsius)')

plt.grid(False)

plt.legend(loc='upper right')

plt.title(
    'Temperature Data'
)

plt.show()