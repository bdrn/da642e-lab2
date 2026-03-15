# Lab 2

## Structure

- `a2.1/`
  - `a21.py` – plots temperature vs. time from `temperature_data.csv`.
- `a2.2/`
  - `a22_visualize.py` – plots accelerometer and gyroscope motion data from `motion_data.csv`.
  - `a22_filter_visualize.py` – removes stationary motion samples and plots the compressed motion data; writes `motion_data_filtered.csv`.
- `a2.2frozen/`
  - `frozen.py`
- `a2.3/`
  - `digitalhealth.py` – processes the Apple Watch / Fitbit dataset for A2.3 (transforms calories, samples participants, visualizes metrics, normalizes/standardizes columns, and creates train/val/test splits).

Each script includes a header comment explaining:

- Which assignment/sub-exercises it solves.
- How to run it.
- Which external libraries are required.

## How to run

From the lab root:

```bash
cd a2.1
python3 a21.py

cd ../a2.2
python3 a22_visualize.py
python3 a22_filter_visualize.py

cd ../a2.3
python3 digitalhealth.py
```

Make sure the corresponding CSV files (e.g. `temperature_data.csv`, `motion_data.csv`, `aw_fb_data.csv`) are present in the same folder as the script before running.

## Dependencies

Install the required libraries (if not already installed):

```bash
pip install matplotlib pandas numpy seaborn scikit-learn
```
