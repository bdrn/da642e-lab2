"""
Lab 2 – Assignment A2.2, sub‑exercise II.
Visualizes motion data (accelerometer and gyroscope) from `motion_data.csv`.

Author: Mohamad Badran
Date: 2026-03-15

How to run:
- Ensure `motion_data.csv` is in the same folder.
- Run:  python3 a22_visualize.py

Required libraries (install if needed):
- matplotlib  ->  pip install matplotlib
- csv (Python standard library)
"""
import csv
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# Load data
time_sec = []
ax, ay, az = [], [], []
gx, gy, gz = [], [], []

with open("motion_data.csv") as f:
    reader = csv.DictReader(f)
    for i, row in enumerate(reader):
        time_sec.append(i * 0.5)  # 2 Hz => 0.5 s per sample
        ax.append(float(row["Ax"]))
        ay.append(float(row["Ay"]))
        az.append(float(row["Az"]))
        gx.append(float(row["Gx"]))
        gy.append(float(row["Gy"]))
        gz.append(float(row["Gz"]))

fig, ax1 = plt.subplots(figsize=(12, 6))

# Left y-axis: Acceleration
ax1.set_xlabel("Time (seconds)")
ax1.set_ylabel("Acceleration (m/s²)")
ax1.plot(time_sec, ax, label="Ax", alpha=0.9)
ax1.plot(time_sec, ay, label="Ay", alpha=0.9)
ax1.plot(time_sec, az, label="Az", alpha=0.9)

# Right y-axis: Gyroscope
ax2 = ax1.twinx()
ax2.set_ylabel("Angular velocity (deg/s)")
ax2.plot(time_sec, gx, label="Gx", alpha=0.9, linestyle="--")
ax2.plot(time_sec, gy, label="Gy", alpha=0.9, linestyle="--")
ax2.plot(time_sec, gz, label="Gz", alpha=0.9, linestyle="--")

# Legend
lines1, labels1 = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax1.legend(lines1 + lines2, labels1 + labels2, loc="upper right")
leg = ax2.get_legend()
if leg is not None:
    leg.remove()

plt.title("Motion data: Accelerometer and Gyroscope")
plt.tight_layout()
plt.savefig("motion_visualization.png", dpi=150)
plt.show()
plt.close()
