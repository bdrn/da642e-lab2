"""
Lab 2 – Assignment A2.2, sub‑exercise III.
Removes rows where acceleration is close to zero (stationary) and re‑plots motion data.

Author: Mohamad Badran
Date: 2026-03-15

How to run:
- Ensure `motion_data.csv` is in the same folder.
- Run:  python3 a22_filter_visualize.py

Required libraries (install if needed):
- matplotlib  ->  pip install matplotlib
- csv (Python standard library)
"""
import csv
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# Thresholds: drop row if all axes are below threshold
THRESHOLD_AX = 0.5
THRESHOLD_AY = 0.5
THRESHOLD_AZ = 0.5
def is_stationary(ax, ay, az):
    return abs(ax) < THRESHOLD_AX and abs(ay) < THRESHOLD_AY and abs(az) < THRESHOLD_AZ

# Load and filter
rows = []
with open("motion_data.csv") as f:
    reader = csv.DictReader(f)
    for row in reader:
        ax = float(row["Ax"])
        ay = float(row["Ay"])
        az = float(row["Az"])
        if not is_stationary(ax, ay, az):
            rows.append(row)

# Build time_sec for filtered data
time_sec = [i * 0.5 for i in range(len(rows))]
ax_vals = [float(r["Ax"]) for r in rows]
ay_vals = [float(r["Ay"]) for r in rows]
az_vals = [float(r["Az"]) for r in rows]
gx_vals = [float(r["Gx"]) for r in rows]
gy_vals = [float(r["Gy"]) for r in rows]
gz_vals = [float(r["Gz"]) for r in rows]

# Save filtered csv
with open("motion_data_filtered.csv", "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=["Date", "Time", "Ax", "Ay", "Az", "Gx", "Gy", "Gz"])
    w.writeheader()
    w.writerows(rows)
print(f"Filtered: {len(rows)} rows kept (stationary removed). Saved to motion_data_filtered.csv")

# Plot
fig, ax1 = plt.subplots(figsize=(8, 6))
ax1.set_xlabel("Time (seconds)")
ax1.set_ylabel("Acceleration (m/s²)")
ax1.plot(time_sec, ax_vals, label="Ax", alpha=0.9)
ax1.plot(time_sec, ay_vals, label="Ay", alpha=0.9)
ax1.plot(time_sec, az_vals, label="Az", alpha=0.9)
ax1.grid(False)

ax2 = ax1.twinx()
ax2.set_ylabel("Angular velocity (deg/s)")
ax2.plot(time_sec, gx_vals, label="Gx", alpha=0.9, linestyle="--")
ax2.plot(time_sec, gy_vals, label="Gy", alpha=0.9, linestyle="--")
ax2.plot(time_sec, gz_vals, label="Gz", alpha=0.9, linestyle="--")

lines1, labels1 = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax1.legend(lines1 + lines2, labels1 + labels2, loc="upper right")
leg = ax2.get_legend()
if leg is not None:
    leg.remove()

plt.title("Motion data (filtered)")
plt.tight_layout()
plt.savefig("motion_visualization_filtered.png", dpi=150)
plt.show()  
plt.close()
