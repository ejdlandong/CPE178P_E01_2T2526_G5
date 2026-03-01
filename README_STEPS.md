# Car Damage AI Project

This document outlines the step-by-step process for both the **website frontend** and the **Flet desktop/web app** created for the Car Damage AI Detection System. It explains the structure, how the code works, and how to run each component.

---

## 📂 Project Structure

```
├── index.html          # Main HTML page for web UI
├── style.css           # Stylesheet for the website
├── script.js           # Interactivity and simulated analysis logic
├── app_flet.py         # Python/Flet application
├── requirements_flet.txt  # Dependencies for Flet app
├── WEBSITE_README.md      # Documentation for the website
├── FLET_README.md          # Documentation for Flet app
└── README_STEPS.md        # This step-by-step guide
```

---

## 🧩 Website Frontend (HTML/CSS/JS)

### 1. **HTML Structure** (`index.html`)
- Sections: `home`, `features`, `detector`, `dataset`, `contact`.
- Navigation bar with links targeting each section ID.
- Detector section contains upload area and hidden preview/results panel.

### 2. **Styling** (`style.css`)
- CSS variables for colors, radius, shadows, etc.
- Responsive layouts using grid and flexbox.
- Animations for hero image, upload icon, fade-in on scroll.
- Media queries for tablet/mobile.

### 3. **Interactivity** (`script.js`)
- **Navigation**: Smooth scroll and active link highlighting.
- **Image Upload**: Drag/drop and file input. Validate file type/size.
- **Preview & Analysis**: Display image, simulate analysis with random results.
- **Simulation Logic**: Randomly choose damage type, severity, confidence, area; display after 2.5 seconds.
- **Recommendations** based on severity.
- **Contact Form**: Validate fields, show alert on send.

### 4. **Running the Website**
- Start simple HTTP server: `python -m http.server 8000` and open `http://localhost:8000/index.html`.

---

## 🐍 Flet Desktop/Web App (`app_flet.py`)

### 1. **Setup & Dependencies**
- Use Python 3.7+ and install `flet` via `pip install flet>=0.20.0`.
- Optional `requirements_flet.txt` contains packages.

### 2. **Main Application Flow**
- `main(page: ft.Page)` initializes page settings, colors, state variables.
- Sections created with helper functions (`create_nav_bar`, `create_section_content`).
- Navigation buttons call `show_section()` which rebuilds page content.

### 3. **Detector Logic in Flet**
- FilePicker triggers `on_image_selected` when a file is chosen.
- Preview area becomes visible, showing image and hiding upload area.
- `simulate_analysis()` picks random values and updates result texts.
- Results displayed after placeholder spinner.
- `reset()` hides preview and resets state.

### 4. **Other Sections**
- **Home**: Hero text with CTA.
- **Features**: Wrap of cards showing key features.
- **Dataset**: Statistics and category chips.
- **Contact**: Contact information and form with snackbar.

### 5. **Running the App**
- Desktop: `python app_flet.py` (might show errors depending on system).
- Web: `python app_flet.py --web` or `flet run app_flet.py --web` if CLI available.

---

## 🛠 Tips & Customization

- Change colors at top of `app_flet.py` or `:root` section of `style.css`.
- Replace simulation logic with real ML model by editing `simulate_analysis()`.
- Add new categories or features in their respective arrays.
- Package the Flet app as an executable using `flet pack ...`.

---

## ✅ Summary
This project demonstrates both a static website and a cross-platform Python application. The step-by-step structure above should help you understand how each part is built and how to run or extend the code.
