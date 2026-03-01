# Car Damage AI - Flet Desktop Application

A native desktop application for car damage detection using Flet framework.

## 🚀 Installation

### 1. Install Flet
```bash
pip install flet>=0.20.0
```

Or install from requirements file:
```bash
pip install -r requirements_flet.txt
```

### 2. Run the Application
```bash
flet run app_flet.py
```

Or for web version:
```bash
flet run app_flet.py --web
```

## 🎯 Features

✅ **Native Desktop App** - Built with Flet for cross-platform compatibility  
✅ **Image Upload** - Browse and select car damage images  
✅ **AI Damage Analysis** - Simulated ML analysis with results  
✅ **Modern UI** - Professional design matching the website  
✅ **All Sections** - Home, Features, Detector, Dataset, Contact  
✅ **Responsive Layout** - Works on different screen sizes  
✅ **Interactive Elements** - Buttons, forms, and navigation  

## 📋 Requirements

- Python 3.7+
- Flet 0.20.0 or higher
- Pillow 9.0.0 or higher (for image handling)

## 🎨 Available Sections

### Home
- Hero section with call-to-action
- Quick navigation to detector

### Features
- 6 key features with icons and descriptions
- Hover effects on feature cards

### Detector
- Image upload area (browse files)
- Real-time preview
- Simulated damage analysis
- Results display with:
  - Damage type
  - Severity level
  - Confidence score
  - Affected area
  - Repair recommendations

### Dataset
- Statistics (5,000+ images, 12 categories, 95% accuracy)
- All damage categories as chips
- Dataset information

### Contact
- Contact information display
- Contact form with validation
- Message submission

## 🖥️ Running on Different Platforms

### Windows
```bash
python app_flet.py
```

### macOS
```bash
python3 app_flet.py
```

### Linux
```bash
python3 app_flet.py
```

### Web Browser
```bash
flet run app_flet.py --web
```

## 🔧 Customization

### Change Color Scheme
Edit the color variables in the `__init__` method:
```python
self.primary_color = "#FF6B6B"      # Red
self.secondary_color = "#4ECDC4"    # Teal
self.accent_color = "#FFE66D"       # Yellow
```

### Modify App Window
```python
self.page.window_width = 1200
self.page.window_height = 800
```

### Add More Features
Edit the respective `create_*_section()` methods

## 📱 Building as Standalone App

### Package as Executable (Windows)
```bash
flet pack app_flet.py --product-name "Car Damage AI"
```

### Package for macOS
```bash
flet pack app_flet.py --product-name "Car Damage AI" --target macos
```

### Package for Linux
```bash
flet pack app_flet.py --product-name "Car Damage AI" --target linux
```

## 🔄 Integrating with Python Backend

To connect with your AI model:

1. Create a Python function for damage analysis
2. Replace the `simulate_analysis()` method with your model

Example:
```python
def analyze_damage(self, image_path):
    # Import your AI model
    from your_model import detect_damage
    
    # Run analysis
    results = detect_damage(image_path)
    
    # Update UI with real results
    self.results_content.controls[0].content.controls[1].value = results['damage_type']
    self.results_content.controls[1].content.controls[1].value = results['severity']
    # ... etc
```

## 🎮 User Interactions

1. **Navigation** - Click nav bar items to switch sections
2. **Upload Image** - Click "Browse Files" to select image
3. **View Results** - Wait for analysis to complete (2.5 seconds simulation)
4. **Remove Image** - Click "Remove ×" to upload another
5. **Send Message** - Fill contact form and click "Send Message"

## 🐛 Troubleshooting

### Flet not found
```bash
pip install --upgrade flet
```

### Image not displaying
Make sure image path is correct and file exists

### App not responding
Check terminal for error messages

## 📞 Support

For Flet documentation: https://flet.dev

## 🎓 Educational Use

This is part of the CPE178P_E01_2T2526 project at Mapua University.

## 📝 License

Same as parent project

---

**Ready to run! 🚀**
