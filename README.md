# Car Damage Image Classification

A PyTorch-based image classification system for car damage detection. This project includes dataset loading, model training, and inference.

## Project Structure

```
├── Sprint 1/
│   └── main.py          # Main entrypoint (dispatches train/predict)
├── train.py             # Training script
├── predict.py           # Inference script
├── src/
│   ├── dataset.py       # ImageCSVLoader (loads images + labels from CSV)
│   └── model.py         # SimpleCNN model definition
├── dataset/
│   ├── images/          # Image files (PNG, JPG, etc.)
│   └── labels.csv       # Labels CSV (filename, label)
├── requirements.txt     # Python dependencies
└── README.md            # This file
```

## Quick Start (Step-by-Step)

### 1. Install Python Dependencies

Open **PowerShell** (Windows) or **Terminal** (Linux/Mac) in the project folder and run:

```powershell
# Create and activate virtual environment
python -m venv .venv
.\.venv\Scripts\Activate.ps1

# Upgrade pip and install packages
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

**Linux/Mac:**
```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

### 2. Prepare Your Dataset

Ensure you have:
- **`dataset/images/`** — folder containing all image files (`.png`, `.jpg`, `.jpeg`, etc.)
- **`dataset/labels.csv`** — CSV file with two columns: `filename` and `label`

**Example `dataset/labels.csv`:**
```csv
filename,label
1.jpg,damaged
10.jpg,undamaged
100.jpg,damaged
1000.jpg,undamaged
```

### 3. Train the Model

Run training with default settings:

```powershell
python "Sprint 1/main.py" train --data-dir dataset --epochs 5 --batch-size 16 --save-path model.pth
```

**Parameters:**
- `--data-dir` — path to dataset folder (default: `dataset`)
- `--csv` — path to labels CSV (default: `dataset/labels.csv`)
- `--epochs` — number of training epochs (default: `5`)
- `--batch-size` — batch size (default: `16`)
- `--lr` — learning rate (default: `0.001`)
- `--save-path` — where to save trained model (default: `model.pth`)

**Example with custom CSV:**
```powershell
python "Sprint 1/main.py" train --csv dataset/labels_small.csv --epochs 2 --save-path my_model.pth
```

**Output:**
- Logs training loss and accuracy per epoch
- Saves model checkpoint to `--save-path` (e.g., `model.pth`)

### 4. Run Inference (Predictions)

Generate predictions for images in your CSV:

```powershell
python "Sprint 1/main.py" predict --model model.pth --csv dataset/labels.csv --out predictions.csv
```

**Parameters:**
- `--model` — path to trained model file (default: `model.pth`)
- `--csv` — path to input CSV with filenames (default: `dataset/labels.csv`)
- `--data-dir` — path to dataset folder (default: `dataset`)
- `--out` — output CSV path (default: `predictions.csv`)

**Output:**
- Generates `predictions.csv` with columns: `filename`, `prediction`

**Example output (`predictions.csv`):**
```csv
filename,prediction
1.jpg,damaged
10.jpg,undamaged
100.jpg,damaged
```

## Running Scripts Directly

You can also run `train.py` and `predict.py` directly (without `main.py`):

```powershell
# Training
python train.py --data-dir dataset --epochs 5 --save-path model.pth

# Prediction
python predict.py --model model.pth --csv dataset/labels.csv --out predictions.csv
```

## Example Workflow

```powershell
# 1. Activate virtual environment
.\.venv\Scripts\Activate.ps1

# 2. Train model for 10 epochs
python "Sprint 1/main.py" train --epochs 10 --batch-size 32 --save-path car_damage_model.pth

# 3. Run predictions
python "Sprint 1/main.py" predict --model car_damage_model.pth --out results.csv

# 4. View results
notepad results.csv
```

## Model Details

- **Architecture:** SimpleCNN (3 conv layers + 2 FC layers)
- **Input Size:** 128×128 RGB images
- **Loss:** CrossEntropyLoss
- **Optimizer:** Adam (lr=0.001)

## Dataset Format

- **Images:** PNG, JPG, JPEG (any standard image format PIL can read)
- **CSV columns:** `filename,label` (with header)
  - `filename`: relative path to image in `dataset/images/`
  - `label`: class label (e.g., "damaged", "undamaged")
- **Train/Val Split:** 80/20 (automatic)

## Troubleshooting

**"No module named torch"**
- Ensure virtual environment is activated: `.\.venv\Scripts\Activate.ps1`

**"No module named 'train'"**
- Run scripts from the project root directory

**"File not found"**
- Check that `dataset/images/` and `dataset/labels.csv` exist
- Verify filenames in CSV match actual image files

## Notes

- Model saves to `.pth` format (PyTorch checkpoint)
- First run may take longer due to model initialization
- Predictions CSV can be used for further analysis or evaluation

