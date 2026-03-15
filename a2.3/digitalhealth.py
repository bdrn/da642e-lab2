"""
Lab 2 – Assignment A2.3, sub‑exercises I–V.
Processes Apple Watch / Fitbit data from `aw_fb_data.csv` and performs
calories transformation, participant sampling, visualization, normalization/
standardization, and train/val/test splitting.

Author: Mohamad Badran
Date: 2026-03-15

How to run:
- Ensure `aw_fb_data.csv` is in the same folder.
- Run:  python3 digitalhealth.py

Required libraries (install if needed):
- pandas, numpy, matplotlib, seaborn, scikit-learn
  pip install pandas numpy matplotlib seaborn scikit-learn
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.model_selection import train_test_split

# Load the data
df = pd.read_csv('aw_fb_data.csv')

# Part I: Calories Transformation
# Using Log transform to handle skewness
df['calories_transformed'] = np.log1p(df['calories'])

# Part II: Participant Sampling
participant_cols = ['age', 'gender', 'height', 'weight']
df['participant_id'] = df.groupby(participant_cols).ngroup()
df_participants = df.drop_duplicates(subset=['participant_id']).copy()

# Visualize Age, Height, Weight
fig, axes = plt.subplots(3, 1, figsize=(10, 12), sharex=True)
axes[0].plot(df_participants.index, df_participants["age"], color="blue", label="Age")
axes[0].grid(True)
axes[0].legend(loc="upper center")
axes[0].set_title("Age")

axes[1].plot(df_participants.index, df_participants["height"], color="green", label="Height")
axes[1].grid(True)
axes[1].legend(loc="upper center")
axes[1].set_title("Height")

axes[2].plot(df_participants.index, df_participants["weight"], color="red", label="Weight")
axes[2].grid(True)
axes[2].legend(loc="upper center")
axes[2].set_title("Weight")

plt.tight_layout()
plt.savefig("participants_age_height_weight.png", dpi=150)
plt.close()

# Part III: First three participants steps, heart rate, calories
first_three_ids = sorted(df["participant_id"].unique())[:3]
p1, p2, p3 = (df[df["participant_id"] == pid].copy() for pid in first_three_ids)

fig, axes = plt.subplots(3, 1, figsize=(12, 12), sharex=True)
metrics = ["steps", "hear_rate", "calories"]
titles = ["Steps", "Heart Rate", "Calories"]
colors = ["tab:blue", "tab:orange", "tab:green"]

participants = [
    (p1, "Participant #1"),
    (p2, "Participant #2"),
    (p3, "Participant #3"),
]

for i, metric in enumerate(metrics):
    for (participant_df, label), color in zip(participants, colors):
        axes[i].plot(
            participant_df.reset_index().index,
            participant_df[metric],
            label=label,
            color=color,
        )
    axes[i].set_title(titles[i])
    axes[i].legend(loc="upper right")
    axes[i].grid(True)

plt.tight_layout()
plt.savefig("first_three_participants_steps_hr_calories.png", dpi=150)
plt.close()

# Part IV: Normalization & Standardization
scaler_norm = MinMaxScaler()
df[['age_norm', 'height_norm', 'weight_norm']] = scaler_norm.fit_transform(df[['age', 'height', 'weight']])

scaler_std = StandardScaler()
df[['steps_std', 'heart_rate_std']] = scaler_std.fit_transform(df[['steps', 'hear_rate']])

# Part V: Dataset Splitting
train_df, temp_df = train_test_split(df, test_size=0.30, random_state=42)
val_df, test_df = train_test_split(temp_df, test_size=0.50, random_state=42)

# Save final csv
df.to_csv('final_processed_aw_fb_data.csv', index=False)