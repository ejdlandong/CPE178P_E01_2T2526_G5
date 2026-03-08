import flet as ft
import random

def main(page: ft.Page):
    page.title = "Car Damage AI - Code Process Breakdown"
    page.window_width = 1400
    page.window_height = 900
    page.scroll = ft.ScrollMode.AUTO
    
    # Colors
    PRIMARY = "#FF6B6B"
    SECONDARY = "#4ECDC4"
    ACCENT = "#FFE66D"
    DARK_BG = "#2C3E50"
    LIGHT_BG = "#ECF0F1"
    TEXT_DARK = "#2C3E50"
    TEXT_LIGHT = "#7F8C8D"
    WHITE = "#FFFFFF"
    
    current_view = {"value": "home"}
    
    def create_header():
        return ft.Container(
            ft.Row([
                ft.Text("🚗 Car Damage AI", color=ACCENT, size=24, weight="bold"),
                ft.Text("Code Process Breakdown", color=TEXT_LIGHT, size=16),
            ]),
            bgcolor=DARK_BG,
            padding=20,
            expand_x=True,
        )
    
    def create_sidebar():
        def nav_click(section):
            current_view["value"] = section
            page.clean()
            page.add(create_header(), ft.Row([create_sidebar(), create_content_area()], expand=True))
        
        nav_items = [
            ("📋 Overview", "overview"),
            ("🌐 Website (HTML/CSS/JS)", "website"),
            ("🐍 Flet App (Python)", "flet"),
            ("🔄 Flow Diagram", "flow"),
            ("⚙️ Setup Guide", "setup"),
        ]
        
        buttons = []
        for label, section in nav_items:
            btn = ft.Container(
                ft.TextButton(
                    label,
                    on_click=lambda e, s=section: nav_click(s),
                    style=ft.ButtonStyle(color=TEXT_DARK if current_view["value"] != section else PRIMARY),
                ),
                bgcolor=SECONDARY if current_view["value"] == section else LIGHT_BG,
                padding=10,
                border_radius=8,
                margin=5,
            )
            buttons.append(btn)
        
        return ft.Container(
            ft.Column(buttons, spacing=10),
            width=250,
            bgcolor=WHITE,
            padding=15,
            border_radius=8,
        )
    
    def create_content_area():
        section = current_view["value"]
        
        if section == "overview":
            content = create_overview()
        elif section == "website":
            content = create_website_section()
        elif section == "flet":
            content = create_flet_section()
        elif section == "flow":
            content = create_flow_section()
        elif section == "setup":
            content = create_setup_section()
        else:
            content = create_overview()
        
        return ft.Container(
            content,
            expand=True,
            padding=20,
            bgcolor=LIGHT_BG,
        )
    
    def create_overview():
        items = [
            ("📁 Project Structure", "The project consists of HTML/CSS/JS for web and Python/Flet for desktop/web apps."),
            ("🎯 Two Versions", "Website version runs on any browser. Flet version is a native cross-platform app."),
            ("🔧 Shared Features", "Both implement image upload, damage analysis simulation, and responsive UI."),
            ("🚀 Easy Integration", "Replace simulation logic with real AI model for production use."),
        ]
        
        cards = []
        for title, desc in items:
            card = ft.Container(
                ft.Column([
                    ft.Text(title, size=16, weight="bold", color=PRIMARY),
                    ft.Text(desc, size=13, color=TEXT_LIGHT),
                ], spacing=10),
                bgcolor=WHITE,
                padding=20,
                border_radius=8,
                border=ft.border.all(2, SECONDARY),
            )
            cards.append(card)
        
        return ft.Column([
            ft.Text("Project Overview", size=28, weight="bold", color=TEXT_DARK),
            ft.Column(cards, spacing=15),
        ], spacing=20)
    
    def create_website_section():
        steps = [
            ("1️⃣ HTML Structure", "`index.html` - 5 main sections (Home, Features, Detector, Dataset, Contact). Navigation bar links to section IDs. Upload area has file input and drag/drop zone."),
            ("2️⃣ CSS Styling", "`style.css` - CSS variables for colors. Responsive grid/flexbox layouts. Animations: float (hero), pulse (upload icon), spin (loading). Media queries for mobile."),
            ("3️⃣ JavaScript Logic", "`script.js` - Navigation highlighting. Drag/drop file handling. Image preview. Simulate analysis with 2.5s delay. Generate random results and recommendations."),
            ("4️⃣ Run Website", "Start server: `python -m http.server 8000`. Open `http://localhost:8000/index.html` in browser."),
        ]
        
        cards = []
        for step, detail in steps:
            card = ft.Container(
                ft.Column([
                    ft.Text(step, size=14, weight="bold", color=PRIMARY),
                    ft.Text(detail, size=12, color=TEXT_DARK),
                ], spacing=8),
                bgcolor=WHITE,
                padding=15,
                border_radius=8,
                border=ft.border.all(1, SECONDARY),
            )
            cards.append(card)
        
        return ft.Column([
            ft.Text("🌐 Website Breakdown", size=28, weight="bold", color=TEXT_DARK),
            ft.Text("Step-by-step process for HTML/CSS/JavaScript", size=14, color=TEXT_LIGHT),
            ft.Column(cards, spacing=12),
        ], spacing=20)
    
    def create_flet_section():
        steps = [
            ("1️⃣ Setup", "Install: `pip install flet>=0.20.0`. Define colors as constants. Initialize page settings."),
            ("2️⃣ State & UI Components", "Create state variables for sections. Define preview_image, results_placeholder, results_content. Set up FilePicker for image upload."),
            ("3️⃣ Navigation & Sections", "`create_nav_bar()` - buttons to switch sections. `create_section_content()` - builds content for each section dynamically."),
            ("4️⃣ Detector Logic", "`on_image_selected()` - handles file selection. `simulate_analysis()` - generates random damage results. `reset()` - clears preview."),
            ("5️⃣ Run App", "Web: `python app_flet.py --web`. Desktop: `python app_flet.py` (may need system setup)."),
        ]
        
        cards = []
        for step, detail in steps:
            card = ft.Container(
                ft.Column([
                    ft.Text(step, size=14, weight="bold", color=SECONDARY),
                    ft.Text(detail, size=12, color=TEXT_DARK),
                ], spacing=8),
                bgcolor=WHITE,
                padding=15,
                border_radius=8,
                border=ft.border.all(1, PRIMARY),
            )
            cards.append(card)
        
        return ft.Column([
            ft.Text("🐍 Flet App Breakdown", size=28, weight="bold", color=TEXT_DARK),
            ft.Text("Step-by-step process for Python/Flet application", size=14, color=TEXT_LIGHT),
            ft.Column(cards, spacing=12),
        ], spacing=20)
    
    def create_flow_section():
        flows = [
            ("Website Flow", "User → Browser → index.html → CSS loads → JS runs → Navigation works → Upload → Analysis"),
            ("Flet Flow", "User → runs app_flet.py → Flet renders UI → Page loads home → Click nav → show_section() → Content updates"),
            ("Analyzer Flow (Both)", "User uploads image → File validation → Preview displayed → Timer starts (2.5s) → simulate_analysis() → Random results → Show results"),
            ("Results Generation", "Random damage type → Random severity → Calc confidence → Random area → Map recommendations → Display"),
        ]
        
        cards = []
        for title, flow in flows:
            card = ft.Container(
                ft.Column([
                    ft.Text(title, size=14, weight="bold", color=PRIMARY),
                    ft.Text(flow, size=11, color=TEXT_DARK),
                ], spacing=5),
                bgcolor=WHITE,
                padding=15,
                border_radius=8,
            )
            cards.append(card)
        
        return ft.Column([
            ft.Text("🔄 Process Flows", size=28, weight="bold", color=TEXT_DARK),
            ft.Text("Execution flow for different user actions", size=14, color=TEXT_LIGHT),
            ft.SizedBox(height=15),
            ft.Column(cards, spacing=12),
        ], spacing=20)
    
    def create_setup_section():
        setup_steps = [
            ("Prerequisites", "Python 3.7+, pip package manager, modern web browser"),
            ("Install Flet", "`pip install flet>=0.20.0` or use `requirements_flet.txt`"),
            ("Fix PowerShell", "`Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser`"),
            ("Activate venv", "`.venv\\Scripts\\Activate.ps1` (Windows) or `source .venv/bin/activate` (Mac/Linux)"),
            ("Website Quick Start", "1. Run `python -m http.server 8000`\n2. Open browser to `http://localhost:8000/index.html`"),
            ("Flet Quick Start", "1. Run `python app_flet.py --web` for web version\n2. Open browser to URL shown in terminal"),
            ("Customize", "Edit color variables, damage categories, contact info, or replace simulation with real AI model"),
        ]
        
        cards = []
        for step, detail in setup_steps:
            card = ft.Container(
                ft.Column([
                    ft.Text(step, weight="bold", color=ACCENT, size=13),
                    ft.Text(detail, color=TEXT_DARK, size=11),
                ], spacing=5),
                bgcolor=WHITE,
                padding=15,
                border_radius=8,
            )
            cards.append(card)
        
        return ft.Column([
            ft.Text("⚙️ Setup & Installation Guide", size=28, weight="bold", color=TEXT_DARK),
            ft.Column(cards, spacing=10),
        ], spacing=20)
    
    # Initial layout
    page.add(
        create_header(),
        ft.Row([create_sidebar(), create_content_area()], expand=True)
    )

if __name__ == "__main__":
    ft.app(target=main)
