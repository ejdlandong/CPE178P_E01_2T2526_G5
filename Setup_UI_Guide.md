# Car Damage Classifier — GUI Instructions

This document explains how to set up the Python environment and run the Flet-based GUI for training and predicting car damage images.

**Quick summary**
- Activate the project's virtual environment
- Install dependencies from `requirements.txt`
- Run the GUI with `python app.py`

## 1) Prerequisites
- Python 3.8+ installed (you are using Python 3.13 — that works)
- Git (optional)
- Recommended: a virtual environment (`venv`) to isolate dependencies

## 2) Create and activate the virtual environment (PowerShell)
Open PowerShell in the project root (where `app.py` is located) and run:

```powershell
python -m venv .venv
# Activate (PowerShell)
.\.venv\Scripts\Activate.ps1
```

If PowerShell blocks script execution, run this in an elevated PowerShell once (adjust policy per your security rules):

```powershell
# Run as admin
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
```

Or activate using Command Prompt:

```cmd
.venv\Scripts\activate.bat
```

## 3) Install dependencies
Install the packages required by the project:

```powershell
pip install -r requirements.txt
# (optional) upgrade flet if you need the latest features
pip install --upgrade flet
```

Note: On Windows the installer may warn about scripts path; that's fine. If activation failed earlier, pip may have installed packages to the user site; re-run activation and install inside the venv.

## 4) Run the GUI
From the project root with the venv active:

```powershell
python app.py
```

The Flet window should open showing a two-column UI: the left side has the Train / Predict controls, and the right side shows the image preview and prediction results.

## 5) Using the GUI — Predict Mode
1. Click `Predict Mode` (the left buttons switch mode).
2. Click `Browse Model` and choose a trained `.pth` model file. If you don't have one yet, you can train using the CLI (see next section).
3. Click `Browse Image` and choose an image file from your `dataset/images` folder (JPEG/PNG).
4. Click `Predict`. The result label will appear in the right panel.

If your environment lacks the Flet `FilePicker` control, the GUI uses the native OS dialog (tkinter) so the Browse buttons work even on older Flet versions.

## 6) Using the GUI — Train Mode
1. Click `Train Mode`.
2. Configure the `Data Directory` (default `dataset`) and `Labels CSV Path` (default `dataset/labels.csv`).
3. Set `Epochs`, `Batch Size`, and `Learning Rate` to taste.
4. Click `Start Training` to begin — the training runs in a background thread and logs appear in the left panel.
5. When training completes, the model is saved to the path you specified in `Save Model As` (default `model.pth`).

## 7) CLI alternatives
You can train or predict from the command line as well.

Train (example):
```powershell
python train.py --data-dir dataset --csv dataset/labels.csv --epochs 5 --batch-size 16 --lr 0.001 --save-path model.pth
```

Predict (example):
```powershell
python predict.py --model model.pth --csv dataset/labels.csv --data-dir dataset --out preds.csv
```

## 8) Troubleshooting
- Error: `Unknown control: FilePicker` — upgrade `flet` (run `pip install --upgrade flet`) or use the Browse buttons (native file dialog) which are implemented as a fallback.
- Error: `A valid src value must be specified.` — occurs when an `ft.Image` was created with an empty `src`; the GUI now uses a placeholder container until you choose an image. Select an image using `Browse Image`.
- PowerShell activation blocked — run as administrator and set execution policy, or use Command Prompt activation.
- If the app shows other widget attribute errors, paste the traceback here and I'll update the code for compatibility with your `flet` version.

## 9) Quick smoke test (no full dataset required)
If you want to quickly verify the pipeline:
1. Create a tiny CSV `dataset/labels_small.csv` with a few filenames from `dataset/images` and labels in `filename,label` format.
2. Run training for 1 epoch and save to `smoke_user_model.pth`:

```powershell
python train.py --data-dir dataset --csv dataset/labels_small.csv --epochs 1 --batch-size 4 --lr 0.001 --save-path smoke_user_model.pth
```

3. Use `smoke_user_model.pth` in the GUI to predict on one of the images.

## 10) Need help?
If anything fails, send the exact error traceback or a screenshot. I can patch `app.py` to match your installed `flet` version, replace FilePicker with another UI, or add additional features (batch predict, progress bars, etc.).

