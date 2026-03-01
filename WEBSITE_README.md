# Car Damage AI Detection System - Website

A modern, professional web interface for car damage detection and analysis using AI technology.

## 🎯 Features

- **Modern Design**: Clean, professional UI with smooth animations and gradients
- **Image Upload**: Drag-and-drop or click-to-upload car damage images
- **Real-time Analysis**: Fast damage detection and classification
- **Responsive Design**: Works perfectly on desktop, tablet, and mobile devices
- **Interactive Dashboard**: View detailed analysis results with damage severity and recommendations
- **Dataset Information**: Browse 5,000+ images across 12 damage categories
- **Contact Section**: Get in touch with the team
- **Smooth Navigation**: Sticky navigation bar with smooth scrolling

## 📁 Project Structure

```
├── index.html          # Main HTML file with page structure
├── style.css           # Modern styling and responsive design
├── script.js           # JavaScript for interactivity
└── README.md          # This file
```

## 🚀 Getting Started

### Quick Start
1. Simply open `index.html` in your web browser
2. No dependencies or installation required!
3. Start exploring the damage detector

### Running Locally
Option 1: Direct File Open
```bash
# Windows
start index.html

# Mac
open index.html

# Linux
xdg-open index.html
```

Option 2: Using a Local Server (Recommended)
```bash
# Using Python 3
python -m http.server 8000

# Using Node.js (if installed)
npx serve

# Using Live Server in VS Code
# Install Live Server extension and right-click index.html > Open with Live Server
```

Then visit `http://localhost:8000` in your browser.

## 🎨 Features Overview

### 1. Navigation Bar
- Sticky navbar with smooth scrolling
- Active section highlighting
- Mobile hamburger menu
- Logo with branding

### 2. Hero Section
- Eye-catching headline and description
- Call-to-action button
- Animated car illustration
- Responsive layout

### 3. Features Section
- 6 key features with icons
- Hover animations
- Grid layout that adapts to screen size
- Easy-to-read descriptions

### 4. Damage Detector
- Drag-and-drop image upload area
- Click to browse files
- Real-time image preview
- Simulated AI analysis with results including:
  - Damage Type Classification
  - Severity Level (Low, Medium, High)
  - Confidence Score
  - Affected Area
  - Repair Recommendations

### 5. Dataset Section
- Statistics on dataset size (5,000+ images)
- Damage categories (12 types)
- Accuracy metrics
- Availability info
- Grid of all damage types

### 6. Contact Section
- Contact information
- Contact form with validation
- Call-to-action for inquiries

## 🎮 How to Use

### Upload & Analyze an Image
1. Scroll to the "Car Damage Detector" section
2. Either:
   - Drag an image onto the upload area
   - Click "Browse Files" to select an image
3. Wait for the AI to analyze (2-3 seconds)
4. View detailed results including damage type, severity, and recommendations
5. Click the × button to upload another image

### Navigate the Site
- Click navigation links to jump to sections
- Click "Try Detector Now" button in hero section
- Use smooth scrolling on all anchor links

## 🛠️ Customization

### Colors
Edit the CSS variables in `style.css`:
```css
:root {
    --primary-color: #FF6B6B;      /* Red */
    --secondary-color: #4ECDC4;    /* Teal */
    --accent-color: #FFE66D;       /* Yellow */
    --dark-bg: #2C3E50;            /* Dark Blue */
    --light-bg: #ECF0F1;           /* Light Gray */
}
```

### Damage Categories
Update the categories in `index.html` (Dataset section):
```html
<div class="category-item">Your Category</div>
```

### Contact Information
Update contact details in `index.html` (Contact section):
```html
<p>Your Email Here</p>
<p>Your Phone Here</p>
<p>Your Location Here</p>
```

## 📱 Responsive Breakpoints

- **Desktop**: 1200px+ (optimal experience)
- **Tablet**: 768px - 1199px (full functionality)
- **Mobile**: Below 768px (optimized layout)
- **Small Mobile**: Below 480px (single column)

## 🔧 Integration with Backend API

To connect this frontend with your Python backend:

1. Create an API endpoint that accepts image uploads
2. Update the `simulateAnalysis()` function in `script.js`:

```javascript
function simulateAnalysis() {
    const formData = new FormData();
    formData.append('image', imageInput.files[0]);

    fetch('/api/analyze', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        // Update UI with real results
        document.getElementById('damageType').textContent = data.damageType;
        document.getElementById('severity').textContent = data.severity;
        // ... etc
    });
}
```

## 📊 Dataset Information

- **Total Images**: 5,000+
- **Categories**: 12 damage types
- **Accuracy**: 95%
- **Update Frequency**: Regular updates with new data

### Damage Categories
1. Dent
2. Scratch
3. Crack
4. Broken Glass
5. Paint Damage
6. Collision Damage
7. Rust
8. Missing Part
9. Tire Damage
10. Alignment Issue
11. Water Damage
12. No Damage

## 🎬 Animations & Effects

- **Floating animation**: Hero car illustration
- **Pulse animation**: Upload icon
- **Spin animation**: Loading spinner
- **Hover effects**: All interactive elements
- **Fade-in animation**: Cards and sections
- **Smooth scrolling**: All anchor links
- **Gradient backgrounds**: Modern gradients throughout

## ♿ Accessibility

- Semantic HTML structure
- ARIA-friendly form elements
- Keyboard navigation support
- Color contrast compliance
- Responsive text sizing

## 📄 Browser Compatibility

- Chrome/Edge: Full support
- Firefox: Full support
- Safari: Full support
- IE11: Partial support (some animations may not work)

## 🔐 Security

- Client-side image validation
- File size limits (5MB)
- File type validation
- No data stored on client without permission

## 📝 License

This project is part of CPE178P_E01_2T2526 at Mapua University.

## 👥 Team

Group 5 - AI Specification Project

## 📞 Support

For issues, questions, or suggestions:
- Email: contact@cardamageai.com
- Phone: +1 (555) 123-4567
- Location: Manila, Philippines

## 🚀 Future Enhancements

- [ ] Real-time camera detection
- [ ] Batch image processing
- [ ] Download analysis reports (PDF)
- [ ] Dark mode toggle
- [ ] Multiple language support
- [ ] User accounts and history
- [ ] Mobile app version
- [ ] Integration with IoT devices

---

**Happy detecting! 🎯**
